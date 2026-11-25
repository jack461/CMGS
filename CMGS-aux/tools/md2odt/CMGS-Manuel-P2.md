---
title: "CMGS — Partie II"
lang: fr-FR
---

# Fenêtre, onglets, panneaux et modules

Les plug-ins de CMGS partagent une même organisation de leur fenêtre. Ce chapitre la décrit pour tous ; les modules
propres à chaque plug-in sont décrits dans son manuel.

## La fenêtre d'un plug-in

En haut de la fenêtre, une première barre appartient à REAPER : nom du préréglage courant, flèches pour passer d'un
préréglage à l'autre, bouton **+** (enregistrer ou charger un préréglage), boutons **Param**, **Edit…** et **MIDI**,
dosage *dry/wet*, et case d'activation du plug-in. Le reste de la fenêtre appartient au plug-in : la **barre
d'onglets**, puis un à quatre **panneaux**, côte à côte, qui contiennent les **modules**.

La fenêtre se redimensionne librement. Si elle devient trop étroite pour le nombre de panneaux choisi, le plug-in en
affiche provisoirement moins (de 4 à 3, puis à 2).

Les plug-ins de CMGS continuent de travailler lorsque leur fenêtre est fermée : un script mSL lancé poursuit son
exécution, un Game Master en *auto-play* continue de jouer.

## Les onglets

La barre d'onglets, en haut de la fenêtre, permet de passer d'un écran à l'autre : on clique sur un onglet, ou l'on
utilise les touches **Tab** (onglet suivant) et **Shift + Tab** (onglet précédent). Chaque onglet a sa propre
disposition de panneaux et de modules. Le nombre d'onglets dépend du plug-in (de 5 à 16) ; ils s'appellent par défaut
« Tab1 », « Tab2 », etc.

On renomme l'onglet courant par le menu des modules (*Tabs Management ▷ Rename tab…*, voir plus bas). Dans FilePlayer,
ScriptMaster et Espaces, un clic droit dans la barre d'onglets propose aussi *Rename tab…* ; dans le Game Master et
Interstys, il ouvre le choix du thème. Dans le Game Master, la droite de la barre d'onglets affiche en outre un ruban
coloré, qui reflète l'activité des lecteurs.

## Les panneaux

Un onglet est partagé en **un à quatre panneaux** verticaux. Avec la souris dans un panneau, **Shift + ◀** et
**Shift + ▶** déplacent sa limite gauche ou droite, au détriment du panneau voisin. Le sous-menu *Panes Arrangement* du
menu des modules permet :

- de choisir le nombre de panneaux (*1 pane* à *4 panes*) et de leur redonner des largeurs égales (*Reset Sizes*) ;
- de déplacer le panneau courant vers la gauche ou la droite (*Move pane left / right*), ou de décaler tous les
  panneaux (*Shift panes left / right*) ;
- de copier le contenu d'un panneau et de le coller dans un autre, éventuellement dans un autre onglet (*Copy pane*,
  *Paste pane*) ;
- de vider le panneau courant (*Clear Pane*), l'onglet courant (*Clear Tab*), ou tous les onglets (*Clear All Tabs*).

## Les modules

Un **module** est un cadre qui remplit une fonction : afficher le journal, régler des paramètres, piloter un lecteur,
éditer une courbe… Un panneau contient un ou plusieurs modules, empilés de haut en bas. Un même module peut être
affiché dans plusieurs panneaux, ou dans plusieurs onglets ; ses réglages (par exemple la liste des paramètres
affichés) lui restent attachés, même lorsqu'il n'est plus affiché nulle part.

On choisit les modules par le **menu des modules**, qui s'ouvre :

- par **Shift + clic droit**, n'importe où dans un panneau ;
- par un **simple clic droit** dans une zone du panneau où il n'y a pas de module.

Ce menu comporte :

