---
title: "Espaces — chapitres Curves et MetaSurfaces"
lang: fr-FR
---

# Les modules Curves A à D

Les modules **Curves A** à **Curves D** (sous-menu Curves du menu des panneaux) dessinent des courbes : des
**enveloppes** (y de 0 à 1) et des **formes d'onde** (y de −1 à 1), 64 au plus, de 2 à 128 points chacune. Chaque
module montre la courbe de son choix ; plusieurs modules peuvent montrer, et éditer, la même. Les courbes sont sauvées
avec le projet.

Dans Espaces, une courbe sert :

- de dynamique (Dyn) au mouvement d'un projecteur spatial (voir « Les modules Space A à D ») ou d'une MetaSurface :
  elle donne la place sur le chemin en fonction du temps ;
- de modulateur à une MetaSurface : la rotation de son pinceau, la vitesse de son mouvement ou son Mix suivent la
  courbe (voir « Les MetaSurfaces »).

C'est le même éditeur que les modules Curves A à H d'Interstys, et les blocs Curve des settings ont les mêmes clés dans
les deux plug-ins.

## Le pad

| Cellule | Contenu | Souris |
|------------|----------------------------------|--------------------------|
| 0 | Curve n : la courbe montrée | gauche : la suivante ; Shift + gauche : la précédente ; droit : la liste |
| 1 | son nom, ou « (no name) » ; « No curve » : la courbe n'existe pas | gauche : saisir le nom |
| 2 | son type | gauche : le suivant ; Shift + gauche : le précédent ; droit : menu |
| 3 | le nombre de points | — |
| 4 | Periodic ou Not periodic (Envelope, Waveform) | gauche : l'autre |
| 5 | la grille : No grid, 4, 8, 16, 32 | gauche : la suivante ; Shift + gauche : la précédente |
| 6 | Undo | gauche : annuler la dernière modification ; de nouveau : la refaire |
| 7 | Actions | gauche ou droit : New envelope, New half envelope (H-Envelope), New waveform, New quarter waveform (Q-Waveform), New half waveform (H-Waveform), Duplicate into the first free curve, Dump in the log, Sustain : the selected point, Sustain : none, Delete, Export : this curve (mSL settings), Export : all the curves (mSL settings) |

Sous le pad, la zone graphique montre la courbe ; par défaut, sa hauteur suit celle du panneau (au moins 100 pixels, au
plus la moitié de la largeur du module) ; la ligne sous le module la règle (au moins 60 pixels), un double clic sur
cette ligne rend la hauteur par défaut. Une ligne de texte donne ensuite x et y sous la souris, ou ceux du point
sélectionné (plusieurs points sélectionnés : leur nombre).

Le nom d'une courbe a de 1 à 31 caractères, sans guillemet ; il est unique, et tient compte de la casse. « New… »
remplace la courbe montrée par une courbe neuve de ce type, « Delete » la supprime : Undo les annule. « Duplicate into
the first free curve » copie la courbe, sans son nom, dans la première courbe libre, que le module montre ensuite.

## Les types

| Type | Partie dessinée |
|------------------|------------------------------------------------------|
| Envelope (Env) | toute l'enveloppe |
| H-Envelope (HEnv) | la montée ; la descente est son miroir |
| Waveform (Wave) | toute la période |
| Q-Waveform (QWave) | un quart de période, à partir de (0, 0) ; le reste est obtenu par symétrie |
| H-Waveform (HWave) | une demi-période, nulle aux deux bouts ; l'autre moitié par symétrie (−x, −y) |

Les points ont des x croissants, de 0 à 1 ; le premier et le dernier restent en x = 0 et en x = 1. Chaque point porte la
courbure c (de −1 à 1) du segment qui part de lui : 0 donne un segment droit, c et −c des arcs symétriques. Une courbe
périodique (Envelope, Waveform) finit au y de son début.

## La souris et le clavier

- Clic gauche sur un point : il est sélectionné et suit la souris tant que le bouton est enfoncé ; les points
  sélectionnés bougent ensemble (en x entre leurs voisins non sélectionnés ; le premier et le dernier, en y seulement).
