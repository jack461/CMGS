---
title: "CMGS — fragment GUI"
lang: fr-FR
---

# Les modules communs

## GUI

Le module **GUI** règle l'aspect de l'application : le thème, le fond, la taille d'affichage, le style, la barre
d'onglets, le dessin des cellules des pads, la palette de leurs couleurs, les textes des pads et des sliders. Il existe
dans les cinq plug-ins (Game Master, FilePlayer, ScriptMaster, Espaces, Interstys) ; on l'ajoute à un panneau par
le menu des modules (Shift + clic droit). Ses réglages sont enregistrés avec le projet ; le thème, la taille
d'affichage et le style le sont par le plug-in lui-même, comme lorsqu'on les choisit dans le menu des modules. Tous
peuvent aussi être donnés par un script (§ 8.7.8).

### Le pad du module

Le pad compte 5 lignes de 7 cellules ; chaque colonne regroupe les réglages d'un même sujet :

| Colonne | Cellules |
|--------------------|------------------------------------------------------------|
| l'aspect général | Theme, Background, Size, Style, Tabs |
| la palette | Palette, Hue, Chroma, Light, Danger |
| les modes | Selection, Hover, Disabled, Contrast, Preview |
| les cellules | Variation, Pads text, Pads bold, Gap X, Gap Y |
| leur remplissage | Corners, Fade, Extend, (vide), Log settings |
| les cadres | Frame, Radius, Thick, Color, Opacity |
| les textes | Fonts, Faders text, Faders bold, Faders width, Defaults |

Les cellules suivent les conventions des pads (§ 6.1) :

| Geste | Effet |
|---------------------------------|----------------------------------------------------------|
| glisser sur une cellule qui porte un nombre | règle la valeur (horizontalement : réglage grossier ; verticalement : réglage fin) |
| Shift + clic gauche sur une telle cellule | rétablit la valeur d'usine |
| clic droit sur une telle cellule | ouvre le menu de ses valeurs usuelles |
| clic gauche sur une cellule de choix (Theme, Style, Variation, Palette…) | passe au choix suivant ; avec Shift, au précédent |
| clic droit sur une cellule de choix | ouvre le menu des choix |

Le pad est lui-même dessiné avec la palette (§ 8.7.5) : une cellule dont la valeur diffère de la valeur d'usine est
en mode « sélectionné » ; une cellule sans effet dans l'aspect courant (par exemple Fade avec la variation Std) est en
mode « désactivé », mais reste réglable.

### Thème, fond, taille, style et onglets

| Cellule | Réglage |
|---------------|------------------------------------------------------------------------|
| Theme | l'un des douze thèmes (§ 5.5) |
| Background | assombrit (−80 à −1 %) ou éclaircit (1 à 80 %) le fond du thème ; 0 : le fond du thème. Les textes, les sliders et les titres des modules restent lisibles sur le nouveau fond |
| Size | la taille d'affichage, de 50 à 200 % (§ 5.5) |
| Style | Classic : les cellules bordées, les sliders et la barre d'onglets d'origine ; Soft : les cellules sans bordure, des sliders fins |
| Tabs | la barre d'onglets : Style (comme le style : toujours affichée en Classic, escamotée en Soft), Always (toujours affichée), Hover (affichée quand la souris s'approche du haut de la fenêtre, et escamotée une dizaine de secondes après qu'elle l'a quittée) |

### Le dessin des cellules

La variation choisit le dessin des cellules des pads :

| Variation | Dessin |
|-------------|--------------------------------------------------------------------------|
| Std | la cellule est remplie de sa couleur ; une cellule sélectionnée porte un anneau de la couleur de son texte |
| Faded | la couleur entoure le texte, puis se fond dans le fond |
| Text | la cellule garde le fond, et son texte prend sa couleur, rendue lisible sur le fond ; une cellule sélectionnée est remplie : jusqu'à son bord en Classic, en dégradé en Soft |
| Outline | comme Text, mais une cellule sélectionnée garde son texte et reçoit un cadre de sa couleur, épais de Thick + 1 unités (un cadre, même si Thick vaut none) |

