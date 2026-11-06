# Bibliothèque d'algorithmes d'Interstys

Des recettes prêtes à l'emploi, pensées pour la création sonore : chaque fichier `.mSL` se dépose dans la
fenêtre d'Interstys et installe aussitôt un algorithme complet, branché sur la piste.

## Utilisation

- **Déposer** un fichier `Matrix-….mSL` dans Interstys : le son de la piste (`In:0`) passe dans
  l'algorithme, le son sec et le son traité sortent vers `Out:0`.
- **Régler** : les paramètres sont sur la ligne `Instance` en bas de chaque fichier (le nombre de canaux
  `nch`, les durées, les fréquences, les niveaux `dry` et `wet`). Modifier la ligne, puis redéposer le
  fichier : l'instance est refaite. Les autres réglages se changent à la main dans les pads des effets
  de l'instance (le module Instances la montre).
- **Essayer sans matériau** : `Sources.mSL` met des clics (ou un buzz) sur le bus 64, que toutes les
  recettes écoutent en plus de leur entrée. `Sources-Stop.mSL` l'arrête.
- **Tout retirer** : `Free-All.mSL`.
- **Plusieurs canaux** : mettre `nch` au nombre de canaux de la piste (jusqu'à 128). Sur une piste
  stéréo, `nch 2`.

**L'effet principal s'affiche** : chaque recette se termine par `Display Effect …` (son effet principal :
`fdn`, `fl`, `ph`, `sh`, `nz`, `rnd`, `rg`, ou pour un Math `fol`, `rect`, `gt`), qui le montre dans un module Effect de l'onglet courant : celui qui le montre déjà,
sinon un module Effect qui montre un effet qui n'existe plus, sinon un nouveau module Effect, à la fin du
panneau qui en a le moins. `Display` montre aussi un reader, un writer, une ligne ou une courbe
(`Display Reader r`, `Display Line l`, `Display Curve c`), ou un module par son nom, celui du menu des modules
(`Display "Globals"`, `Display "System Log"`, `Display "Patch"`…).
`Remove` fait l'inverse : `Remove "Globals"` retire le module de l'onglet courant, `Remove Effect fdn` les vues
de l'onglet qui montrent cet effet (le module n'est pas supprimé : c'est `Free`).
`Display Instance essaim` et `Remove Instance essaim` font de même pour tous les modules d'une instance. Depuis
une autre table (un script lancé plus tard), `essaim:fl` désigne l'effet `fl` de l'instance `essaim` :
`Display Effect essaim:fl`, `Dump Effect essaim:fl`, `Remove Effect essaim:fl`.

La première fois qu'on dépose un fichier, le journal note une erreur 2787 : le fichier retire d'abord une
instance précédente, qui n'existe pas encore. C'est sans conséquence.

## Les recettes de la Matrix (réseau de retards bouclés)

| Fichier | Ce qu'il fait |
|---|---|
| `Matrix-Espace` | Un espace dense : toutes les lignes mélangées à chaque passage (Hadamard) |
| `Matrix-Traines` | Des traînes locales : chaque canal garde la sienne, qui déborde lentement (Householder) |
| `Matrix-Metal` | Un métal accordé : toutes les lignes au même retard, un seul peigne résonant |
| `Matrix-Accord` | Un accord métallique : des retards multiples d'une période |
| `Matrix-Masse` | Une masse qui enfle : la boucle croît (Grow) et sature |
| `Matrix-Pompe` | Un pompage collectif : un couplage négatif entre les lignes |
| `Matrix-Souffle` | Une traîne qui respire : sa durée balayée par un LFO très lent |
| `Matrix-Tenue` | Une pédale de tenue : la durée de la traîne sur un curseur Ctl (automatisable, MIDI) |
| `Matrix-Repandu` | Une source mono sur tous les canaux : le canal 0 dans toutes les lignes |
| `Matrix-Anneau` | Un anneau : chaque écho passe au haut-parleur voisin, le son tourne (Ring) |
| `Matrix-Ondule` | Une traîne qui ondule : les retards modulés lentement, déphasés d'une ligne à l'autre |
| `Matrix-Vrille` | Une vrille métallique : des retards courts modulés à vitesse audio |

Chaque recette se compose de trois effets : `pre` (l'entrée et le bus d'essai), `fdn` (la Matrix),
`post` (le mélange sec et traité vers la sortie) ; `Matrix-Souffle` y ajoute un LFO.

## Les recettes du Flanger et du Chorus (retards modulés)

| Fichier | Ce qu'il fait |
|---|---|
| `Flanger-Jet` | Un jet : le mode Through-zero, le balayage traverse le son direct et l'annule au passage |
| `Flanger-Plaque` | Une plaque de métal qui glisse : des retards très courts, une réinjection près de 1 |
| `Flanger-Hurle` | Une boucle qui hurle : la réinjection dépasse 1, la boucle sature et chante seule, sa hauteur saute au hasard |
| `Flanger-Spirale` | Une spirale sans fin : le barber pole, un balayage qui monte toujours (et tourne entre les haut-parleurs) |
| `Flanger-Escalier` | Un escalier de hauteurs : le barber pole à retards longs transpose, chaque écho monte |
| `Flanger-Cloche` | Une cloche : le retard modulé à vitesse audio, une modulation de phase inharmonique |
| `Chorus-Essaim` | Un essaim : seize voix par canal, chacune à sa vitesse et son retard |
| `Chorus-Ivre` | Une bande ivre : de grands retards qui dérivent, la hauteur tangue |

Chaque recette se compose de trois effets : `pre` (l'entrée et le bus d'essai), `fl` (le Flanger ou le
Chorus), `post` (la sortie ; le mélange sec et traité pour `Escalier`, `Cloche`, `Essaim` et `Ivre`). Dans
`Jet`, `Plaque` et `Spirale`, le son direct passe dans l'effet : son mélange (`blend`, de -100 à 100 %) règle le flanger.

`Flanger-Hurle` ne s'arrête plus une fois excité (la boucle s'entretient) : `regen` sous 1, ou
`Free-All.mSL`.