| Rubrique | Contenu |
|---|---|
| (nom du module) | en tête, le module sous la souris : le choisir le retire du panneau |
| *Modules* | la liste alphabétique des modules du plug-in ; ceux qui sont déjà dans le panneau sont cochés ; un module choisi s'ajoute en bas du panneau |
| *Modules Disposition* | déplacer le module courant vers le haut, le bas, tout en haut, tout en bas, dans le panneau de gauche ou de droite ; le copier, puis le coller dans un autre panneau |
| *Panes Arrangement* | les panneaux : nombre, largeurs, déplacement, copie, effacement (voir plus haut) |
| *Tabs Management* | décaler tous les onglets (*Shift tabs left / right*), passer l'onglet en affichage « Live », renommer l'onglet |
| *Theme* | le thème des couleurs, la taille d'affichage (*Display size*) et le style « doux » (*Soft style*) |

## Apparence

**Thèmes.** Douze thèmes de couleurs sont proposés : *Default*, *Black*, *Tron*, *Light Cyan*, *Orange*, *Blue*,
*Dark Cyan*, *Dark Green*, *Dark Red*, *Light Amber*, *Neon Green* et *Light Magenta*. Les images des thèmes sont lues
dans `Data/CMGS-data/themes`.

**Taille d'affichage.** Chaque plug-in peut être affiché de **50 % à 200 %** (50, 60, 70, 80, 90, 100, 120, 150 et
200 %), par le sous-menu *Theme ▷ Display size* ou au clavier : **Cmd + `+`** (ou **Cmd + `=`**) agrandit,
**Cmd + `-`** réduit, **Cmd + `0`** revient à 100 %. La taille est propre à chaque plug-in et enregistrée avec lui.

**Style doux.** L'option *Theme ▷ Soft style* adoucit le dessin des cellules et escamote la barre d'onglets : celle-ci
apparaît quand la souris s'approche du haut de la fenêtre, et disparaît une dizaine de secondes après que la souris
l'a quittée.

## L'affichage « Live »

L'option *Tabs Management ▷ Live display* remplace les panneaux de l'onglet courant par l'écran « Live » du plug-in,
destiné au concert : dans Espaces, par exemple, un grand écran de boîtes d'affichage pilotées par l'APCmini (voir
son manuel). Dans un onglet « Live », le menu des modules ne s'ouvre que par **Shift + clic droit** ; on y décoche
*Live display* pour revenir aux panneaux.

# Pads, sliders, afficheurs et menus

## Les pads

Un **pad** est une grille de **cellules** colorées, en lignes et en colonnes. Une cellule peut afficher une
information, porter une valeur réglable, déclencher une action, ou ouvrir un menu ; sa couleur indique souvent un
état (actif, en erreur, sélectionné…).

Les plug-ins récents (Espaces, Interstys) suivent les conventions suivantes, que tous les plug-ins rejoignent
progressivement :

| Geste | Effet |
|---|---|
| clic droit | ouvre le menu de la cellule |
| clic gauche | l'action simple et courante de la cellule (basculer, passer à l'élément suivant, démarrer ou arrêter), ou une remise à zéro |
| clic gauche sur une cellule « Action » | ouvre aussi le menu (une telle cellule n'a pas d'action immédiate) |
| glisser avec le bouton gauche sur une cellule de valeur | règle la valeur, comme un potentiomètre (voir ci-dessous) |
| Shift + clic gauche sur une cellule de valeur | rétablit la valeur par défaut |

**Cellules de valeur.** Une cellule qui porte un nombre (un volume, un angle, une durée…) se règle en glissant : un
déplacement **horizontal** parcourt toute l'étendue des valeurs, un déplacement **vertical** fait un réglage fin (dix
fois plus fin ; vers le haut, la valeur augmente). Dans la colonne de la cellule, seul le réglage fin agit ; dans sa
ligne, hors de cette colonne, seul le réglage grossier ; ailleurs, les deux. Un clic gauche simple, sans glisser, ne
change rien.

Certains pads du Game Master, plus anciens, ont leurs propres conventions (par exemple clic gauche pour diminuer, clic
droit pour augmenter) : elles sont décrites dans son manuel.

## Les éditeurs de nombres

Quand la souris est sur une cellule qui porte un numéro (un numéro de configuration, de diffusion, de clip, de
mode…), le clavier permet de le modifier. Les touches et les pas varient un peu d'un plug-in à l'autre (le pas dépend
de la grandeur éditée) ; voici les plus courantes :

