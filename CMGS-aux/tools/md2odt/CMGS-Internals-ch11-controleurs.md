---
title: "CMGS — fragment surfaces de contrôle"
lang: fr-FR
---

# Les surfaces de contrôle (projet)

*Chantier ouvert le 25 novembre 2026. Premier temps : l'inventaire de l'existant et des premières pistes ; rien n'est
encore réalisé.*

## Le but

Les applications de CMGS n'utilisent guère le MIDI dans sa vocation première, transmettre les notes jouées par un
interprète. Elles s'en servent pour offrir à l'utilisateur des manières d'agir sur le logiciel plus agréables qu'un
recours systématique à la souris, en studio comme en concert. Le but, à terme :

- des plug-ins indépendants, chacun spécialisé dans la gestion élaborée d'un type de contrôleur : l'AKAI APCmini
  d'abord, puis l'AKAI MIDI Mix, le Novation Launchpad X, l'ERAE 2 d'Embodme, etc. Chacun connaît tout de son
  matériel : ses messages, ses diodes et leurs couleurs, les gestes qu'il permet ;
- ces plug-ins communiquent avec les applications par la mémoire partagée. Ils sont « multi-tâches » : sur un même
  contrôleur, certaines manipulations peuvent être destinées à une application, en même temps que d'autres le sont à
  une autre ;
- les applications ne reçoivent plus de MIDI : elles sont simplement informées que des réglages ont changé, avec la
  même transparence que si le changement venait de la souris, d'une automation de REAPER ou de l'exécution d'un
  programme mSL ;
- le MIDI ne reste que pour les cas où l'utilisateur veut « jouer » d'une surface de contrôle, par exemple en envoyant
  ses messages à un synthétiseur extérieur à CMGS.

Côté matériel, il faut prendre en compte les potentiomètres rotatifs, les faders, les encodeurs, les touches
(individuelles, ou en pads de N x P), les claviers traditionnels ; en retour, la gestion des couleurs et de l'état des
diverses diodes commandables.

## Inventaire : les chemins actuels

### Vue d'ensemble

| Application | Entrée | Transport | Ce qui est piloté | Retour vers la surface |
|-----------------|---------------------|---------------------|------------------------|-----------------|
| Game Master | MIDI_In ou MIDIduino (plug-ins distincts) ; sliders Ctl 1 à 64 | gmem : l'unité MIDI (entrées de 4 mots) ; `@slider` | Links Manager : un paramètre, une valeur fixe, une action ; les capteurs | aucun |
| Interstys | le MIDI de sa piste ; sliders Ctl 1 à 64 | `midirecv_buf` dans `@block` (le MIDI est consommé) | liens : un slider Ctl, une clé d'un module, une action (LEDs, Rate, Bank) | diodes (`midisend`) |
| Espaces | le MIDI de sa piste (APCmini) ; sliders Ctl 1 à 64 (ils ne pilotent rien) | `midirecv_buf` dans `@block`, module `AKAI-APCmini.jsfx-inc` inclus | ses fonctions internes, appelées directement | diodes, couleurs, clignotements ; écran Live |
| FilePlayer, ScriptMaster | aucune | | | |

Trois mises en œuvre indépendantes, donc, chacune née d'un besoin : le Game Master est centré sur les actions,
Interstys sur l'apprentissage (un contrôle, une cible), Espaces sur une surface conçue comme un instrument (pages,
dispositions, nombreux états affichés).

### REAPER lui-même : les sliders et l'automation

Le Game Master, Interstys et Espaces déclarent 64 sliders génériques, Ctl 1 à Ctl 64 (de −1 à 1), masqués et
automatisables. REAPER peut les piloter par ses propres moyens : enveloppes d'automation, modulation de paramètres,
et apprentissage MIDI (*Learn*) d'un paramètre de l'effet. C'est l'approche la plus simple, sans aucun code dans CMGS :
la correspondance est gardée dans le projet REAPER, l'application voit seulement un slider changer (`@slider`). Il n'y a
pas de retour vers la surface, et la cible est un slider anonyme, non un réglage de l'application.

- Game Master : un slider Ctl k peut être la source d'un lien du Links Manager (vers un paramètre ou une action).
- Interstys : les sliders Ctl sont des sources de modulation (les cellules de contrôle) et des cibles de liens.
- Espaces : ils ne pilotent rien pour l'instant.

### Le Game Master : MIDI_In, MIDIduino et le Links Manager

