## Synchronisation au sample près

### Principe

Le GamePlayer fournit à tous les plug-ins qui le souhaitent un **compteur d'échantillons**
commun : le numéro de l'échantillon en cours, compté depuis le chargement du GamePlayer dans la
session. Ce compteur est transmis **par l'audio**, sur les canaux 1 et 2 (`spl0`, `spl1`) de la
sortie du GamePlayer, que la session REAPER envoie aux plug-ins concernés (en particulier les
FilePlayer). Chaque récepteur connaît ainsi, pour chaque échantillon qu'il traite, son numéro
exact : des opérations peuvent être déclenchées **au sample près**, de façon synchrone dans tous
les plug-ins.

### Codage

Le numéro d'échantillon est décomposé en deux entiers de 24 bits :

    numéro = T0 + 2^24 × T1        avec 0 ≤ T0 < 2^24

et chacun est transmis multiplié par 2^-48 :

    spl0 = T0 × 2^-48        spl1 = T1 × 2^-48

Dans le GamePlayer, `T0` est incrémenté à chaque échantillon (`@sample`) ; dans `@block`, quand
`T0` atteint 2^24, il est diminué de 2^24 et `T1` est incrémenté. (`T0` peut donc dépasser
2^24 de quelques échantillons avant la fin du bloc ; la somme décodée reste exacte.)

Les constantes sont définies dans `mSL_Constants` : `T_fact` = 2^48, `T_maxk` = 2^24 ; le
GamePlayer utilise `T_div` = 1 / `T_fact`.

### Décodage

Au début de `@sample`, chaque récepteur calcule :

    currSmpl = floor(spl0 * T_fact + 0.5) + floor(spl1 * T_fact + 0.5) * 16777216;
    spl0 = spl1 = 0;

L'arrondi (+ 0,5) rend le décodage insensible à une infime erreur de gain sur le trajet. La
remise à zéro de `spl0` et `spl1` évite que ces valeurs poursuivent leur chemin vers les
haut-parleurs. Le même calcul est fait dans le GamePlayer lui-même, qui dispose ainsi du même
`currSmpl` que les récepteurs.

### Propriétés

- **Exactitude** : les valeurs k × 2^-48, pour k < 2^24, sont représentées exactement, même
  dans un trajet audio en flottants 32 bits (mantisse de 24 bits).
- **Durée** : 2^48 échantillons, soit environ 186 ans à 48 kHz.
- **Inaudibilité** : `spl0` est une rampe d'amplitude au plus 2^-24 (environ −144 dBFS), de
  période 2^24 échantillons (349 s à 48 kHz, soit 0,003 Hz) ; `spl1` est un escalier de pas
  2^-48 toutes les 349 s. Même amplifiés de 60 dB, ces signaux restent vers −84 dBFS, dans
  l'infrasonore.
- **Nature du compteur** : il compte les échantillons *traités*. Si REAPER n'exécute pas les
  effets à l'arrêt, il se fige ; tous les récepteurs lisant le même compteur, ils restent
  synchronisés entre eux.

### Conditions d'emploi

- Le GamePlayer et les récepteurs positionnent `ext_noinit = 1` (le compteur n'est pas remis à
  zéro au démarrage de la lecture) et `ext_nodenorm = 1` (JSFX ne modifie pas les échantillons
  pour éviter les nombres dénormalisés).
- Le trajet doit être transparent : envoi à 0 dB, sans loi de panoramique ni effet
  intermédiaire, à la même fréquence d'échantillonnage.
- Les canaux 1 et 2 de la sortie du GamePlayer ne transportent que le compteur : la piste du
  GamePlayer ne doit pas alimenter les haut-parleurs (ce serait inaudible, mais inutile).

### Perte de synchronisation

Si le compteur n'arrive pas (envoi absent ou coupé), `currSmpl` reste figé, et les événements
datés en échantillons (`smplNewEV`) ne se produiraient jamais. Le FilePlayer vérifie, à chaque
`@block`, que `currSmpl` a avancé depuis le bloc précédent ; sinon il écrit une fois dans le
journal système « FilePlayer : no sample counter from the GamePlayer (channels 1-2), sample
dated events stopped », puis, au retour du compteur, « … sample counter from the GamePlayer
received again ».

### Commandes datées

Comme tous les plug-ins partagent le même compteur, une commande peut être déposée dans la
mémoire partagée avec une **date en échantillons** : le destinataire l'exécute au sample près,
pourvu qu'elle lui parvienne avant cette date (au moins un bloc à l'avance). C'est le mécanisme
des événements `smplNewEV` du FilePlayer.

Des canaux supplémentaires (`spl2`, `spl3`) pourraient transporter des commandes de la même
façon (un entier de 24 bits par échantillon et par canal, soit environ 1,15 Mbit/s à 48 kHz,
toujours inaudible) ; ils n'apporteraient un gain que pour une commande décidée dans le
`@sample` ou le `@block` du GamePlayer et devant agir dans le même échantillon. Cette extension
n'est pas réalisée.

### Le plug-in Synchronizer

`Synchronizer.jsfx` est la forme autonome du même mécanisme, pour synchroniser d'autres plug-ins
JSFX sans GamePlayer : placé sur une piste dédiée, il produit le compteur sur ses canaux 1 et 2,
que l'on envoie aux pistes à synchroniser ; son commentaire d'en-tête donne le code de décodage.