| Cellule | Réglage |
|---------------|------------------------------------------------------------------------|
| Gap X, Gap Y | l'espace ajouté entre les cellules (0 à 200 et 0 à 10 unités) : la partie colorée rétrécit, sans devenir plus étroite que son texte ; la cellule garde sa place et ses clics |
| Corners | le rayon des coins des cellules rectangulaires (0 à 20 unités ; « pads » : comme chaque pad les dessine) ; en Classic, il arrondit aussi leur bordure |
| Fade | Faded : la largeur du dégradé autour du texte (0 à 80 pixels) |
| Extend | Faded : le dégradé va jusqu'aux bords de la cellule |
| Frame | Soft : un cadre autour des cellules qui ont un texte : None, Rect ou Round |
| Radius | le rayon des coins d'un cadre Round (0 à 20 unités) |
| Thick | l'épaisseur du cadre (1 à 4 unités) ; 0 (none) : aucun cadre, et en Classic, aucune bordure autour des cellules |
| Color | la couleur du cadre : celle de la cellule (Cell), plus claire (Lighter), plus foncée (Darker) ou grise (Grey) |
| Opacity | l'opacité du cadre (5 à 100 %) |
| Contrast | Text et Outline, les cellules sans rôle : l'écart minimal de luminance entre leur texte et le fond (10 à 80 %) |
| Selection | Faded et Text : une cellule sélectionnée est éclaircie (0 à 80 %) ; les cellules à rôle : l'intensité de leur mode « sélectionné » |

### Les textes et les sliders

| Cellule | Réglage |
|---------------------------|------------------------------------------------------------|
| Fonts | la taille de tous les textes (80 à 150 %) : la barre d'onglets, les journaux, les titres et les messages des modules, les pads, les sliders ; au-delà de 100 %, les lignes grandissent aussi |
| Pads text, Pads bold | la taille (80 à 150 %) et la graisse du texte des cellules ; au-delà de 100 %, les lignes des pads grandissent ; un texte trop large pour sa cellule est réduit |
| Faders text, Faders bold | la taille (70 à 150 %) et la graisse du nom des sliders ; au-delà de 100 %, les sliders grandissent |
| Faders width | la largeur laissée au nom et à la valeur d'un slider (50 à 200 %) ; la barre prend le reste |

### La palette et les rôles des cellules

Les cellules des pads peuvent avoir un **rôle** : leur couleur ne vient plus alors du pad, mais de la palette choisie
dans le module GUI. Ont déjà des rôles : le pad du module GUI, la barre d'onglets de tous les plug-ins, les pads des
modules Readers et Writers d'Interstys et leurs entrées de modulation ; les autres pads suivront.

| Rôle | Cellules |
|---------------|----------------------------------------------------------------|
| Action | ouvre un menu, lance une opération |
| Choice | bascule entre On et Off, choisit un mode parmi plusieurs |
| Navigation | vues, pages, onglets |
| Value | un nombre réglable au glisser |
| Object | un élément d'une liste : effet, lecteur, ligne, courbe… |
| State | un indicateur (en lecture, en écriture…) ; il s'allume quand il est sélectionné |
| Danger | supprimer, réinitialiser |
| Alert | une erreur, une alerte |
| Information | un titre, une légende, un affichage |
| Empty | une cellule inutilisée |

Les éléments numérotés (projecteurs, canaux…) peuvent prendre les couleurs d'une **série d'identité** : 16 couleurs
distinctes, harmonisées avec la palette. Selon son état, une cellule prend l'un de six **modes**, calculés à partir de
la couleur de son rôle :

| Mode | Quand |
|---------------|----------------------------------------------------------------|
| Rest | au repos |
| Hover | la souris est sur la cellule (sauf State, Information et Empty) |
| Pressed | le bouton de la souris est enfoncé sur la cellule |
| Selected | la cellule est choisie, allumée, ou sa valeur est modifiée |
| Disabled | la cellule est sans effet pour l'instant ; elle reste cliquable |
| Locked | la cellule est hachurée : par exemple une entrée de modulation branchée, mais coupée |