- Shift + clic sur un point : ajoute à la sélection les points depuis le premier point sélectionné ; Cmd + clic : ajoute
  le point à la sélection, ou l'en retire.
- Clic gauche près de la courbe, entre deux points, puis glissé vertical : la courbure du segment (un clic sans bouger :
  un segment droit).
- Clic gauche ailleurs : un nouveau point, sélectionné.
- Clic droit sur un point : le supprime, ou supprime toute la sélection s'il en fait partie (sauf le premier et le
  dernier point).
- Shift pendant un déplacement : un mouvement fin (1/10, sans la grille).

Le **point de sustain** (enveloppes seulement) sépare la montée de la descente ; son y est le niveau du plateau. Un cadre
orange et une ligne verticale le marquent.

Touches, la souris sur le module :

| Touche | Effet |
|----------|----------------------------------------------------|
| d | écrit la courbe dans le journal, dans la syntaxe des settings |
| h | fait du point sélectionné le point de sustain ; de nouveau : plus de point de sustain |
| z | annule la dernière modification, comme la cellule Undo ; de nouveau : la refait |
| Cmd + A | sélectionne tous les points |

## Les courbes sur les chemins des MetaSurfaces

Le module Curves utilisé en dernier (la souris sur son graphe, ou un clic dans le module), s'il est visible, marque sa
courbe sur le chemin des MetaSurfaces, tant qu'un de ses points est sélectionné ou que la souris est sur son graphe :
des tirets en travers du chemin là où un rééchantillonnage selon cette courbe placerait les points (voir « Les
trajectoires » dans « Les MetaSurfaces »), les points de la courbe (petits points verts), les points sélectionnés (plus
gros, dorés, avec leur numéro) et l'abscisse sous la souris (un anneau).

En retour, le graphe de ce module montre le pinceau de chaque MetaSurface en mouvement sur son chemin : une ligne
verticale magenta à l'abscisse de sa place (la part de la longueur du chemin parcourue), un point sur la courbe et la
lettre de la vue. En mode Play, une courbe qui module une MetaSurface avec un cycle en secondes montre aussi la phase
de ce modulateur : une ligne orange pour la rotation, bleue pour la vitesse, verte pour le Mix.

## Les settings et les exports

Les courbes se décrivent dans les settings mSL (voir « Le format settings » dans « Les modules Edit A à D ») par des
blocs `Curve`, avec les mêmes clés que dans Interstys :

    settings(data(
        Curve 63  name "Montee"  type Env  sustain 2
            points 0 0 0  0.3 1 0.5  1 0 -0.25
        Curve "Vague"  type Wave  periodic On
            points 0 0 0  0.25 1 0  0.75 -1 0  1 0 0
    ));

- `Curve id` : la courbe, par son numéro (1 à 64) ou par son nom (un mot, ou un "texte") ; un nom qui n'existe pas
  encore prend la première courbe libre.
