---
title: "CMGS — fragment instances"
lang: fr-FR
---

# La communication entre plug-ins

## Plusieurs instances d'une application (projet)

*Réflexion du 22 novembre 2026 : rien n'est encore réalisé.*

### Le besoin

Aujourd'hui, chaque type de plug-in de CMGS suppose qu'il est seul de son type dans la session REAPER. Trois usages
demandent de lever cette limite :

- plusieurs instances d'une même application, actives en même temps : par exemple plusieurs Interstys, chacun sur sa
  piste, avec ses lignes, ses lecteurs et ses effets ;
- des applications associées : une application commandée par une autre (un ScriptMaster piloté par le Game Master),
  qui affiche une fenêtre auxiliaire de l'application principale, ou effectue des calculs pour elle, éventuellement en
  parallèle (§ 7.3) ;
- deux plug-ins de CMGS qui encadrent, sur une même piste, une chaîne d'effets traditionnels : le premier fournit les
  sons, le dernier les recueille, comme une table de mixage (§ 7.4).

Le principe retenu : une seule zone globale par type de plug-in, pour tous les paramètres de ce type, comme
aujourd'hui ; et, pour chaque instance active (une vingtaine), un petit emplacement réservé dans gmem, alloué
dynamiquement dans un pool, par lequel elle communique avec les autres et avec le script auxiliaire. L'une des choses
qu'on peut lui demander est d'exposer ses paramètres dans la zone de son type, ou de les y relire.

### Ce qui empêche aujourd'hui deux instances

| Élément de gmem | Problème |
|---------------------------------------------|-----------------------------------------------------------|
| la plage de paramètres du type, dans `gmem[paramGCopy + n]` (Interstys 256 à 511, Diffusion-3 512 à 639…) | deux instances y publieraient en même temps ; un `set` venu d'une autre application irait à l'une ou à l'autre |
| la boîte aux lettres du script auxiliaire (`dateRqst`, `dateCfrm`, `cmndKode`, `cmndPar1` à `3`, `scptPar1` à `3`, `rtrnVal1` à `4`) | elle est unique et sans adresse : deux requêtes rapprochées s'écrasent (l'export du journal par `p`, l'écriture d'un fichier…) |
| la chaîne échangée (`expldwstr`, `xplStr1`, `xplStr2`) | même problème |
| les noms des fichiers produits (`syslog-<Plugin>-<date>.txt`, les exports) | deux instances peuvent écrire le même nom dans la même seconde |

Ne gênent pas : les messages `event` (internes à chaque plug-in), la mémoire mSL (propre à chaque instance),
l'automation de REAPER (par instance), les variables `shvar0` à `shvar9` (globales, c'est voulu), le temps commun et
le compteur d'échantillons (§ 7.1).

### Le précédent : les unités du Game Master

Les FilePlayers sont déjà multiples : chacun occupe un bloc de contrôle d'unité (UCB : 128 blocs de 400 mots à partir
de `UGAddr` = 0x300), avec un identifiant unique (`cbRUniq`, attribué par `idAlloc`), un type (`cbType` : `uPlayer`,
`uMIDI_In`…), un état (`cbStat`) et une date de dernière utilisation (`cbUSt`). Ce mécanisme, conçu pour le protocole
des lecteurs (les commandes `Kmd…`, les paramètres de jeu), reste tel quel ; le pool proposé ici en reprend les idées
pour toutes les applications, avec des emplacements plus petits et un protocole général.

### Les emplacements d'instance

Un pool de 24 emplacements de 256 mots (6 144 mots), à une adresse fixe déclarée dans `mSL_gmem_map`, pour que le
script auxiliaire la connaisse aussi :

