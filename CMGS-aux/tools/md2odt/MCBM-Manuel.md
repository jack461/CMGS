---
title: "MCBM-64 et MCBM-128"
subtitle: "Gestionnaire de basses multicanal pour REAPER — Manuel de l'utilisateur"
author: "Jean-Jacques Girardot"
date: "Octobre 2026 — document de travail"
lang: fr-FR
toc-title: "Table des matières"
---

# Présentation

## À quoi sert un gestionnaire de basses

Dans une diffusion multicanale, les haut-parleurs principaux sont souvent de taille réduite : ils
restituent mal les fréquences graves. Un *gestionnaire de basses* (« bass manager ») sépare chaque
canal en deux parties :

- la partie **aiguë**, au-dessus d'une fréquence de coupure, qui reste sur son canal ;
- la partie **grave**, au-dessous, qui est envoyée vers un ou plusieurs caissons de basse
  (canaux **LFE**, *Low Frequency Effects*).

Le mélange des deux, dans la salle, doit reconstituer le signal d'origine.

## MCBM-64 et MCBM-128

Les deux plug-ins JSFX font partie de la suite CMGS. Ils ont **la même interface et les mêmes
réglages** ; ils diffèrent par la façon de séparer graves et aigus.

| | MCBM-64 | MCBM-128 |
|---|---|---|
| Canaux traités | jusqu'à 128 | jusqu'à 128 |
| Canaux LFE | 4 au plus | 4 au plus |
| Filtres | cascades de filtres du 1^er^ ordre | filtres de Linkwitz-Riley |
| Pentes | 6, 12, 18 ou 24 dB/octave | 12 (LR2), 24 (LR4) ou 48 (LR8) dB/octave |
| Somme grave + aigu | corrigée par des tables empiriques | plate par construction |
| Fichier | `MCBM-64.jsfx` | `MCBM-128.jsfx` |

Malgré son nom, MCBM-64 traite lui aussi jusqu'à 128 canaux ; le nom a été conservé pour que les
projets existants retrouvent le plug-in.

Avec un filtre de **Linkwitz-Riley**, le passe-bas et le passe-haut sont tous deux à −6 dB à la
fréquence de coupure, et leur somme est parfaitement plate, quelle que soit la pente. C'est la
solution classique des filtres de répartition (*crossovers*). En LR2, les deux parties sont en
opposition de phase : MCBM-128 inverse alors la polarité de la partie grave, pour que la somme
reste plate.

Les deux versions peuvent être utilisées côte à côte pour les comparer à l'écoute (voir le
chapitre [Comparer les deux versions](#comparer-les-deux-versions)). Leurs préréglages (*presets*)
ne sont pas interchangeables.

# Mise en place dans REAPER

## Installation

Les deux fichiers `MCBM-64.jsfx` et `MCBM-128.jsfx` se trouvent dans le répertoire `GameMaster`
de la distribution CMGS, placé dans le répertoire `Effects` des ressources de REAPER (ou dans
celui d'un projet). Ils apparaissent dans la liste des effets sous les noms « MCBM-64 » et
« MCBM-128 ».

## Nombre de canaux

Le plug-in traite tous les canaux de la piste sur laquelle il est placé, jusqu'à 128. Il faut
donc régler le nombre de canaux de la piste (bouton **Route** de la piste, *Track channels*) pour
qu'il comprenne :

- tous les canaux des haut-parleurs principaux ;
- les canaux des caissons de basse (LFE).

Typiquement, le plug-in est placé sur la piste qui alimente la sortie vers les haut-parleurs,
en dernier dans la chaîne d'effets.

## Canaux LFE

Les canaux LFE sont des canaux ordinaires de la piste, que l'on désigne comme tels (réglages
*LFE 1 is channel* à *LFE 4 is channel*). La sortie d'un canal LFE contient :

- son propre signal d'entrée, multiplié par son gain (par exemple le canal « .1 » d'un
  mixage 5.1) ;
- la somme des parties graves envoyées par les autres canaux, multipliée elle aussi par son gain.