- `name "texte"` : son nouveau nom ; `type Env|Wave|HEnv|QWave|HWave` ; `periodic On|Off` (Env et Wave) ;
  `sustain n|Off` (un point d'une enveloppe Env).
- `points x y c x y c …` : de 2 à 128 points, x de 0 à 1 sans décroître, y de 0 à 1 (Env, HEnv) ou de −1 à 1, c de
  −1 à 1. Des points donnés retirent le sustain, sauf s'il est donné aussi.
- Les clés absentes ne changent rien (une courbe nouvelle : celle de son type). Plusieurs blocs d'une même courbe
  s'ajoutent. Le bloc s'arrête au premier mot qui n'est pas une de ses clés.
- Comme les blocs Edit, les blocs Curve ne changent rien si l'analyse trouve une erreur, même après eux ; le journal
  annonce chaque courbe lue (« Curves : curve 63 "Montee" (Env, 3 points) : read from settings »). Les erreurs vont de
  1650 à 1655.

**Exporter.** « Actions › Export : this curve (mSL settings) » écrit la courbe dans un fichier du sous-dossier Data du
dossier du projet, `nom-esp-curve-AAAA-MM-JJ-HH-MM-SS.mSL` (une courbe sans nom : son numéro, `Curve12-esp-curve-….mSL`) ;
« Export : all the curves (mSL settings) » les écrit toutes dans `Curves-esp-curves-….mSL`. Le script CMGS-auxiliary.eel
doit être lancé ; une erreur de l'export est notée dans le journal avec le code 1656.

**Importer.** Le fichier est un script mSL : déposé sur un module Curves, sa première courbe va dans la courbe que ce
module montre, qui prend son nom si aucune autre courbe ne le porte ; déposé ailleurs dans la fenêtre, une courbe
nommée remplace la courbe de même nom, ou prend la première courbe libre, et une courbe sans nom va dans la courbe de
même numéro. Un fichier exporté par Espaces se dépose aussi sur Interstys.

# Les MetaSurfaces

## Le principe

Une **MetaSurface** est un rectangle (ou un disque) sur lequel on dépose des diffusions de la bibliothèque des
configurations, de 2 à 32, chacune en un point et avec un poids. Chaque diffusion règne sur une **zone d'influence**,
dessinée dans sa couleur. Un **pinceau**, le halo qui entoure le pointeur, recueille sur la surface qu'il couvre les parts
des diffusions voisines ; ces parts sont les poids d'un mélange à puissance constante de leurs matrices, qui devient la
diffusion d'un projecteur. On joue ainsi d'un geste entre plusieurs diffusions, à la souris ou le long d'une trajectoire.

- **Les zones.** La distance d'un point à une diffusion est divisée par le poids de celle-ci : un poids de 2 donne une
  zone deux fois plus étendue, un poids de 0,5 une zone deux fois plus petite (1 par défaut). Chaque point de la surface
  appartient à la zone de la diffusion la plus proche ; la couleur pâlit à l'approche des frontières. Une même diffusion
  placée plusieurs fois ne forme qu'une zone.
- **Les parts.** En un point, les parts viennent du triangle des trois diffusions voisines qui le contient (une
  triangulation de Delaunay), au plus trois diffusions ; hors de leur enveloppe, des deux plus proches sur le bord. Chaque
  part suit la loi du Hyper Slider (sin²) : des diffusions placées sur une même ligne donnent exactement l'effet du
  mode Hyper Slider. Le poids d'une diffusion multiplie aussi sa part. Les parts du pinceau sont la moyenne de celles des
  points qu'il couvre, pondérée par son profil d'énergie (Power) : un pinceau très petit donne l'interpolation au point
  du pointeur, un pinceau plus grand un lissage sur la région couverte.
- **La bande.** Autour de la surface, une bande où le pointeur peut aller : elle ne recueille aucune part. La
  **couverture** (la part de l'énergie du pinceau qui tombe dans la surface) règle l'amplitude : un pinceau à moitié
  dehors donne −3 dB, un pinceau entièrement dans la bande ne donne aucun son. En venant de la bande, le son entre donc
  progressivement.

La **bibliothèque** garde 32 MetaSurfaces, MS1 à MS32, sauvées avec le projet : pour chacune, son nom, ses diffusions
placées, les réglages du pinceau, du son et du mouvement, ses trajectoires et leurs placements. Les quatre modules
**MetaSurface A** à **MetaSurface D** (sous-menu MetaSurface du menu des panneaux) sont des vues : chacune montre une
MetaSurface de la bibliothèque, pilote son projecteur et garde son état de jeu. Plusieurs MetaSurfaces peuvent jouer à
la fois, sur des projecteurs différents.

## Les deux modes

Une vue est en mode **Edit**, où l'on construit la surface, ou en mode **Play**, où l'on joue (cellule 1). Séparer les
deux modes évite qu'un geste de jeu déplace une diffusion par erreur.

En **Edit**, la souris sur la surface :

- clic droit sur une place vide : ajoute une diffusion à cet endroit (le menu de la bibliothèque des configurations) ;
- clic droit sur une diffusion : son menu (une autre diffusion, son poids, la retirer) ;
- clic gauche sur une diffusion : la sélectionne (cellule 6 : son poids) ; glisser : la déplace ;
- Alt + glissé vertical sur une diffusion : son poids (vers le haut : plus grand ; 80 pixels : × 2).

Passer de Play à Edit agit comme un bypass : la vue garde son état (le son en cours ou non, le mouvement et son temps,
la pause) et rend son projecteur ; de retour en Play, tout reprend aussitôt là où on en était.

## Le pad

Le pad a sept lignes. Les cellules de valeurs se règlent comme des potentiomètres : glisser ; Shift + clic gauche : la
valeur par défaut ; clic droit : un menu de valeurs.

| Cellule | Contenu | Souris |
|------------|----------------------------------|--------------------------|
| 0 | la MetaSurface montrée : MSn et son nom | gauche : la suivante ; Shift + gauche : la précédente ; droit : la bibliothèque |
| 1 | le mode : Edit ou Play | gauche : l'autre |
| 2 | le nombre de diffusions placées | — |
| 3 | Aspect : les proportions de la surface (1:1, 4:3, 3:2, 16:9, 2:1, 3:4, 2:3, 9:16, 1:2), « disk » pour un disque | gauche : la suivante ; Shift + gauche : la précédente ; droit : menu (les proportions ; tourner de 90° dans un sens ou dans l'autre, retourner de haut en bas ou de gauche à droite, avec les diffusions et le pinceau ; Rectangle ou Disk, une ellipse quand la surface n'est pas carrée) |
| 4 | Band : la largeur de la bande (0 à 50 % ; 8 %) | potentiomètre |
| 5 | Projector n : le projecteur piloté | gauche : le suivant ; Shift + gauche : le précédent ; droit : menu |
| 6 | le poids de la diffusion sélectionnée (0,1 à 10 ; 1) | potentiomètre ; droit : le menu de la diffusion |
| 7 | Actions | les deux clics : Rename…, Duplicate into (une autre MetaSurface, remplacée), Remove the configuration selected, Remove all the configurations, Clear (diffusions, nom, réglages), Export : MSn, Export : all the MetaSurfaces used |
| 8 | Spread : le rayon du pinceau, en % de la diagonale (1 à 100 % ; 15 %) | potentiomètre |
| 9 | Power : le profil d'énergie, de −1 (presque uniforme sur tout le disque) à 1 (concentré près du centre) ; 0 : un cône | potentiomètre |
| 10 | Shape : le contour, du cercle (0) au carré (1) et à la croix (2) | potentiomètre |
| 11 | Stretch : le rapport des axes (0,1 à 10 ; 1) | potentiomètre |
| 12 | Offset : la distance du centre du pinceau au pointeur, en % du rayon (0 à 200 %) | potentiomètre |
| 13 | Rotation : la rotation du pinceau autour du pointeur, en tours par seconde (−4 à 4) ; « ~ » : modulée | potentiomètre ; Shift + clic : Off, puis la rotation d'avant (entre parenthèses) |
| 14 | Angle : l'angle de départ, en degrés (depuis la verticale, dans le sens des aiguilles d'une montre) | potentiomètre (sans butée) |
| 15 | Brush : en Play, sur la souris (mouse) ou tenu (held) ; en Edit, montré ou caché ; puis la couverture | gauche : l'autre |
| 16 | Volume (−60 à +12 dB ; 0) | potentiomètre |
| 17 | Latency : la durée d'interpolation du projecteur (5 à 2000 ms ; 80) | potentiomètre |
| 18 | Rule : la latence fixe, ou pour chaque dixième de la diagonale parcouru (distance) | gauche : l'autre |
| 19, 20 | Attack, Release : les durées du fondu d'entrée et du fondu de sortie (0,01 à 60 s ; 2 et 4 s) | potentiomètres |
| 21 | l'état : Off, Fade-in, On, Fade-out, et le projecteur piloté | en Play : gauche, départ avec fondu ou arrêt avec fondu ; droit, départ ou arrêt immédiats |
| 22 | Pause : le mouvement et la rotation arrêtés, le son continue (Paused) | gauche : l'un ou l'autre |
| 24 | Brush : sur la souris (mouse) ou sur le chemin (path) | gauche : l'autre |
| 25 à 28 | A, B, C, D : les quatre trajectoires | gauche : la suivante ; Shift + gauche : la précédente ; Alt + clic : son placement ; Cmd + clic : un glissement vers elle ; droit : menu |
| 29 | Mix : la place dans la chaîne des trajectoires ; « ~ » : modulé | potentiomètre ; Shift + clic : 0 ; droit : la chaîne (A B, A B C, A B C D) et des valeurs |
| 30 | Glide : le temps d'un glissement (1 à 300 s) ; Gliding n % : un glissement en cours | gauche : le mode Glide ; potentiomètre ; Shift + clic : 10 s ; droit : menu |
| 31 | Dyn : la dynamique du mouvement, sa courbe et son mode | gauche : la courbe suivante ; Shift + gauche : la précédente ; droit : menu |
| 32 | Duration : la durée d'un parcours du chemin (0,5 s à 10 min ; 20 s) ; « ~ » : la vitesse modulée | potentiomètre |
| 33 | le mouvement : Once, Loop, Back and forth, Loop reverse | gauche : le suivant ; Shift + gauche : le précédent ; droit : menu |
| 34 | Speed : constante le long du chemin (path) ou le même temps entre ses points (points) | gauche : l'autre |
| 35 | Radius : le rayon des formes Circle, Square, Star et Spiral (5 à 100 % ; 60 %) | potentiomètre |
| 36 | Simulate : le pinceau sur le chemin, sans son | gauche : marche ou arrêt |
| 37 | Record : l'enregistrement du pinceau (Recording n s : en cours) | gauche : départ ou fin (aussi la touche e) |
| 38 | Restart : le mouvement repart du début du chemin | les deux clics |
| 39 | le compteur : la place sur le chemin (en secondes) et le sens (> ou <) | — |
| 40, 41 | x, y : le déplacement du chemin entier ou de la trajectoire placée (−200 à 200 %) | potentiomètres |
| 42 | turn : sa rotation, en degrés (sans butée) | potentiomètre |
| 43 | scale : sa taille (0,1 à 10 ; 1) | potentiomètre |
| 44 | Placement : un menu | les deux clics : remises à zéro (tout, la position, la rotation, la taille), centrer le chemin, l'ajuster à la surface, le retourner de gauche à droite ou de haut en bas |
| 45 | Place : ce que placent les cellules 40 à 43 et les glissés avec Cmd : le chemin entier (path) ou une trajectoire A, B, C ou D | les deux clics : menu |
| 48, 50, 52 | les modulateurs de la rotation (Rot), de la vitesse (Speed) et du Mix : leur courbe et leur cycle | gauche : la courbe suivante qui existe, puis Off ; Shift + gauche : la précédente ; droit : menu (Off, les courbes, le cycle) |
| 49, 51, 53 | leur profondeur (−4 à 4 ; 1) | potentiomètre |

## Le jeu

En mode **Play**, le pinceau suit la souris sur la surface et sa bande. Il est dessiné en jaune : son contour, le contour
où son énergie est moitié, son centre et la place du pointeur ; à côté de chaque diffusion, sa part. On peut ainsi régler
le pinceau sans son : la diffusion n'est pas calculée tant que la MetaSurface ne sonne pas. Le mode Play ne déplace
jamais les diffusions.

- **Clic gauche** sur la surface ou sa bande : départ avec un fondu d'entrée (Attack : le rayon et le volume montent de 0
  aux valeurs réglées) ; le halo passe au vert. Un nouveau clic gauche : fondu de sortie (Release : le rayon et le volume
  descendent jusqu'à 0), puis le son s'arrête.
- **Clic droit** : départ ou arrêt immédiats (environ 5 ms). Shift + clic droit ouvre toujours le menu des panneaux.
- Pendant le jeu, chaque mouvement du pointeur recalcule la diffusion ; le projecteur y va dans la durée d'interpolation
  (Latency : fixe, ou proportionnelle à la distance parcourue, cellule Rule).
- **La souris quitte la surface et sa bande** : le pinceau reste à sa dernière place et le son continue (on peut aller
  régler un autre module) ; il repart quand la souris revient.
- **Alt + clic** : le pinceau est tenu, détaché de la souris ; il reste où il est, et la souris peut travailler ailleurs,
  même sur la surface. Le même Alt + clic le rattache à la souris (avec la durée d'interpolation), comme la cellule 15.
  Tenu, le pinceau se manipule : glisser sa croix (la place du pointeur) le déplace, un clic sur sa croix le rattache à la
  souris sans le déplacer, glisser sa forme déplace son centre autour de la croix (Offset et Angle).
- **La molette**, le pinceau montré : Spread ; Shift + molette : Power.
- **Pause** (cellule 22) : le mouvement sur la trajectoire et la rotation du pinceau s'arrêtent là où ils sont, le son
  continue ; un second clic les fait repartir. Un départ termine la pause.

En mode Edit, la cellule 15 montre le pinceau (tenu : on le déplace par sa croix et par sa forme) ou le cache.

**Le projecteur.** La matrice mélangée devient la diffusion du projecteur choisi (cellule 5) : son moteur fait la
transition, comme pour un changement de diffusion. Les diffusions d'entrée et de sortie, le volume du module Global, Mute
et Solo du projecteur s'appliquent comme d'habitude. Dès son premier départ, la vue pilote le projecteur : le hasard et
le Hyper Slider ne le touchent plus, et il est silencieux quand la MetaSurface ne sonne pas ; il est rendu quand la vue
quitte le mode Play.

**Les vues Space.** Une vue Space qui montre le projecteur piloté montre, pendant le jeu, sa matrice (les croix) et les
niveaux réels de ses haut-parleurs (les halos). Le pinceau montré sans son, elle montre les énergies calculées par la
MetaSurface, avec la mention « MetaSurface A : simulated ».

## Les trajectoires

Avec **Brush : path** (cellule 24), le pinceau suit un chemin au lieu de la souris. Ce chemin se construit comme celui
d'un projecteur spatial (voir « Les trajectoires », « Le placement des trajectoires » et « Le glissement » dans « Les
projecteurs spatiaux »), dans le plan de la surface :

- **Quatre trajectoires** A, B, C, D (cellules 25 à 28) : une forme (None, Circle, Square, Star, Spiral, Central ; leur
  rayon : cellule 35), le chemin d'un module Edit A à D, ou une trajectoire T1 à T128 de la bibliothèque (on garde x et
  y). Le **Mix** (cellule 29) donne la place dans la chaîne A B, A B C ou A B C D ; en mode **Glide** (cellule 30), un
  changement de Mix, ou Cmd + clic sur A, B, C ou D, glisse de la trajectoire courante à la nouvelle dans le temps du
  Glide.
