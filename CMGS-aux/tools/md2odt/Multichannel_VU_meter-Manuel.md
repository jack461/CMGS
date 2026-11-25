---
title: "Multichannel VU meter"
subtitle: "VU-mètre multicanal pour REAPER — Manuel de l'utilisateur"
author: "Jean-Jacques Girardot"
date: "Octobre 2026 — document de travail"
lang: fr-FR
toc-title: "Table des matières"
---

# Présentation

## À quoi sert ce VU-mètre

Le **Multichannel VU meter** affiche le niveau crête de chacun des canaux d'une piste REAPER, jusqu'à
**128 canaux**. Il permet de voir d'un coup d'œil sur quels canaux il y a du signal, à quel niveau, et
lesquels ont dépassé un seuil de saturation.

Il est destiné aux diffusions multicanales de la suite CMGS (Game Master, Espaces, Interstys…),
mais fonctionne sur n'importe quelle piste. Plusieurs VU-mètres peuvent être placés dans une même
session, chacun avec sa propre couleur.

## Origine

Le plug-in est dérivé du *S&M Multichannel VU meter* de Jeff Bédague (« Jeffos », 2009, licence GPL).
La version CMGS le porte à 128 canaux et ajoute le menu décrit plus loin : seuil de saturation,
couleur, effacement automatique.

Il en existe deux variantes :

| Fichier | Nom dans REAPER | Remarque |
|---|---|---|
| `Multichannel_VU_meter_U.jsfx` | Multichannel_VU_meter (unrolled) | version recommandée, décrite ici |
| `Multichannel_VU_meter.jsfx` | Multichannel_VU_meter | ancienne version, sans le menu |

La version *unrolled* (« boucle déroulée ») traite chaque canal par une instruction séparée, au lieu
d'une boucle sur les canaux : elle consomme nettement moins de temps de calcul.

## Installation

Le plug-in fonctionne avec **REAPER 7.25 ou plus récent**. Le fichier `Multichannel_VU_meter_U.jsfx`
doit se trouver dans le dossier `Effects/` de REAPER (dans la distribution CMGS, sous
`Effects/CMGS/GameMaster/`). Il n'utilise aucune bibliothèque.

Placez-le sur la piste à surveiller, à l'endroit de la chaîne d'effets où vous voulez mesurer le
niveau (en général en fin de chaîne). Il laisse passer le son sans le modifier.

# L'affichage

## Les barres

Le VU-mètre détermine lui-même le nombre de canaux : c'est celui de la piste. Chaque canal a sa
barre, numérotée à partir de 1.

- La barre colorée montre le **niveau crête** du canal, mesuré sur des tranches de 45 ms. L'échelle va
  de **−60 dB à 0 dB**, avec un repère tous les 6 dB. Un signal au-dessus de 0 dB donne une barre
  pleine.
- À côté du numéro, la **valeur maximale** atteinte depuis le dernier effacement est écrite en dB, au
  dixième près. Elle est grisée tant que le canal n'a reçu aucun signal au-dessus de −60 dB.
- Un **rectangle rouge**, au bout de la barre, signale que le canal a atteint ou dépassé le **seuil de
  saturation** (0 dB par défaut).
- Un **indicateur général**, en haut à droite (barres horizontales) ou en haut à gauche (barres
  verticales), devient rouge dès qu'au moins un canal est saturé.

Le rouge reste affiché, même si le signal redescend, jusqu'à ce qu'il soit effacé : par un clic
gauche, ou automatiquement après un délai (voir plus loin).

La mesure est une mesure de **crête échantillon** (la plus grande valeur absolue des échantillons),
et non une moyenne (RMS) ni une crête vraie (*true peak*).

## Les quatre modes d'affichage

| Mode | Disposition |
|---|---|
| Horizontal meters - fixed height | une barre horizontale par canal, de la hauteur d'une ligne de texte |
| Horizontal meters - fit to height | les barres horizontales se partagent toute la hauteur de la fenêtre |
| Vertical meters - fixed width | une barre verticale par canal, de la largeur d'un caractère |
| Vertical meters - fit to width | les barres verticales se partagent toute la largeur de la fenêtre |

