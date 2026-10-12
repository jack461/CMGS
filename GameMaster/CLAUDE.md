# CLAUDE.md

This file gives Claude Code guidance for working in this repository.

## What this is

The **Game Master** is the code of **CMGS** ("Concrete Music Gran Studio"), an electroacoustic music generator and sampler for concrete-music composers, written by Jean-Jacques Girardot. All code is **JSFX** (REAPER's EEL2-based plugin language), so it only runs inside **REAPER ≥ 7.25**. The user manual is `../GameMaster-Doc-1.7.8.pdf` and the command reference is `../GM-Commandes.pdf`. The current version is set in `GM-Libs/GamePlayer.jsfx-inc` (`GameMasterVersion = ui_version(1,7,9)`).

The git repo root is the parent directory `CMGS/` (GitHub: jack461/CMGS). This `GameMaster/` folder sits in REAPER's `Effects/` directory, so REAPER picks up edits directly.

## Build / run / test

- There is no build step and no test suite. To test a change, open a REAPER project that uses the plugin and recompile it: open the JSFX editor and save, or remove and re-add the FX. Compile errors appear in REAPER's JSFX editor or FX window.
- You can't run JSFX from the command line. Check changes by reading the code carefully, then ask the user to try them in REAPER.
- `GM-Libs/mkDistrib.sh` and `GM-Libs/mkConfigs.sh` are old packaging scripts. They refer to files that no longer exist (`GamePlayer_A.jsfx`, `mSL_Xlib.jsfx-inc`, …), so don't rely on them.

## Layout

- Top level `*.jsfx`: the plugins. Most are thin shells that hold only `desc:`, sliders, `options:` and imports. Their real code is in a matching `GM-Libs/<Name>.jsfx-inc`.
- `GM-Libs/`: the shared libraries, the large plugin bodies, theme PNGs (`GM-Libs/themes/`) and a few small utility plugins.
- `GMAuxiliary.eel`: a ReaScript (EEL) helper that talks to the plugins through shared memory.

### Main plugins

| Plugin | Body | Role |
|---|---|---|
| `GamePlayer.jsfx` | `GM-Libs/GamePlayer.jsfx-inc` (~28k lines) | The Game Master itself: clip player, generator, scheduler, UI, mSL host |
| `FilePlayer.jsfx` | `GM-Libs/FilePlayer.jsfx-inc` | Sample/file reader that the Game Master drives |
| `ScriptMaster.jsfx` | `GM-Libs/ScriptMaster.jsfx-inc` | mSL script editor, debugger and runner (disassembler, memory debugger) |
| `Diffusion-3.jsfx` | `GM-Libs/Diffusion-3*.jsfx-inc` | Spatialization of up to 128 in/out channels: projectors, scenes, morphing, XML configs, AKAI APCmini control |
| `Interstys.jsfx` | `GM-Libs/Interstys.jsfx-inc` | Modular fractional delay: lines, readers, writers, effects |
| `MIDI_In.jsfx`, `MIDIduino.jsfx` | `GM-Libs/MIDI_In.jsfx-inc` | MIDI/sensor input into the Game Master |

The small DSP utilities (`ChannelReducer*`, `ChannelsMuter`, `ChannelsSwitcher`, `Mixer_8xM-1xS`, `MCBM-64` bass manager, `SmoothMultiLimiter`, `Multichannel_VU_meter`, `mid-side`, `channels-folder`, `Synchronizer`) stand alone or use only the UI libs. `AKAI-Ex-*.jsfx` are APCmini examples. `TestMaster.jsfx` is a scratch file for trying out the preprocessor.

### mSL: the micro Script Language

The Game Master embeds its own scripting language, **mSL**, implemented in JSFX:
- `mSL_Constants`: symbol encodings, markers, and special values (`Undef`, `Default`, …).
- `mSL_Comp_lib`: the compiler. It requires `mSL_Utilities` to be imported first.
- `mSL_Evaluator`: the interpreter. `mSL_Threads`, `mSL_Events` and `mSL_Scheduler` provide threads, events and timed tasks. `mSL_Garbage_Collector` handles memory reclamation.
- `mSL_Extend`: extra opcodes. `mSL_128`…`mSL_255` can be redefined here. It must come after `mSL_Comp_lib`.
- `mSL_GM_Vars_Access` / `mSL_FR_Vars_Access`: variable-access tables for the Game Master vs. the readers, ScriptMaster and Diffusion.
- `mSL_DeAsm`, `mSL_Dbg_Memory`: disassembler and memory inspector.
- Memory: `mSL_StM_Memory` (static blocks framed by type/size headers) and `mSL_Dyn_Memory` (dynamic allocation).
- `mSL_string_list_*`: they only pre-declare thousands of named `#str…` string slots, because JSFX needs string variables to exist at compile time. Don't edit them by hand.

### UI libraries

`ui-lib.jsfx-inc` is Geraint Luff's JSFX UI library (`ui-lib_d` is a variant of it). The `mSL_ui_LibJJ`, `mSL_ui_Menus`, `mSL_ui_Pads`, `ui-lib-JJ-GUI` and `*Colors*` files are the author's extensions to it.

## Cross-plugin conventions

- **Shared memory:** the cooperating plugins declare `options:gmem=GM_SHM`. `GM-Libs/mSL_clip_map.jsfx-inc` defines the named `gmem[]` slot layout (versions, time, player counters, logs, …). Any change there must stay compatible with `GMAuxiliary.eel`, which includes the same file, and with every plugin that imports it.
- **Import order matters.** JSFX `import`/`include` order sets which functions and variables are defined first. Copy the order of an existing plugin; GamePlayer and ScriptMaster are the reference chains.
- **Two include styles:** older plugins use `import GM-Libs/X.jsfx-inc`. Newer ones (Diffusion-3, Interstys) use the preprocessor form `<? include("GM-Libs/X.jsfx-inc"); ?>` and generate sliders and constants with `<? … printf(…) ?>` blocks. Capacities such as `PRJ_CNT`, `INP_CNT`, `RD_CNT` and `CH_NB` are preprocessor variables set at the top of the shell `.jsfx`.
- **Preprocessor flags:** `no_init` plus `_suppress` keep a library's `@init` header from being emitted twice. Some libs open with `<? no_init != 0 ? _suppress=1; ?>`. `in_eel` marks inclusion from the `.eel` script, and `no_mslog` turns off logging code.
- `options:maxmem` is tuned per plugin. Increase it if a change allocates more memory.
- Sections are `@init`, `@slider`, `@block`, `@sample`, `@serialize` and `@gfx`. In the big `.jsfx-inc` bodies these sections are far apart; search for `^@` to find them.

## Style

- Comments and identifiers mix **French and English**. Match the language of the surrounding code.
- Code is EEL2: everything is a double, memory is the flat `mem[]`/`gmem[]` space, functions use `local(...)` and `instance(...)`, and strings are `#name` or numeric string slots. Four-character constants such as `'Game'` are used as tags and keys.
- `The_Obsolete.jsfx-inc`, `unused.jsfx-inc` and `ZZZ.jsfx-inc` are archives or debug snippets. No plugin imports them.
