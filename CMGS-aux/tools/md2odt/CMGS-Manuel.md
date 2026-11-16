---
title: "CMGS"
subtitle: "Concrete Music Gran Studio — Manuel général"
author: "Jean-Jacques Girardot"
date: "Novembre 2026 — document de travail"
lang: fr-FR
toc-title: "Table des matières"
---

::: {custom-style="part"}
Partie I — Présentation et installation
:::

# Qu'est-ce que CMGS

## Finalités

Le **Concrete Music Gran Studio**, ou **CMGS**, est un ensemble d'outils destinés aux compositeurs de musique
concrète et électroacoustique. Il est né du *Game Master*, un générateur de séquences sonores multicanales, et s'est
enrichi au fil des années d'outils de diffusion, de traitement et de mise au point. Il couvre aujourd'hui trois usages :

- **le studio** : composer à partir de sons fixés (les *clips*), les transformer, les placer dans l'espace, essayer
  rapidement de nombreuses variantes ;
- **le concert** : diffuser une pièce sur un acousmonium, jouer en direct depuis des contrôleurs MIDI ou des capteurs ;
- **l'installation** : laisser le logiciel générer, pendant des heures, des séquences toujours renouvelées, selon des
  règles fixées par le compositeur.

Tous les outils de CMGS sont pensés pour le **multicanal** : la plupart traitent jusqu'à 128 canaux, et une même
session peut se préparer au casque, en stéréophonie, puis se jouer sur une installation de plusieurs dizaines de
haut-parleurs.

## Principe de fonctionnement

CMGS est écrit en **JSFX**, le langage de plug-ins de REAPER : il ne fonctionne donc que dans **REAPER** (version 7.25
ou plus récente), sur Mac comme sur Windows. Chaque outil est un plug-in, que l'on place sur une piste de REAPER comme
n'importe quel effet.

Les plug-ins de REAPER fonctionnent dans un « bac à sable » : ils ne peuvent ni écrire de fichiers, ni connaître le
contenu des dossiers, ni piloter REAPER lui-même. CMGS contourne ces limites de trois façons :