En mode vertical, les numéros de canaux et les valeurs maximales sont écrits verticalement, un
chiffre par ligne.

Dans les modes *fit*, quand les barres deviennent trop étroites, les numéros et les valeurs ne sont
plus écrits. Le curseur **Highlight channel** permet alors de repérer un canal : sa barre est
affichée plus claire et son numéro en blanc. La valeur 0 désactive le repérage.

# Utilisation

## Clic gauche : effacer les saturations

Un clic gauche, n'importe où dans la fenêtre, efface **tous les canaux** : les rectangles rouges,
l'indicateur général et les valeurs maximales, qui repartent de zéro.

## Clic droit : le menu

Un clic droit ouvre un menu de quatre sous-menus. Le choix en cours y est coché.

**GUI mode** : l'un des quatre modes d'affichage décrits plus haut.

**Saturation threshold** : le seuil au-delà duquel un canal est signalé en rouge :
−20, −6, −2, −1, **0** (par défaut), +1, +2, +6 ou +20 dB.

- Un seuil **négatif** sert d'indicateur de niveau : par exemple, à −6 dB, il montre quels canaux
  ont atteint la moitié de la pleine échelle.
- Un seuil **positif** tolère des dépassements, par exemple à l'intérieur d'une chaîne d'effets en
  virgule flottante, avant un limiteur qui ramènera le niveau sous 0 dB.

**Meter color** : la couleur des barres et des numéros de canaux : **Green** (par défaut), Orange,
Blue, Yellow, Cyan ou Violet. Toutes restent bien distinctes du rouge des saturations. Elles servent
à distinguer plusieurs VU-mètres dans une même session, par exemple un par groupe de haut-parleurs.

**Saturation auto clear** : la durée d'affichage des saturations :

| Choix | Effet |
|---|---|
| Permanent | le rouge reste jusqu'au prochain clic gauche (par défaut) |
| After 1 minute | le rouge d'un canal s'efface 1 minute après sa dernière saturation |
| After 3 minutes | idem, après 3 minutes |
| After 5 minutes | idem, après 5 minutes |

Le délai est compté **canal par canal**, à partir de la dernière saturation : un canal qui sature
régulièrement reste rouge. Quand le rouge s'efface, la valeur maximale du canal est remise à zéro.
Si l'on abaisse le seuil et qu'une ancienne valeur maximale se retrouve au-dessus, le délai part du
moment du changement.

Le délai court aussi quand la lecture est arrêtée, et que la fenêtre du VU-mètre soit ouverte ou
fermée.

## Sauvegarde des réglages

Les réglages du menu sont des curseurs cachés du plug-in. Ils sont donc sauvés avec le projet, les
presets et les modèles de piste, et chaque VU-mètre garde sa couleur, son seuil et son mode.

| Curseur | Rôle | Valeur par défaut |
|---|---|---|
| sample time (ms), caché | durée des tranches de mesure | 45 ms |
| Highlight channel | canal repéré (0 = aucun) | 0 |
| GUI mode, caché | mode d'affichage | Horizontal meters - fixed height |
| Saturation threshold, caché | seuil de saturation | 0 dB |
| Meter color, caché | couleur des barres | Green |
| Saturation auto clear, caché | effacement automatique | Permanent |

Les curseurs cachés restent accessibles par l'automation et les enveloppes de REAPER.

# Exemple : une diffusion sur trois groupes

Une diffusion utilise un groupe de 16 haut-parleurs en façade, 16 sur les côtés et 8 au plafond,
chacun sur sa piste.

1. Placez un VU-mètre en fin de chaîne de chaque piste.
2. Donnez à chacun une couleur : Green pour la façade, Cyan pour les côtés, Yellow pour le plafond.
3. Choisissez le mode *Vertical meters - fit to width* et ancrez les trois fenêtres côte à côte.
4. Pendant les répétitions, gardez l'effacement **Permanent** et le seuil à **0 dB** : à la fin, les
   rectangles rouges montrent tous les canaux qui ont saturé.
5. Pendant le concert, passez à **After 3 minutes** : seules les saturations récentes restent
   signalées.
