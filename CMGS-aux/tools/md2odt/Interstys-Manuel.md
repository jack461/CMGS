---
title: "Interstys"
subtitle: "Délai fractionnaire modulaire pour REAPER — Manuel de l'utilisateur"
author: "Jean-Jacques Girardot"
date: "Octobre 2026 — document de travail"
lang: fr-FR
toc-title: "Table des matières"
---

# Présentation

## À quoi sert Interstys

Interstys est un plug-in JSFX de la suite CMGS (*Concrete Music Gran Studio*). C'est un **délai
fractionnaire modulaire** : il enregistre le son dans des mémoires (les *lignes*), le relit à des
vitesses et des retards quelconques, le transforme par des *effets*, et relie tous ces éléments par des
*câbles*, à la manière d'un synthétiseur modulaire.

Il permet, par exemple :

- des échos et des délais multiples, avec retour (*feedback*), sur un nombre quelconque de canaux ;
- la lecture de fichiers son à vitesse variable, en avant ou en arrière, en boucle sur une région ;
- des chaînes de traitement (filtres, saturations, mélangeurs) modulées par des LFO ou par des
  curseurs automatisables de REAPER ;
- la description complète d'un patch dans un script mSL, et la création de *sous-patchs*
  réutilisables (les *algorithmes*).

## Capacités

| Élément | Nombre | Remarque |
|---|---|---|
| Lignes (mémoires audio) | 256 | jusqu'à 128 canaux et 67 108 864 échantillons chacune |
| Readers (lecteurs) | 256 | mode lecture ou mode délai |
| Writers (enregistreurs) | 256 | une source, un mode de recouvrement |
| Effets | 256 | Mixer, Auto Mixer, LFO, Filter, Saturation |
| Canaux de la piste | 256 | entrées `In` et sortie `Out` |
| Bus utilisateur | 64 | largeur automatique |
| Cellules de contrôle | 64 | dont 32 écrites par des curseurs automatisables |
| Instances d'algorithmes | 64 | et 32 modèles |

Ces nombres sont fixés au début du fichier `Interstys.jsfx` (`RD_CNT`, `WR_CNT`, `LN_CNT`, `FX_CNT`,
`CH_NB`, `NB_BUS`, `NB_CTL`, `NB_GSL`). La mémoire du plug-in est de 128 millions de mots
(`options:maxmem`) : une ligne de 10 s en 8 canaux à 48 kHz en occupe environ 3,8 millions.

## Installation

Interstys fonctionne avec **REAPER 7.25 ou plus récent**. Les fichiers `Interstys.jsfx` et le dossier
`GM-Libs/` doivent se trouver dans le dossier `Effects/` de REAPER (dans la distribution CMGS, sous
`Effects/CMGS/GameMaster/`). Le plug-in apparaît dans la liste des effets sous le nom
**Interstys modular fractional delay**.

Le script ReaScript `CMGS-auxiliary.eel`, s'il est lancé, rend deux services : il écrit le journal dans
un fichier texte (touche `p`) et il donne à Interstys le dossier du projet, qui sert aux noms de
fichiers relatifs des scripts.

## Sauvegarde

Tout ce qui est créé dans Interstys est sauvé avec le projet REAPER (ou un preset) :

- les lignes, readers, writers et effets, avec tous leurs réglages ;
- l'organisation de la fenêtre (onglets, panneaux, modules affichés) ;
- les noms des fichiers son lus dans les lignes ;
- les modèles et les instances d'algorithmes.

**Le contenu sonore des lignes n'est pas sauvé.** À l'ouverture du projet, chaque ligne qui avait été
remplie par un fichier son relit ce fichier automatiquement ; le journal l'indique par
« Lines : n file(s) read again, m error(s) ». Une ligne enregistrée par un writer revient vide.

# Principes

## Les cellules et les câbles

Toutes les données audio et de contrôle circulent dans un tableau de **cellules**. À chaque
échantillon, chaque module lit des cellules et en écrit d'autres. Les cellules sont groupées ainsi :

| Groupe | Notation | Rôle |
|---|---|---|
| Entrées | `In:c` | les canaux de la piste, lus au début de chaque échantillon |
| Sortie | `Out:c` | le bus de sortie, rendu à la piste à la fin de l'échantillon |
| Bus | `Bus n:c` | 64 bus utilisateur, numérotés à partir de 1 |
| Contrôles | `Ctl n` | 64 cellules de contrôle, numérotées à partir de 1 |
| Câbles propres | `Reader n:c`, `Effect n:c` | la sortie d'un reader ou d'un effet |
| Zéro | — | cellules toujours nulles : une entrée non branchée les lit |

Les canaux (`c`) sont numérotés **à partir de 0**, les modules, bus et contrôles **à partir de 1**,
comme dans les pads. Un câble de plusieurs canaux est désigné par son premier canal : un effet de
2 canaux dont la source est `In:0` lit `In:0` et `In:1`.

Deux règles, empruntées aux synthétiseurs modulaires :

- **un câble a une seule source.** Le câble propre d'un reader ou d'un effet n'est écrit que par lui ;
- **les bus et `Out` additionnent** toutes les sorties qui y sont envoyées. Ils sont remis à zéro à
  chaque échantillon. La largeur d'un bus est calculée automatiquement : c'est le plus grand
  « premier canal + nombre de canaux » demandé par ses utilisateurs.

Une sortie (d'un reader ou d'un effet) va soit dans son **câble propre** (« Own cable », la valeur par
défaut), soit dans `Out`, soit dans un bus. Une source peut être `In`, `Out`, un bus, une cellule de
contrôle, ou le câble propre d'un reader ou d'un effet.