- les plug-ins de CMGS **partagent une mémoire commune**, par laquelle ils échangent des commandes, des messages et
  des données (le Game Master pilote ainsi ses lecteurs, placés sur d'autres pistes) ;
- ils embarquent un **langage de script**, **mSL** (*micro Script Language*), qui permet de décrire des
  configurations, d'écrire des algorithmes de jeu, d'automatiser des réglages et de faire dialoguer les plug-ins ;
- un **script auxiliaire**, `CMGS-auxiliary.eel`, lancé comme une action de REAPER, écrit les fichiers que lui
  demandent les plug-ins et transmet leurs commandes à REAPER (lecture, marqueurs, actions).

Les plug-ins de CMGS partagent aussi une même **interface utilisateur** : onglets, panneaux, modules, pads et sliders
s'y utilisent de la même façon, et les touches du clavier y ont les mêmes rôles. Cette interface est décrite dans la
Partie II ; le langage mSL dans la Partie III ; la Partie IV rassemble tous les messages d'erreur.

## Ce document et les autres manuels

Ce manuel général présente l'ensemble de CMGS, son installation, et ce qui est commun à tous ses outils. Chaque outil
important a en outre son propre manuel, dans le dossier `CMGS-docs` :

| Fichier | Contenu |
|---|---|
| `GameMaster-Manuel` | le Game Master : clips, modes de jeu et d'espace, banques, jeu automatique, playlog |
| `Diffusion-3-Manuel` | Diffusion-3 : projecteurs, scènes, trajectoires, configurations, APCmini |
| `Interstys-Manuel` | Interstys : lignes, lecteurs, enregistreurs, effets, courbes, liens MIDI |
| `MCBM-Manuel` | les gestionnaires de basses MCBM-64 et MCBM-128 |
| `SmoothMultiLimiter-Manuel` | le limiteur multicanal |
| `Multichannel_VU_meter-Manuel` | le VU-mètre multicanal |
| `CMGS-Keys.md` | les touches du clavier de tous les plug-ins |
| `CMGS-Internals` | la documentation interne, destinée à qui veut modifier le code |

Les fichiers `.fodt` sont les sources LibreOffice des manuels ; les fichiers `.pdf` en sont la version imprimable.

# Les outils

## Le Game Master

Le **Game Master** est l'outil d'origine de CMGS : un échantillonneur couplé à un générateur de musique
électroacoustique. Il joue des *clips*, fichiers son de quelques secondes à quelques minutes (jusqu'à 10 000 par
projet), selon deux algorithmes :

- le jeu **« Play »** lit un segment du clip, avec une vitesse, un sens, un volume et des enveloppes choisis ;
- le jeu **« Loop »** en extrait des fragments, des boucles longues jusqu'aux grains de quelques millisecondes : on
  passe alors du *looper* à la synthèse granulaire.

Le compositeur ne règle pas chaque son : il décrit des **modes de jeu** (comment jouer un clip), des **modes d'espace**
(sur quels haut-parleurs, et comment), et les regroupe en **partiels**, **banques** et **groupes**. Le Game Master
choisit ensuite, à la main (pads, clavier, contrôleurs MIDI, capteurs) ou automatiquement (mode *auto-play*), les
clips à jouer et la façon de les jouer. Chaque son joué est noté dans le **playlog**, qui permet de le rejouer à
l'identique. Toute la configuration d'un projet tient dans un script mSL, le **Profile**.

Le Game Master se compose de plusieurs plug-ins :

| Plug-in | Rôle |
|---|---|
| `GamePlayer` | le Game Master proprement dit : interface, algorithmes, ordonnanceur, scripts mSL ; un seul par session |
| `FilePlayer` | un lecteur, qui joue un clip à la fois ; on en place un par piste, et leur nombre fait la polyphonie (typiquement 8 à 20) |
| `MIDI_In` | transmet au Game Master les messages d'un périphérique MIDI (contrôleurs, notes) |
| `MIDIduino` | transmet au Game Master les notes envoyées par des capteurs (par exemple infrarouges, sur un Arduino), ou par tout clavier MIDI |

## Diffusion-3

**Diffusion-3** diffuse, ou spatialise, des sources multicanales sur une installation multicanale (un acousmonium),
jusqu'à 128 canaux en entrée et en sortie. Il a d'abord été conçu pour diffuser facilement des pièces stéréophoniques
sur un grand nombre de haut-parleurs ; il permet aussi d'essayer la spatialisation d'une piste pendant la composition,
ou de projeter en concert plusieurs sources (un instrument joué en direct, des pistes d'accompagnement).

Il propose 16 **projecteurs** indépendants, des **scènes** et le passage progressif de l'une à l'autre (*morphing*),
des **trajectoires** dans un espace en trois dimensions, avec une vue 3D, des **configurations** de haut-parleurs
décrites en mSL, et la commande depuis un contrôleur **AKAI APCmini**.

## Interstys

**Interstys** est un **délai fractionnaire modulaire** : il enregistre le son dans des mémoires (les *lignes*), le
relit à des vitesses et des retards quelconques, le transforme par des *effets*, et relie tous ces éléments par des
*câbles*, à la manière d'un synthétiseur modulaire. Ses lecteurs savent aussi étirer le temps (*Stretch*) et produire
des grains (*Grains*) ; ses effets vont du filtre et de la saturation aux matrices de réinjection, flanger, phaser,
shimmer, bruits et générateurs aléatoires. Les réglages peuvent être modulés, liés à des contrôleurs MIDI, et décrits
entièrement en mSL : un patch peut être sauvegardé, rechargé, ou construit par un script.

## ScriptMaster

**ScriptMaster** est un atelier pour les scripts mSL. On y dépose un script, qui est compilé et exécuté ; on suit son
travail dans le journal (*System Log*), l'ordonnanceur (*Scheduler*), les processus (*Processes Manager*) et la
mémoire (*Memory*). Il sert à mettre au point des scripts, à faire tourner des tâches indépendantes des autres outils,
et à passer les séries de tests du langage.

## Les plug-ins auxiliaires

CMGS fournit aussi des plug-ins plus simples, utiles dans une session multicanale :

| Plug-in | Rôle |
|---|---|
| `MCBM-64`, `MCBM-128` | gestionnaires de basses multicanaux, jusqu'à 128 canaux : les graves de chaque canal sont envoyés vers un ou plusieurs caissons (`MCBM-128` : filtres de Linkwitz-Riley) |
| `SmoothMultiLimiter` | limiteur multicanal, jusqu'à 128 canaux (d'après un plug-in de Geraint Luff) |
| `Multichannel_VU_meter` | VU-mètre jusqu'à 128 canaux (dérivé du *S&M Multichannel VU meter* de Jeff Bédague) ; `Multichannel_VU_meter_U` en est une variante |
| `channels-folder` | replie les canaux d'une piste sur un nombre plus petit (par exemple sur 2, pour écouter au casque une session octophonique) |
| `CheapChannelReducer` | réduction stéréo sommaire : les canaux impairs à gauche, les pairs à droite |
| `ChannelReducer16`, `24`, `48` | envoie chaque canal d'entrée vers le canal de sortie de son choix |
| `ChannelsMuter` | coupe tous les canaux d'une piste |
| `ChannelsSwitcher` | sélecteur de canaux pour 8 canaux, à quelques configurations fixes |
| `mid-side` | réglage séparé des parties *mid* et *side* d'une stéréo |
| `Synchronizer` | fournit aux autres plug-ins le numéro exact de l'échantillon courant, pour les synchroniser à l'échantillon près |

Trois plug-ins servent d'exemples : `AKAI-Ex-01` et `AKAI-Ex-02` (programmation d'un AKAI APCmini), et `Space3D-Demo`
(la vue en trois dimensions de Diffusion-3).