| Touches | Effet |
|---|---|
| `0` à `9` | ajoutent un chiffre à droite du nombre |
| `%`, `z`, `Origine` | remettent le nombre à 0 |
| `;` ou `.` | ajoute 1 |
| `,` ou `?` | retranche 1 |
| `+` ou `=` | augmente d'un grand pas |
| `:` ou `/` | diminue d'un grand pas |
| `n`, `▶` | élément suivant |
| `p`, `b`, `◀` | élément précédent |
| `▼` et `▲` | avancent ou reculent d'un pas plus grand |
| `Page ▼` et `Page ▲` | avancent ou reculent d'un pas encore plus grand |

Lorsque le nombre désigne un objet (un clip, un mode, une configuration), le plug-in passe souvent directement à
l'objet suivant ou précédent **qui existe**, en sautant les numéros inutilisés. La liste exacte des touches de chaque
éditeur figure dans `CMGS-Keys.md` (section « Éditeurs de nombres »).

## Les sliders

Un **slider** règle un paramètre entre deux bornes. Il affiche, de gauche à droite, le nom du paramètre et sa valeur,
puis une barre et sa poignée.

| Geste | Effet |
|---|---|
| appui sur la poignée | garde la valeur ; on peut ensuite glisser |
| appui ailleurs sur la barre | amène la valeur à cet endroit |
| glisser dans la barre | réglage grossier : la poignée suit la souris |
| glisser au-dessus ou au-dessous de la barre | réglage fin (dix fois plus fin ; vers le haut, la valeur augmente) |
| double clic, ou Ctrl + Shift + clic | rétablit la valeur par défaut |

Le réglage est relatif : on peut sortir de la barre en cours de geste sans que la valeur saute.

## Les afficheurs

Les **afficheurs** présentent des valeurs et leurs étiquettes : version, compteurs, état d'un lecteur, statistiques de
mémoire… Dans certains modules (par exemple les modules *Parameters* du Game Master), l'utilisateur choisit lui-même
les sliders ou les afficheurs présentés : un clic droit sur l'un d'eux, ou sur la ligne « (unset entry) », ouvre un
menu qui permet d'en ajouter, d'en remplacer, d'en déplacer ou d'en retirer.

## Les menus

Les menus de CMGS sont des menus contextuels : ils s'ouvrent **au relâchement** du bouton droit, et l'on choisit une
entrée avec l'un ou l'autre bouton. Une coche marque les choix en cours (le thème, le nombre de panneaux, les modules
présents…). Un clic hors du menu, ou la touche Échap, le referme sans rien choisir.

# Le clavier

## Principes

Un plug-in reçoit les touches du clavier lorsque sa fenêtre est active (on a cliqué dedans) et que la souris s'y
trouve. Chaque touche n'est utilisée qu'une fois : elle est proposée successivement, dans l'ordre suivant, aux
éléments du plug-in, et le premier qui la reconnaît la prend.

1. La **taille d'affichage** : Cmd + `+`, `=`, `-` ou `0`.
2. Le **module sous la souris**, puis ses pads (et leurs éditeurs de nombres).
3. Le **panneau** : Shift + ◀ et Shift + ▶.
4. L'**onglet** : Tab et Shift + Tab ; dans le Game Master, les commandes de concert (voir son manuel).
5. Les **commandes du plug-in**.
6. Les **commandes système** (sauf dans le Game Master) ; dans le Game Master, les raccourcis définis par
   l'utilisateur (module *Links Manager*), puis le jeu au clavier du *Studio Play Pad*.

Il en découle qu'un module peut, lorsque la souris est sur lui, utiliser pour lui-même une touche qui a ailleurs un
autre sens. La liste complète des touches de chaque plug-in, module par module, avec ces recouvrements, est dans le
fichier `CMGS-docs/CMGS-Keys.md`, produit à partir du code.

Par convention, les **minuscules** commandent des actions, les **majuscules** des affichages.

## Les touches communes

| Touche | Effet | Plug-ins |
|---|---|---|
| Tab, Shift + Tab | onglet suivant, précédent | tous |
| Cmd + `+` ou `=`, Cmd + `-`, Cmd + `0` | taille d'affichage : agrandir, réduire, 100 % | tous |
| Shift + ◀, Shift + ▶ | déplacer la limite du panneau | tous |
| `L`, `M` | afficher le journal, la mémoire | FilePlayer, ScriptMaster |
| `S` | afficher ou masquer les sliders de REAPER | Espaces, Interstys |
| `U` | afficher ou masquer l'interface | Interstys |

