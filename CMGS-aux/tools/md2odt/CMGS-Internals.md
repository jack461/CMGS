---
title: "CMGS — Documentation interne"
subtitle: "Les fonctions communes aux plug-ins"
author: "Jean-Jacques Girardot"
date: "Octobre 2026 — document de travail"
lang: fr-FR
toc-title: "Table des matières"
---

# Finalité des fonctions communes

## Le contexte : une suite de plug-ins coopérants

CMGS (*Concrete Music Gran Studio*) est une suite de plug-ins pour REAPER, destinée à la
composition et à la diffusion de musique concrète. Elle comprend principalement :

| Plug-in | Rôle |
|---|---|
| **GamePlayer** (le *Game Master*) | génération et ordonnancement du jeu des clips, interface principale, exécution des scripts |
| **FilePlayer** | lecture des fichiers sonores, pilotée par le Game Master |
| **ScriptMaster** | édition, mise au point et exécution des scripts mSL |
| **Interstys** | lignes à retard fractionnaires modulaires (lignes, lecteurs, écrivains, effets) |
| **Diffusion-3** | spatialisation sur un grand nombre de haut-parleurs (projecteurs, scènes, morphing) |
| **MIDI_In**, **MIDIduino** | entrée de commandes MIDI et de capteurs vers le Game Master |
| **GMAuxiliary.eel** | script REAPER (ReaScript) qui réalise pour les plug-ins ce qu'ils ne peuvent pas faire eux-mêmes |

Ces plug-ins sont écrits en **JSFX**, le langage d'effets de REAPER (fondé sur EEL2). Ils
fonctionnent ensemble : le Game Master commande les lecteurs, les scripts peuvent agir sur
tous les plug-ins, et les informations circulent de l'un à l'autre.

## Ce que JSFX ne fournit pas

JSFX est conçu pour des traitements audio simples. Il impose des contraintes fortes à un
ensemble de cette taille :

- **une mémoire plate** : un tableau de nombres (`mem[]`), sans structures, sans allocation
  dynamique, sans libération ;
- **des chaînes de caractères numérotées**, en nombre fixé à la compilation ;
- **pas de multitâche** : seulement les sections exécutées par REAPER (`@init`, `@slider`,
  `@block`, `@sample` dans le fil audio, `@gfx` dans le fil graphique, `@serialize`) ;
- **une interface graphique rudimentaire** : quelques primitives de dessin et la souris ;
- **pas d'accès à REAPER** (projet, pistes, actions) ;
- **une seule zone d'échange entre plug-ins**, la mémoire partagée `gmem[]`, elle aussi
  plate ;
- **des fonctions qui doivent être définies avant d'être utilisées**, et aucun mécanisme de
  modules.

## La finalité du socle commun

Les fonctions communes construisent, au-dessus de JSFX, l'environnement dont chaque plug-in a
besoin, une fois pour toutes et de la même façon pour tous :

1. **Gérer la mémoire** comme dans un langage moderne : blocs typés, allocation statique pendant
   l'initialisation, allocation dynamique ensuite, et récupération automatique des blocs
   devenus inutiles (ramasse-miettes).
2. **Gérer des chaînes de caractères dynamiques**, allouées, libérées et récupérées.
3. **Offrir un langage de script**, **mSL** (*micro Script Language*) : un compilateur et un
   interprète intégrés à chaque plug-in, qui permettent de programmer le comportement de
   l'ensemble sans modifier les plug-ins eux-mêmes.
4. **Exécuter plusieurs tâches** : processus (*threads*) mSL, ordonnanceur de tâches datées,
   événements et messages entre processus.
5. **Faire communiquer les plug-ins** : organisation de la mémoire partagée, échange de valeurs
   et de chaînes, journal commun, temps partagé, et accès à REAPER par le script GMAuxiliary.
6. **Fournir une interface graphique commune** : thèmes, menus, pads, curseurs, onglets et
   panneaux de modules, affichages système (journal, mémoire, processus), écran *Live*.
7. **Rassembler les utilitaires** : fichiers, chemins du projet, configuration, édition de
   valeurs, journalisation et contrôles d'intégrité.

Grâce à ce socle, un nouveau plug-in de la suite hérite immédiatement de toutes ces capacités,
avec la même apparence et le même comportement que les autres.

## Les grandes familles de fonctions

Les fonctions communes se trouvent dans le répertoire `GM-Libs`. Elles se regroupent en sept
familles.