- MIDI_In (ou MIDIduino, pour les capteurs d'un Arduino), placé sur la piste qui reçoit le MIDI, écrit chaque message
  dans un anneau de son unité en gmem (`uMIDI_MGR_In`) : quatre mots, le statut, les deux octets de données, la date
  (`time_precise` corrigé de `timeDelta`).
- Le Game Master lit cet anneau dans `@block` (`ucbMIDIget`, `localMIDIget`), le note dans le journal si on le demande
  (`MIDILogActive`), apprend un lien si le Links Manager est en apprentissage (`SysLinksActive`), et cherche le message
  dans une table de hachage (`Links_HTab`, 1 999 entrées) : la clé est `statut << 8 | donnée 1` pour le MIDI,
  `0x1000 + k` pour le slider Ctl k. Une entrée trouvée est mise dans une petite file (`W_Actions`, 1 024 entrées) avec
  une valeur entre 0 et 1 (donnée 2 / 127, ou (Ctl + 1) / 2).
- Quatre sortes de liens : CC (un paramètre, entre deux bornes, avec la pente du paramètre :
  `uix_slider_ratio_to_value`), SV (une valeur fixe), Slider (comme CC, depuis un slider), Act (l'une des 87 actions,
  par `Simple_Action`).
- Les capteurs ont leur propre état en gmem (`sensorsPadState`).
- L'anneau MIDI n'a qu'un lecteur : une seconde application qui le lirait volerait des messages au Game Master.
- Aucun retour vers la surface. Un événement mSL « MIDI » avait été prévu (`mSL_signal_event`, en commentaire).

### Interstys : les liens MIDI

C'est aujourd'hui l'apprentissage MIDI le plus complet (testé avec une AKAI MIDI Mix).

- Interstys lit et consomme le MIDI de sa piste (`its_Lk_Recv`, dans `@block`).
- Une table de 256 liens de 20 mots, sauvée avec le projet, écrite par les réglages (`Link n cc m | note m [chan c]
  target ...`, `Inject` pour les tests, `Dump`, `Check`, `Free`) ou par apprentissage dans le module Links (le dernier
  slider ou paramètre touché devient la cible).
- Les cibles : un slider Ctl k (écrit aussitôt dans `@block`, signalé à REAPER par `slider_automate` dans `@gfx`) ; une
  clé d'un module (Reader, Writer, Effect : bornes min et max, loi Lin ou Exp), appliquée dans `@gfx` par les mêmes
  fonctions que les réglages (`its_Tb_SetFx`…) ; une action : renvoyer les diodes (LEDs), basculer le mode incrémental
  (Rate), changer de banque (Bank Prev, Next ou n).
- Les comportements : modes Abs, Toggle, Push ; reprise de valeur (*pickup* : le contrôle n'agit qu'après avoir rejoint
  la valeur courante, une flèche ↑ ↓ dans le module dit dans quel sens le bouger) ; glissement (*glide*, en secondes) ;
  paliers (*steps*) ; courbe (une courbe de la bibliothèque des courbes) ; mode incrémental (*rate* : un potentiomètre
  devient une vitesse, en zones, de 300 s à 0,1 s pour toute la course) ; banques 1 à 16 (0 : toujours active), un
  changement de banque imposant la reprise de valeur.
- Le retour : une diode par contrôle, dont le « propriétaire » est le premier lien Toggle, sinon le premier lien ; les
  messages partent par `midisend` depuis `@block` (anneau `its_LkOutQ`) ; l'état est renvoyé après un relâchement (la
  MIDI Mix éteint elle-même ses diodes).

### Espaces : l'APCmini

Le module `AKAI-APCmini.jsfx-inc` (1 423 lignes) est inclus dans le plug-in. Il lit le MIDI de la piste
(`midirecv_buf` dans `@block`, puis `MIDI_in`), et met à jour les diodes dans `@gfx` (`MIDI_handle`). Le manuel
d'Espaces (chapitre « La surface de contrôle AKAI APCmini ») décrit son usage. Ce qu'il pilote :

- les projecteurs : le projecteur courant, son état (Off, Active, Mute, Solo), son volume, l'ajustement de volume ;
- les diffusions : les 16 du groupe courant, les 16 du pad, les 64 qui suivent le début du pad ; les groupes ; les
  scènes ; les présets de projecteurs ; les paquets d'actions ;
- le morphing (Run, Hold, Freeze ; son temps), le mode aléatoire et son délai, l'hyper slider et son ambitus, le flou
  (*Blur*) ;
