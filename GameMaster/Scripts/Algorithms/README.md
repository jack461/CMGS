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
`fdn`, `fl`, `ph` ou `sh`), qui le montre dans un module Effect de l'onglet courant : celui qui le montre déjà,
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