| Famille | Fichiers principaux | Rôle |
|---|---|---|
| Mémoire | `mSL_StM_Memory`, `mSL_Dyn_Memory`, `mSL_Garbage_Collector`, `mSL_Dbg_Memory` | blocs typés, allocation statique et dynamique, ramasse-miettes, inspection |
| Chaînes | `mSL_Strings`, `mSL_string_list_*`, `mSL_gmem_Strings` | réserve de chaînes, allocation, chaînes échangées par la mémoire partagée |
| Langage mSL | `mSL_Constants`, `mSL_Comp_lib`, `mSL_Evaluator`, `mSL_Extend`, `mSL_DeAsm`, `mSL_GM_Vars_Access`, `mSL_FR_Vars_Access` | compilateur, interprète, extensions, désassembleur, accès aux variables JSFX |
| Exécution | `mSL_Scheduler`, `mSL_Threads`, `mSL_Events` | ordonnanceur, processus mSL, événements et messages |
| Communication | `mSL_clip_map`, `mSL_clip_lib`, `clip_lib_MIDI`, `GMAuxiliary.eel` | carte de la mémoire partagée, échanges entre plug-ins, MIDI, accès à REAPER |
| Interface | `ui-lib`, `ui-lib-JJ-GUI`, `mSL_ui_LibJJ`, `mSL_ui_Menus`, `mSL_ui_Pads`, `mSL_ui_audio`, `mSL_Panes`, `mSL_show_Utilities`, `mSL_Live_Screen`, `mSL_Colors` | bibliothèque graphique et ses extensions, onglets et panneaux, affichages système |
| Utilitaires | `mSL_Utilities`, `mSL_Utilities2` | fichiers, chemins, verrous, journal, tris, contrôles |

La bibliothèque graphique de base, `ui-lib`, est celle de Geraint Luff ; les autres fichiers
sont propres à CMGS.

## Qui utilise quoi

Les cinq grands plug-ins utilisent l'ensemble du socle ; MIDI_In n'en utilise que la partie
nécessaire à son interface et à sa communication avec le Game Master.

| Famille | GP | FP | SM | IN | D3 | MI |
|----------------------------------------------|-----|-----|-----|-----|-----|-----|
| Mémoire statique et chaînes | oui | oui | oui | oui | oui | oui |
| Mémoire dynamique | oui | oui | oui | oui | oui | — |
| Ramasse-miettes | oui | oui | oui | oui | oui | — |
| Compilateur mSL | oui | oui | oui | oui | oui | — |
| Interprète mSL, processus, événements | oui | oui | oui | oui | oui | — |
| Ordonnanceur | oui | oui | oui | oui | oui | — |
| Mémoire partagée et échanges | oui | oui | oui | oui | oui | oui |
| Interface (ui-lib et extensions) | oui | oui | oui | oui | oui | oui |
| Onglets et panneaux (`mSL_Panes`) | — | — | — | — | oui | — |
| Affichages système (`mSL_show_Utilities`) | oui | oui | oui | oui | oui | — |
| Écran *Live* | oui | — | — | oui | oui | — |

*GP : GamePlayer, FP : FilePlayer, SM : ScriptMaster, IN : Interstys, D3 : Diffusion-3, MI : MIDI_In.*

GamePlayer et Interstys disposent de leur propre gestion des onglets et des panneaux, plus
ancienne ; `mSL_Panes` en est la version partagée, utilisée par Diffusion-3. Le
désassembleur (`mSL_DeAsm`) et l'inspection de la mémoire (`mSL_Dbg_Memory`) sont présents dans
les cinq grands plug-ins ; ScriptMaster y ajoute ses outils d'édition des scripts
(`ScriptMaster_Utilities`, également utilisés par Interstys).

## Les principes de conception communs

**Une seule base de code.** Chaque plug-in est une coquille (`.jsfx`) qui déclare ses
curseurs et ses options, puis inclut les bibliothèques communes et son propre corps
(`GM-Libs/<Nom>.jsfx-inc`). L'ordre des inclusions compte, puisqu'une fonction doit être
définie avant d'être utilisée. Le préprocesseur de JSFX permet d'adapter une bibliothèque à
chaque plug-in (capacités, parties à inclure, variantes).

