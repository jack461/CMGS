# Touches du clavier dans CMGS

*Fichier produit par `Scripts/keys_table.py` : ne pas le modifier à la main, relancer le script.*

Pour chaque plugin, les touches testées par le code `@gfx`, par niveau dans l'ordre où les niveaux voient la touche pendant une trame. « Modif. » : les modificateurs testés sur la même ligne (vide : non testés, la touche agit avec ou sans modificateur ; « none » : sans modificateur). L'action est le début du code exécuté. Les bibliothèques partagées (mSL_Dbg_Memory…) apparaissent dans chaque plugin qui les inclut.

## Conflits

### GamePlayer

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (13)

- `$` : commandes d'onglet (GamePlayer.jsfx-inc:18748), pas au-dessus de : Scripts / Settings
- `Backspace` : commandes d'onglet (GamePlayer.jsfx-inc:18773), pas au-dessus de : Scripts / Settings
- `Shift+Left` : largeur des colonnes (GamePlayer.jsfx-inc:27088), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (GamePlayer.jsfx-inc:27060), pas au-dessus de : mémoire (débogueur)
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de Banks : `g`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de Clips selection : `a` `c` `d` `e` `f` `g` `h` `i` `j` `k` `l` `m` `q` `r` `s` `t` `u` `v` `w` `x` `y` `z`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de LED interactive : `x`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de Play control : `a` `c` `g` `r` `s`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de Scripts / Settings : `a` `c` `d` `e` `f` `g` `h` `i` `j` `k` `l` `m` `q` `r` `s` `t` `u` `w` `x` `z`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de Units : `a` `c` `d` `e` `f` `g` `h` `i` `j` `k` `l` `m` `q` `r` `s` `t` `u` `v` `w` `z`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de log système / log utilisateur : `j` `k` `l` `m` `t` `v` `z`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de mémoire (débogueur) : `c` `g` `j` `k` `l` `m` `x`
- pad Studio : jeu au clavier (aussi au survol du pad) (GamePlayer.jsfx-inc), pas au-dessus de paramètres dynamiques : `a` `c` `f` `i` `m` `q` `r` `s` `t` `v` `x` `z`

### FilePlayer

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (9)

- `Shift+Left` : largeur des colonnes (mSL_Panes.jsfx-inc:791), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (mSL_Panes.jsfx-inc:763), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `s` : commandes système (mSL_System_Keys.jsfx-inc:37), pas au-dessus de : File Player Status
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : log système

### ScriptMaster

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (8)

- `Shift+Left` : largeur des colonnes (mSL_Panes.jsfx-inc:791), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (mSL_Panes.jsfx-inc:763), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : log système

### Diffusion-3

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (8)

- `Shift+Left` : largeur des colonnes (mSL_Panes.jsfx-inc:791), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (mSL_Panes.jsfx-inc:763), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : log système

### Interstys

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (10)

- `Shift+Left` : largeur des colonnes (Interstys.jsfx-inc:17605), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (Interstys.jsfx-inc:17577), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `r` : commandes système (mSL_System_Keys.jsfx-inc:30), pas au-dessus de : Reader
- `s` : commandes système (mSL_System_Keys.jsfx-inc:37), pas au-dessus de : ?
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : Reader, log système

## Commandes des plugins : comparaison

Les commandes du plugin (do_Plugin_Keys : Tab, affichages) et les commandes système (do_System_Keys, communes à FilePlayer, ScriptMaster, Diffusion-3 et Interstys). Majuscules pour les affichages, minuscules pour les commandes. GamePlayer : ses commandes de concert sont au niveau de l'onglet, et ses raccourcis sont définis par l'utilisateur.