## Les recettes du Phaser (filtres passe-tout balayés)

| Fichier | Ce qu'il fait |
|---|---|
| `Phaser-Vent` | Un vent : le phaser classique, lent et profond, la réinjection creuse des sifflements |
| `Phaser-Vortex` | Un tourbillon sans fin : le barber pole, des creux qui montent toujours (et tournent entre les haut-parleurs) |
| `Phaser-Cristal` | Un cristal : trente-deux étages résonants, espacés, une réinjection forte |
| `Phaser-Grele` | Une grêle : les creux sautent au hasard, plusieurs fois par seconde |
| `Phaser-Bourdon` | Un bourdon : le balayage à vitesse audio, le son vrombit |
| `Phaser-Laser` | Un laser : soixante-quatre étages fixes, chaque attaque devient un chirp |

Les effets sont `pre`, `ph` (le Phaser) et `post`. Le son direct passe dans le Phaser (son mélange
`blend`), sauf dans `Phaser-Laser` (`dry` et `wet`).

## Les recettes du Shimmer (le Matrix avec un transpositeur dans chaque ligne)

| Fichier | Ce qu'il fait |
|---|---|
| `Shimmer-Ciel` | Un ciel : la traîne monte d'octave en octave, le shimmer classique |
| `Shimmer-Abime` | Un abîme : la traîne descend d'octave en octave et s'enfonce dans le grave |
| `Shimmer-Quinte` | Une quinte : les lignes paires montent d'une octave, les impaires d'une quinte, un accord qui s'élève |
| `Shimmer-Derive` | Une dérive : des intervalles infimes, la traîne se désaccorde lentement sans fin |
| `Shimmer-Givre` | Un givre : des grains très courts transposés très haut, une poussière scintillante |

Les effets sont `pre`, `sh` (le Shimmer) et `post` (le son sec et le son traité : `dry`, `wet`). `thick` règle
le nombre de lignes du réseau (8 et plus : une traîne dense, même en stéréo).

## Les recettes du Noise (bruits, impulsions, applications chaotiques)

| Fichier | Ce qu'il fait |
|---|---|
| `Noise-Static` | Des parasites : des impulsions au hasard (Dust), chacune sur un haut-parleur |
| `Noise-Rafale` | Une rafale : un bruit rose dans un passe-bande que balaie un LFO lent |
| `Noise-Velours` | Un velours : des impulsions serrées (Velvet), un souffle plus doux que le blanc |
| `Noise-Crepite` | Un crépitement : l'application chaotique Crackle, des braises qui craquent |
| `Noise-Cascade` | Une cascade de périodes : l'application logistique, un son qui glisse et se dédouble |
| `Noise-Static2` | Un bruit rose dont la corrélation des canaux suit un LFO lent : l'image passe du diffus au centre |
| `Noise-Fracas` | Un fracas : le rumble seul, un bruit très grave qui enfle et retombe, autrement sur chaque haut-parleur |
| `Noise-Epines` | Des épines : le bruit blanc à la puissance 5 (`power`), il ne reste que des pointes éparses |