| Cellule | Réglage |
|---------------|------------------------------------------------------------------------|
| Palette | la famille : Theme (les couleurs du thème : les cellules Action ont la couleur de ses boutons, les autres rôles des teintes voisines), Mono (une seule teinte : les rôles se distinguent par leur luminosité), Analog (des teintes voisines), Complement (les commandes et les données de part et d'autre du cercle des couleurs), Spectrum (six teintes réparties sur le cercle), Muted (des teintes voisines et peu saturées), Pastel (des cellules claires, un texte foncé), Contrast (des teintes fixes, qui restent distinctes pour les daltoniens) |
| Hue | la teinte de base (0 à 359°) ; « theme » : celle du thème (sauf avec Theme et Contrast, qui la fixent) |
| Chroma | la saturation (0 à 100 %) |
| Light | la luminosité (0 à 100 %) |
| Danger | les cellules Danger en rouge et Alert en orange (red), ou dans des teintes de la palette (palette) |
| Hover, Disabled | l'intensité des modes « survol » et « désactivé » (0 à 100 %) ; celle du mode « sélectionné » est réglée par Selection |
| Preview | affiche ou masque l'aperçu de la palette |

Les couleurs sont calculées dans l'espace OKLCH, qui donne à tous les rôles la même luminosité perçue ; elles suivent
le thème et le fond, et sont recalculées dès qu'un réglage change. Le texte de chaque cellule prend, du clair ou du
foncé, le plus lisible sur sa couleur ; celui des cellules Information est, sur un fond sombre, un blanc légèrement
teinté.

**L'aperçu.** Avec Preview: On, le module affiche sous son pad un aperçu de la palette : les dix rôles dans leurs six
modes (« - » : un mode qui ne s'applique pas au rôle), la série d'identité, puis la ligne de retouche (§ 8.7.6).
Dessous, trois mesures : le contraste du texte le moins lisible (bon à partir de 4,5, acceptable à partir de 3),
l'écart entre les deux rôles les plus proches (bon à partir de 10, acceptable à partir de 6), l'écart entre un rôle et
le fond (bon à partir de 15, acceptable à partir de 9). L'aperçu ne s'affiche que si le panneau est assez haut.

**Le rôle d'une cellule.** Avec Alt (ou Alt + Cmd) enfoncé, la souris sur une cellule de n'importe quel pad affiche
une étiquette : le numéro de la cellule, son rôle et son mode, ou « no role » si elle n'a pas de rôle.

### Retoucher un rôle

La dernière ligne de l'aperçu retouche la couleur d'un rôle, dans la famille courante :

| Cellule | Effet |
|------------------|---------------------------------------------------------------------|
| Adjust: (rôle) | le rôle retouché ; un clic sur une ligne de l'aperçu le choisit aussi ; clic gauche : le rôle suivant (avec Shift, le précédent) ; clic droit : le menu des rôles |
| Hue | l'écart de teinte (−180 à 180°) |
| Light | l'écart de luminosité (−30 à 30 %) |
| Chroma | l'écart de saturation (−100 à 100 % de celle de la palette) ; pour Information et Empty, presque sans couleur, la saturation s'ajoute |
| Reset role | efface les retouches du rôle |
| Reset palette | efface, après confirmation, les retouches de tous les rôles de la famille |

Hue, Light et Chroma se règlent comme les autres cellules de valeur : glisser, Shift + clic gauche pour revenir à 0,
clic droit pour le menu des valeurs. Les six modes du rôle suivent sa couleur retouchée ; pour Information, la retouche
touche aussi la couleur de son texte. Les retouches sont relatives à la palette, ce qui leur permet de suivre le thème
et le fond ; elles sont propres à chaque famille : une retouche de Spectrum ne change pas Analog.

### Le défaut de l'utilisateur

La cellule Defaults ouvre un menu :

| Entrée | Effet |
|---------------------|---------------------------------------------------------------------|
| Reset to default | applique le défaut enregistré : tous les réglages du module, son style et ses retouches ; le thème et la taille d'affichage ne changent pas (grisée tant qu'aucun défaut n'est enregistré) |
| Save as default | enregistre l'aspect courant comme défaut (sauf le thème et la taille d'affichage) |
| Factory defaults | les valeurs d'usine : style Classic, Tabs Always, palette Pastel, variation Outline, Gap X 40, Gap Y 4, Frame Rect, Corners « pads », Thick none, les autres réglages à leur valeur de départ ; le thème et la taille d'affichage ne changent pas |

La cellule Defaults est en mode « sélectionné » lorsqu'un défaut est enregistré. Le défaut est enregistré avec le
projet ; pour le reprendre dans un autre projet, on passe par Log settings (§ 8.7.8). Une nouvelle instance d'un
plug-in démarre avec les valeurs d'usine.

### Les réglages GUI

Tous les réglages du module peuvent être donnés par un script, sous la forme `settings(data( GUI clé valeur … ))` :

    settings(data( GUI style Soft tabs Hover variant Outline palette Spectrum hue 200 adjust Action 20 -5 0 ));

Les clés absentes ne changent pas. Une partie GUI peut aussi se placer n'importe où dans les réglages d'Interstys, de
Espaces ou du Game Master : ses clés vont jusqu'au premier mot qui n'en est pas une. La cellule **Log settings**
écrit dans le journal système la ligne complète de l'aspect courant, prête à être copiée dans un fichier ; s'il existe
un défaut de l'utilisateur, il suit, après le mot `default`.

| Clé | Valeurs | Cellule |
|-------------|-------------------------------------------------------------|----------------------|
| `theme` | 0 à 11, ou le nom du thème entre guillemets (`"Dark Cyan"`) | Theme |
| `shade` | −80 à 80 | Background |
| `size` | 50 à 200 (la plus proche des tailles d'affichage) | Size |
| `style` | `Classic`, `Soft` | Style |
| `tabs` | `Style`, `Always`, `Hover` | Tabs |
| `variant` | `Std`, `Faded`, `Text`, `Outline` | Variation |
| `fonts` | 80 à 150 | Fonts |
| `palette` | `Theme`, `Mono`, `Analog`, `Complement`, `Spectrum`, `Muted`, `Pastel`, `Contrast` | Palette |
| `hue` | −1 à 359, ou `Theme` (la teinte du thème) | Hue |
| `chroma`, `light` | 0 à 100 | Chroma, Light |
| `danger` | `Red`, `Palette` | Danger |
| `hover`, `disabled` | 0 à 100 | Hover, Disabled |
| `select` | 0 à 80 | Selection |
| `contrast` | 10 à 80 | Contrast |
| `ptext` | 80 à 150 | Pads text |
| `bold`, `fbold`, `extend` | `Off`, `On` | Pads bold, Faders bold, Extend |
| `ftext` | 70 à 150 | Faders text |
| `fwidth` | 50 à 200 | Faders width |
| `gapx`, `gapy` | 0 à 200, 0 à 10 | Gap X, Gap Y |
| `corners` | −1 à 20 (−1 : comme chaque pad) | Corners |
| `fade` | 0 à 80 | Fade |
| `frame` | `None`, `Rect`, `Round` | Frame |
| `radius` | 0 à 20 | Radius |
| `thick` | 0 à 4 (0 : aucun cadre) | Thick |
| `color` | `Cell`, `Lighter`, `Darker`, `Grey` | Color |
| `opacity` | 5 à 100 | Opacity |
| `adjust` | [famille] rôle h l c ; [famille] `reset` ; `reset all` | la ligne de retouche |
| `defaults` | (sans valeur) les valeurs d'usine, style Classic compris | Factory defaults |
| `default` | les clés qui suivent définissent le défaut de l'utilisateur, sans l'appliquer (sauf `theme` et `size`) | Save as default |
| `restore` | (sans valeur) applique le défaut de l'utilisateur | Reset to default |

Dans `adjust`, la famille est celle du moment si elle n'est pas donnée ; les rôles s'écrivent comme dans l'aperçu
(Action, Choice, Navigation, Value, Object, State, Danger, Alert, Information, Empty). Tout ce qui suit `default`
va au défaut : on écrit donc `restore` et les réglages courants avant lui. Les erreurs de ces réglages sont les codes
1640 (une clé attendue), 1641 (une valeur hors de sa plage) et 1642 (une valeur qui n'est pas l'une de celles de la
clé) ; la première erreur arrête la lecture, les réglages pris avant elle restent.