**Une mémoire structurée et vérifiable.** Toute donnée importante est un bloc muni d'un type,
d'une taille et d'une marque de fin calculée (somme de contrôle). Les allocateurs, le
ramasse-miettes et les outils d'inspection peuvent ainsi détecter une corruption au lieu de la
propager. Les blocs créés pendant l'initialisation sont statiques ; ceux créés ensuite sont
dynamiques et récupérés par le ramasse-miettes, qui part de racines déclarées (objets protégés,
listes de l'ordonnanceur, tables des processus).

**Le temps réel d'abord.** Les traitements audio (`@block`, `@sample`) doivent rester brefs et
prévisibles. Les travaux longs ou irréguliers — compilation d'un script, passage du
ramasse-miettes, affichage — se font dans le fil graphique (`@gfx`), sous la protection d'un
verrou qui suspend l'exécution des processus pendant ce temps.

**Un langage pour tout piloter.** Plutôt que de multiplier les commandes dans chaque plug-in,
CMGS confie les comportements complexes à des scripts mSL, compilés dans le plug-in qui les
exécute. Les variables JSFX des plug-ins sont accessibles aux scripts par des tables générées.

**Une coopération par la mémoire partagée.** Le Game Master orchestre ; les autres plug-ins
exécutent et rendent compte. La carte de la mémoire partagée (`mSL_clip_map`) fixe la place de
chaque information échangée ; elle doit rester compatible entre tous les plug-ins et avec
GMAuxiliary. Ce script, qui tourne en permanence, réalise les opérations que JSFX ne permet pas
(chemin du projet, écriture du journal dans un fichier, etc.) à la demande des plug-ins.

**Une interface homogène.** Tous les plug-ins partagent les mêmes thèmes, menus, pads,
curseurs, styles (classique ou *soft*) et affichages système, ce qui permet de passer de l'un à
l'autre sans réapprendre.

**Des erreurs traçables.** Chaque erreur détectée porte un code à quatre chiffres, unique dans
les sources (ce qui permet de le retrouver par une simple recherche), et les incidents sont
notés dans le journal système, consultable dans chaque plug-in et exportable dans un fichier.

## Plan du document

Les chapitres suivants décrivent chaque famille de fonctions en détail :

1. Finalité des fonctions communes (ce chapitre).
2. Organisation des sources : coquilles, corps, inclusions, préprocesseur, sections JSFX.
3. La mémoire : blocs, allocation statique, allocation dynamique, ramasse-miettes.
4. Les chaînes de caractères.
5. Le langage mSL : compilateur, code produit, interprète, extensions.
6. L'exécution : ordonnanceur, processus, événements et messages.
7. La communication entre plug-ins : mémoire partagée, GMAuxiliary, MIDI.
8. L'interface graphique : ui-lib et ses extensions, onglets et panneaux, affichages système.
9. Les utilitaires.
10. Annexes : codes d'erreur, conventions de nommage, liste des fichiers.

# Organisation des sources

Coquilles des plug-ins, corps, inclusions et leur ordre, préprocesseur, sections JSFX. *À rédiger.*

# La mémoire

Blocs, allocation statique, allocation dynamique, ramasse-miettes, inspection. *À rédiger.*

# Les chaînes de caractères

Réserve de chaînes, allocation, chaînes échangées par la mémoire partagée. *À rédiger.*

# Le langage mSL

Compilateur, code produit, interprète, extensions, désassembleur. *À rédiger.*

# L'exécution

Ordonnanceur, processus, événements et messages. *À rédiger.*

# La communication entre plug-ins

Ce chapitre décrira la mémoire partagée (`mSL_clip_map`, `mSL_clip_lib`), le script GMAuxiliary et la liaison MIDI ; seule la synchronisation au sample près est rédigée pour l'instant.

## Synchronisation au sample près

### Principe

Le GamePlayer fournit à tous les plug-ins qui le souhaitent un **compteur d'échantillons**
commun : le numéro de l'échantillon en cours, compté depuis le chargement du GamePlayer dans la
session. Ce compteur est transmis **par l'audio**, sur les canaux 1 et 2 (`spl0`, `spl1`) de la
sortie du GamePlayer, que la session REAPER envoie aux plug-ins concernés (en particulier les
FilePlayer). Chaque récepteur connaît ainsi, pour chaque échantillon qu'il traite, son numéro
exact : des opérations peuvent être déclenchées **au sample près**, de façon synchrone dans tous
les plug-ins.

### Codage

Le numéro d'échantillon est décomposé en deux entiers de 24 bits :

    numéro = T0 + 2^24 × T1        avec 0 ≤ T0 < 2^24

et chacun est transmis multiplié par 2^-48^ :

    spl0 = T0 × 2^-48        spl1 = T1 × 2^-48

Dans le GamePlayer, `T0` est incrémenté à chaque échantillon (`@sample`) ; dans `@block`, quand
`T0` atteint 2^24^, il est diminué de 2^24^ et `T1` est incrémenté. (`T0` peut donc dépasser
2^24^ de quelques échantillons avant la fin du bloc ; la somme décodée reste exacte.)

Les constantes sont définies dans `mSL_Constants` : `T_fact` = 2^48^, `T_maxk` = 2^24^ ; le
GamePlayer utilise `T_div` = 1 / `T_fact`.

### Décodage

Au début de `@sample`, chaque récepteur calcule :

    currSmpl = floor(spl0 * T_fact + 0.5) + floor(spl1 * T_fact + 0.5) * 16777216;
    spl0 = spl1 = 0;

L'arrondi (+ 0,5) rend le décodage insensible à une infime erreur de gain sur le trajet. La
remise à zéro de `spl0` et `spl1` évite que ces valeurs poursuivent leur chemin vers les
haut-parleurs. Le même calcul est fait dans le GamePlayer lui-même, qui dispose ainsi du même
`currSmpl` que les récepteurs.

### Propriétés

- **Exactitude** : les valeurs k × 2^-48^, pour k < 2^24^, sont représentées exactement, même
  dans un trajet audio en flottants 32 bits (mantisse de 24 bits).
- **Durée** : 2^48^ échantillons, soit environ 186 ans à 48 kHz.
- **Inaudibilité** : `spl0` est une rampe d'amplitude au plus 2^-24^ (environ −144 dBFS), de
  période 2^24^ échantillons (349 s à 48 kHz, soit 0,003 Hz) ; `spl1` est un escalier de pas
  2^-48^ toutes les 349 s. Même amplifiés de 60 dB, ces signaux restent vers −84 dBFS, dans
  l'infrasonore.
- **Nature du compteur** : il compte les échantillons *traités*. Si REAPER n'exécute pas les
  effets à l'arrêt, il se fige ; tous les récepteurs lisant le même compteur, ils restent
  synchronisés entre eux.

### Conditions d'emploi

- Le GamePlayer et les récepteurs positionnent `ext_noinit = 1` (le compteur n'est pas remis à
  zéro au démarrage de la lecture) et `ext_nodenorm = 1` (JSFX ne modifie pas les échantillons
  pour éviter les nombres dénormalisés).
- Le trajet doit être transparent : envoi à 0 dB, sans loi de panoramique ni effet
  intermédiaire, à la même fréquence d'échantillonnage.
- Les canaux 1 et 2 de la sortie du GamePlayer ne transportent que le compteur : la piste du
  GamePlayer ne doit pas alimenter les haut-parleurs (ce serait inaudible, mais inutile).

### Perte de synchronisation

Si le compteur n'arrive pas (envoi absent ou coupé), `currSmpl` reste figé, et les événements
datés en échantillons (`smplNewEV`) ne se produiraient jamais. Le FilePlayer vérifie, à chaque
`@block`, que `currSmpl` a avancé depuis le bloc précédent ; sinon il écrit une fois dans le
journal système « FilePlayer : no sample counter from the GamePlayer (channels 1-2), sample
dated events stopped », puis, au retour du compteur, « … sample counter from the GamePlayer
received again ».

### Commandes datées

Comme tous les plug-ins partagent le même compteur, une commande peut être déposée dans la
mémoire partagée avec une **date en échantillons** : le destinataire l'exécute au sample près,
pourvu qu'elle lui parvienne avant cette date (au moins un bloc à l'avance). C'est le mécanisme
des événements `smplNewEV` du FilePlayer.

Des canaux supplémentaires (`spl2`, `spl3`) pourraient transporter des commandes de la même
façon (un entier de 24 bits par échantillon et par canal, soit environ 1,15 Mbit/s à 48 kHz,
toujours inaudible) ; ils n'apporteraient un gain que pour une commande décidée dans le
`@sample` ou le `@block` du GamePlayer et devant agir dans le même échantillon. Cette extension
n'est pas réalisée.

### Le plug-in Synchronizer

`Synchronizer.jsfx` est la forme autonome du même mécanisme, pour synchroniser d'autres plug-ins
JSFX sans GamePlayer : placé sur une piste dédiée, il produit le compteur sur ses canaux 1 et 2,
que l'on envoie aux pistes à synchroniser ; son commentaire d'en-tête donne le code de décodage.

# L'interface graphique

ui-lib et ses extensions, thèmes, menus, pads, onglets et panneaux, affichages système. *À rédiger.*

# Les utilitaires

Fichiers, chemins, configuration, journal, contrôles. *À rédiger.*

# Annexes

Codes d'erreur, conventions de nommage, liste des fichiers. *À rédiger.*
