---
title: "CMGS — fragment MetaSurface"
lang: fr-FR
---

# La MetaSurface de Diffusion-3 (projet)

*Conception du 23 novembre 2026, d'après la maquette de J.-J. Girardot (`JJG-MetaSurface.png`) et sa description ; les
choix ont été validés le même jour. L'étape 1 est en cours.*

## Principe

Une MetaSurface est un rectangle sur lequel on dépose N configurations de diffusion (2 au minimum, 32 au plus ; 6 sur la
maquette), chacune en un point (x, y) et avec un poids. Chaque configuration règne sur une zone d'influence (les cellules
de la maquette). Un pinceau, le halo qui entoure le pointeur, recueille sur la surface qu'il couvre les parts des
configurations voisines. Ces parts w₁ … w_N (de somme 1) sont les poids d'une interpolation à puissance constante des
matrices des configurations :

    g[k] = A · sqrt( Σ wᵢ · gᵢ[k]² )        (k : un couple entrée → sortie)

C'est la généralisation à N configurations du Hyper Slider : `mergeconf` mélange deux matrices avec cos² et sin², dont
la somme vaut 1. Exigence (J.-J. Girardot) : une MetaSurface dont toutes les configurations sont sur une même ligne doit
donner exactement l'effet du Hyper Slider. A est l'amplitude : volume, enveloppe (fade-in, fade-out), couverture (voir plus bas).

La matrice obtenue devient la consigne (`prx_pcons`) d'un projecteur, le projecteur cible de la MetaSurface. Son moteur
fait la transition depuis la matrice courante (morph), avec la durée d'interpolation de la MetaSurface. Les entrées
(indiff), les sorties (outdiff), le volume du module Global, Mute et Solo du projecteur s'appliquent comme aujourd'hui :
une MetaSurface ne demande pas de nouveau moteur audio.

## Le modèle

### Les zones d'influence

La distance effective du point x à la configuration i est dᵢ(x) = |x − pᵢ| / poidsᵢ : un poids de 2 donne une zone deux
fois plus étendue, un poids de 0,5 une zone deux fois plus petite. Le poids vaut 1 par défaut. Le point x appartient à la
zone de la configuration dont la distance effective est la plus petite (un diagramme de Voronoï pondéré) ; les frontières
entre zones de poids différents sont des arcs de cercle. Les zones sont ce que l'on voit ; le son vient de l'interpolation
entre configurations voisines (ci-dessous), dont elles donnent l'image.