- **Le placement** : chaque trajectoire a le sien (déplacement, rotation, taille, autour de son barycentre), puis le
  chemin entier a le sien, autour du centre de la surface. Alt + clic sur A, B, C ou D, ou la cellule Place (45), choisit
  ce que placent les cellules 40 à 43 : la trajectoire placée est alors dessinée seule, en or, avec son pivot. À la
  souris, sur la vue : Cmd + glisser (gauche) déplace, Cmd + Shift + glisser (gauche) change la taille, Cmd + glisser
  (droit) tourne, Cmd + Shift + glisser (droit) tourne et change la taille. Le menu Placement retourne aussi le chemin
  ou la trajectoire, de gauche à droite ou de haut en bas.
- **Le menu de A, B, C, D** (clic droit) : les trajectoires, le placement et sa remise à zéro, un glissement vers elle ;
  pour une trajectoire de la bibliothèque, la retirer de la bibliothèque, et ses transformations, avec Undo : un lissage
  (léger, moyen, fort ; il ne rétrécit pas la trajectoire), un rééchantillonnage à distances égales, ou selon la densité
  d'une courbe du module Curves (une courbe haute rapproche les points : le pinceau y ralentit quand Speed est sur
  « points » ; une courbe plate : distances égales). Un rééchantillonnage fait depuis une MetaSurface passe sa cellule
  Speed sur « points ».