| Mots | Contenu |
|------------|----------------------------------------------------------------------|
| 0 | la marque `'inst'` (0 : emplacement libre) |
| 1 | le propriétaire : l'identifiant unique de l'instance (la réservation, ci-dessous) |
| 2 | le type d'application (Game Master, FilePlayer, ScriptMaster, Interstys, Diffusion-3, MIDI) |
| 3 | le numéro d'instance dans son type (1, 2, 3…) |
| 4 | le battement de cœur : `time_precise()` au dernier passage dans `@gfx` |
| 5 | l'état : indicateurs (exposée, fenêtre ouverte, occupée, en erreur…) |
| 6, 7 | la version du protocole, la version de l'application |
| 8 à 23 | le nom (16 mots, 6 caractères par mot, comme `mSL_g6packStr`) |
| 24 à 31 | la requête au script auxiliaire : date, code, trois paramètres, valeur rendue (la boîte de 0x30, par emplacement) |
| 32 à 159 | l'anneau des commandes reçues : 8 entrées de 16 mots (émetteur, séquence, code, 13 arguments), index d'écriture et de lecture |
| 160 à 191 | les réponses |
| 192 à 255 | une chaîne échangée (64 mots, 383 caractères) |

### Réservation, battement de cœur, libération

- À `@init`, l'instance tire un identifiant (`rand()` et `time_precise()`), parcourt le pool, et réserve le premier
  emplacement libre ou abandonné par `atomic_setifequal(gmem[e + 1], 0, id)`. Elle relit le mot : s'il porte son
  identifiant, l'emplacement est à elle. Deux instances qui s'initialisent en même temps ne peuvent pas prendre le
  même. Les fonctions `atomic_*` opèrent aussi sur gmem ; elles sont déjà employées dans le code (Diffusion-3).
- L'instance écrit son battement de cœur à chaque passage dans `@gfx`, qui tourne même fenêtre fermée
  (`options:gfx_idle`).
- Un emplacement dont le battement a plus de 5 s est abandonné (instance supprimée, mise hors ligne, plantage) : une
  autre instance peut le reprendre, par `atomic_setifequal` sur l'ancien identifiant.
- Une instance qui trouve son emplacement repris (après une longue interruption de son `@gfx`) en réserve un autre, et
  le signale dans le journal.
- Le numéro d'instance dans le type est celui enregistré avec le projet s'il est libre, sinon le plus petit numéro
  libre pour ce type.

### L'identité d'une instance

- Interne : le numéro d'emplacement (0 à 23) et l'identifiant ; ils changent d'une session à l'autre.
- Visible : le type, le numéro d'instance (Interstys 1, Interstys 2…) et un nom, enregistrés avec le projet
  (`@serialize`) : un script retrouve la même instance d'une session à l'autre.
- Pour REAPER : un slider caché « Instance » porte l'identifiant (comme les sliders génériques Ctl). Le script
  auxiliaire, qui lit les paramètres des effets (`TrackFX_GetParam`), trouve ainsi la piste et la position de chaque
  instance ; il peut lui donner le nom de sa piste.

### La zone de type et l'instance exposée

- Un en-tête par type (quelques mots) désigne l'emplacement de l'instance exposée, avec une séquence.
- Seule l'instance exposée publie ses paramètres dans la plage de son type, et lit les changements que d'autres y
  écrivent, comme le fait aujourd'hui l'application unique. Les autres gardent leurs paramètres pour elles.
- Trois commandes :
  - exposer : prendre la plage, y publier ses valeurs, prévenir l'instance qui l'avait ;
  - relire : importer les valeurs présentes dans la plage (pour copier un réglage d'une instance à une autre) ;
  - libérer : rendre la plage.
- À décider : l'instance exposée par défaut (la première chargée ; celle dont la fenêtre a servi en dernier, par une
  exposition automatique ; ou seulement sur commande), et le sort d'un `set` qui vise un paramètre d'une instance non
  exposée (transmis par sa boîte, comme une commande ; ou une erreur, comme 0621 aujourd'hui pour un paramètre d'une
  autre application).

### Les messages entre instances

- Écrire : l'émetteur réserve une entrée de l'anneau du destinataire par `atomic_add` sur l'index d'écriture, remplit
  l'entrée, puis écrit sa séquence en dernier. Le destinataire ne lit une entrée qu'une fois sa séquence écrite : c'est
  le principe de `prv_seq` dans Diffusion-3-Projectors.
- Lire : le destinataire traite ses entrées dans l'ordre, dans `@gfx` (ou dans `@block` pour une commande audio), et
  avance l'index de lecture. Si l'anneau est plein, l'émetteur reçoit une erreur.