## L'ordre de traitement

À chaque échantillon, Interstys exécute dans cet ordre :

1. la lecture des entrées de la piste (`In`, multipliées par le gain d'entrée) ; `Out` et les bus
   sont remis à zéro ;
2. les effets de la phase **Pre** (avant les readers) ;
3. les **readers** ;
4. les effets de la phase **Std** (phase standard) ;
5. les **writers** ;
6. les effets de la phase **Post** (après les writers) ;
7. l'écriture de `Out` dans la piste (multiplié par le volume de sortie).

Dans chaque phase, les effets sont exécutés **dans l'ordre des câbles** : un effet passe après les
effets dont il lit la sortie (câble propre, bus ou `Out`). Interstys calcule cet ordre lui-même chaque
fois que le patch change. Les effets indépendants gardent l'ordre de leurs numéros. Une boucle de
rétroaction (un effet A lit B qui lit A) garde aussi l'ordre des numéros : le câble qui « remonte » la
chaîne a un retard d'un échantillon.

Pour les autres modules, un câble lu par un module placé plus loin dans cet ordre n'a pas de retard ;
un câble lu par un module placé avant a un retard d'un échantillon.

## Les entrées de modulation

Certains réglages peuvent être modulés par un câble : la vitesse et le volume d'un reader, le gain d'un
writer, la fréquence de coupure d'un filtre, etc. Une entrée de modulation a :

- une **source** (un câble, souvent un LFO ou une cellule de contrôle) et son canal ;
- une **profondeur** (*depth*), dans l'unité du réglage (octaves, dB, ms...) ;
- un **atténuverteur** (*att*), entre −10 et 10 (1 à la connexion) : il multiplie la profondeur, et
  l'inverse s'il est négatif.

La valeur effective est : *réglage de base + profondeur × atténuverteur × valeur du câble*. Une
entrée non branchée ne change rien, comme un jack normalisé. Une cellule de contrôle est lissée pour
éviter les clics.

## Le traitement des échantillons de la piste

Le module **Globals** choisit ce que fait Interstys du son de la piste (« Track Samples ») :

| Mode | Entrées `In` | Sortie de la piste |
|---|---|---|
| **Merge** | le son de la piste, multiplié par le gain d'entrée | `Out`, multiplié par le volume de sortie |
| **Ignore** | muettes (le son de la piste n'est pas lu) | `Out`, multiplié par le volume de sortie |
| **Pass** | — | le son de la piste, inchangé : Interstys ne traite rien |

Dans les modes Merge et Ignore, la piste ne contient que ce qu'Interstys écrit dans `Out` : pour
entendre aussi le son direct, il faut l'envoyer dans `Out` (par exemple par un Mixer dont une source
est `In:0`).

**Attention :** en mode Ignore, toute la chaîne qui part de `In` est muette.

# L'interface

## Onglets, panneaux et modules

La fenêtre d'Interstys est organisée en **onglets** (en haut). Chaque onglet contient de 1 à 4
**panneaux** (colonnes), et chaque panneau une pile de **modules**. Le menu du clic droit sur la barre
des onglets et sur les panneaux permet de :

- choisir les modules affichés (sous-menu **Modules**) : les quatre premiers groupes donnent huit
  vues des lignes (Line A à H), des readers, des writers et des effets ; viennent ensuite les autres
  modules, par ordre alphabétique ;
- déplacer, copier et coller un module ou un panneau, changer le nombre de panneaux, remettre les
  largeurs à zéro, vider un panneau ;
- renommer un onglet, décaler les onglets ;
- choisir un thème de couleurs et un style d'affichage.

Les vues A à H d'un même type sont indépendantes : chacune montre le module de son choix (par exemple,
Reader A montre le reader 1 et Reader B le reader 12). Le numéro montré par chaque vue est sauvé avec
le projet.

`Tab` et `Shift+Tab` passent à l'onglet suivant ou précédent. `Shift+←` et `Shift+→` changent la
largeur des panneaux sous la souris.

## Les pads

La plupart des modules présentent un **pad** : une grille de cellules (8 par ligne). Chaque cellule
affiche une information et réagit à la souris :