Les **commandes système** servent surtout à la mise au point ; elles sont les mêmes dans FilePlayer, ScriptMaster,
Espaces et Interstys (le Game Master utilise ces touches pour ses commandes de concert) :

| Touche | Effet |
|---|---|
| `g` | lance le ramasse-miettes (*garbage collector*) de la mémoire dynamique |
| `k` | arrête tous les scripts mSL en cours (*kill*) |
| `m`, `n` | parcourt la mémoire dynamique et en affiche l'état (deux modes) |
| `c` | active ou désactive le recyclage de la mémoire dynamique |
| `l` | change la limite d'affichage de la mémoire |
| `r` | relance le premier processus suspendu |
| `t`, `o`, `s` | séries de tests mSL : marche ou arrêt, un seul passage, arrêt |

# Les modules communs

Plusieurs modules se retrouvent, sous le même nom et avec le même fonctionnement, dans plusieurs plug-ins :

| Module | Game Master | FilePlayer | ScriptMaster | Espaces | Interstys |
|---|---|---|---|---|---|
| *Main Infos* / *Main Status* | oui | oui | oui | oui | oui |
| *System Log* | oui | oui | oui | oui | oui |
| *Memory 1*, *Memory 2* | oui | oui | oui | oui | oui |
| *Scheduler* | oui | oui | oui | oui | oui |
| *Processes Manager* | oui | oui | oui | oui | oui |
| *User Log* | oui | | | | |

## Main Infos, Main Status

Ce module affiche les caractéristiques du plug-in : version, date de lancement, et divers compteurs (mémoire,
processus, activité). Il s'appelle *Main Infos* dans le Game Master et Interstys, *Main Status* dans les autres
plug-ins ; son contenu dépend du plug-in.

## System Log

Le **journal système** affiche les messages du plug-in et des scripts mSL (fonctions `GM_Log` et `print`) : étapes de
l'initialisation, erreurs, résultats. Il conserve les derniers messages (environ 800 lignes) ; les plus anciens
disparaissent.

Un clic droit dans le journal ouvre le menu *Log Layout* : affichage sur 1 à 8 colonnes, espacement des lignes
(*height +*, *height -*), ajout d'une ligne blanche (*blank*), effacement (*clear*). La souris dans le journal, le
clavier permet :

| Touche | Effet |
|---|---|
| Espace, Entrée | ajoute une ligne blanche |
| `1` à `8` | affiche le journal sur 1 à 8 colonnes |
| `j`, `k` | fait défiler d'une ligne |
| `▼`, `▲` | fait défiler de dix lignes |
| `▶` | avance de cent lignes |
| `z`, `◀` | revient aux dernières lignes |
| `m`, `l` | augmente, diminue l'espacement des lignes |
| `t` | inscrit la date et l'heure |
| `v` | inscrit la version et la configuration |
| `p` | enregistre le journal dans un fichier texte, `syslog-<plug-in>-<date>.txt`, dans le dossier du projet |
| `P` | copie le journal dans la console de REAPER, d'où l'on peut le copier ailleurs |

Les touches `p` et `P` passent par le script auxiliaire, qui doit être lancé. Le Game Master a en outre un second
journal, *User Log*, qui fonctionne de la même façon.

## Memory 1, Memory 2