- Répondre : dans la zone de réponses de l'émetteur, avec la séquence de la demande.
- Diffuser : un message à toutes les instances d'un type est un envoi à chacun des emplacements de ce type.
- Les commandes datées en échantillons restent possibles (§ 7.1.7).

### Le script auxiliaire

- Une requête par emplacement (les mots 24 à 31), au lieu de la boîte unique de 0x30 : le script parcourt les
  emplacements actifs à chaque passage, et sert les requêtes dans l'ordre de leurs dates.
- La boîte de 0x30 reste, pour la compatibilité (le Game Master, les versions précédentes).
- `CMGS-auxiliary-src.eel` inclut `mSL_gmem_map` : la carte du pool lui est commune avec les plug-ins ; le script
  régénéré (`make_auxiliary.py`) accompagne la nouvelle version des plug-ins.
- Les fichiers écrits portent le numéro d'instance : `syslog-Interstys-2-<date>.txt`.

### Ce que verraient mSL et l'interface

- mSL : lister les instances (type, numéro, nom, état) ; envoyer à une instance (désignée par son type et son numéro,
  ou par son nom) une commande, un bloc de réglages ou un message ; exposer, relire.
- L'interface : Main Infos affiche « Interstys 2 / 3 — exposée » ; le menu des modules propose « Expose
  parameters » ; un module « Instances » pourrait montrer le pool.

## Applications associées

### Une application au service d'une autre

Une instance peut se mettre au service d'une autre : par exemple un ScriptMaster commandé par le Game Master. Le
maître lui envoie des commandes par son emplacement (§ 7.2.8) ; le serviteur rend compte par sa zone de réponses et sa
chaîne. Deux usages :

- une fenêtre auxiliaire : le serviteur affiche une vue de l'application principale (un grand journal, la liste des
  clips joués, le graphe d'un patch, une vue 3D) dans une autre fenêtre, éventuellement sur un autre écran ;
- des calculs : le maître confie au serviteur un travail long (une analyse, une recherche, une génération) et poursuit
  le sien.

### Une fenêtre auxiliaire

- Le serviteur ne voit pas la mémoire du maître (`mem[]` est propre à chaque instance) : il n'affiche que ce que le
  maître publie dans gmem (état, paramètres, petites tables, lignes de journal), dans son emplacement ou dans une zone
  d'échange réservée pour l'occasion.
- Les gestes faits dans la fenêtre auxiliaire reviennent au maître sous forme de commandes.
- Le débit reste celui de gmem : une vue qui demande beaucoup de données (des formes d'onde) doit les résumer, ou les
  lire elle-même dans les fichiers.

### Calculer en parallèle dans @block

REAPER traite les pistes sur plusieurs fils audio, donc sur plusieurs cœurs : le `@block` d'un plug-in placé sur sa
propre piste s'exécute en parallèle avec ceux des autres pistes. Le `@gfx` de toutes les instances, lui, partage le
fil graphique. Un calcul découpé en tranches dans `@block` avance donc en parallèle du maître, avec ces précautions :

- chaque tranche doit tenir dans une petite fraction de la durée d'un bloc, sinon l'audio de la piste, et de toute la
  session, décroche ;
- `@block` ne tourne que lorsque REAPER traite l'audio (en lecture, ou à l'arrêt si les effets y sont exécutés,
  selon les préférences) ;
- le traitement anticipé (*anticipative FX processing*) peut exécuter des blocs en avance sur le temps réel : le temps
  de `@block` n'est pas celui de l'horloge ;