- **clic gauche** : l'action la plus courante (élément suivant, marche/pause, choix du canal...) ;
- **Shift + clic gauche** : souvent l'action inverse (élément précédent) ;
- **clic droit** : un menu (choix d'une source, d'un mode, d'une action...).

La cellule 0 de chaque pad donne le numéro du module affiché : un clic gauche passe au suivant,
Shift + clic gauche au précédent, un clic droit ouvre la liste. Si le module appartient à une instance
d'algorithme, son nom est ajouté : « Reader 4 (e1) ».

La dernière cellule de la première ligne, **Action**, ouvre au clic droit le menu des actions du
module (Copy, Paste, Clear, Create, Show, Delete...). **Show** et la touche `d` écrivent le contenu
brut du module dans le journal.

## Les curseurs

Sous le pad, les **curseurs** règlent les valeurs continues du module affiché. Un clic droit sur un
curseur lui rend sa valeur par défaut. Les curseurs des entrées de modulation (profondeur,
atténuverteur) n'apparaissent que si l'entrée est branchée ; l'atténuverteur s'affiche par un clic
gauche sur la cellule de l'entrée.

Les curseurs natifs de JSFX (en haut de la fenêtre de l'effet) sont masqués au démarrage : la touche
`S` les montre ou les cache. Ils sont conservés pour la compatibilité ; tous les réglages se font dans
les modules.

## Les formes d'onde

Les modules Line, Reader et Writer montrent la forme d'onde de leur ligne, avec la position des têtes
de lecture et d'écriture. Sous la souris :

| Touche | Action |
|---|---|
| `w` | montrer ou cacher la forme d'onde |
| `+`, `=` | agrandir la forme d'onde |
| `-` | la réduire |
| `v` | superposer les canaux ou les séparer |

Le curseur **Zoom** du reader agrandit la forme d'onde horizontalement autour de la position de
lecture.

# Le module Line

Une **ligne** est une mémoire audio : un tampon circulaire de un à 128 canaux. Les writers y
enregistrent, les readers la lisent. Une ligne peut aussi être remplie par un fichier son.

## Le pad

| Cellule | Contenu | Souris |
|---|---|---|
| 0 | Line *n* (et son instance) | gauche : suivante ; droit : liste |
| 1 | état : Undefined ou Ready | droit, ligne absente : Create |
| 2 | durée (s) | — |
| 3 | nombre d'échantillons | — |
| 4 | nombre de canaux | droit, ligne absente : le nombre de canaux à créer |
| 5 | fréquence d'enregistrement (Hz) | — |
| 6 | erreur 2610 si la mémoire a manqué | — |
| 7 | Action | droit : Clear, Create, Delete |

Pour créer une ligne : choisir sa durée (curseur **Line size**, Shift pour des secondes entières) et
son nombre de canaux (cellule 4), puis **Create** (cellule 1 ou Action). Une ligne existante ne change
pas de taille : il faut la supprimer (Delete) et la recréer. **Clear** remet son contenu à zéro.

## Le fichier de la ligne

Sous le pad, une cellule occupant toute la largeur montre le **fichier son** de la ligne (son nom, sans
le dossier), ou « No file ».

- **Déposer un fichier son** (WAV, AIFF, FLAC, MP3, OGG) sur cette cellule le lit **dans cette ligne** :
  la ligne est créée, ou remplacée si sa durée ou son nombre de canaux diffèrent ; ses readers et ses
  writers la suivent. La fréquence du fichier est conservée (cellule 5) : les readers la compensent.
- **Clic gauche** : le chemin complet s'affiche pendant 20 secondes ; un deuxième clic remet le nom.
- **Clic droit** : un menu : **Reload** (relire le fichier), **Forget the name** (oublier le nom sans
  toucher au son), **Path in the log** (écrire le chemin dans le journal).

Un fichier déposé ailleurs dans le module est lu dans la ligne affichée si elle a la bonne taille, et
sinon dans une nouvelle ligne.

Le nom du fichier est effacé quand la ligne est supprimée, remise à zéro (Clear) ou remplacée. Il est
sauvé avec le projet : à l'ouverture, la ligne relit son fichier. Si le fichier a disparu, le journal
l'indique (erreur 2771) et la ligne garde le nom : il suffit de remettre le fichier en place et de
faire **Reload**.

# Le module Reader

Un **reader** lit une ligne et envoie le son lu vers une sortie. Il a deux modes :

- **Reader** (mode lecture) : il parcourt la ligne à une **vitesse** quelconque (négative pour lire à
  l'envers), en boucle ou non, éventuellement sur une **région** ;
- **Delay** (mode délai) : il suit un **writer** avec un **retard** fixe ou modulé, pour faire des
  échos et des délais.

## Le pad

| Cellule | Contenu | Souris |
|---|---|---|
| 0 | Reader *n* (et son instance) | gauche : suivant ; droit : liste |
| 1 | état : Created, Ready, Paused, Reading | gauche : lecture ↔ pause ; droit : menu |
| 2 | mode : Reader ou Delay | droit : menu |
| 3 | ligne lue | droit : liste des lignes |
| 4 | durée de la ligne | — |
| 5 | nombre de canaux de la ligne | — |
| 6 | premier canal lu | droit : menu |
| 7 | nombre de canaux lus | droit : menu |
| 8 | Mute | gauche : muet ou non |
| 9 | Solo | gauche : solo ou non |
| 10 | sortie : câble propre, `Out` ou un bus | droit : menu ; gauche : premier canal |
| 11 | position de lecture (s) | — |
| 12 | vitesse | droit : plage du curseur Speed |
| 13 | mode délai : le writer suivi | droit : liste des writers |
| 14 | erreur | gauche : l'effacer |
| 15 | Action | droit : Copy, Paste, Clear, Rewind, Speed 1, Create, Activate, Show, Delete |

En mode lecture, une troisième ligne de cellules sert de **transport** :

| Cellule | Clic gauche | Shift + clic gauche | Clic droit |
|---|---|---|---|
| 16 `<<<` | lecture à −3 | vitesse −1/4 | vitesse −1/4 |
| 17 `<<` | lecture à −2 | vitesse −1/64 | vitesse −1/64 |
| 18 `<` | lecture à −1 | vitesse −1/1024 | vitesse −1/1024 |
| 19 boucle | type de boucle suivant | lecture ↔ arrêt | menu des boucles |
| 20 `[=]` | lecture ↔ pause | pause | longueur de la région |
| 21 `>` | lecture à 1 | vitesse +1/1024 | vitesse +1/1024 |
| 22 `>>` | lecture à 2 | vitesse +1/64 | vitesse +1/64 |
| 23 `>>>` | lecture à 3 | vitesse +1/4 | vitesse +1/4 |

Avec `Cmd` (Ctrl sous Windows), les vitesses des cellules 16 à 23 sont divisées par 4 ; avec `Alt`,
par 16.

Sous la souris, la touche `r` fait passer de la lecture à la pause et inversement ; `t` change la
longueur de la région (Full, 10 s, 1 s).

Un fichier son déposé sur le module Reader est lu dans une ligne (celle du reader si elle convient),
et le reader est relié à cette ligne.

## Les types de boucle

| Type | Comportement |
|---|---|
| once | lit la ligne une fois, puis s'arrête avec un fondu |
| repeat | lit la ligne en boucle (d'un bout à l'autre) |
| catch | lit normalement ; une fois entré dans la région, y reste en boucle |
| loop | démarre dans la région et y boucle |
| exit | lit jusqu'à la limite de la région, puis s'arrête avec un fondu |
| stop | s'arrête avec un fondu |

Les passages d'un bout de boucle à l'autre se font par un fondu enchaîné (curseur **Cross Fade**).

## Les curseurs

En mode lecture :

| Curseur | Plage | Rôle |
|---|---|---|
| Play Speed | ±32 (plage choisie en cellule 12) | vitesse de lecture (1 : vitesse normale) |
| Play Volume | −120 à 40 dB | volume de sortie |
| Play position | 0 à la durée | position de lecture |
| Loop Low Lim., Loop High Lim. | en s | limites de la région |
| Loop position, Loop Length | en s | position et longueur de la région |
| Cross Fade | 0,01 à 20 000 ms | durée des fondus de boucle |
| Zoom | 1 à 100 | zoom de la forme d'onde |

En mode délai : **Play Volume** et **Delay Offset** (le retard, en s).

## Les entrées de modulation

Une ligne de cellules sous le pad donne les trois entrées de modulation du reader :

| Entrée | Mode | Profondeur | Unité |
|---|---|---|---|
| Offset | délai | 0 à 5000 (défaut 2) | ms de retard |
| Speed | lecture | 0 à 32 (défaut 0,1) | vitesse |
| Volume | les deux | 0 à 2 (défaut 0,5) | fraction du volume |

Clic droit : choisir la source ; Shift + clic gauche : son canal ; clic gauche : montrer le curseur de
l'atténuverteur.

# Le module Writer

Un **writer** enregistre une source dans une ligne, en boucle. Il peut remplacer l'ancien contenu ou
s'y ajouter (*overdub*), ce qui donne avec un reader en mode délai un écho avec retour.

## Le pad

| Cellule | Contenu | Souris |
|---|---|---|
| 0 | Writer *n* (et son instance) | gauche : suivant ; droit : liste |
| 1 | état : Created, Ready, Paused, Writing | gauche : écriture ↔ pause ; droit : menu |
| 3 | ligne écrite | droit : liste des lignes |
| 4 | durée de la ligne | — |
| 5 | nombre de canaux de la ligne | — |
| 6 | premier canal écrit dans la ligne | droit : menu |
| 7 | nombre de canaux écrits (0 : tous) | droit : menu |
| 10 | source | droit : menu ; gauche : premier canal |
| 11 | position d'écriture (s) | — |
| 12 | mode : Overdub X-fade ou Overdub Sum | gauche : l'autre mode |
| 15 | Action | droit : Copy, Paste, Clear, Rewind, Reset, Create, Activate, Show, Delete |

Un writer sans ligne ou sans source reste dans l'état **Created**.

## Le recouvrement (overdub)

Le curseur **Overdub** (−150 à 150 %) règle la part de l'ancien contenu conservée à chaque passage :

- **X-fade** : *nouveau = gain × (ancien × overdub + source × (1 − min(1, |overdub|)))* ;
- **Sum** : *nouveau = ancien × overdub + gain × source*.

(*overdub* est ici la valeur du curseur divisée par 100, *gain* le gain d'enregistrement.) À 0 %, le
writer remplace le contenu. Une valeur négative inverse la polarité à chaque tour. Quand le gain de la
boucle dépasse 1, le contenu croîtrait sans fin : une saturation douce (tanh) le limite.

Le curseur **Record Gain** (−120 à 40 dB) règle le gain de la source.

## Les entrées de modulation

| Entrée | Profondeur | Unité |
|---|---|---|
| Gain | 0 à 60 (défaut 6) | dB |
| Overdub | 0 à 150 (défaut 20) | % |

# Le module Effect

Un **effet** lit une ou plusieurs sources, les traite, et écrit le résultat dans sa sortie. Chaque
effet a un **type**, choisi en cellule 1 ; le pad change selon le type.

## La partie commune

| Cellule | Contenu | Souris |
|---|---|---|
| 0 | Effect *n* (et son instance) | gauche : suivant ; droit : liste |
| 1 | type | droit : menu (crée l'effet si besoin) |
| 2 | phase : Std, Pre, Post | gauche : suivante ; droit : menu |
| 3 | On, Off, Bypass | gauche : On ↔ Off ; droit : Bypass ↔ On |
| 4 | nombre de canaux | droit : menu (1 à 128) |
| 5 | sortie : câble propre, `Out` ou un bus | droit : menu ; gauche : premier canal |
| 6 | état : OK, erreur, `...` (pas encore vérifié) | — |
| 7 | Action | droit : Copy, Paste, Clear, Auto gains, Create, Show, Delete |
| 23 | limiteur : Off, ou la réduction de gain en dB | clic : en service ou non |

- **Off** : l'effet n'est pas exécuté ; son câble propre devient silencieux.
- **Bypass** : la première source passe telle quelle vers la sortie (un LFO se tait).
- Le **limiteur automatique** (pas pour le LFO) protège la sortie : attaque 5 ms, relâchement 1,5 s.
  Il est en service par défaut pour une Saturation. La cellule passe au doré dès que la réduction
  dépasse 0,1 dB.

Le choix d'un nouveau type donne ses valeurs par défaut aux réglages du type (par exemple 1000 Hz,
Q 0,707 et passe-bas pour un Filter).

Les types Mover, Action et Script sont réservés : ils ne sont pas encore exécutés (erreur 2706).

## Mixer

Le **Mixer** additionne jusqu'à **8 sources**, chacune avec son gain.

- Ligne 1 (cellules 8 à 15) : les 8 sources. Clic droit : choisir la source ; clic gauche : son
  premier canal.
- Curseurs **Gain 1** à **Gain 8** (−120 à 20 dB), pour les sources branchées.

## Auto Mixer

L'**Auto Mixer** est un Mixer dont les gains sont calculés : chacune des *N* sources branchées reçoit
−20·log10(*N*) dB (−6,02 dB pour deux sources), si bien que la somme garde le niveau d'une source. Les
gains sont recalculés à chaque changement de source ; l'action **Auto gains** du menu les recalcule
aussi pour un Mixer.

## LFO

Le **LFO** (oscillateur basse fréquence) n'a pas de source : il produit un signal de modulation dans sa
sortie, sur autant de canaux que voulu.

- Cellule 8 : la forme : Sine, Triangle, Saw up, Saw down, Square (clic gauche : la suivante ; clic
  droit : menu).
- Curseurs : **LFO Frequency** (0,001 à 10 000 Hz), **LFO Amplitude** (0 à 10), **LFO Offset**
  (−10 à 10, ajouté au signal), **LFO Phase spread** (0 à 1 : le décalage de phase entre deux canaux
  successifs, en tours).

## Filter

Le **Filter** filtre une source (cellule 8 : clic droit, la source ; clic gauche, son premier canal).

- Cellule 9 : le **mode** : LP 1 pole, HP 1 pole (filtres du premier ordre), Low pass, High pass,
  Band pass, Notch (biquads). Clic gauche : le suivant ; clic droit : menu.
- Cellule 10 : la **pente** : 1, 2, 4 ou 8 étages (6 à 48 dB/octave pour un premier ordre, 12 à
  96 dB/octave pour un passe-bas ou passe-haut biquad). Les passe-bas et passe-haut à plusieurs étages
  sont des Butterworth dont le dernier étage porte la résonance.
- Curseurs : **Cutoff** (1 à 20 000 Hz), **Resonance** (Q, 0,1 à 1000), **Gain 1** (gain d'entrée).
- Entrées de modulation (ligne 2) : **Cutoff** (en octaves, profondeur 0 à 10, défaut 2) et **Reso**
  (en octaves, profondeur 0 à 4, défaut 1).

## Saturation

La **Saturation** déforme une source par une courbe non linéaire, avec suréchantillonnage.

- Cellule 9 : le **mode** :

| Mode | Courbe |
|---|---|
| Soft (tanh) | saturation douce |
| Hard clip | écrêtage à ±1 |
| Fold | repli triangulaire (*wavefolder*) |
| Sine fold | repli sinusoïdal |
| x − A sin(nx) | ½·(x − A·sin(n·x·π/2)) : ordre *n*, amplitude *A* |
| Chebyshev | polynôme de Tchebychev *T~n~* (ordre réel *n*) |
| Cheb. sum | somme pondérée de *T~1~* à *T~16~*, étirée |

- Cellule 10 : le **suréchantillonnage** : 1, 2, 4 ou 8 fois.
- Cellule 11 (mode Cheb. sum) : des **préréglages des harmoniques** : Fundamental only, Odd 1/k,
  All 1/k, Odd 1/k², Even 1/k, Random, Normalize, Clear.
- Curseurs : **Drive** (0 à 96 dB), **Bias** (−4 à 4), **Mix** (0 à 100 % de son traité),
  **Output** (−48 à 24 dB), **Order** (modes x − A sin et Chebyshev, 0 à 32), **Sine amount**
  (*A*, −8 à 8), **Stretch** (mode Cheb. sum, 0 à 16), **Gain 1** (gain d'entrée).
- En mode Cheb. sum, une zone graphique montre les **16 poids** des harmoniques, entre −1 et 1 :
  clic gauche ou glissé pour régler un poids, clic droit pour le mettre à 0 ; le poids sous la souris
  est affiché.
- Entrées de modulation : **Drive** (dB, profondeur 0 à 96), **Bias** (0 à 4), **Order** (l'ordre,
  ou l'étirement en mode Cheb. sum ; 0 à 32).

Un filtre anti-repliement et un filtre de composante continue (10 Hz) suivent la courbe.

# Le module Globals

Le module **Globals** regroupe les réglages généraux.

| Cellule | Contenu | Souris |
|---|---|---|
| 0 | Globals | — |
| 1 | nombre de canaux de la piste | — |
| 2 | Track Samples : Merge (vert), Ignore (orange), Pass (bleu) | gauche : suivant ; droit : menu |
| 3 à 6 | nombre de lignes, readers, writers, effets | — |
| 7 | Action | droit : Stop all, Pause all, Restart all, Rewind all, Clear all, Delete all structures |

Curseurs : **Input Gain** (en mode Merge) et **Output Volume** (en modes Merge et Ignore), de −120 à
40 dB. Le sens des modes Merge, Ignore et Pass est décrit au chapitre « Principes ».

**Delete all structures** supprime toutes les lignes, tous les readers, writers et effets.

# Le module Controls

Interstys déclare **32 curseurs automatisables** (sliders 129 à 160 de JSFX), de −1 à 1. Chacun écrit
une cellule de contrôle, `Ctl 1` à `Ctl 32`, que les modules peuvent prendre comme source (menu des
sources, sous-menu « Controls »). Ces curseurs peuvent être automatisés par des enveloppes de REAPER,
appris par un contrôleur MIDI, ou pilotés par un autre plug-in.

Le module **Controls** montre ces curseurs par pages de 8 : la cellule 0 porte le titre, les cellules
suivantes choisissent la page (clic gauche). Un clic droit sur un curseur le remet à 0.

# Le module Patch

Le module **Patch** montre l'état des câbles.

- Ligne 1 : les vues **In**, **Out**, **Buses**, **Controls**, **Cables** (clic gauche), la **page**
  (clic gauche : suivante ; clic droit : précédente), et le nombre de **problèmes**.
- La grille : une cellule par entrée, par sortie, par bus, par contrôle ou par câble propre. Couleurs :
  **vert** écrit et lu, **orange** écrit mais pas lu, **rouge** lu mais jamais écrit (un bus), **gris**
  inutilisé.
- Le texte : pour la cellule sous la souris, sa valeur, qui l'écrit et qui la lit.

Les problèmes comptés sont : les connexions invalides, les bus lus mais jamais écrits, les câbles
propres que personne ne lit.

# Le module Instances

Le module **Instances** montre les instances d'algorithmes (voir « Les algorithmes »).

- Ligne 1 : le nombre d'instances et de modèles ; cellule 7, **Action** (clic droit) : **Dump all**
  (le Dump de chaque instance dans le journal), **Templates in the log** (chaque modèle avec ses
  déclarations), **Free all instances**.
- La grille : une cellule par instance, à la place de son numéro, « nom : Modèle » (verte ; dorée si
  elle est sélectionnée). Clic gauche : sélectionner ; clic droit : **Dump** ou **Free** (supprime ses
  modules).
- Le texte : pour l'instance sous la souris (ou sélectionnée), son appel complet et le nombre de ses
  modules.

# Les modules système

Ces modules sont communs aux plug-ins CMGS.

## Main Infos

L'état général du plug-in : version, mémoire, threads mSL, statistiques.

## System Log

Le **journal** du système : messages, résultats des scripts, erreurs (« ERR: NNNN »). Sous la souris :

| Touche | Action |
|---|---|
| `p` | écrire le journal dans un fichier texte (`syslog-Interstys-date.txt`, dans le dossier du projet ; CMGS-auxiliary.eel doit tourner) |
| `P` | écrire le journal dans la console de CMGS-auxiliary.eel, pour le copier |
| `1` à `8` | nombre de colonnes |
| `j`, `k`, `↑`, `↓` | faire défiler (1 ou 10 lignes) |
| `→`, `←`, `z` | avancer de 100 lignes, revenir au début |
| `m`, `l` | augmenter ou réduire la hauteur |
| `t` | écrire l'heure |
| `Entrée`, `Espace` | écrire une ligne vide |

Le journal est un anneau d'environ 800 lignes : les plus anciennes sont remplacées.

## Memory 1 et Memory 2

Deux inspecteurs de la mémoire (débogage) : ils montrent le contenu de la mémoire à partir d'une
adresse, avec les flèches pour se déplacer (Shift : par pages).

## Scheduler et Processes Manager

Le **Scheduler** montre les tâches programmées des scripts mSL ; le **Processes Manager** montre les
threads mSL en cours, avec leur état. La touche `k` (commande système) arrête tous les threads.

# Le clavier

Interstys suit le schéma de clavier commun à CMGS : une touche est d'abord proposée au module sous la
souris, puis au panneau, aux commandes de l'onglet, aux commandes du plug-in, enfin aux commandes
système. La liste complète est dans `Documents/CMGS-Keys.md`.

| Touche | Niveau | Action |
|---|---|---|
| `d` | Line, Reader, Writer, Effect | contenu du module dans le journal |
| `r` | Reader | lecture ↔ pause |
| `t` | Reader | longueur de la région |
| `w`, `+`, `-`, `v` | Line, Reader, Writer | forme d'onde |
| `p`, `P`, ... | System Log | voir ce module |
| `Shift+←`, `Shift+→` | panneau | largeur des panneaux |
| `Tab`, `Shift+Tab` | plug-in | onglet suivant, précédent |
| `S` | plug-in | montrer ou cacher les curseurs natifs |
| `U` | plug-in | montrer ou cacher l'interface |
| `g` | système | lancer le ramasse-miettes |
| `k` | système | arrêter tous les threads mSL |
| `m`, `n` | système | parcourir la mémoire |

# Les scripts mSL

Interstys contient l'interpréteur **mSL** (*micro Script Language*) de CMGS. Un fichier `.mSL` déposé
n'importe où dans la fenêtre est compilé et exécuté. Ses `print` écrivent dans le journal.

## Les paramètres

Un script lit un paramètre par son nom court : `gui(\`slider, \`LineSize)` rend son descripteur
(`[1]` numéro, `[3]` valeur, `[4]` nom, `[5]` format), ou `$undef` si le nom est inconnu. Les noms
courts sont ceux de la déclaration des paramètres : `PlaySpd`, `PlayVol`, `LineSize`, `CrssFade`,
`WrOvrdb`, `LfoFreq`, `FltFreq`, `FltQ`, `SatDrive`...

## La table : décrire un patch

L'opération mSL **table** décrit des modules dans une liste de mots, `data(...)` :

```
var r = table(data(
    Interstys
    Line l  length 2  chan 2
    Writer w  line l  source In:0  overdub 40  status Writing
    Reader r  writer w  delay 0.375  out Out:0  status Reading
));
```

Le résultat est 0, ou le code de la première erreur. La table est une suite de **blocs** ; un bloc
commence par son mot de tête et finit au bloc suivant. Le premier mot `Interstys` est facultatif.

Dans un bloc :

- les **clés** vont par paires « clé valeur », dans n'importe quel ordre ; une clé omise garde la
  valeur du module, ou sa valeur par défaut s'il est créé ;
- les **unités** sont celles de l'interface : s, dB, Hz, %, octaves ;
- un module est désigné par un **numéro** (1 à 256) ou par un **nom** (un identificateur qui n'est
  pas un mot réservé). Un nom n'est valable que dans la table : il reçoit un module libre, qu'aucun
  numéro de la table ne désigne. Le journal indique « Interstys table : w = Writer 3 » ;
- les sources s'écrivent `In:c`, `Out:c`, `Bus n[:c]`, `Ctl n`, `Reader id[:c]`, `Effect id[:c]`, ou
  `none` ; les sorties `Own`, `Out:c`, `Bus n[:c]`.

La table est analysée en **quatre passes**, et **rien n'est modifié avant la dernière** : une erreur
n'importe où dans la table empêche tout changement. Les passes sont : les numéros, les noms, une
simulation (lignes, canaux, retards...), puis l'exécution.

### Line

```
Line id  [length s]  [chan n]  [spls n]  [file "nom.wav"]
```

Crée la ligne, la garde si elle est identique, la remplace sinon (ses writers et readers suivent).
`file` lit un fichier son dans la ligne : sa durée et ses canaux viennent du fichier (`length`,
`chan`, `spls` sont alors ignorés). Un nom relatif est cherché dans le dossier du projet, donné par
CMGS-auxiliary.eel (le journal indique « Project folder : ... »).

### Writer

```
Writer id  line L  source S  gain dB  overdub %  mode XFade|Sum  first n  used n
           status Ready|Paused|Writing
```

### Reader

```
Reader id  line L | writer W  delay s  speed x  out D  vol dB  first n  used n
           loop once|repeat|catch|loop|exit|stop  status Ready|Paused|Reading
```

`line` met le reader en mode lecture, `writer` en mode délai. L'état est appliqué en dernier.

### Effect

```
Effect id  type T  status On|Off|Bypass  phase Std|Pre|Post  chan n  out D  limiter On|Off
```

suivi des clés du type :

| Type | Clés |
|---|---|
| None | — |
| Mixer | `src1 S gain1 dB` ... `src8 S gain8 dB` |
| AutoMix | `src1 S` ... `src8 S` (gains calculés) |
| LFO | `freq Hz`, `mode` (Sine, Triangle, SawUp, SawDown, Square), `amp a`, `offset o`, `spread s` (pas de limiteur) |
| Filter | `source S`, `gain dB`, `freq Hz`, `q x`, `mode` (LP1, HP1, LP, HP, BP, Notch), `stages` (1, 2, 4, 8), `mod Cutoff S [depth d] [att a]`, `mod Reso S ...` |
| Saturation | `source S`, `gain dB`, `mode` (Soft, Hard, Fold, SineFold, XSin, Cheb, ChebSum), `drive dB`, `bias b`, `mix %`, `os` (1, 2, 4, 8), `output dB`, `order n`, `stretch s`, `amount A`, `harm w1 ... w16`, `mod Drive S ...`, `mod Bias S ...`, `mod Order S ...` |

- `source` et `gain` sont `src1` et `gain1`.
- `harm` prend de 1 à 16 poids (les nombres jusqu'au mot suivant) ; les poids non donnés valent 0.
- `mod X none` débranche une entrée.
- Un nouveau type donne d'abord ses valeurs par défaut, comme dans le pad.

### Global

```
Global  samples Merge|Ignore|Pass  input dB  output dB  latency ms
        action StopAll|PauseAll|RestartAll|RewindAll|ClearAll  chan n
```

L'action est exécutée en dernier, tout de suite. `chan` (les canaux de la piste) ne peut pas être
changé : la clé est acceptée pour qu'un Dump puisse être relu, et vérifiée par Check.

### Dump, Check, Free, Clear

| Bloc | Rôle |
|---|---|
| `Dump Line id` (ou Writer, Reader, Effect) | écrit le module dans le journal, **dans la syntaxe de la table** |
| `Dump Global`, `Dump All` | les réglages généraux ; tous les modules |
| `Dump Order` | l'ordre d'exécution des effets, et le nombre de boucles |
| `Check Line id clé valeur ...` (ou Writer, Reader, Effect) | « Check ... OK », ou une erreur 2759 par différence |
| `Check Global clé valeur ...` | la même chose pour les réglages généraux |
| `Free Line id` (ou Writer, Reader, Effect) | supprime le module |
| `Clear` | supprime toutes les lignes, readers, writers, effets et instances |

Un Dump peut être relu tel quel : c'est aussi une façon d'exporter un patch.

## Les algorithmes

Un **algorithme** est un modèle de sous-patch. Il se déclare dans une table et s'utilise autant de
fois que voulu ; chaque utilisation, une **instance**, a ses propres modules.

```
table(data(
  Algorithm Echo
    input  src
    output dst
    param  time 0.25 0.001 5
    param  fb 0 -150 150
    Line l  length 5  chan 1
    Writer w  line l  source src  overdub fb  status Writing
    Reader r  writer w  delay time  out dst  status Reading
  End
  Instance e1 Echo  src In:0  dst Out:0  time 0.5  fb -3
  Instance e2 Echo  src Reader 3  dst Bus 2
))
```

- **Les déclarations** viennent en tête du modèle : `input nom`, `output nom`, `param nom défaut min
  max`. Un nom déclaré ne peut pas être un mot réservé ni une clé (`delay`, `vol`...).
- **Une instance** remplace chaque paramètre par sa valeur (ou son défaut), partout où un nombre est
  attendu, et chaque entrée ou sortie par les mots donnés, lus dans la table : `src Reader rd` désigne
  le reader `rd` de la table. Les noms du modèle (`l`, `w`, `r`) reçoivent des modules propres à
  l'instance.
- **Chaque module** nommé dans le modèle appartient à l'instance : son pad l'indique.

| Bloc | Rôle |
|---|---|
| `Instance i Modèle arg valeur ...` | crée une instance (les entrées et sorties sont obligatoires) |
| `Set i arg valeur ...` | change des arguments de l'instance |
| `Dump Instance i` | l'appel, puis les modules de l'instance |
| `Free Instance i` | supprime l'instance et ses modules |
| `Free Algorithm Modèle` | oublie le modèle (les instances gardent leur copie) |

**Set** ne réapplique que les clés dont la valeur dépend d'un argument changé : les autres réglages
des modules de l'instance (faits dans les pads, par une pause générale...) sont conservés.

Les modèles et les instances sont sauvés avec le projet. Le module **Instances** les montre.

## Un exemple

Le script `Scripts/Interstys-Chain.mSL` construit une chaîne à écouter (le module Globals doit être en
Merge) :

```
LFO 246 (0,2 Hz) --mod Cutoff--> Filter 245 (passe-bande 800 Hz) <-- In:0-1
Filter 245 --> Saturation 244 --> Writer 250 / Reader 250 (écho 0,375 s) --> Bus 6
Mixer 243 : In (-6 dB) + Saturation 244 (-3 dB) + Bus 6 (-6 dB) --> Out:0-1
```

Ses numéros sont fixes : le relancer remplace les mêmes modules. Les effets sont numérotés à l'envers
de la chaîne ; `Dump Order` montre qu'ils s'exécutent pourtant dans l'ordre des câbles.

Les scripts `Scripts/Ex-1001.mSL` à `Ex-1019.mSL` sont les tests d'Interstys : chacun est aussi un
exemple d'emploi de la table.

# Les codes d'erreur

Les erreurs sont écrites dans le journal sous la forme « ERR: NNNN » suivie d'un message.

## Les modules

| Code | Sens |
|---|---|
| 2607 | numéro de ligne incorrect |
| 2608 | l'entrée de la ligne n'est pas une ligne valide |
| 2609 | action inconnue sur une ligne |
| 2610 | pas assez de mémoire pour la ligne |
| 2701 | effet : nombre de canaux incorrect |
| 2702 | effet : sortie incorrecte |
| 2703 | effet : source incorrecte |
| 2704 | effet : une source chevauche la sortie |
| 2705 | effet : aucune source |
| 2706 | effet : type non exécuté (Mover, Action, Script) |
| 2711 | reader : sortie incorrecte |
| 2712 | writer : source incorrecte |
| 2715 | effet : une entrée de modulation n'est pas valide (l'effet tourne sans elle) |
| 2771 | fichier son : impossible de l'ouvrir |
| 2772 | fichier son : pas utilisable pour une ligne (canaux, fréquence, durée) |
| 2773 | fichier son : erreur de lecture |

## La table

| Code | Sens |
|---|---|
| 2750 | un bloc est attendu |
| 2751 | type de module incorrect après Dump, Check ou Free |
| 2752 | identificateur incorrect (ni numéro, ni nom) |
| 2753 | clé inconnue |
| 2754 | valeur incorrecte ou hors bornes |
| 2755 | plus de module libre pour un nom |
| 2756 | le nom désigne un module d'un autre type |
| 2757 | nom inconnu |
| 2758 | la nouvelle ligne n'a pas assez de canaux pour un reader |
| 2759 | Check : une différence |
| 2762 | trop de noms |
| 2763 | ligne ou writer non défini |
| 2764 | canaux en dehors de la ligne |
| 2765 | retard plus long que la ligne |
| 2766 | pas assez de mémoire pour le module |
| 2767 | la clé n'a pas de sens pour ce type d'effet |
| 2768 | l'effet est sa propre source |
| 2769 | le dossier du projet est inconnu (CMGS-auxiliary.eel) |
| 2770 | le fichier ne peut pas être ouvert |

## Les algorithmes

| Code | Sens |
|---|---|
| 2780 | `End` manquant |
| 2781 | modèle inconnu |
| 2782 | déclaration incorrecte |
| 2783 | nom d'instance incorrect ou déjà utilisé |
| 2784 | argument inconnu ou mal formé |
| 2785 | paramètre hors bornes |
| 2786 | entrée ou sortie manquante |
| 2787 | instance inconnue |
| 2788 | trop de modèles, d'instances ou d'arguments |
| 2789 | Algorithm ou Instance à l'intérieur d'un modèle |
| 2790 | pas assez de mémoire |