Si un canal LFE est choisi au-delà du nombre de canaux de la piste, il n'est pas produit : la
fenêtre du plug-in l'indique par un message en rouge, par exemple
« LFE 2 is channel 100, beyond the 64 track channels : not output ».

# Concepts

## Types de canaux

Chaque canal a un **type** (réglage *Channel type*) :

**Pass through**
:   Le canal passe sans filtrage ; seul son gain est appliqué, ce qui permet d'ajuster finement
    le niveau de chaque haut-parleur de l'installation. C'est le type par défaut.

**Filtered**
:   Le canal est séparé : la partie aiguë reste sur le canal, la partie grave est envoyée vers
    les canaux LFE, selon les niveaux d'envoi du canal.

**Check tone**
:   Le canal est séparé comme un canal *Filtered*, mais les deux parties sont réunies sur le
    canal lui-même, sans envoi vers les LFE. Ce type sert à vérifier le filtre : le canal doit
    sonner comme l'original.

**LFE 1 à LFE 4**
:   Le canal est l'un des quatre canaux de caisson de basse.

## Filtres

Pour un canal *Filtered* ou *Check tone*, le filtre est défini par :

- son **type** (*Filter type*) : passe-haut et passe-bas (*hp+lp*, le cas normal), passe-haut
  seul (les graves sont supprimés), passe-bas seul (le canal ne garde que ses graves, envoyés
  vers les LFE), ou aucun (*none*) ;