- les échanges avec le maître passent par gmem, avec des séquences et des fonctions atomiques (pas de jeton : les deux
  instances n'ont aucune mémoire commune en dehors de gmem) ;
- la piste du serviteur ne produit pas de son (sortie nulle, piste sans envoi).

Le serviteur peut aussi exécuter des processus mSL, comme le ScriptMaster aujourd'hui ; mais ils tournent dans son
`@gfx`, donc dans le fil graphique commun : seul `@block` apporte un vrai parallélisme.

## Encadrer une chaîne d'effets : la source et le collecteur

### Le principe

Deux plug-ins de CMGS, sur une même piste, encadrent un ou plusieurs effets traditionnels (réverbérations, filtres,
plug-ins VST…) :

- la source, en tête de la chaîne, fournit les sons sur les canaux de la piste (un Interstys, un FilePlayer, un
  générateur) ;
- les effets les transforment ;
- le collecteur, en fin de chaîne, les recueille. Il se comporte comme une table de mixage (gains, coupures, groupes,
  format de sortie), et place le résultat sur les canaux que la piste envoie à la piste Master ou à une sous-piste.

### Ce que porte l'audio, ce que porte gmem

- Les sons passent par l'audio de la piste, d'un effet à l'autre, comme pour tout effet de REAPER.
- Les informations (ce que porte chaque canal, les niveaux, les ordres de mixage) passent par les emplacements des
  deux instances (§ 7.2.4).
- Sur une même piste, REAPER exécute les effets dans l'ordre : pour un bloc donné, le `@block` de la source précède
  celui du collecteur. Une information écrite par la source pendant un bloc est donc lue par le collecteur dans le même
  bloc, à la latence des effets intermédiaires près (§ 7.4.4).

### L'appairage

Le collecteur doit connaître sa source. Trois moyens :

- par l'audio : la source réserve deux canaux (par exemple les deux derniers de la piste) et y code, comme le compteur
  d'échantillons du § 7.1, son identifiant et le numéro de l'échantillon ; les effets intermédiaires ne doivent pas
  toucher ces canaux (le routage des broches des effets de REAPER le permet) ; le collecteur décode, et trouve
  l'emplacement de sa source. Cette méthode est automatique, et résiste au déplacement des effets et des pistes ;
- par un nom : la source et le collecteur portent le même nom d'appairage, enregistré avec le projet ;
- par le script auxiliaire : il sait que les deux instances sont sur la même piste.

Le premier moyen est le plus sûr.

### La latence

- Les effets intermédiaires peuvent retarder l'audio (une latence qu'ils déclarent à REAPER) : l'audio arrive alors au
  collecteur en retard sur les informations écrites par la source dans le même bloc.
- Le numéro d'échantillon porté par l'audio (l'appairage par l'audio) règle ce problème : la source date ses
  informations en échantillons ; le collecteur les applique quand l'audio de cette date lui parvient.

### Le collecteur, une table de mixage

- Entrées : les canaux de la piste (128 au plus) ; pour chacun, un gain, une coupure, un solo, un groupe.
- Sorties : un format choisi (stéréo, quadriphonie, 8 canaux, la disposition de Diffusion-3…), placé sur les premiers
  canaux de la piste ; les autres canaux sont mis à zéro.
- Le routage vers la piste Master ou une sous-piste reste celui de REAPER (envoi au parent, envois, nombre de canaux de
  la piste) : un JSFX ne peut pas envoyer de son hors de sa piste.
- Le collecteur peut aussi mesurer et protéger : VU-mètres, limiteur (les moteurs de GM-Meters existent déjà).

### Les limites

- 128 canaux par piste au plus.
- Un effet traditionnel stéréo ne traite que deux canaux : pour en traiter plus, il faut plusieurs instances de
  l'effet, ou un routage des broches.
- Les canaux d'appairage doivent traverser les effets intacts.

## Étapes et décisions

### Les étapes

1. Le pool, l'identité et le battement de cœur ; l'affichage dans Main Infos.
2. La requête au script auxiliaire par emplacement, et les noms de fichiers numérotés : l'export du journal fonctionne
   avec plusieurs instances.
3. La zone de type et l'instance exposée : exposer, relire, libérer.
4. Les messages entre instances, et leur adressage en mSL.
5. Les applications associées : la fenêtre auxiliaire, les calculs en tranches dans `@block`.
6. La source et le collecteur : l'appairage par l'audio, les informations datées, la table de mixage.

### Les décisions à prendre

- Le nombre d'emplacements (24 proposés) et leur taille (256 mots).
- L'instance exposée par défaut.
- Le sort d'un `set` qui vise une instance non exposée.
- Le Game Master : rejoindre le pool, ou garder ses unités telles quelles.
- La forme de l'adressage en mSL : par numéro, par nom, ou les deux.
