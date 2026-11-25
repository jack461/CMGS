# CMGS scripts (mSL)

*Français plus bas.*

Scripts in **mSL**, the scripting language embedded in the CMGS applications (GamePlayer, Espaces, Interstys,
ScriptMaster, FilePlayer). The applications do not need them: they are recipes, presets, examples and tests.

**Running a script:** drop the `.mSL` file into the window of the plugin (GamePlayer: with Alt, or in the top band;
the other plugins: anywhere in the window). Its messages go to the system log of the plugin.

**Option:** this folder may also be copied (or linked) into the `Data` folder of REAPER, next to `CMGS-data`. A plugin
can then open a script by a name relative to `Data`, for instance `CMGS-scripts/Algorithms/Matrix-Metal.mSL`.

| Folder | Contents |
|---|---|
| `Algorithms/` | Interstys: ready-to-use creative recipes (Matrix, Flanger, Chorus, Phaser, Shimmer, Noise, Random, Math, Ring), each with its parameters on its `Instance` line; `Sources.mSL` gives test material. See its README (in French). |
| `Presets/` | Interstys: five generation presets (mSL conductors that transform an input buffer into about ten minutes of sound). See its README (in French). |
| `Examples/` | Interstys: small examples (a chain of effects, curves, MIDI links of an AKAI MIDI Mix, the dump and removal of the MIDI links, the check of an exported session). |
| `Tests/` | The test series `Ex-NNNN.mSL` and `check_scripts.py` (below). |

## Tests

The scripts "Ex-NNNN.mSL" announce their expected output with lines such as
`// Expected "Ex-0001. s vaut 55"` (sprintf formats like `%d` or `%.2f` are allowed) or
`// Expected error 1629` (`// Allowed error 0621` : an error that may appear or not, never a failure).
After running them in a plug-in, export the system log to a file
('p'), then check it with:

    python3 -I CMGS-scripts/Tests/check_scripts.py [log file | project folder] [-a]

(by default, the most recent "syslog-*.txt" of ~/Music/REAPER-Projects/*/).

Numbering of the scripts:

    Ex-0NNN   generic tests of the language : they must run correctly in every plugin
    Ex-1NNN   functions or structures specific to Interstys
    Ex-2NNN   specific to GamePlayer
    Ex-3NNN   specific to Espaces

check_scripts.py takes the plugin from the name of the log ("syslog-Interstys-..."): it ignores the
specific scripts of the other plugins, and reports one run in the wrong plugin as a failure.

The table of the keyboard keys of the plugins is now made by `CMGS-aux/tools/keys_table.py`
(it writes `CMGS-docs/CMGS-Keys.md`).

---

# Scripts de CMGS (mSL)

Des scripts en **mSL**, le langage de script intégré aux applications de CMGS (GamePlayer, Espaces, Interstys,
ScriptMaster, FilePlayer). Les applications n'en ont pas besoin : ce sont des recettes, des presets, des exemples et
des tests.

**Lancer un script :** déposer le fichier `.mSL` dans la fenêtre du plugin (GamePlayer : avec Alt, ou dans le bandeau
du haut ; les autres plugins : n'importe où dans la fenêtre). Ses messages vont dans le journal système du plugin.

**Option :** ce dossier peut aussi être copié (ou lié) dans le dossier `Data` de REAPER, à côté de `CMGS-data`. Un
plugin peut alors ouvrir un script par un nom relatif à `Data`, par exemple `CMGS-scripts/Algorithms/Matrix-Metal.mSL`.

| Dossier | Contenu |
|---|---|
| `Algorithms/` | Interstys : des recettes de création prêtes à l'emploi (Matrix, Flanger, Chorus, Phaser, Shimmer, Noise, Random, Math, Ring), chacune avec ses paramètres sur sa ligne `Instance` ; `Sources.mSL` fournit du matériau d'essai. Voir son README. |
| `Presets/` | Interstys : cinq presets de génération (des chefs d'orchestre en mSL qui transforment un buffer d'entrée en une dizaine de minutes de son). Voir son README. |
| `Examples/` | Interstys : de petits exemples (une chaîne d'effets, des courbes, les liens MIDI d'une MIDI Mix d'AKAI, l'affichage et le retrait des liens MIDI, la vérification d'une session exportée). |
| `Tests/` | La série de tests `Ex-NNNN.mSL` et `check_scripts.py` (voir *Tests* plus haut). |