Le dessin : chaque configuration a sa couleur, un pastel léger (sa teinte vient de son numéro : une même configuration a
la même couleur partout), qui tend vers le blanc (thèmes clairs) ou le noir (thèmes sombres) à l'approche des frontières ;
les couleurs ne se recouvrent pas. La même configuration placée deux fois, ou plus, ne forme qu'une zone : pas de
frontière entre ses copies (la frontière se cherche avec la configuration voisine d'un autre numéro). Le dessin est calculé une fois, dans une image hors écran, quand la surface, ses
configurations ou la taille du module changent ; chaque image de l'écran ne fait que la recopier.

### Le pinceau

- **Spread** : le rayon, en fraction de la diagonale de la surface.
- **Power** P ∈ [−1, 1] : le profil d'énergie, p(r) = (1 − r)^γ avec γ = 8^P et r le rayon normalisé. P = 0 donne le
  cône de la maquette ; P = −1 une énergie presque uniforme sur tout le disque (la forme grise externe) ; P = +1 une
  énergie concentrée tout près du centre (la forme grise interne).
- **Shape** S ∈ [0, 2] : le contour, cercle (0), carré (1), croix (2), avec toutes les formes intermédiaires.
- **Stretch** : le rapport des axes (forme asymétrique, ellipse).
- **Offset** : la distance entre le centre du pinceau et le curseur, en % du spread.
- **Rotation** : la vitesse de rotation du pinceau autour du curseur, en tours par seconde, positive ou négative ;
  **Angle** : l'angle de départ. Même avec la souris immobile, la rotation fait varier les parts.

Calcul : le pinceau est échantillonné sur une grille polaire de 8 anneaux × 24 rayons, plus le centre. Chaque point
d'échantillon est pondéré par p(r) et par l'aire qu'il représente. Le coût est de l'ordre de 200 × N distances par mise à
jour, en @gfx.

### Les parts : l'interpolation

- **En un point x** : les coordonnées barycentriques de x dans le triangle de Delaunay des configurations qui le contient
  (la triangulation de Delaunay est le dual du diagramme de Voronoï des zones) ; au plus trois configurations y
  participent, et les parts varient linéairement de l'une à l'autre. Hors de l'enveloppe convexe des configurations, x
  est ramené sur son bord : deux configurations. Configurations alignées, ou deux seulement : l'interpolation linéaire
  entre les deux voisines sur la ligne.
- **La loi du Hyper Slider** : chaque coordonnée b devient sin²(π b / 2), puis les parts sont normalisées (somme 1). Sur
  un segment entre deux configurations (b = 1 − t et t), cela donne cos²(π t / 2) et sin²(π t / 2), les poids de
  `mergeconf` : la même interpolation à puissance constante.
- **Les copies d'une configuration** : leurs parts s'additionnent (la même matrice) ; on passe de l'une à l'autre sans
  changement audible.
- **Le poids d'une configuration** multiplie sa part avant la normalisation (son influence s'étend sur ses voisines) ; il
  élargit aussi sa zone dessinée.
- **Le pinceau** : les parts sont la moyenne de celles de ses points d'échantillon dans la surface, pondérée par son profil
  d'énergie (Power) ; c'est le calcul simple « par les zones recouvertes par la brosse ». Un Spread très petit donne
  l'interpolation au point du pointeur : exactement le Hyper Slider pour des configurations alignées ; un Spread plus
  grand, un lissage sur la région couverte. Les points tombés dans la bande ne recueillent rien.
- **Le coût** : la triangulation (32 points au plus) est calculée quand les configurations changent ; chaque mise à jour
  cherche le triangle d'environ 200 points d'échantillon.

### La couverture

c = (énergie du pinceau dans la surface) / (énergie totale du pinceau). L'amplitude est multipliée par √c, si bien que
l'énergie l'est par c : un pinceau à moitié dehors donne −3 dB, un pinceau entièrement dans la bande ne donne aucun son.
En approchant depuis la bande, le son entre donc progressivement.

### L'énergie des haut-parleurs

Pour chaque sortie, on prend le maximum des |g[k]| sur ses entrées, normalisé à 1. Ce sont les halos de la vue 3D.

## Les interactions

### Deux modes du module

- **Edit** : on construit la surface. Clic droit sur une place vide : ajouter une configuration (menu de la bibliothèque
  des configurations). Glisser un marqueur : le déplacer. Clic droit sur un marqueur : son menu (changer de
  configuration, poids, supprimer). Alt + glisser vertical sur un marqueur : son poids.
- **Play** : on joue.

Séparer les deux modes évite qu'un clic de jeu déplace une configuration par erreur. Le passage de Play à Edit agit comme
un bypass : la vue garde son état (son en cours ou non, la trajectoire et son temps, la pause) et rend son projecteur ;
de retour en Play, tout reprend aussitôt là où on en était (le son sans fondu).

### Le jeu (mode Play)

- **Survol, inactif** : halo jaune. Les parts sont calculées et affichées (pourcentage dans chaque zone), ce qui permet de
  régler le pinceau sans son. La diffusion n'est pas calculée. Le mode Play ne déplace jamais les configurations.
- **Clic gauche** : départ avec fade-in (Attack) : le spread et le volume montent de 0 aux valeurs réglées. Le halo passe
  au vert.
