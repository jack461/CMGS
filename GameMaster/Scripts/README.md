
# mSL Scripts

This directory contains a few "mSL" scripts that may be used to test the mSL byte code compiler/interpreter included in "GameMaster", "Diffusion-3" or "Interstys".

The scripts "Ex-NNNN.mSL" announce their expected output with lines such as
`// Expected "Ex-0001. s vaut 55"` (sprintf formats like `%d` or `%.2f` are allowed) or
`// Expected error 1629`. After running them in a plug-in, export the system log to a file
('p'), then check it with:

    python3 check_scripts.py [log file | project folder] [-a]

(by default, the most recent "syslog-*.txt" of ~/Music/REAPER-Projects/*/).

Numbering of the scripts:

    Ex-0NNN   generic tests of the language : they must run correctly in every plugin
    Ex-1NNN   functions or structures specific to Interstys
    Ex-2NNN   specific to GamePlayer
    Ex-3NNN   specific to Diffusion-3

check_scripts.py takes the plugin from the name of the log ("syslog-Interstys-..."): it ignores the
specific scripts of the other plugins, and reports one run in the wrong plugin as a failure.

## Keyboard keys table

    python3 -I keys_table.py [-raw] [-o output.md]

lists the keys used by the `@gfx` code of the plugins (GamePlayer, FilePlayer, ScriptMaster, Diffusion-3,
Interstys), per plugin and per level, in the order the levels see the key (the same scheme everywhere, see
`GM-Libs/mSL_ui_LibJJ.jsfx-inc`, Keyboard: module, pane, tab, plugin, system, Studio pad). It reports the
branches never reached and the commands masked over a module that uses the same key, and compares the
commands of the plugins. The levels of the handlers are declared in `HANDLERS` at the top of the script:
add a line there for a new keyboard handler. By default it writes `../Documents/CMGS-Keys.md` (in `CMGS/`);
`-raw` prints one line per key test.