| Touche | FilePlayer | ScriptMaster | Diffusion-3 | Interstys |
|---|---|---|---|---|
| `c` | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; |
| `g` | gc_run(2); | gc_run(2); | gc_run(2); | gc_run(2); |
| `k` | mSL_kill_all_thread(); | mSL_kill_all_thread(); | mSL_kill_all_thread(); | mSL_kill_all_thread(); |
| `l` | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) /  | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) /  | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) /  | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) /  |
| `m` | mem_walk(0); mem_show(); | mem_walk(0); mem_show(); | mem_walk(0); mem_show(); | mem_walk(0); mem_show(); |
| `n` | mem_walk(8); mem_show(); | mem_walk(8); mem_show(); | mem_walk(8); mem_show(); | mem_walk(8); mem_show(); |
| `o` | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test =  | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test =  | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test =  | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test =  |
| `r` | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNon | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNon | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNon | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNon |
| `S` |  |  | togglesliders(-1); | (gui_show_sliders = gui_show_sliders ? 0 : 1) ? ( |
| `s` | mSL_run_test = 0; | mSL_run_test = 0; | mSL_run_test = 0; | mSL_run_test = 0; |
| `t` | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = |
| `Tab` | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui_jtab_step(uix_jG_menuscr, -1); 1 |
| `U` |  |  |  | gui_show_UI = gui_show_UI ? 0 : 1; |

## GamePlayer

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris (puis ses pads) → panneau → commandes d'onglet (do_Generic_Commands) → raccourcis de l'utilisateur (do_Plugin_Keys) → pad Studio, s'il est affiché (do_StudioPadKeyboard) ; pendant l'apprentissage d'un raccourci, la touche va d'abord à celui-ci.

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:108 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:110 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `?` |  | module | ? (clDirResolve) | str_setchar(#clDirW, n-1, F_SEP, 'cu') | GamePlayer.jsfx-inc:404 |
| `g` |  | module | Banks (doBanksInteract) | GM_key_take('g'); | GamePlayer.jsfx-inc:22629 |
| `g` |  | module | Banks (doBanksInteract) | BnkGrpLock(); | GamePlayer.jsfx-inc:22630 |
| `Ctrl+C` |  | module | Clips selection (show_Clips_Selection) | i = curB; loop(100,  // ^C | GamePlayer.jsfx-inc:21319 |
| `Enter` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21204 |
| `Enter` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21254 |
| `Ctrl+Z` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? ( | GamePlayer.jsfx-inc:21327 |
| `Space` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21204 |
| `Space` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21254 |
| `!` |  | module | Clips selection (show_Clips_Selection) | gmem[clClAlias+xcell] = 0;  // remove the alias and clear the entry | GamePlayer.jsfx-inc:21221 |
| `%` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs - 1 + showStates) % showStates ; | GamePlayer.jsfx-inc:21287 |
| `+` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? (  // validate/unvalidate all entries | GamePlayer.jsfx-inc:21274 |
| `/` |  | module | Clips selection (show_Clips_Selection) | i = curB; loop(100,  // clear all entries | GamePlayer.jsfx-inc:21266 |
| `0..9` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 1 | GamePlayer.jsfx-inc:21208 |
| `0..9` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 0 - 9 | GamePlayer.jsfx-inc:21258 |
| `:` |  | module | Clips selection (show_Clips_Selection) | gmem[clInfStart+xcell] = 0;  // clear the entry | GamePlayer.jsfx-inc:21216 |
| `=` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? (  // (un)validate the entry | GamePlayer.jsfx-inc:21227 |
| `A..Z` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 10 - N | GamePlayer.jsfx-inc:21262 |
| `a..z` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 10 - N | GamePlayer.jsfx-inc:21212 |
| `0xA0` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // alt+' '  => play | GamePlayer.jsfx-inc:21298 |
| `Up` | none | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 1) % 10; | GamePlayer.jsfx-inc:21085 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 100 - 10) % 100; | GamePlayer.jsfx-inc:21243 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs + 1) % showStates ; | GamePlayer.jsfx-inc:21290 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 1) % 10; | GamePlayer.jsfx-inc:21311 |
| `Down` | none | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 10 - 1) % 10; | GamePlayer.jsfx-inc:21082 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 10) % 100; | GamePlayer.jsfx-inc:21240 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs - 1 + showStates) % showStates ; | GamePlayer.jsfx-inc:21287 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 10 - 1) % 10; | GamePlayer.jsfx-inc:21308 |
| `Home` | none | module | Clips selection (show_Clips_Selection) | slBankset = slGroupNum = 0; | GamePlayer.jsfx-inc:21088 |
| `Home` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB; | GamePlayer.jsfx-inc:21246 |
| `Left` | none | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 10 - 1) % 10; | GamePlayer.jsfx-inc:21079 |
| `Left` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 100 - 1) % 100; | GamePlayer.jsfx-inc:21237 |
| `Left` |  | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 10 - 1) % 10; | GamePlayer.jsfx-inc:21305 |
| `Right` | none | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 1) % 10; | GamePlayer.jsfx-inc:21076 |
| `Right` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 1) % 100; | GamePlayer.jsfx-inc:21234 |
| `Right` |  | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 1) % 10; | GamePlayer.jsfx-inc:21302 |
| `Up` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + readerCount - 8) % readerCount; | GamePlayer.jsfx-inc:19860 |
| `Down` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + 8) % readerCount; | GamePlayer.jsfx-inc:19854 |
| `Left` | none | module | Generator (show_Generator) | unitbkl[0] = (unitbkl[0] - 1 + 4) % 4; | GamePlayer.jsfx-inc:19846 |
| `Left` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + readerCount - 1) % readerCount; | GamePlayer.jsfx-inc:19857 |
| `Right` | none | module | Generator (show_Generator) | unitbkl[0] = (unitbkl[0] + 1) % 4; | GamePlayer.jsfx-inc:19843 |
| `Right` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + 1) % readerCount; | GamePlayer.jsfx-inc:19851 |
| `x` |  | module | LED interactive (show_jled) | led[ui_jled_status] = led[ui_jled_status] > 0.5 ? 0 : 1; | mSL_ui_Pads.jsfx-inc:118 |
| `*` |  | module | Play control (show_Play_Control) | // very slow stop all... | GamePlayer.jsfx-inc:25943 |
| `a` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypAnyClip | GamePlayer.jsfx-inc:25940 |
| `b` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypBank | GamePlayer.jsfx-inc:25939 |
| `c` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypClip | GamePlayer.jsfx-inc:25934 |
| `g` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypGroup | GamePlayer.jsfx-inc:25938 |
| `p` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypPartial | GamePlayer.jsfx-inc:25937 |
| `r` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypRange | GamePlayer.jsfx-inc:25936 |
| `s` |  | module | Play control (show_Play_Control) | GvPlayTyp = 0 | GamePlayer.jsfx-inc:25935 |
| `Left` |  | module | Play control (show_Play_Control) | GvPlayTyp = (GvPlayTyp + menuActModeCnt - 1) % menuActModeCnt | GamePlayer.jsfx-inc:25941 |
| `Right` |  | module | Play control (show_Play_Control) | GvPlayTyp = (GvPlayTyp + 1) % menuActModeCnt | GamePlayer.jsfx-inc:25942 |
| `Backspace` |  | module | Scripts / Settings (show_Scripts) | (v !== 0\|v) ? (  // backspace | GamePlayer.jsfx-inc:23144 |
| `$` |  | module | Scripts / Settings (show_Scripts) | ssnd = 1; | GamePlayer.jsfx-inc:23163 |
| `+` |  | module | Scripts / Settings (show_Scripts) | v = v + 1; | GamePlayer.jsfx-inc:23132 |
| `-` |  | module | Scripts / Settings (show_Scripts) | v = v + u - 1; | GamePlayer.jsfx-inc:23135 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23110 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23114 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | // goto marker "n" | GamePlayer.jsfx-inc:24198 |
| `=` |  | module | Scripts / Settings (show_Scripts) | v = v + 1; | GamePlayer.jsfx-inc:23132 |
| `A..F` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23122 |
| `X` |  | module | Scripts / Settings (show_Scripts) | padSettingC7fmt = padSettingC7fmt === 0; | GamePlayer.jsfx-inc:23129 |
| `Z` |  | module | Scripts / Settings (show_Scripts) | v = 0; | GamePlayer.jsfx-inc:23126 |
| `_` |  | module | Scripts / Settings (show_Scripts) | v = v + u - 1; | GamePlayer.jsfx-inc:23135 |
| `a..f` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23118 |
| `a` |  | module | Scripts / Settings (show_Scripts) | parSet(p_GvAutoMd, ! paramValues[p_GvAutoMd]); | GamePlayer.jsfx-inc:24140 |
| `e` |  | module | Scripts / Settings (show_Scripts) | playSkipSlnc = ! playSkipSlnc ; | GamePlayer.jsfx-inc:24195 |
| `g` |  | module | Scripts / Settings (show_Scripts) | recOptMarkReplay = ! recOptMarkReplay ; | GamePlayer.jsfx-inc:24160 |
| `h` |  | module | Scripts / Settings (show_Scripts) | setRModeStop(); | GamePlayer.jsfx-inc:24180 |
| `i` |  | module | Scripts / Settings (show_Scripts) | // invert read direction | GamePlayer.jsfx-inc:24163 |
| `j` |  | module | Scripts / Settings (show_Scripts) | playJmpLoop = ! playJmpLoop ; | GamePlayer.jsfx-inc:24154 |
| `k` |  | module | Scripts / Settings (show_Scripts) | playAndLock ? SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:24146 |
| `l` |  | module | Scripts / Settings (show_Scripts) | playRepeatMd = ! playRepeatMd ; | GamePlayer.jsfx-inc:24157 |
| `m` |  | module | Scripts / Settings (show_Scripts) | replayUnMute = ! replayUnMute; | GamePlayer.jsfx-inc:24184 |
| `o` |  | module | Scripts / Settings (show_Scripts) | recOptLockSnds = ! recOptLockSnds; | GamePlayer.jsfx-inc:24187 |
| `p` |  | module | Scripts / Settings (show_Scripts) | setPModeSwitch(); | GamePlayer.jsfx-inc:24133 |
| `q` |  | module | Scripts / Settings (show_Scripts) | playReeval = 1; | GamePlayer.jsfx-inc:24136 |
| `r` |  | module | Scripts / Settings (show_Scripts) | setRModeSwitch(); | GamePlayer.jsfx-inc:24143 |
| `s` |  | module | Scripts / Settings (show_Scripts) | playModeStep = ! playModeStep ; | GamePlayer.jsfx-inc:24173 |
| `t` |  | module | Scripts / Settings (show_Scripts) | recOptRecReplay = ! recOptRecReplay ; | GamePlayer.jsfx-inc:24177 |
| `u` |  | module | Scripts / Settings (show_Scripts) | playAndUnLock = ! playAndUnLock ; | GamePlayer.jsfx-inc:24150 |
| `w` |  | module | Scripts / Settings (show_Scripts) | // various play speed | GamePlayer.jsfx-inc:24168 |
| `x` |  | module | Scripts / Settings (show_Scripts) | padSettingC7fmt = padSettingC7fmt === 0; | GamePlayer.jsfx-inc:23129 |
| `z` |  | module | Scripts / Settings (show_Scripts) | v = 0; | GamePlayer.jsfx-inc:23126 |
| `z` |  | module | Scripts / Settings (show_Scripts) | parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:24190 |
| `Up` |  | module | Scripts / Settings (show_Scripts) | Settings_F_Sel = (Settings_F_Sel - 1 + FlagsCount) % FlagsCount; | GamePlayer.jsfx-inc:23160 |
| `Up` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? 10 : (jmc === 0x04) ? 60 : (jmc === 0x10) ? 300 : (jmc === 0x14) ? 1800 : 0; | GamePlayer.jsfx-inc:24209 |
| `Down` |  | module | Scripts / Settings (show_Scripts) | Settings_F_Sel = (Settings_F_Sel + 1) % FlagsCount; | GamePlayer.jsfx-inc:23157 |
| `Down` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? -10 : (jmc === 0x04) ? -60 : (jmc === 0x10) ? -300 : (jmc === 0x14) ? -1800 : 0; | GamePlayer.jsfx-inc:24212 |
| `Left` | none | module | Scripts / Settings (show_Scripts) | v = (padSettingC7fmt === 0) ? v << 4 : v * 10; | GamePlayer.jsfx-inc:23138 |
| `Left` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? -1 : (jmc === 0x04) ? -0.1 : (jmc === 0x10) ? -0.01 : (jmc === 0x14) ? -0.001 : 0; | GamePlayer.jsfx-inc:24203 |
| `Right` | none | module | Scripts / Settings (show_Scripts) | v = (padSettingC7fmt === 0) ? v >> 4 : (v / 10); | GamePlayer.jsfx-inc:23141 |
| `Right` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? 1 : (jmc === 0x04) ? 0.1 : (jmc === 0x10) ? 0.01 : (jmc === 0x14) ? 0.001 : 0; | GamePlayer.jsfx-inc:24206 |
| `+` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += 1; | GamePlayer.jsfx-inc:20207 |
| `-` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += MIDI_States_siz - 1; | GamePlayer.jsfx-inc:20210 |
| `0..9` |  | module | Sensors (show_Sensors) | GM_key_take(zzch); | GamePlayer.jsfx-inc:20213 |
| `2` |  | module | Sensors (show_Sensors) | setSensorSize(zzch) | GamePlayer.jsfx-inc:20269 |
| `3` |  | module | Sensors (show_Sensors) | setSensorSize(zzch) | GamePlayer.jsfx-inc:20269 |
| `=` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += MIDI_States_siz - 1; | GamePlayer.jsfx-inc:20210 |
| `_` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += 1; | GamePlayer.jsfx-inc:20207 |
| `!` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 2.5, 0, 0); | GamePlayer.jsfx-inc:22011 |
| `E` |  | module | Units (show_Units) | gmem[Un+RCB_State_Changed] \|= i_M_Rst; | GamePlayer.jsfx-inc:21986 |
| `E` |  | module | Units (show_Units) | gmem[Un+RCB_Cl_Flgs] = 1;  // also Lock entry (the key is already taken) | GamePlayer.jsfx-inc:21989 |
| `a` |  | module | Units (show_Units) | BplayerA[2] = rd; | GamePlayer.jsfx-inc:21970 |
| `b` |  | module | Units (show_Units) | BplayerB[2] = rd; | GamePlayer.jsfx-inc:21974 |
| `c` |  | module | Units (show_Units) | BplayerC[2] = rd; | GamePlayer.jsfx-inc:21978 |
| `d` |  | module | Units (show_Units) | BplayerD[2] = rd; | GamePlayer.jsfx-inc:21982 |
| `e` |  | module | Units (show_Units) | gmem[Un+RCB_State_Changed] \|= i_M_Rst; | GamePlayer.jsfx-inc:21986 |
| `f` |  | module | Units (show_Units) | SchedAddTask(5, 8, -1, -1, 1, 0, 0); | GamePlayer.jsfx-inc:21995 |
| `g` |  | module | Units (show_Units) | parSet(p_GvAutoMd, ! paramValues[p_GvAutoMd]); | GamePlayer.jsfx-inc:21967 |
| `h` |  | module | Units (show_Units) | SchedAddTask(5, 8, -1, -1, 0.20, 0, 0); | GamePlayer.jsfx-inc:21998 |
| `i` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 3.5, 0, 0); | GamePlayer.jsfx-inc:22014 |
| `j` |  | module | Units (show_Units) | Kbtp = cmdClMdBase + GvPlayTypGrLoop; | GamePlayer.jsfx-inc:22036 |
| `k` |  | module | Units (show_Units) | SchedAddTask(5, 7, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22001 |
| `l` |  | module | Units (show_Units) | SchedAddTask(5, 1\|ActFlg1, 1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21964 |
| `m` |  | module | Units (show_Units) | SchedAddTask(5, 6, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21946 |
| `n` |  | module | Units (show_Units) | lmode = ! lmode ; | GamePlayer.jsfx-inc:22017 |
| `o` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 5, 0, 0); | GamePlayer.jsfx-inc:22023 |
| `p` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 8, 0, 0); | GamePlayer.jsfx-inc:22026 |
| `q` |  | module | Units (show_Units) | qmode = ! qmode ; | GamePlayer.jsfx-inc:22020 |
| `r` |  | module | Units (show_Units) | SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22029 |
| `s` |  | module | Units (show_Units) | SchedAddTask(5, 5\|ActFlg1, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21950 |
| `t` |  | module | Units (show_Units) | SchedAddTask(5, 3, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22004 |
| `u` |  | module | Units (show_Units) | SchedAddTask(5, 1, 1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21961 |
| `v` |  | module | Units (show_Units) | gDispPlay = rd; | GamePlayer.jsfx-inc:22008 |
| `w` |  | module | Units (show_Units) | SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22033 |
| `z` |  | module | Units (show_Units) | SchedAddTask(5, 1\|ActFlg1, 3, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21958 |
| `Enter` |  | module | log système / log utilisateur (show_SysLog) | mSL_log(box, " "); | GamePlayer.jsfx-inc:20378 |
| `Space` |  | module | log système / log utilisateur (show_SysLog) | mSL_log(box, " "); | GamePlayer.jsfx-inc:20378 |
| `1` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 1; | GamePlayer.jsfx-inc:20390 |
| `2` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 2; | GamePlayer.jsfx-inc:20391 |
| `3` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 3; | GamePlayer.jsfx-inc:20392 |
| `4` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 4; | GamePlayer.jsfx-inc:20393 |
| `5` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 5; | GamePlayer.jsfx-inc:20394 |
| `6` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 6; | GamePlayer.jsfx-inc:20395 |
| `7` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 7; | GamePlayer.jsfx-inc:20396 |
| `8` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 8; | GamePlayer.jsfx-inc:20397 |
| `P` |  | module | log système / log utilisateur (show_SysLog) | sysout(SysLogBox, 31);  // the log in the console of GMAuxiliary.eel, to copy it | GamePlayer.jsfx-inc:20399 |
| `j` |  | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+1) % box[2]; | GamePlayer.jsfx-inc:20383 |
| `k` |  | module | log système / log utilisateur (show_SysLog) | box[7] = max(0, box[7]-1); | GamePlayer.jsfx-inc:20382 |
| `l` |  | module | log système / log utilisateur (show_SysLog) | box[6] = max(0, box[6]-1); | GamePlayer.jsfx-inc:20380 |
| `m` |  | module | log système / log utilisateur (show_SysLog) | box[6] = min(20, box[6]+1); | GamePlayer.jsfx-inc:20379 |
| `p` |  | module | log système / log utilisateur (show_SysLog) | sysout(SysLogBox); | GamePlayer.jsfx-inc:20398 |
| `t` |  | module | log système / log utilisateur (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | GamePlayer.jsfx-inc:20384 |
| `v` |  | module | log système / log utilisateur (show_SysLog) | ShowConfig(); | GamePlayer.jsfx-inc:20385 |
| `z` |  | module | log système / log utilisateur (show_SysLog) | box[7] = 0; | GamePlayer.jsfx-inc:20381 |
| `Up` |  | module | log système / log utilisateur (show_SysLog) | box[7] = max(0, box[7]-10); | GamePlayer.jsfx-inc:20386 |
| `Down` |  | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+10) % box[2]; | GamePlayer.jsfx-inc:20387 |
| `Left` | none | module | log système / log utilisateur (show_SysLog) | box[7] = 0; | GamePlayer.jsfx-inc:20388 |
| `Right` | none | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+100) % box[2]; | GamePlayer.jsfx-inc:20389 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:243 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:294 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:239 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:290 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:249 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:300 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:303 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:258 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:261 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:255 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:252 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:246 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:297 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:215 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:233 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:278 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:218 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:236 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:281 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:221 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:227 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:284 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:224 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:230 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:287 |
| `+` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact += max(0.1, padStGFact * 0.1); | GamePlayer.jsfx-inc:25716 |
| `-` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact = max(0, padStGFact - padStGFact * 0.1); | GamePlayer.jsfx-inc:25719 |
| `=` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact = 2; | GamePlayer.jsfx-inc:25722 |
| `+` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell + 1)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24564 |
| `+` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = (currCpMode + 1) % 3; | GamePlayer.jsfx-inc:24624 |
| `-` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24567 |
| `:` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24567 |
| `=` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell + 1)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24564 |
| `=` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = (currCpMode + 1) % 3; | GamePlayer.jsfx-inc:24624 |
| `A` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 2, 0) | GamePlayer.jsfx-inc:24409 |
| `E` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 10, 0) | GamePlayer.jsfx-inc:24411 |
| `I` |  | module | paramètres dynamiques (show_Dyn_pars) | interType = 1; | GamePlayer.jsfx-inc:24415 |
| `R` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 25, 0) | GamePlayer.jsfx-inc:24412 |
| `T` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 50, 0) | GamePlayer.jsfx-inc:24413 |
| `X` |  | module | paramètres dynamiques (show_Dyn_pars) | interType = 2; | GamePlayer.jsfx-inc:24422 |
| `Y` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 75, 0) | GamePlayer.jsfx-inc:24414 |
| `Z` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 5, 0) | GamePlayer.jsfx-inc:24410 |
| `_` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24567 |
| `a` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // abend edit | GamePlayer.jsfx-inc:24606 |
| `a` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 0; | GamePlayer.jsfx-inc:24615 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy current currpad | GamePlayer.jsfx-inc:24539 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy if valid | GamePlayer.jsfx-inc:24575 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy to "65" | GamePlayer.jsfx-inc:24928 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs1, mSL_Dyn_Flg1_def); | GamePlayer.jsfx-inc:24632 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs2, mSL_Dyn_Flg2_def); | GamePlayer.jsfx-inc:24640 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_And_Mask = mSL_Dyn_Mask_def; | GamePlayer.jsfx-inc:24648 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_Or_Mask = mSL_Dyn_Mask_def; | GamePlayer.jsfx-inc:24656 |
| `i` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // install in clip and save right now | GamePlayer.jsfx-inc:24597 |
| `m` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 2; | GamePlayer.jsfx-inc:24621 |
| `p` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  65; | GamePlayer.jsfx-inc:24552 |
| `p` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 1; | GamePlayer.jsfx-inc:24618 |
| `q` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  66; | GamePlayer.jsfx-inc:24555 |
| `r` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  67; | GamePlayer.jsfx-inc:24558 |
| `s` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  68; | GamePlayer.jsfx-inc:24561 |
| `s` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // save right now | GamePlayer.jsfx-inc:24589 |
| `t` |  | module | paramètres dynamiques (show_Dyn_pars) | // alternate "show mode" | GamePlayer.jsfx-inc:24669 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste to currpad | GamePlayer.jsfx-inc:24544 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste to clip if valid | GamePlayer.jsfx-inc:24582 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste "65" | GamePlayer.jsfx-inc:24936 |
| `x` |  | module | paramètres dynamiques (show_Dyn_pars) | // alternate "show mode" | GamePlayer.jsfx-inc:24661 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  0; | GamePlayer.jsfx-inc:24549 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs1, 0); | GamePlayer.jsfx-inc:24629 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs2, 0); | GamePlayer.jsfx-inc:24637 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_And_Mask = 0; | GamePlayer.jsfx-inc:24645 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_Or_Mask = 0; | GamePlayer.jsfx-inc:24653 |
| `Left` |  | module | paramètres dynamiques (show_Dyn_pars) | iKPar = (iKPar + paramDynCnt - 1) % paramDynCnt; | GamePlayer.jsfx-inc:24842 |
| `Right` |  | module | paramètres dynamiques (show_Dyn_pars) | iKPar = (iKPar + 1) % paramDynCnt; | GamePlayer.jsfx-inc:24843 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | GamePlayer.jsfx-inc:27088 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | GamePlayer.jsfx-inc:27060 |
| `Backspace` |  | onglet | commandes d'onglet (do_Generic_Commands) | flagStopOne += 1; | GamePlayer.jsfx-inc:18773 |
| `"` |  | onglet | commandes d'onglet (do_Generic_Commands) | parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:18768 |
| `#` |  | onglet | commandes d'onglet (do_Generic_Commands) | ui_GFXdoNow \|= 1; ui_GFXReason = 38; | GamePlayer.jsfx-inc:18734 |
| `$` |  | onglet | commandes d'onglet (do_Generic_Commands) | setRModeRec(); | GamePlayer.jsfx-inc:18748 |
| `&` |  | onglet | commandes d'onglet (do_Generic_Commands) | setPlayMark(-1, psKPlaying, recOptMarkReplay ? psKReplaying : 0, 0); | GamePlayer.jsfx-inc:18744 |
| `'` |  | onglet | commandes d'onglet (do_Generic_Commands) | setRModeSwitch(); | GamePlayer.jsfx-inc:18755 |
| `;` |  | onglet | commandes d'onglet (do_Generic_Commands) | DynParamsReset(); | GamePlayer.jsfx-inc:18752 |
| `<` |  | onglet | commandes d'onglet (do_Generic_Commands) | switchAuto(); ui_GFXdoNow \|= 1; ui_GFXReason = 38; | GamePlayer.jsfx-inc:18727 |
| `>` |  | onglet | commandes d'onglet (do_Generic_Commands) | ui_GFXdoNow \|= 1; parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:18730 |
| `@` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 11\|ActFlg1, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:18738 |
| `\|` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '\|' : switch to previous tabulation | GamePlayer.jsfx-inc:18789 |
| `}` |  | onglet | commandes d'onglet (do_Generic_Commands) | // switch tabulations | GamePlayer.jsfx-inc:18797 |
| `~` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '~' : switch to next tabulation | GamePlayer.jsfx-inc:18793 |
| `Del` |  | onglet | commandes d'onglet (do_Generic_Commands) | studPrefDispPanes = 1 + (studPrefDispPanes % 4) ; | GamePlayer.jsfx-inc:18776 |
| `0x80` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18724 |
| `0x90` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18724 |
| `à` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 11\|ActFlg1, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:18738 |
| `0xF9` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18724 |
| `0x42A` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '~' : switch to next tabulation | GamePlayer.jsfx-inc:18793 |
| `Del` |  | onglet | commandes d'onglet (do_Generic_Commands) | // clearCmd(); | GamePlayer.jsfx-inc:18719 |
| `End` |  | onglet | commandes d'onglet (do_Generic_Commands) | Kbtp = cmdClMdBase + GvPlayTypGrLoop; | GamePlayer.jsfx-inc:18765 |
| `F10` |  | onglet | commandes d'onglet (do_Generic_Commands) | // switch tabulations | GamePlayer.jsfx-inc:18797 |
| `F11` |  | onglet | commandes d'onglet (do_Generic_Commands) | uix_switch += 1; | GamePlayer.jsfx-inc:18781 |
| `F12` |  | onglet | commandes d'onglet (do_Generic_Commands) | studPrefDispPanes = 1 + (studPrefDispPanes % 4) ; | GamePlayer.jsfx-inc:18776 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:586 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:587 |
| `a` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 0 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25551 |
| `c` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispClip; | GamePlayer.jsfx-inc:25572 |
| `d` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 10 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25561 |
| `e` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 2 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25553 |
| `f` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 11 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25562 |
| `g` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 12 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25563 |
| `h` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 13 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25564 |
| `i` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 7 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25558 |
| `j` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 14 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25565 |
| `k` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 15 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25566 |
| `l` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispRng; | GamePlayer.jsfx-inc:25570 |
| `m` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispErr; | GamePlayer.jsfx-inc:25571 |
| `q` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 8 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25559 |
| `r` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 3 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25554 |
| `s` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 9 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25560 |
| `t` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 4 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25555 |
| `u` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 6 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25557 |
| `v` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispGrp; | GamePlayer.jsfx-inc:25568 |
| `w` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispPar; | GamePlayer.jsfx-inc:25567 |
| `x` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispGBk; | GamePlayer.jsfx-inc:25569 |
| `y` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 5 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25556 |
| `z` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 1 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25552 |