- **Clic droit** : départ immédiat (attaque d'environ 5 ms).
- **Actif** : chaque mouvement du pointeur recalcule la diffusion. La durée d'interpolation (Latency) est soit fixe (en ms),
  soit proportionnelle à la distance parcourue (en ms pour 10 % de la diagonale) : la cellule Rule.
- **Pause** : le mouvement sur la trajectoire et la rotation du pinceau s'arrêtent là où ils sont, le son continue dans la
  configuration calculée ; un second clic les fait repartir de là. Un départ (On) termine la pause.
- **Nouveau clic gauche** : fade-out (Release) : le spread et le volume descendent jusqu'à 0, puis le son s'arrête.
- **Nouveau clic droit** : arrêt immédiat (environ 5 ms).
- **Volume** : 0 dB par défaut, réglable pendant le jeu.
- **La souris quitte la surface et sa bande** : le pinceau reste à sa dernière place et le son continue (on peut aller
  régler un autre module) ; il repart quand la souris revient.
- **Le pinceau tenu** (détaché de la souris) : un clic sur sa croix (la place de la souris) le rattache, sans le
  déplacer ; glisser sa croix le déplace ; glisser sa forme (son contour, ou son intérieur) déplace son centre autour de
  la croix : Offset et Angle (compté depuis la verticale, dans le sens des aiguilles d'une montre), ce qui permet de
  juger de l'effet de la rotation. D'autres formes de pinceau viendront ensuite.
- **Shift + clic sur Rotation** : Off, puis retour à la rotation d'avant (affichée entre parenthèses).
- **En mode Edit**, la cellule Brush montre le pinceau (tenu : on le déplace par sa croix et par sa forme) ou le cache.
- **Alt + clic** : désolidarise le pinceau de la souris (il reste où il est, la souris peut aller travailler ailleurs,
  même sur la surface) ; le même Alt + clic les solidarise de nouveau, le pinceau rejoignant la souris (avec la durée
  d'interpolation).
- **La bande** : sa largeur est réglable (Band) ; le pointeur peut y évoluer (voir la couverture).
- **Molette** (proposition) : le spread ; Shift + molette : Power.

## Les trajectoires

- **Lecture** : une trajectoire 2D est plaquée sur la surface, puis parcourue en un temps donné (Duration), en mode Once,
  Loop, Back and forth ou Loop reverse (de la fin vers le début), à vitesse constante le long du chemin ou à temps égal
  entre ses points.
  - Les trajectoires viennent de la bibliothèque T1 … T128 (on garde x et y), d'un éditeur Edit A … D ou d'un
    enregistrement.
  - Le placement de la trajectoire sur la surface, autour du centre de celle-ci : déplacement en x (en % de la largeur,
    vers la droite) et en y (en % de la hauteur, vers le haut), rotation (en degrés, sens des aiguilles d'une montre),
    homothétie (0,1 … 10) ; Placement : remises à zéro, centrer, ajuster à la surface (90 %). À la souris, sur la vue :
    Cmd + glisser (gauche) déplace, Cmd + Shift + glisser (gauche) change la taille, Cmd + glisser (droit) tourne,
    Cmd + Shift + glisser (droit) tourne et change la taille, autour du centre du placement. Un enregistrement est rangé
    sans placement : la trajectoire placée le rejoue exactement.
  - L'éditeur Edit A … D a deux présentations (menu de la vue) : le chemin tel qu'il est, la surface placée dessous à
    l'inverse ; ou « Follow the MetaSurface » : la même vue que la MetaSurface (la surface droite, le chemin placé ;
    la caméra de l'éditeur est ramenée dans le repère du chemin, si bien que les points, la grille et les axes tournent
    et changent de taille avec le placement, et que l'édition à la souris reste celle des points du chemin). Dans les
    deux : la molette rapproche la caméra puis zoome (jusqu'à × 16), Cmd + glisser sur le vide (en View : partout)
    déplace la vue ; « Reset the zoom and the move of the view » ; les boules gardent leur taille. Le fond de la
    MetaSurface est posé sur le plan z = 0 tel que la caméra le voit (gfx_transformblit), dans toutes les vues.
  - **Lock 2D** (case de la vue, ou menu de la vue) : les points restent dans le plan z = 0 (leurs z et ceux de leurs
    courbures sont remis à 0 à chaque image), la vue est celle de dessus ; glisser sur le vide déplace la vue,
    Shift + glisser la fait tourner autour de la verticale ; pas d'orbite, pas de déplacement en profondeur, Z, Rot X et
    Rot Y de la colonne inactifs ; choisir une autre vue déverrouille.
  - Les angles (Angle du pinceau, Path turn) tournent sans butée tant que la souris bouge (un degré par pixel).
  - Le mouvement avance avec le temps (en pause, il reste où il est ; une nouvelle durée ne change que sa vitesse). Un
    changement de mode pendant le mouvement garde la place du pinceau sur le chemin : seul le sens change (Back and
    forth : le sens du moment). Le compteur montre la place sur le chemin (en secondes) et le sens (> ou <).
  - Le chemin est tracé en magenta (foncé sur les thèmes clairs, clair sur les sombres) sur un liseré du fond, avec son
    départ (un point) et son sens (une flèche à mi-parcours), en Edit comme en Play.
- **Départ et arrêt** : les mêmes clics que le jeu à la souris (gauche avec fondu, droit immédiat).
- **Enregistrement** (Record) : le chemin de la souris pendant que la MetaSurface est active devient une trajectoire de
  la bibliothèque, avec son temps.
- **Simulation** (Simulate) : la trajectoire est parcourue sans son. Le halo suit, et la vue 3D montre les énergies
  calculées. Le mode sert à construire et à régler une trajectoire.
- **Fil d'exécution** (décidé) : tout se fait en mode graphique ; le déroulement tourne en @gfx (environ 30 fois par seconde, même fenêtre fermée grâce à
  gfx_idle) ; la transition du projecteur lisse les pas. Limite : un rendu hors ligne (bounce) ne fait pas tourner @gfx.
  S'il faut rendre une trajectoire hors ligne, son déroulement passera plus tard en @block.

## La vue 3D

Les vues Space A … D montrent déjà, pour un projecteur, les gains (des croix) et les niveaux des haut-parleurs (des
halos ; touche h). Une vue Space liée à une MetaSurface affiche :
- en jeu : les niveaux réels de son projecteur ;
- en simulation : les énergies calculées, le halo maximal correspondant au coefficient normalisé 1.

Le seul ajout est une source de niveaux simulée pour la vue.

## La bibliothèque, les vues, la sauvegarde

- **Bibliothèque** : MS1 … MS32. Une MetaSurface y garde :
  - son nom ;
  - ses configurations (numéro, x, y, poids) ;
  - les réglages du pinceau, des temps, de la bande ;
  - sa trajectoire et son placement.

  La bibliothèque est sauvée avec le projet.
- **Vues** : 4 modules, « MetaSurface A » … « D ». Chacune montre une entrée de la bibliothèque, pilote un projecteur et
  garde son état de jeu (actif, position, angle, enveloppe). Plusieurs MetaSurfaces peuvent jouer à la fois, sur des
  projecteurs différents.
- **Export** : en réglages mSL, par mSL_Export (`Data/<nom>-d3-metasurface-<date>.mSL`), par exemple :

      settings(data( MetaSurface 3 "Nuage" conf 12 0.2 0.3 1, conf 15 0.7 0.25 1.5, conf 21 0.5 0.8 1 ;
                     brush spread 0.15 power 0 shape 0 stretch 1 offset 0 rotation 0.25 ;
                     time latency 80 attack 2 release 4 ; band 0.1 ));

  L'import passe par les réglages de Diffusion-3 (Set_Table). Les erreurs prendront une nouvelle plage de codes à 4
  chiffres.
- **Le projecteur** : pendant qu'une MetaSurface le pilote, il est dans un nouveau mode « Meta » : le hasard et le Hyper
  Slider ne le touchent plus. MetaSurface inactive, il est silencieux. Le mode apparaît dans sa cellule et dans le module
  Projectors.

## Le pad du module

Une ligne d'état, puis les réglages ; les valeurs sont des potentiomètres (glisser ; Shift + clic : la valeur par défaut ;
clic droit : menu).
- **État** : la MetaSurface (menu de la bibliothèque), son nom, le projecteur, le mode (Edit, Play, Trajectory,
  Simulate, Record), l'état (Off, Fade-in, On, Fade-out), Save, Export.
- **Pinceau** : Spread, Power, Shape, Stretch, Offset, Rotation, Angle.
- **Temps** : Volume, Latency (et Fixed / Distance), Attack, Release, Band.
- **Trajectoire** : la trajectoire (T n ou enregistrée), Duration, Once / Loop / Back and forth / Loop reverse, Speed
  (chemin / points).
- **Placement** (5e ligne) : Path x, Path y, Path turn, Path scale, Placement (menu).

Les réglages du jeu (Spread, Power, Volume, Rotation…) pourront être liés aux faders de l'AKAI APCmini, comme ceux du
module Global.

## Les fils d'exécution et la mémoire

- **@gfx** :
  - la souris, le pinceau, les parts ;
  - l'enveloppe (fade-in, fade-out) et la trajectoire ;
  - la publication pour @block des parts, de l'amplitude et de la durée d'interpolation, en double tampon avec numéro de
    séquence, comme `sp_` dans Diffusion-3-Spatial.
- **@block** : le mélange (voir le principe) dans `prx_pcons` du projecteur, puis `cfchng` : le moteur actuel (buildiff, morph) fait
  la transition.
- **Les matrices** : à l'activation, chaque configuration est chargée une fois par confload (outdiff × configuration ×
  indiff), et seuls ses coefficients non nuls sont gardés : une liste commune des couples k et, pour chacun, les N gains.
  Le mélange ne parcourt que cette liste : typiquement 2 entrées × 80 sorties = 160 couples × N, au lieu des 16384 de
  la matrice. La liste est reconstruite quand une configuration ou les diffusions du projecteur changent.
- **La bibliothèque** : 32 × (64 + 32 × 4) mots, environ 6 K mots en mémoire statique.

## Les étapes

1. (En cours, 23 novembre 2026.) La bibliothèque et les modules MetaSurface A … D en mode Edit : la surface, la bande,
   les marqueurs, les zones (couleurs, dégradés aux frontières), ajouter, déplacer, pondérer, supprimer ; sauvegarde
   avec le projet. Pas de son.
2. (Écrite le 23 novembre 2026.) Le pinceau : tous ses réglages, le halo jaune, les parts affichées. Pas de son.
3. (Écrite le 23 novembre 2026.) Le son : le projecteur piloté (à partir du premier départ : mode manuel, actif,
   silencieux quand la MetaSurface ne sonne pas ; rendu quand on quitte Play), le mode « Meta » du projecteur (son
   affichage reste à faire), la liste des coefficients, le mélange en @block, les clics (fondus, départ et
   arrêt immédiats), le halo vert, le volume, la durée d'interpolation, la couverture.
4. (Écrite le 23 novembre 2026.) La vue 3D : en jeu, la vue Space du projecteur montre déjà sa matrice vivante
   (croix) et les niveaux réels (halos) ; brosse affichée sans son, elle montre les énergies simulées (croix et halos),
   avec la mention « MetaSurface A : simulated ».
5. (Écrite le 23 novembre 2026.) Les trajectoires : l'éditeur est Edit A … D (dans sa vue de dessus, les zones de la
   MetaSurface qui suit son chemin sont sous ses points ; la surface posée sur le carré [−1, 1], son grand côté en
   travers), ou une trajectoire T1 … T128 de la bibliothèque ; durée, Once / Loop / aller-retour, vitesse constante le
   long du chemin ou temps égal entre les points ; Simulate (le pinceau sur le chemin sans son, la vue Space en
   simulation) ; Record (le pinceau sur la souris, enregistré toutes les 50 ms dans la bibliothèque). Et la surface :
   9 formats (portraits compris), rotations de 90° et retournements (configurations, pinceau, angle avec elle),
   rectangle ou disque (une ellipse si le format n'est pas carré). Le placement d'une trajectoire se fait dans
   l'éditeur, au-dessus de la surface.
   Compléments (23 novembre 2026, demandes de l'utilisateur) : Play / Edit en bypass, Pause, Rule, Loop reverse, le
   placement de la trajectoire sur la surface (5e ligne du pad), un chemin bien visible ; dans Edit A … D, la taille des
   points (menu de la vue, « Size of the points », comme « Size of … » des vues Space).
6. Export et import, faders de l'APCmini, chapitre du manuel de Diffusion-3, tests mSL (Ex-30xx).

## Extension : les trajectoires A … D et les courbes (24 novembre 2026)

Décidé avec l'utilisateur :

- **Le système de Space dans la MetaSurface** : quatre trajectoires A, B, C, D (les formes de Space 3D avec leur rayon,
  les chemins des éditeurs Edit A … D, la bibliothèque T1 … T128), un placement par trajectoire (x, y, rotation, taille),
  Mix le long de la chaîne (A B, A B C, A B C D), Glide, Dyn (les courbes d'accélération de Space et les courbes de
  l'utilisateur) ; le placement actuel devient celui du chemin entier. Le mélange réutilise celui des projecteurs
  spatiaux (sp_Native, sp_MkBlend), dans le plan x, y. Les MetaSurfaces sauvées sont reprises (leur chemin dans A).
- **Le module Curves dans Diffusion-3** : une bibliothèque partagée, mSL_Curves (préfixe crv_), tirée du module Curves
  d'Interstys : 64 courbes en mémoire statique (lisibles par @block sans allocation), leurs types (Env, Wave, HEnv, QWave,
  HWave), périodique, sustain, la forme des segments, les noms, Undo ; les éditeurs « Curves A … D » ; des tables de
  1 025 échantillons de la forme complète, construites par @gfx quand une courbe change (crv_F) ; la sauvegarde avec le
  projet (enregistrement 'crv1'). Interstys garde son code ; il passera à la bibliothèque plus tard.
- **Moduler par des courbes** : Dyn par une courbe (la place sur le chemin en fonction du temps, la durée respectée) ;
  trois modulateurs Rotation, Speed, Mix (une courbe, un cycle « Path » ou une période en secondes, une profondeur :
  les vitesses multipliées par la courbe, Mix + profondeur × courbe). Dyn accepte aussi les courbes dans les vues Space.

Les étapes : 1. le module Curves (écrit le 24 novembre 2026, testé) ; 2. les trajectoires A … D de la MetaSurface (écrite le
24 novembre 2026 : le pad passe à 6 lignes — ligne 4 Brush, A, B, C, D, Mix, Glide, Dyn ; ligne 5 Duration, le mode, Speed,
Radius, Simulate, Record, Restart, le compteur ; ligne 6 x, y, turn, scale, Placement, Place ; Alt + clic sur A … D : son
placement, la trajectoire dessinée seule en or avec son pivot ; Cmd + clic : un glide vers elle ; un enregistrement va dans A) ; 3. les
modulations par les courbes (et Dyn de Space) ; 4. l'export et l'import, Interstys sur mSL_Curves, le manuel, les tests.

Compléments (24 novembre 2026, demandes de l'utilisateur) : la touche e lance et arrête Record ; le tracé de
l'enregistrement en cours ; les flips (gauche - droite, haut - bas) du chemin entier et de chaque trajectoire A … D ;
Remove (une trajectoire de la bibliothèque) ; les transformations d'une trajectoire de la bibliothèque (menus de A … D et
module Trajectories, avec Undo) : lissage (Taubin, sans rétrécissement ; léger, moyen, fort), rééchantillonnage à
distances égales, ou selon la densité d'une courbe de Curves (2^(profondeur × F(s)), s la part de la longueur : une
courbe haute rapproche les points, le pinceau ralentit quand le chemin est parcouru à temps égal entre ses points ;
plate : distances égales). Un rééchantillonnage depuis la MetaSurface passe Speed sur « points ». Les repères de la
courbe éditée sur le chemin (le module Curves utilisé en dernier, visible ; tant qu'un de ses points est sélectionné ou que
la souris est sur son graphe) : des tirets en travers du chemin là où le rééchantillonnage placerait les points (rapprochés :
le pinceau y ralentira), les points de la courbe (petits points verts), les points sélectionnés (plus gros, or, avec leur
numéro), le x sous la souris (un anneau) ; les types HEnv, QWave, HWave : chaque place de la forme complète. En retour,
le graphe de ce module Curves montre le pinceau de chaque MetaSurface en mouvement sur son chemin : une ligne verticale
magenta au x de sa place (la part de la longueur du chemin), un point sur la courbe, la lettre de la vue.

L'étape 3 (écrite le 24 novembre 2026) :

- **Dyn par une courbe** (MetaSurface et vues Space) : après les dix courbes d'accélération, les courbes du module Curves
  (le code 100 + k ; menus « Curves 1 - 32 », « Curves 33 - 64 » ; le clic gauche passe aux courbes qui existent). La
  courbe donne la place sur le chemin en fonction du temps de la durée : une enveloppe telle quelle, une forme d'onde
  ramenée de [-1, 1] à [0, 1] ; les modes in, out, in-out, out-in s'y appliquent comme aux autres (in : la courbe telle
  qu'elle est dessinée). Une courbe qui ne monte pas sans cesse fait revenir le pinceau en arrière.
- **Trois modulateurs** (une 7e ligne du pad : pour chacun, sa courbe et son cycle, puis sa profondeur) : la rotation du
  pinceau et la vitesse du mouvement multipliées par 1 + profondeur × F(phase) (une profondeur de -4 à 4 : au-dessous de 0,
  le pinceau tourne ou va en sens inverse ; Once : pas avant le départ), le Mix augmenté de profondeur × F(phase) (borné
  à [0, 1]). Le cycle : « Path », la phase est la place du pinceau sur le chemin (la part de sa longueur, comme les
  repères et la ligne du pinceau dans Curves), ou une période de 0,5 à 300 s (une phase propre, arrêtée par la Pause,
  remise à 0 par Restart et au départ du mouvement). Dans le graphe de leur courbe, en Play, la phase des modulateurs à
  cycle en secondes (une ligne orange pour la rotation, bleue pour la vitesse, verte pour le mix). Les réglages 54 … 62
  de la MetaSurface (courbe + 1, 0 : aucune ; cycle ; profondeur) ; une MetaSurface sauvée avant : modulateurs éteints,
  la profondeur mise à 1 quand une courbe est choisie.

L'étape 4, premier volet (écrit le 24 novembre 2026) : les réglages et les exports.

- **Les blocs Curve** des réglages mSL (`settings(data( ... ))`), les clés d'Interstys : `Curve id name "texte" type
  Env|Wave|HEnv|QWave|HWave periodic On|Off sustain n|Off points x y c ...`. L'id : un numéro de 1 à 64, ou un nom (la
  courbe de ce nom ; sinon la première courbe libre, qui prend ce nom). Les clés absentes ne changent rien ; des points
  donnés retirent le sustain (sauf s'il est donné aussi). Le code est partagé (mSL_Curves, partie 1 : incluse avant
  l'analyse des réglages ; Interstys pourra s'en servir), ses erreurs 1650 … 1655.
- **Les blocs MetaSurface** : `MetaSurface n` (1 … 32), puis des clés dans n'importe quel ordre : `name`, `zone c x y
  [poids]` (les configurations placées : données, elles les remplacent toutes), les réglages du pad (aspect, surface
  Rect|Disk, band, proj, spread, power, shape, stretch, offset, rotation, angle, volume, latency, rule Fixed|Distance,
  attack, release, brush Mouse|Path, duration, mode Once|Loop|Back|Reverse, speed Path|Points, radius, chain AB|ABC|ABCD,
  mix), `A` … `D` suivis de la trajectoire (None, Circle, Square, Star, Spiral, Central, Edit A … D, T1 … T128), `place x
  y tour échelle` et `flip None|X|Y|XY` (pour la trajectoire nommée juste avant, ou pour le chemin entier après `path`),
  `glide t [On|Off]`, `dyn` (Linear, Quad, Cubic, Quartic, Quintic, Exp, Circle, Sine, Elastic, Bounce, ou `Curve id`)
  suivi de `In|Out|InOut|OutIn`, `modrot`, `modspeed`, `modmix` (`Off` ou `Curve id`, puis `cycle Path|secondes`,
  `depth d`). Erreurs 2441, 2443 … 2449.
- Comme les blocs Edit, les blocs Curve et MetaSurface ne changent rien si l'analyse trouve une erreur, même après eux. Un
  fichier déposé sur un module Curves ou sur une vue MetaSurface : son premier bloc va dans la courbe ou dans la
  MetaSurface qu'il montre.
- **Les exports** (fichiers `.mSL` du dossier Data du projet, écrits par CMGS-auxiliary.eel) : une courbe ou toutes
  (Actions du module Curves) ; une MetaSurface, ou toutes celles qui sont utilisées (Actions de la MetaSurface), précédées
  de ce qu'elles utilisent : leurs courbes, leurs trajectoires de la bibliothèque (`trajectory n`), les chemins de leurs
  éditeurs (`Edit X`). Les configurations ne sont pas dans le fichier : celles du projet de mêmes numéros (une
  configuration absente est signalée dans le journal). Erreurs 1656, 2450, 2451.
- Les tests Ex-3007 (les courbes) et Ex-3008 (les MetaSurfaces).

L'étape 4, deuxième volet (écrit le 24 novembre 2026) : Interstys passe sur mSL_Curves.

- Les courbes d'Interstys sont celles de mSL_Curves (mémoire statique, plus de blocs dynamiques) ; ses modules « Curves A »
  … « H » sont les éditeurs de la bibliothèque (crv_Editor : en plus, la touche z pour Undo, Duplicate, le menu du type au
  clic droit, la hauteur du graphe qui suit le panneau, les exports en réglages : `nom-its-curve-date.mSL`).
- Les tables de mSL_Curves prennent le format d'Interstys : 4 096 échantillons, deux gardes de chaque côté (un cycle pour
  l'interpolation cubique), le palier des enveloppes (les Grains) ; Diffusion-3 en profite (1 024 échantillons avant).
  Le dernier échantillon est maintenant F(1) (Interstys y mettait F(0)) : une courbe non périodique lue en cycle (LFO)
  saute à la fin de son cycle au lieu de rejoindre son début sur 1/4 096 de la période.
- Le bloc d'une courbe de mSL_Curves est celui d'Interstys précédé d'un mot (la courbe existe) : Interstys garde ses
  noms (its_Crv_B(k) = crv_B(k) + 1, its_CrvTab … en alias), ses enregistrements 'crvc' (les projets se relisent), son
  analyse des blocs Curve (ses passes, ses erreurs 2792 … 2799), Check, Free, Dump.
- Corrigé au passage : `its_CrvK` était à la fois le tableau des clés d'un bloc Curve et la constante 1 000 de la forme
  des segments ; l'analyse écrivait dans `mem[1000]` … `mem[1004]`.