## Le script auxiliaire

`CMGS-auxiliary.eel` n'est pas un plug-in mais un *ReaScript*, que l'on charge une fois dans la liste des actions de
REAPER (voir l'installation). Lancé, il reste en tâche de fond et répond aux demandes des plug-ins :

- **écrire des fichiers** : export du journal d'un plug-in (touche `p`), patchs et sessions d'Interstys, exports de
  Diffusion-3 ;
- **afficher** un texte dans la console de REAPER (touche `P` du journal) ou une boîte de dialogue ;
- **piloter REAPER** : lecture, arrêt, pause, déplacement vers un marqueur, position du curseur, exécution de
  n'importe quelle action de REAPER par son numéro ;
- **fournir le dossier du projet**.

Les plug-ins fonctionnent sans lui, mais ces services ne sont alors pas disponibles.

# Tutoriels et scripts fournis

## Le tutoriel « GM-Octo »

Le dépôt **CMGS-Tutorials** (<https://github.com/jack461/CMGS-Tutorials>) contient un projet complet, *GM-Octo-2024*
(dossier `Tuto-01`), d'environ 1 Go. C'est à l'origine un programme de concert pour lequel plusieurs compositeurs
ont fourni des sons ; seuls ont été gardés les fichiers placés par leurs auteurs sous licence *Creative Commons*
(Gilles Roussi, Diego Losa, Francis Valery, Alain Girardot, Jean-Jacques Girardot).

Le projet réunit un Game Master, douze lecteurs, les pistes de mixage et d'écoute au casque, et un Profile qui décrit
les modes de jeu et d'espace, les banques et les capteurs. Une fois CMGS installé :

1. téléchargez le dépôt (bouton vert **Code**, puis **Download ZIP**), décompressez-le, et placez le dossier
   `GM-Octo-2024` où vous voulez ;
2. double-cliquez sur `GM-Octo.RPP` : REAPER s'ouvre, mais le journal du GamePlayer (piste « GAME PLAYER ») signale
   des erreurs, car le plug-in utilise encore les chemins de l'ordinateur où le projet a été enregistré ;
3. faites glisser le fichier `GM-Octo.RPP` dans la fenêtre du GamePlayer : le plug-in apprend ainsi où se trouve le
   projet ;
4. enregistrez le projet, quittez REAPER et relancez-le : la dernière ligne du journal affiche
   `** GAME MASTER / SESSION OCTO READY **`.

Cliquez alors sur **Auto-play** : le Game Master commence à jouer. La sortie est en stéréophonie ; pour écouter en
octophonie, désactivez le plug-in `channels-folder` de la piste MASTER.

## Les scripts de `CMGS-scripts`

Le dossier `CMGS-scripts` contient des scripts mSL dont les plug-ins n'ont pas besoin pour fonctionner, mais qui
servent d'exemples, de recettes ou d'outils de vérification. Pour lancer un script, il suffit de déposer le fichier
`.mSL` dans la fenêtre d'un plug-in ; ses messages apparaissent dans le journal de celui-ci.

| Dossier | Contenu |
|---|---|
| `Algorithms` | Interstys : des recettes prêtes à l'emploi (Matrix, Flanger, Chorus, Phaser, Shimmer, Noise, Random, Math, Ring), chacune avec ses paramètres ; `Sources.mSL` fournit du matériau d'essai |
| `Presets` | Interstys : cinq presets de génération, qui transforment un son d'entrée en une dizaine de minutes de musique |
| `Examples` | Interstys : petits exemples (chaîne d'effets, courbes, liens MIDI d'un AKAI MIDI Mix) |
| `Tests` | les séries de tests `Ex-NNNN.mSL` du langage et des plug-ins, et l'outil `check_scripts.py` qui en vérifie les résultats (voir la Partie III) |

# Installation

## REAPER

Installez **REAPER 7.25 ou plus récent** (<https://www.reaper.fm/download.php>). CMGS n'a besoin d'aucune extension
de REAPER. Au premier lancement, vérifiez que votre carte son est reconnue (*Options ▷ Preferences… ▷ Audio ▷
Device*) et choisissez la fréquence d'échantillonnage et la taille des blocs.

Certains réglages de REAPER sont indispensables au bon fonctionnement de CMGS :

| Réglage (*Options ▷ Preferences…*) | Valeur | Raison |
|---|---|---|
| *Audio* ▷ les deux options *Close audio device when stopped…* | décochées | sinon les plug-ins cessent de travailler quand REAPER est à l'arrêt ou en arrière-plan |
| *Audio ▷ Playback* ▷ *Run FX when stopped* | cochée | les plug-ins doivent travailler même quand REAPER ne lit rien |
| *General* ▷ *Maximum undo memory use* | 0 | l'état du Game Master est volumineux : REAPER perdrait beaucoup de temps à le sauvegarder pour ses « undo » |
| *MIDI Devices* | *Enable input* et *Enable input for control messages* pour chaque contrôleur utilisé | pour piloter les plug-ins depuis des contrôleurs MIDI |

## Récupérer CMGS

CMGS est distribué sur <https://github.com/jack461/CMGS>. Cliquez sur le bouton vert **Code**, puis sur
**Download ZIP**, et décompressez `CMGS-main.zip` où vous voulez (on peut aussi faire un `git clone` du dépôt). Ne
placez pas ce dossier lui-même dans le dossier des ressources de REAPER : on n'en copie que trois éléments.

## Mettre CMGS en place

Ouvrez le dossier des ressources de REAPER (*Options ▷ Show REAPER resource path in explorer/finder*) et copiez-y :

| Depuis le dossier de CMGS | Vers le dossier des ressources de REAPER | Contenu |
|---|---|---|
| `CMGS-effects/` | `Effects/CMGS-effects/` | les plug-ins, et leurs bibliothèques dans `CMGS-libs/` |
| `CMGS-data/` | `Data/CMGS-data/` | les données lues par les plug-ins : thèmes de l'interface, configurations de Diffusion-3 |
| `CMGS-auxiliary.eel` | `Scripts/CMGS-auxiliary.eel` | le script auxiliaire |

**Gardez ces noms** : les plug-ins cherchent ces dossiers sous ces noms, et les projets de REAPER désignent les
plug-ins sous la forme `CMGS-effects/GamePlayer.jsfx`. Les plug-ins apparaissent alors dans le navigateur d'effets de
REAPER, sous *JS*, dans le dossier `CMGS-effects`.

Facultativement, copiez aussi `CMGS-scripts/` dans `Data/`, à côté de `CMGS-data` : les plug-ins pourront alors ouvrir
un script par un nom tel que `CMGS-scripts/Algorithms/Matrix-Metal.mSL`.

## Charger le script auxiliaire

Une fois pour toutes :

1. ouvrez la liste des actions (*Actions ▷ Show action list…*) ;
2. cliquez sur *New action…* ▷ *Load ReaScript…* et choisissez `Scripts/CMGS-auxiliary.eel` ;
3. l'action « Script: CMGS-auxiliary.eel » apparaît dans la liste.

À chaque session de REAPER, lancez cette action (sélectionnez-la, puis *Run*). Le script écrit dans la console de
REAPER un premier message, « GMA … started », suivi de la date, et reste actif jusqu'à la fermeture de REAPER. Pour
l'arrêter avant, choisissez *Actions ▷ Running script: CMGS-auxiliary.eel*, puis *Terminate instances*.

## Mettre à jour CMGS

Remplacez `Effects/CMGS-effects`, `Data/CMGS-data` et `Scripts/CMGS-auxiliary.eel` par les nouvelles versions. Vos
projets continuent de fonctionner : ils désignent les plug-ins par leur nom. Les préréglages enregistrés dans REAPER
(dossier `presets`, fichiers `js-CMGS-effects_…_jsfx.ini`) sont conservés.

## Organisation d'un projet

Un projet de REAPER qui utilise le Game Master est un dossier qui contient, outre le fichier `.RPP` :

| Dossier du projet | Contenu |
|---|---|
| `Data/Scripts/` | les scripts mSL du projet, dont le **Profile** `GM_mSL_ini.mSL`, qui décrit toute la configuration du Game Master |
| `Data/WAVES/` | les clips, nommés `clip1NNNN.ext` (`NNNN` de `0000` à `9999`, `ext` : `wav`, `aif`, `flac`, `mp3`…) |
| `Data/Sounds/` | d'autres sons, de noms quelconques, que l'on associe à des numéros de clips par glisser-déposer |

Le Game Master doit connaître le dossier du projet : on le lui indique en faisant glisser le fichier `.RPP` dans sa
fenêtre, puis en enregistrant le projet. Il faut refaire cette opération après avoir déplacé ou copié le projet,
en particulier sur une autre machine. Les sons du dossier `Data` suivent le projet : un projet ainsi organisé se
transporte d'une machine à l'autre, pourvu que CMGS y soit installé.

Interstys et Diffusion-3 ont leurs propres fichiers (patchs, sessions, configurations), décrits dans leurs manuels.

## Pour les développeurs

Au lieu de copier les dossiers, on peut créer, dans le dossier des ressources de REAPER, des liens symboliques vers
un clone du dépôt (`ln -s` sous macOS et Linux, `mklink /D` sous Windows) : REAPER voit alors directement chaque
modification des sources. Les alias du Finder de macOS ne fonctionnent pas. Le script `CMGS-auxiliary.eel` est
généré : on modifie `CMGS-effects/CMGS-libs/CMGS-auxiliary-src.eel`, puis on lance
`python3 -I CMGS-aux/tools/make_auxiliary.py`.

Le dépôt est organisé ainsi :

| Chemin | Contenu |
|---|---|
| `CMGS-effects/` | les plug-ins (`.jsfx`) ; `CMGS-libs/` contient les bibliothèques communes et le code des gros plug-ins (`.jsfx-inc`) |
| `CMGS-data/` | les données lues à l'exécution : thèmes, configurations de Diffusion-3 |
| `CMGS-auxiliary.eel` | le script auxiliaire (généré) |
| `CMGS-scripts/` | les scripts mSL : algorithmes, presets, exemples, tests |
| `CMGS-docs/` | les manuels |
| `CMGS-aux/` | outils de développement (Python) et archives |

::: {custom-style="part"}
Partie II — L'interface commune
:::

# Fenêtre, onglets, panneaux et modules

*À rédiger.*

# Pads, sliders, afficheurs et menus

*À rédiger.*

# Le clavier

*À rédiger.*

# Les modules communs

*À rédiger.*

# Fichiers, préréglages et exports

*À rédiger.*

::: {custom-style="part"}
Partie III — mSL, le langage de CMGS
:::

# Premiers pas

*À rédiger.*

# Le langage en détail

*À rédiger.*

# Exécution des scripts

*À rédiger.*

::: {custom-style="part"}
Partie IV — Les erreurs
:::

# Liste des erreurs

*À rédiger.*