- l'écran Live : l'horloge et le chronomètre, l'affichage graphique.

Les manières d'agir qu'il met en œuvre :

- des pages (les huit boutons ronds de droite ; un second appui choisit une variante, le bouton clignote alors) ;
- la touche Shift, seule (passer des projecteurs 1 à 8 aux projecteurs 9 à 16, et rallumer toutes les diodes après une
  reconnexion) ou tenue (elle modifie l'action d'une autre touche) ;
- l'appui bref et l'appui long (de 1 à 6 s ; au moins 3 s pour mettre un projecteur à Off) ;
- des ensembles à choix unique (une diffusion, un groupe, un projecteur éclairés parmi d'autres) ;
- l'accusé de réception (la touche rouge un instant, puis verte) ;
- des faders avec reprise de valeur (à moins de 3 dB pour le volume ; pendant le mouvement, les deux rangées du bas
  montrent la position du fader : rouge s'il est désynchronisé, vert dès qu'il a rejoint la valeur) ;
- une valeur faite de deux faders (l'ajustement de volume est leur somme) ; des lois non linéaires (0 dB en haut,
  −18 dB à mi-course) ;
- deux modèles, l'APCmini (vert, jaune, rouge) et l'APCmini MK2 (couleurs RVB), avec des couleurs adaptées ; la
  reprise après un débranchement.

Le couplage est direct : le module appelle les fonctions d'Espaces (`apc_SelPrj`, `apc_PVol`…) et lit son état interne
pour les diodes. Espaces ne publie aucun paramètre : sa plage de paramètres (512 à 639) est vide (`paramCount = 0`).
Les plug-ins AKAI-Ex-01 et AKAI-Ex-02 sont des exemples indépendants de programmation de l'APCmini.

### Les autres sources d'interaction

Les mêmes réglages sont atteints par la souris (pads, potentiomètres `ui_jdrag`, sliders), par le clavier (le schéma
commun : le module sous la souris, puis le panneau, l'onglet, le plug-in, le système ; les commandes de concert du Game
Master), par mSL (`get` et `set(`pval, n)`, les réglages `settings`, `event(...)` entre plug-ins) et par l'automation.
Deux mécanismes communs existent déjà en gmem :

- l'espace des paramètres : 1 024 numéros, une plage par application (Game Master 0 à 255, Interstys 256 à 511,
  Espaces 512 à 639, ScriptMaster 640 à 703, MIDI_In et MIDIduino 704 à 767) ; chacune publie sa plage et lit celle des
  autres ; écrire le paramètre d'une autre application est refusé (erreur 0621), un changement par événement adressé
  au propriétaire étant prévu ;
- la conception des instances multiples (§ 7.2) : un pool d'emplacements par instance, une file de messages.

## Les finalités, regroupées

| Finalité | Exemples | Contrôles habituels | Retour |
|----------------|----------------------------------|--------------------|------------------------------|
| régler une grandeur continue | volume d'un projecteur, temps de morphing, flou, gain d'un écrivain, Ctl k | fader, potentiomètre, encodeur | position (fader motorisé, couronne de diodes, rangée de pads en barre-graphe) ; désynchronisation |
| basculer un état | Mute et RecArm (Interstys), Run / Hold / Freeze, manuel / aléatoire, Off / Active / Mute / Solo | touche (bascule), appui long | diode allumée ou éteinte, une couleur par état |
| choisir dans un ensemble | projecteur courant, groupe, scène, diffusion, préset, banque | rangée ou grille de pads, fader (la scène) | l'élément choisi éclairé |
| déclencher | paquet d'actions, choix au hasard, chargement d'une diffusion ; plus tard, lancer des clips | pad, touche | bref accusé de réception |
| changer de contexte | pages, banques, Shift (1 à 8 / 9 à 16), projecteur courant | touches | diode de la page, clignotement de la variante |
| informer | boîtes de l'écran Live, horloge, position d'un fader, couleur d'un préset ou d'un groupe de projecteurs | diodes, afficheurs | |
| jouer | des notes vers un synthétiseur | clavier, pads | le MIDI passe tel quel |

« Changer de contexte » est à part : il ne règle rien, il change la cible des autres contrôles (le projecteur courant
est l'équivalent du « navigateur » de CSI, plus bas).

Les gestes, du côté de la surface : appui, relâchement, appui bref ou long (seuils de durée), double appui (pas encore
utilisé), modificateur tenu ou appuyé seul, toucher (ERAE, faders motorisés), rotation relative (encodeurs, avec
accélération), pression (*aftertouch* : Launchpad X, ERAE 2), position XY (les surfaces de l'ERAE 2).

Les comportements d'une grandeur continue, entre le contrôle et la cible : loi (linéaire, exponentielle, courbe),
bornes, paliers, glissement, reprise de valeur, mode incrémental, mode relatif (encodeur), combinaison de plusieurs
contrôles (une somme).

## Ce que montre l'inventaire

- Les mêmes notions sont écrites trois fois, différemment : la reprise de valeur (3 dB dans l'APCmini, 2,5 / 127 ou un
  croisement dans Interstys), la loi (la pente des paramètres du Game Master, la loi et la courbe d'Interstys, les lois
  fixes de l'APCmini), les pages et les banques, les bascules, le journal des messages.
- Le MIDI d'une piste est consommé par le plug-in de cette piste : une surface ne sert qu'une application (le Game
  Master passe par MIDI_In, mais son anneau n'a qu'un lecteur).
- Espaces n'offre aucun point d'entrée adressable (ni paramètres, ni table d'actions) : l'APCmini appelle ses
  fonctions. Exposer ces points est le préalable à l'extraction de l'APCmini.
- Le retour vers la surface demande l'état de l'application, pas seulement des valeurs : l'état d'un projecteur,
  l'élément choisi d'un ensemble, la présence d'un préset, une couleur. Interstys lit la valeur de la cible ; l'APCmini
  lit l'état interne d'Espaces ; le Game Master n'a pas de retour.
- L'identité de la cible est aujourd'hui implicite (le plug-in de la piste). Avec plusieurs instances (§ 7.2), une cible
  est : un type d'application, une instance, un point.
- Les adresses stables ne sont pas les mêmes partout : les paramètres du Game Master ont des métadonnées (bornes,
  pente) ; les paramètres d'Interstys (`p_*`) sont des vues du module affiché, pas des adresses stables, celles-ci sont
  les clés de ses réglages (le gain du Writer 2…) ; Espaces n'a rien.

## Références : CSI

Le fil « Control Surface Integrator » du forum *MIDI hardware* de REAPER (t=183143, 2016-2017) contient surtout les
besoins et les débats qui ont précédé le projet. Les leçons qui nous concernent :

- l'interface et le coût de la configuration sont le plus difficile, pas la technique ;
- « les potentiomètres et les touches sont inutiles si l'on ne sait pas à quoi ils sont affectés » : il faut montrer
  l'affectation (chez nous, l'écran Live ou un module dédié) ;
- réglages globaux et réglages par projet sont tous deux nécessaires ; plusieurs surfaces forment un ensemble.

La documentation de CSI (wiki communautaire, `github.com/GeoffAWaddington/CSIWiki/wiki`) décrit l'architecture qui en est
sortie :

- la **surface** (fichier `.mst`) décrit seulement ce que le matériel sait faire, jamais le comportement : des
  **widgets** nommés, chacun avec un générateur de messages (`Press`, `Fader7Bit`, `Fader14Bit`, `Encoder`, `Touch`,
  `Toggle`) et un processeur de retour (`FB_TwoState`, `FB_Fader14Bit`, `FB_Encoder`, des retours RVB propres à
  certains modèles). Par exemple : `Widget UpperButton1` / `Press 90 20 7f` / `FB_TwoState 90 20 7f 90 20 00` /
  `WidgetEnd` ;
- les **zones** (fichiers `.zon`) associent des widgets à des actions (`PlayButton Play`), avec des couleurs pour les
  états (`{ 0 25 255 0 189 255 }`), des paliers (`[ 0.0 0.34 0.67 1.0 ]`) ; des zones associées se comportent comme
  des boutons radio, une sous-zone s'appelle depuis sa zone ;
- les **pages** regroupent surfaces et zones, une seule active à la fois ;
- les **modificateurs** (Shift, Option, Control, Alt, et tout widget déclaré comme tel ; Hold, un appui d'une seconde ;
  Toggle, Touch, Increase et Decrease pour un encodeur…) sont globaux à une page, ou locaux à une surface ;
- le **retour** est toujours décidé par le logiciel, jamais par la surface ; par défaut seule la première action d'un
  widget donne le retour ;
- des surfaces peuvent diffuser leurs commandes à d'autres (*Broadcast*, *Listen*), pour se suivre.

À retenir pour CMGS : séparer ce que sait faire un contrôleur (dans le plug-in de ce contrôleur) de ce qu'on lui fait
faire (une correspondance chargée, sauvée, exportable) ; le retour piloté par l'application ; les pages et les
modificateurs dans le plug-in du contrôleur.

## Pistes (à discuter)

### Trois couches

```
surface <-> plug-in du contrôleur <-> bus (gmem) <-> application
```

- **Le plug-in du contrôleur** : la connaissance du matériel (messages, codes des diodes, couleurs, détection du
  modèle, reconnexion) ; les gestes (appui bref ou long, Shift, double appui, accélération des encodeurs) ; la
  disposition (pages, zones) ; les comportements d'une grandeur continue (loi, reprise de valeur, glissement, paliers,
  mode incrémental) ; le rendu du retour (des états publiés aux diodes). Il lit le MIDI de sa propre piste et renvoie
  les diodes par la sortie MIDI de cette piste.
- **Le bus de contrôle**, en gmem :
  - un annuaire des **points de contrôle** publiés par chaque instance d'application : un numéro, un nom, une sorte
    (grandeur continue, bascule, état parmi n, choix parmi n, déclencheur), les bornes, la loi et l'unité (pour
    l'affichage), la valeur ou l'état courant avec un numéro de séquence, la disponibilité et la couleur des éléments
    d'un choix ;
  - une file de **requêtes** par instance : fixer une valeur, ajouter un écart (encodeur), déclencher, choisir
    l'élément n ; avec l'origine (le contrôleur). L'application l'applique comme un changement venu de la souris (les
    mêmes fonctions que le pad ou mSL), et la publication qui en résulte sert de retour à tous ;
  - le **dernier point touché** de chaque instance, pour un apprentissage fait dans le plug-in du contrôleur.
- **L'application** : publie ses points, applique les requêtes (dans `@block` pour ce qui touche le son, dans `@gfx`
  sinon, avec les règles du jeton), ne reçoit plus de MIDI.

### Où vit la correspondance

Comme dans CSI, la description du matériel est dans le code du plug-in du contrôleur (un plug-in par modèle), et la
correspondance (quel contrôle agit sur quel point, de quelle instance) est une donnée : des réglages mSL
(`settings(data( ... ))`) chargés par le plug-in du contrôleur, sauvés avec le projet, exportables, complétés par un
apprentissage. Les pages de l'APCmini deviennent des zones, chacune avec son application cible : une page pour
Espaces, une autre pour Interstys.

### Questions

1. La correspondance : seulement dans les plug-ins des contrôleurs, ou aussi un apprentissage générique (les liens
   d'Interstys passant dans le plug-in du contrôleur) ? Que deviennent le Links Manager du Game Master et les liens
   d'Interstys : gardés pour la compatibilité, ou migrés ?
2. L'annuaire : des points fixes, déclarés par l'application au démarrage (les points d'Espaces), et des points
   dynamiques (les modules d'Interstys créés par l'utilisateur) ; leur numérotation, leurs noms.
3. La latence : les requêtes lues dans `@block` (à chaque bloc audio) ou dans `@gfx` (30 fois par seconde) ? Un fader
   qui règle un volume demande `@block` ; le retour peut rester dans `@gfx`.
4. Plusieurs contrôles sur un même point (deux Launchpad X, une surface et la souris) : le dernier l'emporte, la reprise
   de valeur évite les sauts.
5. Les données au-delà de 0 à 127 : 14 bits, pression, position XY (ERAE 2) : des valeurs entre 0 et 1 en double
   précision, ou des écarts.

### Premières étapes proposées

1. Espaces expose comme points ce que pilote l'APCmini (grandeurs continues, états, choix, déclencheurs), et le module
   APCmini passe par ces points au lieu d'appeler ses fonctions : toujours dans le plug-in, vérifiable sans nouveau
   transport.
2. La conception du bus en gmem (annuaire, requêtes, états), compatible avec le pool des instances (§ 7.2).
3. Le plug-in APCmini, sorti d'Espaces, communiquant par le bus ; Espaces garde son module interne en option jusqu'à
   validation.
4. Un deuxième contrôleur, la MIDI Mix (la référence des liens d'Interstys), pour vérifier la généralité :
   apprentissage, reprise de valeur, banques dans le plug-in du contrôleur.
5. Puis le Launchpad X (deux exemplaires ; le lancement des clips du Game Master) et l'ERAE 2.