Ces recettes ne prennent pas d'entrée : le bruit sort vers `Out:0`. L'effet principal est `nz` (le Noise) ;
`Noise-Rafale` y ajoute `lfo` et `wf` (le filtre), `Noise-Cascade` et `Noise-Static2` un `lfo`. Chaque canal
a son propre bruit : `corr` (de 0 à 1) y mélange un bruit commun, de l'image diffuse à la source au centre. Les niveaux
(`output`) sont ceux des crêtes, comme les lit un crête-mètre : chaque couleur est calibrée sur le bruit blanc. La
couleur `Mix` passe continûment du brun au rose, au blanc puis au violet (`tilt`, de -6 à +6 dB/oct) ; `power`
élève chaque échantillon à une puissance (sign(x) |x|^e : 2, 3, 5… des grains de plus en plus épars ; 0 : un bruit
binaire) ; `rumble` mêle un grondement très grave et mouvant (`rfreq`, sa fréquence).

## Les recettes du Random (signaux de commande aléatoires)

| Fichier | Ce qu'il fait |
|---|---|
| `Random-Errance` | Une errance : la traîne d'une Matrix s'allonge et se raccourcit au hasard, sans période |
| `Random-Tangage` | Un tangage : le retard d'un Chorus marche au hasard, la hauteur dérive comme une bande qui tangue |
| `Random-Sauts` | Des sauts : un filtre résonant saute d'une fréquence à l'autre (13 paliers), à des instants irréguliers |
| `Random-Pouls` | Un pouls : la densité d'un Noise Velvet marche au hasard, les impulsions accélèrent et ralentissent |
| `Random-Drops` | Des gouttes : des impulsions au hasard (Noise Dust) déclenchent les sauts d'un filtre résonant |
| `Random-Wah` | Un wah-wah au hasard : chaque attaque du son (son enveloppe) déplace un filtre résonant sur ce son, en glissant |

L'effet affiché est `rnd`, le Random : ses réglages (mode Step, Smooth ou Walk ; loi Uniform, Gauss, Binary ou
Curve ; horloge commune ou propre à chaque canal…) changent le caractère de la recette. Un Random module une
entrée de modulation (`mod … Effect rnd`) : comme un LFO, mais sans période.
Sa source est un déclenchement : chaque front montant au-dessus du seuil (`thresh`) donne une nouvelle valeur et
relance son horloge (`rate 0` : les déclenchements seuls) ; `detect Env` : les attaques d'un son (son enveloppe).

## Les recettes du Math (opérations sur les câbles)

| Fichier | Ce qu'il fait |
|---|---|
| `Math-Contour` | Un bruit qui parle : l'enveloppe du son (Env) imposée à un bruit rose (Mul) |
| `Math-Redresse` | Un redresseur : la valeur absolue du son (Abs), une octave au-dessus, rugueuse |
| `Math-Porte` | Une porte : Env, Gate, Slew puis Mul, le son ne passe qu'au-dessus d'un seuil, canal par canal |

Un Math lit une source A (`source`, ou `src1`) et une source B facultative (`src2` ; sans elle, `value`), et donne
`offset + amp × l'opération`. Ses effets se chaînent : un suiveur d'enveloppe, une porte, un adoucissement, un VCA.

## Les recettes du Ring (modulateur en anneau, AM, décaleur de fréquence)

| Fichier | Ce qu'il fait |
|---|---|
| `Ring-Gong` | Des gongs : le modulateur en anneau, un son métallique, inharmonique ; chaque canal a sa porteuse |
| `Ring-Glisse` | Un glissement : le spectre descend de quelques Hz (Down) et dérive au rythme d'un LFO lent |
| `Ring-Tourne` | Un tournoiement : un trémolo (AM) dont la crête passe d'un haut-parleur au suivant |

Un Ring multiplie sa source A par une porteuse : la source B si elle est branchée (`src2`), sinon son oscillateur
(`freq`, `wave`, `detune` et `spread` d'un canal au suivant). Modes : `Ring`, `AM` (`amount`), `Up` et `Down` (le
décaleur de fréquence).