- **Le parcours** : Duration (cellule 32), Once, Loop, Back and forth ou Loop reverse (cellule 33 ; Loop reverse : de la
  fin vers le début), à vitesse constante le long du chemin ou au même temps entre ses points (cellule 34). Dyn
  (cellule 31) change l'allure : une courbe d'accélération (Linear, Quad, Cubic, Quartic, Quintic, Exp, Circle, Sine,
  Elastic, Bounce) ou une courbe du module Curves, avec un mode (in, out, in-out, out-in). Une courbe du module Curves donne
  la place sur le chemin en fonction du temps : une enveloppe telle quelle, une forme d'onde ramenée de [−1, 1] à
  [0, 1] ; une courbe qui ne monte pas sans cesse fait revenir le pinceau en arrière. Le mouvement avance avec le temps :
  une nouvelle durée ne change que sa vitesse, un changement de mode garde la place du pinceau sur le chemin. Restart
  (cellule 38) repart du début ; le compteur (cellule 39) montre la place et le sens.
- **Le chemin** est tracé en magenta sur un liseré, avec son départ (un point) et son sens (une flèche à mi-parcours),
  en Edit comme en Play. Les départs et les arrêts se font par les mêmes clics que le jeu à la souris.
- **Simulate** (cellule 36 ; Play, le pinceau sur le chemin) : le pinceau parcourt le chemin sans son, et la vue Space
  du projecteur montre les énergies calculées ; c'est le mode pour construire et régler une trajectoire.
