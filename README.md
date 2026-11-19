# CMGS — Concrete Music Gran Studio

*[Version française plus bas](#version-française).*

The **Concrete Music Gran Studio**, or **CMGS**, is a set of tools for composers of concrete and electroacoustic
music: a sampler coupled with a music generator, a multichannel spatialization system, a modular delay, and the
auxiliary plugins they need in the studio, in concerts or in installations.

CMGS is written in **JSFX**, the plugin language of [REAPER](https://www.reaper.fm), so it runs only inside
REAPER, version **7.25 or later**.

## The applications

| Application | Plugins | Role |
|---|---|---|
| **Game Master** | `GamePlayer`, with `FilePlayer`, `ScriptMaster`, `MIDI_In`, `MIDIduino` | Sampler and electroacoustic music generator: clip players, generator, scheduler, live control. `FilePlayer` is a sample reader driven by the Game Master, `ScriptMaster` an editor, debugger and runner of scripts, `MIDI_In` and `MIDIduino` bring MIDI and sensors into the Game Master. |
| **Diffusion-3** | `Diffusion-3` | Spatialization of up to 128 inputs and outputs: projectors, scenes, morphing, 3D trajectories, configurations of the loudspeakers, control by an AKAI APCmini. |
| **Interstys** | `Interstys` | Modular fractional delay: lines, readers (Stretch, Grains…), writers, effects (filters, saturation, feedback matrix, flanger, phaser, shimmer, noise, random…), curves, MIDI links. |

These applications share **mSL**, a small scripting language: scripts drive them, exchange messages, and describe
their configurations, patches and presets. Ready-to-use scripts are in [`CMGS-scripts/`](CMGS-scripts/README.md).

### Auxiliary plugins

- `MCBM-64`, `MCBM-128`: multichannel bass managers, up to 128 channels (`MCBM-128`: Linkwitz-Riley crossovers).
- `SmoothMultiLimiter`: a limiter for up to 128 channels.
- `Multichannel_VU_meter` (and its variant `Multichannel_VU_meter_U`): a VU meter for up to 128 channels.
- Small utilities: `ChannelReducer16/24/48`, `CheapChannelReducer`, `ChannelsMuter`, `ChannelsSwitcher`,
  `mid-side`, `channels-folder`, `Synchronizer`.
- Examples: `AKAI-Ex-01`, `AKAI-Ex-02` (AKAI APCmini), `Space3D-Demo` (the 3D view of Diffusion-3).

## Installation

1. Install **REAPER** 7.25 or later (<https://www.reaper.fm/download.php>), and check that it recognizes your sound
   card (*Options > Settings… > Audio > Device*).

   > [!IMPORTANT]
   > Some settings stop the Game Master. In *Options > Settings… > Audio*, the two options *Close audio device
   > when stopped…* must **not** be checked, and in *Audio > Playback*, *Run FX when stopped* must be checked.

2. Get CMGS: on <https://github.com/jack461/CMGS>, click the green **Code** button, then **Download ZIP**, and
   unzip `CMGS-main.zip` wherever you like (or `git clone` the repository). Do not put this folder itself in the
   REAPER resource folder.

3. Open the REAPER resource folder (*Options > Show REAPER resource path in explorer/finder*), and copy into it:

   | From the CMGS folder | To the REAPER resource folder |
   |---|---|
   | `CMGS-effects/` | `Effects/CMGS-effects/` |
   | `CMGS-data/` | `Data/CMGS-data/` |
   | `CMGS-auxiliary.eel` | `Scripts/CMGS-auxiliary.eel` |

   Keep these names: the plugins look for these folders, and REAPER projects refer to the plugins as
   `CMGS-effects/<plugin>.jsfx`.

4. Load the auxiliary script: *Actions > Show action list… > New action > Load ReaScript…*, choose
   `Scripts/CMGS-auxiliary.eel`, then run this action once in each REAPER session. It stays in the background and
   lets the plugins write files (for instance the export of the system log with the key `p`, or the patches and
   sessions exported by Interstys), know the folder of the project, and drive the transport of REAPER from scripts.

5. Optional: copy `CMGS-scripts/` into `Data/` as well (next to `CMGS-data`); the plugins can then open a script by
   a name such as `CMGS-scripts/Algorithms/Matrix-Metal.mSL`.

The plugins now appear in the FX browser of REAPER, under *JS*, in the folder `CMGS-effects`.

**Updating:** replace `Effects/CMGS-effects`, `Data/CMGS-data` and `Scripts/CMGS-auxiliary.eel` by the new
versions. Your projects keep working: they refer to the plugins by name.

**For developers:** instead of copying, you may make symbolic links from the REAPER resource folder to a clone of
the repository (`ln -s` on macOS and Linux, `mklink /D` on Windows); REAPER then sees every change of the sources.
macOS Finder aliases do not work. `CMGS-auxiliary.eel` is generated: edit
`CMGS-effects/CMGS-libs/CMGS-auxiliary-src.eel`, then run `python3 -I CMGS-aux/tools/make_auxiliary.py`.

A first tutorial, a complete project with about 1 GB of samples, is available at
<https://github.com/jack461/CMGS-Tutorials>.

## Documentation

The manuals are in [`CMGS-docs/`](CMGS-docs/) and are written in French (the `.fodt` files are their LibreOffice
sources).

| File | Contents |
|---|---|
| `CMGS-Manuel.pdf` | General manual: what CMGS is, installation, the common user interface, the mSL language (with a programming course), the list of all the error codes |
| `GameMaster-Manuel.pdf` | The Game Master (what is specific to it; the rest is in the general manual) |
| `GameMaster-Doc-1.7.8.pdf` | The former complete manual of the Game Master (version 1.7.8, 2024) |
| `GM-Commandes.pdf` | Commands of the Game Master |
| `Diffusion-3-Manuel.pdf` | Diffusion-3 |
| `Interstys-Manuel.pdf` | Interstys |
| `MCBM-Manuel.pdf`, `SmoothMultiLimiter-Manuel.pdf`, `Multichannel_VU_meter-Manuel.pdf` | Auxiliary plugins |
| `CMGS-Keys.md` | The keyboard keys of all the plugins |
| `CMGS-Internals.fodt` | Internal documentation (in progress) |

## Repository layout

| Path | Contents |
|---|---|
| `CMGS-effects/` | The plugins (`.jsfx`) and `README.txt`, a marker the Game Master looks for. `CMGS-libs/` holds the shared libraries and the code of the large plugins (`.jsfx-inc`). |
| `CMGS-data/` | What the plugins read at run time: `themes/` (the bitmap themes), `Diffusions/` (configurations read by Diffusion-3). |
| `CMGS-auxiliary.eel` | The auxiliary ReaScript (generated, see above). |
| `CMGS-scripts/` | mSL scripts: algorithms and presets for Interstys, examples, test series. |
| `CMGS-docs/` | The manuals. |
| `CMGS-aux/` | Development tools (Python) and archives. |

## Credits

CMGS is written by **Jean-Jacques Girardot**, with the invaluable help of **Jean-François Minjard**.
The UI library `ui-lib.jsfx-inc` and the original *SmoothMultiLimiter* are by **Geraint Luff**.

---

# Version française

Le **Concrete Music Gran Studio**, ou **CMGS**, est un ensemble d'outils pour les compositeurs de musique concrète et
électroacoustique : un échantillonneur couplé à un générateur de musique, un système de spatialisation multicanal, un
délai modulaire, et les plugins auxiliaires dont ils ont besoin en studio, en concert ou en installation.

CMGS est écrit en **JSFX**, le langage de plugins de [REAPER](https://www.reaper.fm) : il ne fonctionne donc que dans
REAPER, version **7.25 ou ultérieure**.

## Les applications

| Application | Plugins | Rôle |
|---|---|---|
| **Game Master** | `GamePlayer`, avec `FilePlayer`, `ScriptMaster`, `MIDI_In`, `MIDIduino` | Échantillonneur et générateur de musique électroacoustique : lecteurs de clips, générateur, ordonnanceur, contrôle en direct. `FilePlayer` est un lecteur d'échantillons piloté par le Game Master, `ScriptMaster` un éditeur, débogueur et exécuteur de scripts, `MIDI_In` et `MIDIduino` font entrer le MIDI et les capteurs dans le Game Master. |
| **Diffusion-3** | `Diffusion-3` | Spatialisation jusqu'à 128 entrées et sorties : projecteurs, scènes, morphing, trajectoires 3D, configurations des haut-parleurs, contrôle par un AKAI APCmini. |
| **Interstys** | `Interstys` | Délai fractionnaire modulaire : lignes, lecteurs (Stretch, Grains…), écrivains, effets (filtres, saturation, matrice de réinjection, flanger, phaser, shimmer, bruit, aléatoire…), courbes, liens MIDI. |

Ces applications partagent **mSL**, un petit langage de script : les scripts les pilotent, échangent des messages, et
décrivent leurs configurations, leurs patchs et leurs presets. Des scripts prêts à l'emploi se trouvent dans
[`CMGS-scripts/`](CMGS-scripts/README.md).

### Plugins auxiliaires

- `MCBM-64`, `MCBM-128` : gestionnaires de basses multicanaux, jusqu'à 128 canaux (`MCBM-128` : filtres de
  Linkwitz-Riley).
- `SmoothMultiLimiter` : un limiteur jusqu'à 128 canaux.
- `Multichannel_VU_meter` (et sa variante `Multichannel_VU_meter_U`) : un VU-mètre jusqu'à 128 canaux.
- Petits utilitaires : `ChannelReducer16/24/48`, `CheapChannelReducer`, `ChannelsMuter`, `ChannelsSwitcher`,
  `mid-side`, `channels-folder`, `Synchronizer`.
- Exemples : `AKAI-Ex-01`, `AKAI-Ex-02` (AKAI APCmini), `Space3D-Demo` (la vue 3D de Diffusion-3).

## Installation

1. Installez **REAPER** 7.25 ou ultérieur (<https://www.reaper.fm/download.php>), et vérifiez qu'il reconnaît votre
   carte son (*Options > Préférences… > Audio > Périphérique*).

   > [!IMPORTANT]
   > Certains réglages arrêtent le Game Master. Dans *Options > Préférences… > Audio*, les deux options *Fermer le
   > périphérique audio à l'arrêt…* ne doivent **pas** être cochées, et dans *Audio > Lecture*, *Exécuter les effets
   > à l'arrêt* doit être cochée.

2. Récupérez CMGS : sur <https://github.com/jack461/CMGS>, cliquez sur le bouton vert **Code**, puis sur
   **Download ZIP**, et décompressez `CMGS-main.zip` où vous voulez (ou faites un `git clone` du dépôt). Ne placez
   pas ce dossier lui-même dans le dossier des ressources de REAPER.

3. Ouvrez le dossier des ressources de REAPER (*Options > Afficher le chemin des ressources de REAPER dans
   l'explorateur/le Finder*), et copiez-y :

   | Depuis le dossier de CMGS | Vers le dossier des ressources de REAPER |
   |---|---|
   | `CMGS-effects/` | `Effects/CMGS-effects/` |
   | `CMGS-data/` | `Data/CMGS-data/` |
   | `CMGS-auxiliary.eel` | `Scripts/CMGS-auxiliary.eel` |

   Gardez ces noms : les plugins cherchent ces dossiers, et les projets REAPER désignent les plugins par
   `CMGS-effects/<plugin>.jsfx`.

4. Chargez le script auxiliaire : *Actions > Afficher la liste des actions… > Nouvelle action > Charger un
   ReaScript…*, choisissez `Scripts/CMGS-auxiliary.eel`, puis lancez cette action une fois à chaque session de
   REAPER. Il reste en tâche de fond et permet aux plugins d'écrire des fichiers (par exemple l'export du journal
   système avec la touche `p`, ou les patchs et sessions exportés par Interstys), de connaître le dossier du projet,
   et de piloter le transport de REAPER depuis les scripts.

5. Facultatif : copiez aussi `CMGS-scripts/` dans `Data/` (à côté de `CMGS-data`) ; les plugins peuvent alors ouvrir
   un script par un nom comme `CMGS-scripts/Algorithms/Matrix-Metal.mSL`.

Les plugins apparaissent alors dans le navigateur d'effets de REAPER, sous *JS*, dans le dossier `CMGS-effects`.

**Mise à jour :** remplacez `Effects/CMGS-effects`, `Data/CMGS-data` et `Scripts/CMGS-auxiliary.eel` par les
nouvelles versions. Vos projets continuent de fonctionner : ils désignent les plugins par leur nom.

**Pour les développeurs :** au lieu de copier, vous pouvez créer des liens symboliques du dossier des ressources de
REAPER vers un clone du dépôt (`ln -s` sous macOS et Linux, `mklink /D` sous Windows) ; REAPER voit alors chaque
modification des sources. Les alias du Finder de macOS ne fonctionnent pas. `CMGS-auxiliary.eel` est généré :
modifiez `CMGS-effects/CMGS-libs/CMGS-auxiliary-src.eel`, puis lancez
`python3 -I CMGS-aux/tools/make_auxiliary.py`.

Un premier tutoriel, un projet complet avec environ 1 Go d'échantillons, est disponible sur
<https://github.com/jack461/CMGS-Tutorials>.

## Documentation

Les manuels se trouvent dans [`CMGS-docs/`](CMGS-docs/) et sont écrits en français (les fichiers `.fodt` en sont les
sources LibreOffice).

| Fichier | Contenu |
|---|---|
| `CMGS-Manuel.pdf` | Manuel général : présentation de CMGS, installation, l'interface commune, le langage mSL (avec une initiation à la programmation), la liste de tous les codes d'erreur |
| `GameMaster-Manuel.pdf` | Le Game Master (ce qui lui est propre ; le reste est dans le manuel général) |
| `GameMaster-Doc-1.7.8.pdf` | L'ancien manuel complet du Game Master (version 1.7.8, 2024) |
| `GM-Commandes.pdf` | Les commandes du Game Master |
| `Diffusion-3-Manuel.pdf` | Diffusion-3 |
| `Interstys-Manuel.pdf` | Interstys |
| `MCBM-Manuel.pdf`, `SmoothMultiLimiter-Manuel.pdf`, `Multichannel_VU_meter-Manuel.pdf` | Plugins auxiliaires |
| `CMGS-Keys.md` | Les touches du clavier de tous les plugins |
| `CMGS-Internals.fodt` | Documentation interne (en cours) |

## Organisation du dépôt

| Chemin | Contenu |
|---|---|
| `CMGS-effects/` | Les plugins (`.jsfx`) et `README.txt`, un repère que cherche le Game Master. `CMGS-libs/` contient les bibliothèques partagées et le code des gros plugins (`.jsfx-inc`). |
| `CMGS-data/` | Ce que les plugins lisent à l'exécution : `themes/` (les thèmes bitmap), `Diffusions/` (configurations lues par Diffusion-3). |
| `CMGS-auxiliary.eel` | Le ReaScript auxiliaire (généré, voir plus haut). |
| `CMGS-scripts/` | Scripts mSL : algorithmes et presets pour Interstys, exemples, séries de tests. |
| `CMGS-docs/` | Les manuels. |
| `CMGS-aux/` | Outils de développement (Python) et archives. |

## Crédits

CMGS est écrit par **Jean-Jacques Girardot**, avec l'aide précieuse de **Jean-François Minjard**.
La bibliothèque d'interface `ui-lib.jsfx-inc` et le *SmoothMultiLimiter* original sont de **Geraint Luff**.