Ces deux modules identiques affichent une zone de la mémoire du plug-in, ou de la mémoire partagée, sous différents
formats (nombres, caractères, blocs de mémoire dynamique). Ils servent à la mise au point du système et des scripts
mSL : les flèches déplacent la zone affichée (d'un mot, d'une ligne, d'une page), et d'autres touches changent le
format. Leur usage est détaillé dans la documentation interne (`CMGS-Internals`).

## Scheduler

L'**ordonnanceur** (*scheduler*) exécute les tâches différées et les processus du plug-in : scripts mSL, actions
programmées, opérations à délai. Lorsqu'il est arrêté, la plupart des fonctions du plug-in sont suspendues. Le module
est un pad de 16 cellules :

| Cellule | Rôle |
|---|---|
| 1 | état de l'ordonnanceur : « Scheduler on » (vert) ou « Sch. off » ; un clic le relance ; avec Ctrl (ou Cmd), la cellule devient « Turn off » et l'arrête |
| 2 | la prochaine tâche en attente |
| 3 | le délai, en secondes, avant son lancement |
| 4 | « Now » : lance cette tâche tout de suite ; avec Ctrl (ou Cmd), la cellule devient « Kill » et supprime la tâche |
| 5 | inutilisée |
| 6 à 16 | les tâches « Task A » à « Task K » : un clic gauche lance la tâche, un clic droit la retire de la file d'attente ; une tâche en attente est colorée |

Le rôle des tâches A à K dépend du plug-in (dans le Game Master, par exemple, les tâches A, B et C font évoluer le
groupe, le volume et le nombre de générateurs en mode *auto-play*).

## Processes Manager

Le **gestionnaire de processus** suit les scripts mSL et la mémoire dynamique :

- **Load** (clic droit) : menu des scripts connus, pour en charger et en exécuter un ;
- avec Ctrl (ou Cmd) enfoncée, deux cellules deviennent **Kill Scripts**, qui arrête tous les scripts en cours, et
  **Unlock Scripts**, qui débloque les scripts verrouillés ;
- **Run GC** : lance le ramasse-miettes, en silence (clic gauche) ou en détaillant son travail dans le journal (clic
  droit) ;
- **Show Mem.** : calcule et affiche l'état de la mémoire dynamique (taille, mémoire libre, blocs utilisés) ;
- des compteurs : processus actifs, en attente, verrouillés ; nombre d'instructions exécutées par seconde ; nombre et
  durée des passages du ramasse-miettes.

# Fichiers, préréglages et exports

## Le glisser-déposer

On peut faire glisser des fichiers depuis le Finder (ou l'Explorateur) dans la fenêtre d'un plug-in :

| Fichier | Plug-in | Effet |
|---|---|---|
| script `.mSL` | tous | le script est compilé et exécuté ; ses messages vont dans le journal ; on peut en déposer plusieurs à la fois |
| script `.mSL` sur la case *Profile* du module *Scripts Settings* | Game Master | le script devient le Profile du projet |
| fichier `.RPP` | Game Master | le Game Master apprend où se trouve le projet (à faire après tout déplacement du projet) |
| `Clips.txt` | Game Master | la liste des clips du dossier `WAVES` (voir le manuel du Game Master) |
| sons (`.wav`, `.aif`, `.flac`, `.mp3`…) | Game Master, Interstys | associés à des numéros de clips (module *Clips Selection*) ou chargés dans une ligne d'Interstys |
| configurations et trajectoires de *GRM Spaces* (`.ala`, `.lay`, `.xml`) | Espaces | pour la vue 3D et les modules *Edit* |

Chaque plug-in précise dans son manuel où déposer ses fichiers, quand l'endroit compte.

## Préréglages et sauvegarde

L'état complet d'un plug-in — onglets, panneaux, modules, réglages, thème, taille d'affichage, et les données propres
au plug-in — est enregistré par REAPER **avec le projet**, dans le fichier `.RPP`. On retrouve donc tout à la
réouverture du projet.

Le même état peut être enregistré comme **préréglage** (bouton **+** de la barre de REAPER, *Save preset…*), pour
être rechargé dans un autre projet. REAPER range les préréglages dans le dossier `presets` de ses ressources, dans un
fichier par plug-in (`js-CMGS-effects_<plug-in>_jsfx.ini`). Le choix *Reset to factory default* du même menu rend au
plug-in son état initial.

L'état de certains plug-ins, du Game Master en particulier, est volumineux : c'est pourquoi on conseille de régler à 0
la mémoire d'annulation de REAPER (voir l'installation).

## Les exports

Les plug-ins n'écrivent pas eux-mêmes de fichiers : ils passent par le script auxiliaire `CMGS-auxiliary.eel`, qui
doit donc être lancé. Ainsi :

- la touche `p` d'un journal l'enregistre dans un fichier texte du dossier du projet, la touche `P` le copie dans la
  console de REAPER ;
- Interstys exporte ses patchs et ses sessions sous forme de scripts mSL, que l'on peut relire ou modifier ;
- Espaces exporte les points de ses modules *Edit* sous forme de tables mSL.

Ces exports sont décrits dans les manuels des plug-ins concernés.