## FilePlayer

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris → panneau → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys).

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:108 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:110 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `+` |  | module | File Player Status (do_local_Control) | gfx_col_width = min(560, gfx_col_width + 10) ; | FilePlayer.jsfx-inc:7153 |
| `-` |  | module | File Player Status (do_local_Control) | gfx_col_width = max(260, gfx_col_width - 10) ; | FilePlayer.jsfx-inc:7154 |
| `=` |  | module | File Player Status (do_local_Control) | gfx_col_width = gfx_col_def_width ; | FilePlayer.jsfx-inc:7155 |
| `A` |  | module | File Player Status (do_local_Control) | info_config(0, 4, 5, 6, 7, 8, 1, 2, 3, 9, 10, 11); | FilePlayer.jsfx-inc:7151 |
| `Z` |  | module | File Player Status (do_local_Control) | info_config(0, 1, 2, 3); | FilePlayer.jsfx-inc:7152 |
| `a` |  | module | File Player Status (do_local_Control) | nbligMax = min(glIsizCnt, nbligMax+1) ; | FilePlayer.jsfx-inc:7156 |
| `s` |  | module | File Player Status (do_local_Control) | nbligMax = max(1, nbligMax-1); memset(glIsizTab, 0, glIsizCnt); | FilePlayer.jsfx-inc:7157 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | FilePlayer.jsfx-inc:7329 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | FilePlayer.jsfx-inc:7329 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | FilePlayer.jsfx-inc:7341 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | FilePlayer.jsfx-inc:7342 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | FilePlayer.jsfx-inc:7343 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | FilePlayer.jsfx-inc:7344 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | FilePlayer.jsfx-inc:7345 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | FilePlayer.jsfx-inc:7346 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | FilePlayer.jsfx-inc:7347 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | FilePlayer.jsfx-inc:7348 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | FilePlayer.jsfx-inc:7350 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | FilePlayer.jsfx-inc:7334 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | FilePlayer.jsfx-inc:7333 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | FilePlayer.jsfx-inc:7331 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | FilePlayer.jsfx-inc:7330 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | FilePlayer.jsfx-inc:7349 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | FilePlayer.jsfx-inc:7335 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | FilePlayer.jsfx-inc:7332 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | FilePlayer.jsfx-inc:7337 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | FilePlayer.jsfx-inc:7338 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | FilePlayer.jsfx-inc:7339 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | FilePlayer.jsfx-inc:7340 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:243 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:294 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:239 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:290 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:249 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:300 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:303 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:258 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:261 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:255 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:252 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:246 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:297 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:215 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:233 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:278 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:218 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:236 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:281 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:221 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:227 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:284 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:224 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:230 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:287 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:791 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:763 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:586 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:587 |
| `c` |  | système | commandes système (do_System_Keys) | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_System_Keys.jsfx-inc:28 |
| `g` |  | système | commandes système (do_System_Keys) | gc_run(2); | mSL_System_Keys.jsfx-inc:24 |
| `k` |  | système | commandes système (do_System_Keys) | mSL_kill_all_thread(); | mSL_System_Keys.jsfx-inc:25 |
| `l` |  | système | commandes système (do_System_Keys) | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) / 10; | mSL_System_Keys.jsfx-inc:29 |
| `m` |  | système | commandes système (do_System_Keys) | mem_walk(0); mem_show(); | mSL_System_Keys.jsfx-inc:26 |
| `n` |  | système | commandes système (do_System_Keys) | mem_walk(8); mem_show(); | mSL_System_Keys.jsfx-inc:27 |
| `o` |  | système | commandes système (do_System_Keys) | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test = 1; mSL_run_max = 1); | mSL_System_Keys.jsfx-inc:36 |
| `r` |  | système | commandes système (do_System_Keys) | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNone) ? ( | mSL_System_Keys.jsfx-inc:30 |
| `s` |  | système | commandes système (do_System_Keys) | mSL_run_test = 0; | mSL_System_Keys.jsfx-inc:37 |
| `t` |  | système | commandes système (do_System_Keys) | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = 25; | mSL_System_Keys.jsfx-inc:35 |

## ScriptMaster

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris → panneau → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys).

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:108 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:110 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | ScriptMaster.jsfx-inc:2555 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | ScriptMaster.jsfx-inc:2555 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | ScriptMaster.jsfx-inc:2567 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | ScriptMaster.jsfx-inc:2568 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | ScriptMaster.jsfx-inc:2569 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | ScriptMaster.jsfx-inc:2570 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | ScriptMaster.jsfx-inc:2571 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | ScriptMaster.jsfx-inc:2572 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | ScriptMaster.jsfx-inc:2573 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | ScriptMaster.jsfx-inc:2574 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | ScriptMaster.jsfx-inc:2576 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | ScriptMaster.jsfx-inc:2560 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | ScriptMaster.jsfx-inc:2559 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | ScriptMaster.jsfx-inc:2557 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | ScriptMaster.jsfx-inc:2556 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | ScriptMaster.jsfx-inc:2575 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | ScriptMaster.jsfx-inc:2561 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | ScriptMaster.jsfx-inc:2558 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | ScriptMaster.jsfx-inc:2563 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | ScriptMaster.jsfx-inc:2564 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | ScriptMaster.jsfx-inc:2565 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | ScriptMaster.jsfx-inc:2566 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:243 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:294 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:239 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:290 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:249 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:300 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:303 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:258 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:261 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:255 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:252 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:246 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:297 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:215 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:233 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:278 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:218 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:236 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:281 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:221 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:227 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:284 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:224 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:230 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:287 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:791 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:763 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:586 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:587 |
| `c` |  | système | commandes système (do_System_Keys) | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_System_Keys.jsfx-inc:28 |
| `g` |  | système | commandes système (do_System_Keys) | gc_run(2); | mSL_System_Keys.jsfx-inc:24 |
| `k` |  | système | commandes système (do_System_Keys) | mSL_kill_all_thread(); | mSL_System_Keys.jsfx-inc:25 |
| `l` |  | système | commandes système (do_System_Keys) | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) / 10; | mSL_System_Keys.jsfx-inc:29 |
| `m` |  | système | commandes système (do_System_Keys) | mem_walk(0); mem_show(); | mSL_System_Keys.jsfx-inc:26 |
| `n` |  | système | commandes système (do_System_Keys) | mem_walk(8); mem_show(); | mSL_System_Keys.jsfx-inc:27 |
| `o` |  | système | commandes système (do_System_Keys) | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test = 1; mSL_run_max = 1); | mSL_System_Keys.jsfx-inc:36 |
| `r` |  | système | commandes système (do_System_Keys) | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNone) ? ( | mSL_System_Keys.jsfx-inc:30 |
| `s` |  | système | commandes système (do_System_Keys) | mSL_run_test = 0; | mSL_System_Keys.jsfx-inc:37 |
| `t` |  | système | commandes système (do_System_Keys) | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = 25; | mSL_System_Keys.jsfx-inc:35 |

## Diffusion-3

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris (écran Live : la boîte sous la souris) → panneau → écran Live (do_live_actions) → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys).

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:108 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:110 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `h` |  | module | Space 3D (la vue) (show_Space3D_Pad) | s3d_style = !s3d_style; ui_GFXdoNow \|= 4;  // balls, or crosses and halos | Diffusion-3-Space3D.jsfx-inc:769 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Diffusion-3.jsfx-inc:5713 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Diffusion-3.jsfx-inc:5713 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | Diffusion-3.jsfx-inc:5725 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | Diffusion-3.jsfx-inc:5726 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | Diffusion-3.jsfx-inc:5727 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | Diffusion-3.jsfx-inc:5728 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | Diffusion-3.jsfx-inc:5729 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | Diffusion-3.jsfx-inc:5730 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | Diffusion-3.jsfx-inc:5731 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | Diffusion-3.jsfx-inc:5732 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | Diffusion-3.jsfx-inc:5734 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | Diffusion-3.jsfx-inc:5718 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | Diffusion-3.jsfx-inc:5717 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | Diffusion-3.jsfx-inc:5715 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | Diffusion-3.jsfx-inc:5714 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | Diffusion-3.jsfx-inc:5733 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | Diffusion-3.jsfx-inc:5719 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | Diffusion-3.jsfx-inc:5716 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | Diffusion-3.jsfx-inc:5721 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | Diffusion-3.jsfx-inc:5722 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | Diffusion-3.jsfx-inc:5723 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | Diffusion-3.jsfx-inc:5724 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:243 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:294 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:239 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:290 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:249 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:300 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:303 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:258 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:261 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:255 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:252 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:246 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:297 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:215 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:233 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:278 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:218 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:236 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:281 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:221 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:227 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:284 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:224 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:230 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:287 |
| `$` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_opt = s3d_opt ~ s3d_oLevels; | Diffusion-3.jsfx-inc:6105 |
| `%` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_opt = s3d_opt ~ s3d_oGains; | Diffusion-3.jsfx-inc:6108 |
| `,` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_dist = min(12, s3d_dist * 1.02); | Diffusion-3.jsfx-inc:6099 |
| `/` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_lbg = !sx_lbg; | Diffusion-3.jsfx-inc:6111 |
| `:` |  | module | écran Live : boîte sous la souris (mouse_hover) | HP_Dr_updsize(mh_cur_box, max(10, floor(mh_cur_box[bx_sfact]  * 0.96))); | Diffusion-3.jsfx-inc:6092 |
| `;` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_dist = max(1.8, s3d_dist * 0.98); | Diffusion-3.jsfx-inc:6096 |
| `=` |  | module | écran Live : boîte sous la souris (mouse_hover) | HP_Dr_updsize(mh_cur_box, max(mh_cur_box[bx_sfact] + 1, ceil(mh_cur_box[bx_sfact]  * 1.04))); | Diffusion-3.jsfx-inc:6089 |
| `?` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_SetView((sx_view + 1) % 4); | Diffusion-3.jsfx-inc:6102 |
| `Up` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_el += 0.05; | Diffusion-3.jsfx-inc:6118 |
| `Down` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_el -= 0.05; | Diffusion-3.jsfx-inc:6121 |
| `Home` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_SetView(sx_view); | Diffusion-3.jsfx-inc:6114 |
| `Left` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_az -= 0.05; | Diffusion-3.jsfx-inc:6124 |
| `Right` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_az += 0.05; | Diffusion-3.jsfx-inc:6127 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:791 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:763 |
| `-` |  | onglet | écran Live : commandes (do_live_actions) | check_graph = 1 - check_graph; | Diffusion-3.jsfx-inc:5279 |
| `.` |  | onglet | écran Live : commandes (do_live_actions) | mk_display_box(1, "*", 1, -1, 180); | Diffusion-3.jsfx-inc:5282 |
| `C` |  | onglet | écran Live : commandes (do_live_actions) | coloriterate = coloriterate ? 0: 1; | Diffusion-3.jsfx-inc:5227 |
| `a` |  | onglet | écran Live : commandes (do_live_actions) | wrefresh = 1; | Diffusion-3.jsfx-inc:5220 |
| `b` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(7, 0, actpars); | Diffusion-3.jsfx-inc:5258 |
| `c` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5223 |
| `g` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5212 |
| `i` |  | onglet | écran Live : commandes (do_live_actions) | HP_Box[bx_activ] & bx__drawbox ? HP_Box[bx_activ] &= 0x7FFFFFFF - bx__drawbox : HP_Box[bx_activ] \|= bx__drawb… | Diffusion-3.jsfx-inc:5276 |
| `j` |  | onglet | écran Live : commandes (do_live_actions) | HP_ViewN = (HP_ViewN + 1) % 4; | Diffusion-3.jsfx-inc:5271 |
| `k` |  | onglet | écran Live : commandes (do_live_actions) | statkeyd = statkeyd ? 0 : 1; | Diffusion-3.jsfx-inc:5243 |
| `l` |  | onglet | écran Live : commandes (do_live_actions) | // Clear non permanent boxes | Diffusion-3.jsfx-inc:5264 |
| `m` |  | onglet | écran Live : commandes (do_live_actions) | show_mouse = 1 - show_mouse; | Diffusion-3.jsfx-inc:5236 |
| `p` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5254 |
| `r` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = 1; | Diffusion-3.jsfx-inc:5239 |
| `s` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5216 |
| `t` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5246 |
| `u` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1;  // next tabulation (Tab, Shift + Tab : see do_Plugin_Keys) | Diffusion-3.jsfx-inc:5250 |
| `v` |  | onglet | écran Live : commandes (do_live_actions) | show_used = 1 - show_used; | Diffusion-3.jsfx-inc:5233 |
| `w` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(8, 0, actpars); | Diffusion-3.jsfx-inc:5268 |
| `x` |  | onglet | écran Live : commandes (do_live_actions) | wrefresh = 3; | Diffusion-3.jsfx-inc:5230 |
| `z` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(10, 0, actpars); | Diffusion-3.jsfx-inc:5261 |
| `S` |  | plugin | commandes de Diffusion-3 (do_Plugin_Keys) | togglesliders(-1); | Diffusion-3.jsfx-inc:5296 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:586 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:587 |
| `c` |  | système | commandes système (do_System_Keys) | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_System_Keys.jsfx-inc:28 |
| `g` |  | système | commandes système (do_System_Keys) | gc_run(2); | mSL_System_Keys.jsfx-inc:24 |
| `k` |  | système | commandes système (do_System_Keys) | mSL_kill_all_thread(); | mSL_System_Keys.jsfx-inc:25 |
| `l` |  | système | commandes système (do_System_Keys) | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) / 10; | mSL_System_Keys.jsfx-inc:29 |
| `m` |  | système | commandes système (do_System_Keys) | mem_walk(0); mem_show(); | mSL_System_Keys.jsfx-inc:26 |
| `n` |  | système | commandes système (do_System_Keys) | mem_walk(8); mem_show(); | mSL_System_Keys.jsfx-inc:27 |
| `o` |  | système | commandes système (do_System_Keys) | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test = 1; mSL_run_max = 1); | mSL_System_Keys.jsfx-inc:36 |
| `r` |  | système | commandes système (do_System_Keys) | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNone) ? ( | mSL_System_Keys.jsfx-inc:30 |
| `s` |  | système | commandes système (do_System_Keys) | mSL_run_test = 0; | mSL_System_Keys.jsfx-inc:37 |
| `t` |  | système | commandes système (do_System_Keys) | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = 25; | mSL_System_Keys.jsfx-inc:35 |

## Interstys

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris (puis ses pads) → panneau → commandes d'onglet (do_Generic_Commands) → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys).

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:108 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:110 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `Ctrl+A` | Cmd | module | ? (show_Curves_Pad) | i = 0; loop(b[its_Crv_N], its_CrvSelF[i] = 1; i += 1;); | Interstys.jsfx-inc:16535 |
| `Ctrl+A..Ctrl+E` |  | module | ? (show_Curves_Pad) | its_Crv_Pre(k); its_Crv_Commit();  // (Undo) | Interstys.jsfx-inc:16615 |
| `Ctrl+A..Ctrl+E` |  | module | ? (show_Curves_Pad) | // a new curve (the one shown, replaced) | Interstys.jsfx-inc:16616 |
| `a` | Cmd | module | ? (show_Curves_Pad) | i = 0; loop(b[its_Crv_N], its_CrvSelF[i] = 1; i += 1;); | Interstys.jsfx-inc:16535 |
| `d` |  | module | ? (show_Curves_Pad) | its_Crv_Dump(k) | Interstys.jsfx-inc:16531 |
| `s` |  | module | ? (show_Curves_Pad) | its_Crv_SetSus(b, k, -2) | Interstys.jsfx-inc:16533 |
| `d` |  | module | ? (show_Effect_Pad) | GM_Dump(fx, its_Efx_BlkSize, sprintf(#, "Effect %d", fxn+1)) | Interstys.jsfx-inc:15042 |
| `d` |  | module | Line (show_Line_Pad) | GM_Dump(lcbl, its_Lin_BlkSize, sprintf(#, "Line %d", lnr+1)) | Interstys.jsfx-inc:14359 |
| `d` |  | module | Reader (show_Reader_Pad) | GM_Dump(rcbl, its_Rdr_BlkSize, sprintf(#, "Reader %d", rdr+1)) | Interstys.jsfx-inc:13442 |
| `r` |  | module | Reader (show_Reader_Pad) | // toggle run/pause state | Interstys.jsfx-inc:13980 |
| `t` |  | module | Reader (show_Reader_Pad) | RDBL[6] = (RDBL[6] + 1) % 3; | Interstys.jsfx-inc:13984 |
| `d` |  | module | Writer (show_Writer_Pad) | GM_Dump(wcbl, its_Wrt_BlkSize, sprintf(#, "Writer %d", wrt+1)) | Interstys.jsfx-inc:15315 |
| `+` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = min(its_WaveHMax, h + its_WaveHStep); | Interstys.jsfx-inc:1217 |
| `-` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = max(its_WaveHMin, h - its_WaveHStep); | Interstys.jsfx-inc:1221 |
| `=` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = min(its_WaveHMax, h + its_WaveHStep); | Interstys.jsfx-inc:1217 |
| `v` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | fp[0] = fp[0] ~ its_WaveOver; | Interstys.jsfx-inc:1225 |
| `w` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | fp[0] = fp[0] ~ its_WaveHide; | Interstys.jsfx-inc:1214 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Interstys.jsfx-inc:13014 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Interstys.jsfx-inc:13014 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | Interstys.jsfx-inc:13026 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | Interstys.jsfx-inc:13027 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | Interstys.jsfx-inc:13028 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | Interstys.jsfx-inc:13029 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | Interstys.jsfx-inc:13030 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | Interstys.jsfx-inc:13031 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | Interstys.jsfx-inc:13032 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | Interstys.jsfx-inc:13033 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | Interstys.jsfx-inc:13035 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | Interstys.jsfx-inc:13019 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | Interstys.jsfx-inc:13018 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | Interstys.jsfx-inc:13016 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | Interstys.jsfx-inc:13015 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | Interstys.jsfx-inc:13034 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | Interstys.jsfx-inc:13020 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | Interstys.jsfx-inc:13017 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | Interstys.jsfx-inc:13022 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | Interstys.jsfx-inc:13023 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | Interstys.jsfx-inc:13024 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | Interstys.jsfx-inc:13025 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:243 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:294 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:239 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:290 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:249 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:300 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:303 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:258 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:261 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:255 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:252 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:246 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:297 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:215 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:233 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:278 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:218 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:236 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:281 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:221 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:227 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:284 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:224 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:230 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:287 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | Interstys.jsfx-inc:17605 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | Interstys.jsfx-inc:17577 |
| `S` |  | plugin | commandes d'Interstys (do_Plugin_Keys) | (gui_show_sliders = gui_show_sliders ? 0 : 1) ? ( | Interstys.jsfx-inc:12406 |
| `U` |  | plugin | commandes d'Interstys (do_Plugin_Keys) | gui_show_UI = gui_show_UI ? 0 : 1; | Interstys.jsfx-inc:12403 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:586 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:587 |
| `c` |  | système | commandes système (do_System_Keys) | mSL_Dyn_RecycleF = mSL_Dyn_RecycleF ? 0 : 1; | mSL_System_Keys.jsfx-inc:28 |
| `g` |  | système | commandes système (do_System_Keys) | gc_run(2); | mSL_System_Keys.jsfx-inc:24 |
| `k` |  | système | commandes système (do_System_Keys) | mSL_kill_all_thread(); | mSL_System_Keys.jsfx-inc:25 |
| `l` |  | système | commandes système (do_System_Keys) | mm_show_limit = ((mm_show_limit * 10 + 1) % 20) / 10; | mSL_System_Keys.jsfx-inc:29 |
| `m` |  | système | commandes système (do_System_Keys) | mem_walk(0); mem_show(); | mSL_System_Keys.jsfx-inc:26 |
| `n` |  | système | commandes système (do_System_Keys) | mem_walk(8); mem_show(); | mSL_System_Keys.jsfx-inc:27 |
| `o` |  | système | commandes système (do_System_Keys) | mSL_run_once = mSL_run_once ? 0 : (mSL_run_test = 1; mSL_run_max = 1); | mSL_System_Keys.jsfx-inc:36 |
| `r` |  | système | commandes système (do_System_Keys) | ((ent = SchedDetachHead(SchedSuspPts)) != SchedNone) ? ( | mSL_System_Keys.jsfx-inc:30 |
| `s` |  | système | commandes système (do_System_Keys) | mSL_run_test = 0; | mSL_System_Keys.jsfx-inc:37 |
| `t` |  | système | commandes système (do_System_Keys) | mSL_run_test = mSL_run_test ? 0 : 1; mSL_run_max = 25; | mSL_System_Keys.jsfx-inc:35 |

## Éditeurs de nombres

Appelés par les modules avec la touche qu'ils ont reçue (hors analyse des conflits).

| Fonction | Fichier | Touches |
|---|---|---|
| updtBNumber | Diffusion-3.jsfx-inc | `0..9` `%` `z` `+` `=` `:` `/` `;` `.` `,` `?` `$` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` `Home` |
| updtBNumber | FilePlayer.jsfx-inc | `0..9` `%` `z` `+` `=` `:` `/` `;` `.` `,` `?` `$` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` `Home` |
| updtNumber | GamePlayer.jsfx-inc | `0..9` `%` `Home` `+` `=` `:` `/` `;` `.` `,` `?` `_` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` |
| updtBNumber | GamePlayer.jsfx-inc | `0..9` `%` `z` `+` `=` `:` `/` `-` `;` `.` `,` `?` `$` `_` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` `Home` |
| updClipNumber | GamePlayer.jsfx-inc | `0..9` `(` `)` `%` `Home` `+` `=` `:` `/` `-` `;` `,` `.` `?` `_` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` |
| updPlMdNumber | GamePlayer.jsfx-inc | `0..9` `%` `z` `Home` `+` `=` `:` `/` `-` `;` `.` `,` `?` `_` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` |
| updSpMdNumber | GamePlayer.jsfx-inc | `0..9` `%` `z` `Home` `+` `=` `:` `/` `-` `_` `n` `p` `b` `Right` `Left` `,` `;` `?` `.` `Down` `Up` `PgDn` `PgUp` |
| updGrBkNumber | GamePlayer.jsfx-inc | `0..9` `%` `Home` `+` `=` `:` `/` `-` `_` `Down` `Up` `n` `p` `b` `Right` `Left` |
| updGroupNumber | GamePlayer.jsfx-inc | `0..9` `%` `Home` `+` `=` `:` `/` `-` `Down` `PgDn` `Up` `PgUp` `n` `p` `b` `Right` `Left` |
| updGroupBnkNumber | GamePlayer.jsfx-inc | `n` `+` `=` `p` `:` `/` `-` `Right` `Left` `Up` `PgUp` `Down` `PgDn` |
| updPartNumber | GamePlayer.jsfx-inc | `0..9` `%` `Home` `+` `=` `_` `:` `/` `-` `Up` `PgUp` `Down` `PgDn` `n` `p` `b` `Right` `Left` |
| updStudPadKey | GamePlayer.jsfx-inc | `'` `(` `)` `>` `,` |
| updHPSel | GamePlayer.jsfx-inc | `0..9` `%` `+` `=` `:` `/` `d` `m` `.` `?` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` `Home` |
| updtBNumber | ScriptMaster_Utilities.jsfx-inc | `0..9` `%` `z` `+` `=` `:` `/` `;` `.` `,` `?` `$` `n` `p` `b` `Right` `Left` `Down` `Up` `PgDn` `PgUp` `Home` |