- **Record** (cellule 37, ou la touche e la souris sur le module ; Play, le pinceau sur la souris) : le chemin de la
  souris, relevé toutes les 50 ms, devient une trajectoire de la bibliothèque, avec son temps, rangée dans A ; son
  tracé apparaît pendant l'enregistrement. Elle est rangée sans placement : la trajectoire placée rejoue exactement le
  geste.

Un module Edit A à D dont le chemin sert de trajectoire montre, dans sa vue de dessus, les zones de la MetaSurface sous
ses points. Le menu de sa vue offre deux présentations : le chemin tel qu'il est, la surface placée dessous ; ou
« Follow the MetaSurface », la même vue que la MetaSurface (la surface droite, le chemin placé ; l'édition à la souris
reste celle des points du chemin). Dans les deux, la molette rapproche la caméra puis zoome (jusqu'à × 16), Cmd +
glisser sur le vide déplace la vue, et « Reset the zoom and the move of the view » les remet à zéro. **Lock 2D** (case
de la vue, ou menu de la vue) garde les points dans le plan horizontal (z = 0) et montre la vue de dessus : glisser sur
le vide la déplace, Shift + glisser la fait tourner autour de la verticale.

## Les modulateurs

La septième ligne du pad module trois réglages par des courbes du module Curves :

- **Rot** : la rotation du pinceau est multipliée par 1 + profondeur × F(phase) ;
- **Speed** : la vitesse du mouvement sur le chemin est multipliée par 1 + profondeur × F(phase) ;
- **Mix** : le Mix augmente de profondeur × F(phase), borné à [0, 1].

F est la courbe (une forme d'onde de −1 à 1, ou une enveloppe de 0 à 1) ; la profondeur va de −4 à 4 (au-dessous de 0,
le pinceau tourne ou avance en sens inverse). Le **cycle** donne la phase : **Path**, la place du pinceau sur le chemin
(la part de sa longueur parcourue) ; ou une période de 0,5 à 300 s, avec une phase propre au modulateur, arrêtée par la
Pause et remise à 0 par Restart et au départ du mouvement. Une cellule modulée porte « ~ ». Le graphe de la courbe, dans
un module Curves, montre la phase des modulateurs à cycle en secondes (voir « Les modules Curves A à D »).

## Les settings et les exports

Une MetaSurface se décrit dans les settings mSL par un bloc `MetaSurface`, à la suite des blocs `Curve` des courbes
qu'elle utilise :

    settings(data(
        Curve "Montee"  type Env  points 0 0 0  0.5 1 0  1 0 0
        MetaSurface 3  name "Nuage"
            zone 12 0.2 0.3 1  zone 15 0.7 0.25 1.5
            zone 21 0.5 0.8
            aspect 1.5  surface Rect  band 0.08  proj 1
            spread 0.15  power 0  shape 0  stretch 1
            offset 0  rotation 0.25  angle 0
            volume 0  latency 80  rule Fixed
            attack 2  release 4
            brush Path  duration 20  mode Loop
            speed Path  radius 0.6
            A Circle  place 0 0 0 1
            B T12  place 0.1 0 45 0.8  flip X
            chain AB  mix 0.25  glide 10 Off
            dyn Curve "Montee" In
            modrot Off
            modspeed Curve 5  cycle 8  depth 0.5
    ));

- `MetaSurface n` : la MetaSurface MSn de la bibliothèque (1 à 32), puis des clés dans n'importe quel ordre ; les clés
  absentes ne changent rien. Le bloc s'arrête au premier mot qui n'est pas une de ses clés.
- `name "texte"` ; `zone c x y [poids]` : la diffusion c placée en x, y (de 0 à 1 ; x vers la droite, y vers le bas),
  avec son poids (0,1 à 10 ; 1 par défaut). Données, les zones remplacent toutes les diffusions placées (32 au plus).
- Les réglages du pad, par un nombre : `aspect` (le rapport largeur / hauteur, 0,5 à 4), `band`, `proj`, `spread`,
  `power`, `shape`, `stretch`, `offset`, `rotation`, `angle`, `volume`, `latency`, `attack`, `release`, `duration`,
  `radius`, `mix` ; ou par un mot : `surface Rect|Disk`, `rule Fixed|Distance`, `brush Mouse|Path`,
  `mode Once|Loop|Back|Reverse`, `speed Path|Points`, `chain AB|ABC|ABCD`. Band, Spread, Radius et Mix s'écrivent de 0
  à 1 (0.08 pour 8 %), Offset de 0 à 2 (en rayons du pinceau).
- `A` … `D` suivis de la trajectoire : `None`, `Circle`, `Square`, `Star`, `Spiral`, `Central`, `Edit A` … `Edit D`,
  `T1` … `T128` (ou `T 12`) ; puis `place x y tour taille` (x et y : des parts de la largeur et de la hauteur, 0.1
  pour 10 % ; le tour en degrés) et `flip None|X|Y|XY` pour cette trajectoire. Après `path`,
  `place` et `flip` placent le chemin entier.
- `glide t [On|Off]` (le temps et le mode Glide) ; `dyn` suivi d'une courbe d'accélération (`Linear` … `Bounce`) ou de
  `Curve id` (son numéro ou son nom : une courbe du projet, ou d'un bloc Curve placé avant), puis `In|Out|InOut|OutIn`.
- `modrot`, `modspeed`, `modmix` : `Off` ou `Curve id`, puis `cycle Path|secondes` et `depth d`.

Comme les blocs Edit et Curve, les blocs MetaSurface ne changent rien si l'analyse trouve une erreur, même après eux. Le
journal annonce chaque MetaSurface lue (« MetaSurface MS3 : Nuage : read from settings (3 configurations) ») et les
diffusions qu'elle place sans qu'elles soient définies dans le projet. Les erreurs sont 2441 et 2443 à 2449.

**Exporter.** « Actions › Export : MSn » écrit la MetaSurface dans un fichier du sous-dossier Data du dossier du projet,
`nom-esp-MS3-AAAA-MM-JJ-HH-MM-SS.mSL` (sans nom : `MetaSurface-esp-MS3-….mSL`) ; « Export : all the MetaSurfaces used »
écrit toutes celles qui sont utilisées dans `MetaSurfaces-esp-library-….mSL`. Chaque MetaSurface y est précédée de ce
qu'elle utilise : ses courbes (blocs Curve), ses trajectoires de la bibliothèque (`trajectory n`) et les chemins de ses
modules Edit (blocs Edit). Les diffusions ne sont pas dans le fichier : ce sont celles du projet qui le lit, de mêmes
numéros (une diffusion absente est signalée dans le journal). Le script CMGS-auxiliary.eel doit être lancé ; les erreurs
de l'export sont 2450 et 2451.

**Importer.** Déposé sur une vue MetaSurface, le fichier envoie son premier bloc MetaSurface dans la MetaSurface que
montre la vue ; déposé ailleurs dans la fenêtre, chaque bloc va dans la MetaSurface de son numéro.