- sa **pente** (*Filter order*), qui dépend de la version (voir le tableau du chapitre
  [Présentation](#présentation)) ;
- sa **fréquence de coupure** (*Filter frequency*), de 20 à 400 Hz, typiquement de 80 à 120 Hz ;
- le **recouvrement** des deux filtres (*HPF/LPF overlap*), de 0 à 2 :
    - dans MCBM-128, la valeur 1 place les deux coupures à la même fréquence (vrai
      Linkwitz-Riley). À 0, le passe-bas descend d'une octave et le passe-haut monte d'une
      octave (un « trou » entre les deux) ; à 2, c'est l'inverse (les deux parties se
      recouvrent) ;
    - dans MCBM-64, ce réglage module l'écart entre les deux fréquences de coupure, calculé à
      partir de tables empiriques ; la valeur 1 est celle prévue par ces tables.

## Volumes

- **Gain** : gain du canal, de −60 à +20 dB, quel que soit son type (pour un canal *Pass through*,
  il sert à ajuster le niveau du haut-parleur).
- **LF/HF balance** : de −1 à +1, renforce l'une des deux parties au détriment de l'autre ;
  à 0, les deux parties sont inchangées.
- **Dry/Wet Mix** : à 100 %, seul le signal filtré est produit ; au-dessous, une part du signal
  non filtré lui est ajoutée (mélange à puissance constante).
- **Send to LFE 1 à 4** : niveau (en dB) auquel la partie grave du canal est envoyée vers chaque
  canal LFE ; −120 dB signifie « pas d'envoi ».
- **Channel status** : *mute* coupe complètement le canal, y compris ses envois vers les LFE.
- **General volume** : volume général, de −60 à +20 dB, appliqué à la sortie de **tous** les canaux,
  LFE compris. Ses variations sont adoucies (en une dizaine de millisecondes), pour éviter les clics.

## Modèles

Le plug-in conserve **16 modèles**, nommés **A** à **P**. Un modèle contient un jeu complet de
réglages de canal (type, filtre, volumes, envois). Les modèles permettent de régler de la même
manière un grand nombre de canaux : on règle un canal, on le copie dans un modèle, puis on charge
ce modèle dans les autres canaux.

Le **modèle cible** (*Target channel model*) est celui sur lequel portent les opérations de
copie ; il est rappelé sous la grille des canaux (« set: A »).

Les canaux, les modèles et les affectations LFE sont enregistrés avec le projet et avec les
préréglages du plug-in.

# Les réglages

| N° | Réglage | Valeurs | Rôle |
|---|---|---|---|
| 1 | Settings for channel | 1 à 128, puis A à P | canal (ou modèle) dont les réglages sont affichés et modifiés |
| 2 | Channel status | normal, mute | canal actif ou coupé |
| 3 | Gain (dB) | −60 à +20 | gain du canal |
| 4 | Channel type | Pass through, Filtered, Check tone, LFE 1 à 4 | type du canal |
| 5 | Filter type | hp+lp, hp only, lp only, none | filtres utilisés |
| 6 | Filter order | MCBM-64 : 6 à 24 dB ; MCBM-128 : LR2, LR4, LR8 | pente des filtres |
| 7 | Filter frequency (Hz) | 20 à 400 | fréquence de coupure |
| 8 | HPF/LPF overlap | 0 à 2 | recouvrement des deux filtres |
| 9 | LF/HF balance | −1 à +1 | équilibre graves / aigus |
| 10 | Dry/Wet Mix (%) | 0 à 100 | part du signal filtré |
| 11 à 14 | Send to LFE 1 à 4 (dB) | −120 à +20 | envoi de la partie grave vers chaque LFE |
| 15 | Edit operation | voir ci-dessous | opérations sur les canaux et les modèles |
| 16 | Target channel model | A à P | modèle cible |
| 17 à 20 | LFE 1 à 4 is channel | none, 1 à 128 | canal utilisé comme LFE 1 à 4 |
| 21 | General volume (dB) | −60 à +20 | volume général de tous les canaux, LFE compris |

Le réglage **Settings for channel** choisit le canal dont les réglages 2 à 14 sont affichés ;
au-delà de 128, il affiche les réglages des modèles A à P, que l'on peut alors modifier
directement.

## Opérations d'édition

Le réglage **Edit operation** exécute une opération, puis revient à « - » :

| Opération | Effet |
|---|---|
| reset channel | remet le canal courant à ses valeurs par défaut |
| save to target | copie les réglages du canal courant dans le modèle cible |
| load from target | charge le modèle cible dans le canal courant (son état *mute* est conservé) |
| load & next | idem, puis passe au canal suivant |
| load all channels from target | charge le modèle cible dans tous les canaux qui ne sont pas des LFE |
| load selected channels from target | charge le modèle cible dans les canaux sélectionnés (voir la fenêtre graphique), puis les désélectionne |
| unselect all | désélectionne tous les canaux |
| mute others | coupe tous les canaux sauf le canal courant (et les LFE) |
| unmute all | rétablit tous les canaux |
| recompile filters | recalcule tous les filtres |

# La fenêtre graphique

## La grille des canaux

La fenêtre du plug-in montre tous les canaux de la piste, par groupes de quatre, sur autant de
lignes que nécessaire (le nombre de canaux par ligne s'adapte à la largeur de la fenêtre).
Chaque case indique :

- le **numéro** du canal, en rouge si le canal est coupé (*mute*) ;
- un séparateur : « **:** » si les réglages du canal sont exactement ceux d'un modèle,
  « **#** » s'ils ont été modifiés depuis ;
- une **lettre** : le modèle dont le canal suit les réglages, ou un **chiffre** de 1 à 4 pour un
  canal LFE.

La couleur de la lettre indique le type du canal : gris pour *Pass through*, **vert** pour
*Filtered*, **orange** pour *Check tone*, **bleu** pour un LFE.

Le canal courant est entouré d'un cadre gris ; les canaux sélectionnés, d'un cadre orange.
Sous la grille, « set: A » rappelle le modèle cible.

## Actions à la souris

Les clics s'appliquent au canal sur lequel on clique. Les touches de modification n'ont pas le
même nom sous macOS et sous Windows : ⌘ (Commande) correspond à **Ctrl**, ⌥ (Option) à **Alt**,
⇧ à **Maj**, et la touche Contrôle du Mac à la **touche Windows**.

| macOS | Windows | Effet |
|---|---|---|
| clic | clic | rend ce canal courant (ses réglages s'affichent) |
| ⇧ clic | Maj clic | coupe / rétablit le canal |
| ⌥ clic | Alt clic | bascule le canal entre *Pass through* et *Filtered* |
| ⌘ clic | Ctrl clic | sélectionne / désélectionne le canal |
| ⌥ ⇧ clic | Alt Maj clic | copie les réglages du canal dans le modèle cible |
| clic droit (ou Contrôle clic) | clic droit (ou Win clic) | affiche le modèle du canal, pour le modifier |
| ⇧ clic droit | Maj clic droit | fait du modèle du canal le modèle cible |
| ⌥ ⇧ clic droit (ou Contrôle ⌥ ⇧ clic) | Alt Maj clic droit (ou Win Alt Maj clic) | charge le modèle cible dans le canal |

## Raccourcis clavier

La fenêtre du plug-in doit avoir le focus. Ces raccourcis sont les mêmes sous macOS et sous
Windows (« début » et « fin » : touches *Début* et *Fin*, ou *Home* et *End*).

| Touche | Effet |
|---|---|
| n ou → | canal suivant |
| p ou ← | canal précédent |
| o ou ↑ | canal de la ligne précédente |
| j ou ↓ | canal de la ligne suivante |
| début / fin | premier / dernier canal |
| m | coupe / rétablit le canal courant |
| z | coupe tous les autres canaux |
| u | rétablit tous les canaux |
| t | bascule le canal courant entre *Pass through* et *Filtered* |
| c | bascule le canal courant entre *Pass through* et *Check tone* |
| s | copie les réglages du canal courant dans le modèle cible |
| l | charge le modèle cible dans le canal courant |
| r | recharge dans le canal courant son propre modèle |
| d | désélectionne tous les canaux |
| A à P (majuscules) | choisit le modèle cible |

# Utilisation pas à pas

## Configurer une installation

1. Régler le nombre de canaux de la piste (principaux + LFE).
2. Désigner les canaux LFE : réglages *LFE 1 is channel* (et suivants si besoin).
3. Choisir un canal principal ; le passer en *Filtered* ; régler la fréquence de coupure
   (par exemple 80 Hz), la pente, et l'envoi vers LFE 1 (par exemple 0 dB).
4. Copier ces réglages dans un modèle : choisir le modèle cible (touche **A**), puis touche
   **s** (ou *Edit operation* ▸ *save to target*).
5. Charger ce modèle dans tous les autres canaux : *Edit operation* ▸
   *load all channels from target*.
6. Ajuster individuellement les canaux qui le demandent ; leur séparateur devient « # ».

## Régler un groupe de canaux

1. Sélectionner les canaux concernés par ⌘ clic (cadre orange).
2. Choisir le modèle cible.
3. *Edit operation* ▸ *load selected channels from target*.

## Vérifier un filtre

1. Passer un canal en *Check tone* (touche **c**) : graves et aigus sont réunis sur ce canal.
2. Écouter en balayant la fréquence de coupure et la pente : le signal doit rester semblable à
   l'original. Un creux ou une bosse autour de la fréquence de coupure révèle un défaut de
   raccordement des deux filtres.
3. Repasser le canal en *Filtered* (touche **c**, puis **t**).

Pour isoler un canal, la touche **z** coupe tous les autres, la touche **u** les rétablit.

# Comparer les deux versions

On peut placer MCBM-64 et MCBM-128 sur deux copies de la même piste, avec les mêmes réglages, et
passer de l'une à l'autre (ou comparer les canaux en *Check tone*) :

- en **MCBM-128**, la somme des graves et des aigus est plate quels que soient la fréquence et la
  pente (*HPF/LPF overlap* à 1) ;
- en **MCBM-64**, la qualité du raccordement dépend des tables de correction, établies
  empiriquement ; elle peut varier avec la fréquence et la pente.

Les préréglages des deux plug-ins ne sont pas interchangeables : chacun ignore ceux de l'autre
(le réglage *Filter order* n'a pas le même sens dans les deux).

# Remarques et limites

- Un canal *Filtered* avec le filtre *lp only* ne produit sur son propre canal que la part non
  filtrée (*Dry/Wet Mix* au-dessous de 100 %) : ses aigus sont supprimés.
- Avec le filtre *hp only*, les graves du canal sont supprimés et ne sont envoyés vers aucun LFE.
- Un canal LFE choisi au-delà des canaux de la piste n'est pas produit (message en rouge).
- Les préréglages enregistrés avec les anciennes versions (avant octobre 2026) ne sont pas relus :
  les canaux reprennent leurs valeurs par défaut.
