# Touches du clavier dans CMGS

*Fichier produit par `Scripts/keys_table.py` : ne pas le modifier à la main, relancer le script.*

Pour chaque plugin, les touches testées par le code `@gfx`, par niveau dans l'ordre où les niveaux voient la touche pendant une trame. « Modif. » : les modificateurs testés sur la même ligne (vide : non testés, la touche agit avec ou sans modificateur ; « none » : sans modificateur). L'action est le début du code exécuté. Les bibliothèques partagées (mSL_Dbg_Memory…) apparaissent dans chaque plugin qui les inclut.

## Conflits

### GamePlayer

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (13)

- `$` : commandes d'onglet (GamePlayer.jsfx-inc:18753), pas au-dessus de : Scripts / Settings
- `Backspace` : commandes d'onglet (GamePlayer.jsfx-inc:18778), pas au-dessus de : Scripts / Settings
- `Shift+Left` : largeur des colonnes (GamePlayer.jsfx-inc:27093), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (GamePlayer.jsfx-inc:27065), pas au-dessus de : mémoire (débogueur)
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

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (12)

- `Shift+Left` : largeur des colonnes (Interstys.jsfx-inc:18815), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (Interstys.jsfx-inc:18787), pas au-dessus de : mémoire (débogueur)
- `Shift+Tab` : onglet suivant / précédent (ui-lib-JJ-GUI.jsfx-inc:586), pas au-dessus de : ?
- `Tab` : onglet suivant / précédent (ui-lib-JJ-GUI.jsfx-inc:587), pas au-dessus de : ?
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
| `S` |  |  | togglesliders(-1); | // the generic sliders in the panel of REAPER |
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
| `g` |  | module | Banks (doBanksInteract) | GM_key_take('g'); | GamePlayer.jsfx-inc:22634 |
| `g` |  | module | Banks (doBanksInteract) | BnkGrpLock(); | GamePlayer.jsfx-inc:22635 |
| `Ctrl+C` |  | module | Clips selection (show_Clips_Selection) | i = curB; loop(100,  // ^C | GamePlayer.jsfx-inc:21324 |
| `Enter` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21209 |
| `Enter` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21259 |
| `Ctrl+Z` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? ( | GamePlayer.jsfx-inc:21332 |
| `Space` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21209 |
| `Space` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // play | GamePlayer.jsfx-inc:21259 |
| `!` |  | module | Clips selection (show_Clips_Selection) | gmem[clClAlias+xcell] = 0;  // remove the alias and clear the entry | GamePlayer.jsfx-inc:21226 |
| `%` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs - 1 + showStates) % showStates ; | GamePlayer.jsfx-inc:21292 |
| `+` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? (  // validate/unvalidate all entries | GamePlayer.jsfx-inc:21279 |
| `/` |  | module | Clips selection (show_Clips_Selection) | i = curB; loop(100,  // clear all entries | GamePlayer.jsfx-inc:21271 |
| `0..9` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 1 | GamePlayer.jsfx-inc:21213 |
| `0..9` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 0 - 9 | GamePlayer.jsfx-inc:21263 |
| `:` |  | module | Clips selection (show_Clips_Selection) | gmem[clInfStart+xcell] = 0;  // clear the entry | GamePlayer.jsfx-inc:21221 |
| `=` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? (  // (un)validate the entry | GamePlayer.jsfx-inc:21232 |
| `A..Z` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 10 - N | GamePlayer.jsfx-inc:21267 |
| `a..z` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 10 - N | GamePlayer.jsfx-inc:21217 |
| `0xA0` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // alt+' '  => play | GamePlayer.jsfx-inc:21303 |
| `Up` | none | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 1) % 10; | GamePlayer.jsfx-inc:21090 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 100 - 10) % 100; | GamePlayer.jsfx-inc:21248 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs + 1) % showStates ; | GamePlayer.jsfx-inc:21295 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 1) % 10; | GamePlayer.jsfx-inc:21316 |
| `Down` | none | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 10 - 1) % 10; | GamePlayer.jsfx-inc:21087 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 10) % 100; | GamePlayer.jsfx-inc:21245 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs - 1 + showStates) % showStates ; | GamePlayer.jsfx-inc:21292 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 10 - 1) % 10; | GamePlayer.jsfx-inc:21313 |
| `Home` | none | module | Clips selection (show_Clips_Selection) | slBankset = slGroupNum = 0; | GamePlayer.jsfx-inc:21093 |
| `Home` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB; | GamePlayer.jsfx-inc:21251 |
| `Left` | none | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 10 - 1) % 10; | GamePlayer.jsfx-inc:21084 |
| `Left` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 100 - 1) % 100; | GamePlayer.jsfx-inc:21242 |
| `Left` |  | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 10 - 1) % 10; | GamePlayer.jsfx-inc:21310 |
| `Right` | none | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 1) % 10; | GamePlayer.jsfx-inc:21081 |
| `Right` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 1) % 100; | GamePlayer.jsfx-inc:21239 |
| `Right` |  | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 1) % 10; | GamePlayer.jsfx-inc:21307 |
| `Up` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + readerCount - 8) % readerCount; | GamePlayer.jsfx-inc:19865 |
| `Down` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + 8) % readerCount; | GamePlayer.jsfx-inc:19859 |
| `Left` | none | module | Generator (show_Generator) | unitbkl[0] = (unitbkl[0] - 1 + 4) % 4; | GamePlayer.jsfx-inc:19851 |
| `Left` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + readerCount - 1) % readerCount; | GamePlayer.jsfx-inc:19862 |
| `Right` | none | module | Generator (show_Generator) | unitbkl[0] = (unitbkl[0] + 1) % 4; | GamePlayer.jsfx-inc:19848 |
| `Right` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + 1) % readerCount; | GamePlayer.jsfx-inc:19856 |
| `x` |  | module | LED interactive (show_jled) | led[ui_jled_status] = led[ui_jled_status] > 0.5 ? 0 : 1; | mSL_ui_Pads.jsfx-inc:118 |
| `*` |  | module | Play control (show_Play_Control) | // very slow stop all... | GamePlayer.jsfx-inc:25948 |
| `a` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypAnyClip | GamePlayer.jsfx-inc:25945 |
| `b` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypBank | GamePlayer.jsfx-inc:25944 |
| `c` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypClip | GamePlayer.jsfx-inc:25939 |
| `g` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypGroup | GamePlayer.jsfx-inc:25943 |
| `p` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypPartial | GamePlayer.jsfx-inc:25942 |
| `r` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypRange | GamePlayer.jsfx-inc:25941 |
| `s` |  | module | Play control (show_Play_Control) | GvPlayTyp = 0 | GamePlayer.jsfx-inc:25940 |
| `Left` |  | module | Play control (show_Play_Control) | GvPlayTyp = (GvPlayTyp + menuActModeCnt - 1) % menuActModeCnt | GamePlayer.jsfx-inc:25946 |
| `Right` |  | module | Play control (show_Play_Control) | GvPlayTyp = (GvPlayTyp + 1) % menuActModeCnt | GamePlayer.jsfx-inc:25947 |
| `Backspace` |  | module | Scripts / Settings (show_Scripts) | (v !== 0\|v) ? (  // backspace | GamePlayer.jsfx-inc:23149 |
| `$` |  | module | Scripts / Settings (show_Scripts) | ssnd = 1; | GamePlayer.jsfx-inc:23168 |
| `+` |  | module | Scripts / Settings (show_Scripts) | v = v + 1; | GamePlayer.jsfx-inc:23137 |
| `-` |  | module | Scripts / Settings (show_Scripts) | v = v + u - 1; | GamePlayer.jsfx-inc:23140 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23115 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23119 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | // goto marker "n" | GamePlayer.jsfx-inc:24203 |
| `=` |  | module | Scripts / Settings (show_Scripts) | v = v + 1; | GamePlayer.jsfx-inc:23137 |
| `A..F` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23127 |
| `X` |  | module | Scripts / Settings (show_Scripts) | padSettingC7fmt = padSettingC7fmt === 0; | GamePlayer.jsfx-inc:23134 |
| `Z` |  | module | Scripts / Settings (show_Scripts) | v = 0; | GamePlayer.jsfx-inc:23131 |
| `_` |  | module | Scripts / Settings (show_Scripts) | v = v + u - 1; | GamePlayer.jsfx-inc:23140 |
| `a..f` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23123 |
| `a` |  | module | Scripts / Settings (show_Scripts) | parSet(p_GvAutoMd, ! paramValues[p_GvAutoMd]); | GamePlayer.jsfx-inc:24145 |
| `e` |  | module | Scripts / Settings (show_Scripts) | playSkipSlnc = ! playSkipSlnc ; | GamePlayer.jsfx-inc:24200 |
| `g` |  | module | Scripts / Settings (show_Scripts) | recOptMarkReplay = ! recOptMarkReplay ; | GamePlayer.jsfx-inc:24165 |
| `h` |  | module | Scripts / Settings (show_Scripts) | setRModeStop(); | GamePlayer.jsfx-inc:24185 |
| `i` |  | module | Scripts / Settings (show_Scripts) | // invert read direction | GamePlayer.jsfx-inc:24168 |
| `j` |  | module | Scripts / Settings (show_Scripts) | playJmpLoop = ! playJmpLoop ; | GamePlayer.jsfx-inc:24159 |
| `k` |  | module | Scripts / Settings (show_Scripts) | playAndLock ? SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:24151 |
| `l` |  | module | Scripts / Settings (show_Scripts) | playRepeatMd = ! playRepeatMd ; | GamePlayer.jsfx-inc:24162 |
| `m` |  | module | Scripts / Settings (show_Scripts) | replayUnMute = ! replayUnMute; | GamePlayer.jsfx-inc:24189 |
| `o` |  | module | Scripts / Settings (show_Scripts) | recOptLockSnds = ! recOptLockSnds; | GamePlayer.jsfx-inc:24192 |
| `p` |  | module | Scripts / Settings (show_Scripts) | setPModeSwitch(); | GamePlayer.jsfx-inc:24138 |
| `q` |  | module | Scripts / Settings (show_Scripts) | playReeval = 1; | GamePlayer.jsfx-inc:24141 |
| `r` |  | module | Scripts / Settings (show_Scripts) | setRModeSwitch(); | GamePlayer.jsfx-inc:24148 |
| `s` |  | module | Scripts / Settings (show_Scripts) | playModeStep = ! playModeStep ; | GamePlayer.jsfx-inc:24178 |
| `t` |  | module | Scripts / Settings (show_Scripts) | recOptRecReplay = ! recOptRecReplay ; | GamePlayer.jsfx-inc:24182 |
| `u` |  | module | Scripts / Settings (show_Scripts) | playAndUnLock = ! playAndUnLock ; | GamePlayer.jsfx-inc:24155 |
| `w` |  | module | Scripts / Settings (show_Scripts) | // various play speed | GamePlayer.jsfx-inc:24173 |
| `x` |  | module | Scripts / Settings (show_Scripts) | padSettingC7fmt = padSettingC7fmt === 0; | GamePlayer.jsfx-inc:23134 |
| `z` |  | module | Scripts / Settings (show_Scripts) | v = 0; | GamePlayer.jsfx-inc:23131 |
| `z` |  | module | Scripts / Settings (show_Scripts) | parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:24195 |
| `Up` |  | module | Scripts / Settings (show_Scripts) | Settings_F_Sel = (Settings_F_Sel - 1 + FlagsCount) % FlagsCount; | GamePlayer.jsfx-inc:23165 |
| `Up` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? 10 : (jmc === 0x04) ? 60 : (jmc === 0x10) ? 300 : (jmc === 0x14) ? 1800 : 0; | GamePlayer.jsfx-inc:24214 |
| `Down` |  | module | Scripts / Settings (show_Scripts) | Settings_F_Sel = (Settings_F_Sel + 1) % FlagsCount; | GamePlayer.jsfx-inc:23162 |
| `Down` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? -10 : (jmc === 0x04) ? -60 : (jmc === 0x10) ? -300 : (jmc === 0x14) ? -1800 : 0; | GamePlayer.jsfx-inc:24217 |
| `Left` | none | module | Scripts / Settings (show_Scripts) | v = (padSettingC7fmt === 0) ? v << 4 : v * 10; | GamePlayer.jsfx-inc:23143 |
| `Left` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? -1 : (jmc === 0x04) ? -0.1 : (jmc === 0x10) ? -0.01 : (jmc === 0x14) ? -0.001 : 0; | GamePlayer.jsfx-inc:24208 |
| `Right` | none | module | Scripts / Settings (show_Scripts) | v = (padSettingC7fmt === 0) ? v >> 4 : (v / 10); | GamePlayer.jsfx-inc:23146 |
| `Right` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? 1 : (jmc === 0x04) ? 0.1 : (jmc === 0x10) ? 0.01 : (jmc === 0x14) ? 0.001 : 0; | GamePlayer.jsfx-inc:24211 |
| `+` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += 1; | GamePlayer.jsfx-inc:20212 |
| `-` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += MIDI_States_siz - 1; | GamePlayer.jsfx-inc:20215 |
| `0..9` |  | module | Sensors (show_Sensors) | GM_key_take(zzch); | GamePlayer.jsfx-inc:20218 |
| `2` |  | module | Sensors (show_Sensors) | setSensorSize(zzch) | GamePlayer.jsfx-inc:20274 |
| `3` |  | module | Sensors (show_Sensors) | setSensorSize(zzch) | GamePlayer.jsfx-inc:20274 |
| `=` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += MIDI_States_siz - 1; | GamePlayer.jsfx-inc:20215 |
| `_` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += 1; | GamePlayer.jsfx-inc:20212 |
| `!` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 2.5, 0, 0); | GamePlayer.jsfx-inc:22016 |
| `E` |  | module | Units (show_Units) | gmem[Un+RCB_State_Changed] \|= i_M_Rst; | GamePlayer.jsfx-inc:21991 |
| `E` |  | module | Units (show_Units) | gmem[Un+RCB_Cl_Flgs] = 1;  // also Lock entry (the key is already taken) | GamePlayer.jsfx-inc:21994 |
| `a` |  | module | Units (show_Units) | BplayerA[2] = rd; | GamePlayer.jsfx-inc:21975 |
| `b` |  | module | Units (show_Units) | BplayerB[2] = rd; | GamePlayer.jsfx-inc:21979 |
| `c` |  | module | Units (show_Units) | BplayerC[2] = rd; | GamePlayer.jsfx-inc:21983 |
| `d` |  | module | Units (show_Units) | BplayerD[2] = rd; | GamePlayer.jsfx-inc:21987 |
| `e` |  | module | Units (show_Units) | gmem[Un+RCB_State_Changed] \|= i_M_Rst; | GamePlayer.jsfx-inc:21991 |
| `f` |  | module | Units (show_Units) | SchedAddTask(5, 8, -1, -1, 1, 0, 0); | GamePlayer.jsfx-inc:22000 |
| `g` |  | module | Units (show_Units) | parSet(p_GvAutoMd, ! paramValues[p_GvAutoMd]); | GamePlayer.jsfx-inc:21972 |
| `h` |  | module | Units (show_Units) | SchedAddTask(5, 8, -1, -1, 0.20, 0, 0); | GamePlayer.jsfx-inc:22003 |
| `i` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 3.5, 0, 0); | GamePlayer.jsfx-inc:22019 |
| `j` |  | module | Units (show_Units) | Kbtp = cmdClMdBase + GvPlayTypGrLoop; | GamePlayer.jsfx-inc:22041 |
| `k` |  | module | Units (show_Units) | SchedAddTask(5, 7, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22006 |
| `l` |  | module | Units (show_Units) | SchedAddTask(5, 1\|ActFlg1, 1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21969 |
| `m` |  | module | Units (show_Units) | SchedAddTask(5, 6, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21951 |
| `n` |  | module | Units (show_Units) | lmode = ! lmode ; | GamePlayer.jsfx-inc:22022 |
| `o` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 5, 0, 0); | GamePlayer.jsfx-inc:22028 |
| `p` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 8, 0, 0); | GamePlayer.jsfx-inc:22031 |
| `q` |  | module | Units (show_Units) | qmode = ! qmode ; | GamePlayer.jsfx-inc:22025 |
| `r` |  | module | Units (show_Units) | SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22034 |
| `s` |  | module | Units (show_Units) | SchedAddTask(5, 5\|ActFlg1, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21955 |
| `t` |  | module | Units (show_Units) | SchedAddTask(5, 3, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22009 |
| `u` |  | module | Units (show_Units) | SchedAddTask(5, 1, 1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21966 |
| `v` |  | module | Units (show_Units) | gDispPlay = rd; | GamePlayer.jsfx-inc:22013 |
| `w` |  | module | Units (show_Units) | SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22038 |
| `z` |  | module | Units (show_Units) | SchedAddTask(5, 1\|ActFlg1, 3, -1, 0, 0, 0); | GamePlayer.jsfx-inc:21963 |
| `Enter` |  | module | log système / log utilisateur (show_SysLog) | mSL_log(box, " "); | GamePlayer.jsfx-inc:20383 |
| `Space` |  | module | log système / log utilisateur (show_SysLog) | mSL_log(box, " "); | GamePlayer.jsfx-inc:20383 |
| `1` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 1; | GamePlayer.jsfx-inc:20395 |
| `2` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 2; | GamePlayer.jsfx-inc:20396 |
| `3` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 3; | GamePlayer.jsfx-inc:20397 |
| `4` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 4; | GamePlayer.jsfx-inc:20398 |
| `5` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 5; | GamePlayer.jsfx-inc:20399 |
| `6` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 6; | GamePlayer.jsfx-inc:20400 |
| `7` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 7; | GamePlayer.jsfx-inc:20401 |
| `8` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 8; | GamePlayer.jsfx-inc:20402 |
| `P` |  | module | log système / log utilisateur (show_SysLog) | sysout(SysLogBox, 31);  // the log in the console of GMAuxiliary.eel, to copy it | GamePlayer.jsfx-inc:20404 |
| `j` |  | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+1) % box[2]; | GamePlayer.jsfx-inc:20388 |
| `k` |  | module | log système / log utilisateur (show_SysLog) | box[7] = max(0, box[7]-1); | GamePlayer.jsfx-inc:20387 |
| `l` |  | module | log système / log utilisateur (show_SysLog) | box[6] = max(0, box[6]-1); | GamePlayer.jsfx-inc:20385 |
| `m` |  | module | log système / log utilisateur (show_SysLog) | box[6] = min(20, box[6]+1); | GamePlayer.jsfx-inc:20384 |
| `p` |  | module | log système / log utilisateur (show_SysLog) | sysout(SysLogBox); | GamePlayer.jsfx-inc:20403 |
| `t` |  | module | log système / log utilisateur (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | GamePlayer.jsfx-inc:20389 |
| `v` |  | module | log système / log utilisateur (show_SysLog) | ShowConfig(); | GamePlayer.jsfx-inc:20390 |
| `z` |  | module | log système / log utilisateur (show_SysLog) | box[7] = 0; | GamePlayer.jsfx-inc:20386 |
| `Up` |  | module | log système / log utilisateur (show_SysLog) | box[7] = max(0, box[7]-10); | GamePlayer.jsfx-inc:20391 |
| `Down` |  | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+10) % box[2]; | GamePlayer.jsfx-inc:20392 |
| `Left` | none | module | log système / log utilisateur (show_SysLog) | box[7] = 0; | GamePlayer.jsfx-inc:20393 |
| `Right` | none | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+100) % box[2]; | GamePlayer.jsfx-inc:20394 |
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
| `+` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact += max(0.1, padStGFact * 0.1); | GamePlayer.jsfx-inc:25721 |
| `-` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact = max(0, padStGFact - padStGFact * 0.1); | GamePlayer.jsfx-inc:25724 |
| `=` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact = 2; | GamePlayer.jsfx-inc:25727 |
| `+` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell + 1)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24569 |
| `+` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = (currCpMode + 1) % 3; | GamePlayer.jsfx-inc:24629 |
| `-` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24572 |
| `:` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24572 |
| `=` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell + 1)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24569 |
| `=` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = (currCpMode + 1) % 3; | GamePlayer.jsfx-inc:24629 |
| `A` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 2, 0) | GamePlayer.jsfx-inc:24414 |
| `E` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 10, 0) | GamePlayer.jsfx-inc:24416 |
| `I` |  | module | paramètres dynamiques (show_Dyn_pars) | interType = 1; | GamePlayer.jsfx-inc:24420 |
| `R` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 25, 0) | GamePlayer.jsfx-inc:24417 |
| `T` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 50, 0) | GamePlayer.jsfx-inc:24418 |
| `X` |  | module | paramètres dynamiques (show_Dyn_pars) | interType = 2; | GamePlayer.jsfx-inc:24427 |
| `Y` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 75, 0) | GamePlayer.jsfx-inc:24419 |
| `Z` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 5, 0) | GamePlayer.jsfx-inc:24415 |
| `_` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:24572 |
| `a` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // abend edit | GamePlayer.jsfx-inc:24611 |
| `a` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 0; | GamePlayer.jsfx-inc:24620 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy current currpad | GamePlayer.jsfx-inc:24544 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy if valid | GamePlayer.jsfx-inc:24580 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy to "65" | GamePlayer.jsfx-inc:24933 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs1, mSL_Dyn_Flg1_def); | GamePlayer.jsfx-inc:24637 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs2, mSL_Dyn_Flg2_def); | GamePlayer.jsfx-inc:24645 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_And_Mask = mSL_Dyn_Mask_def; | GamePlayer.jsfx-inc:24653 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_Or_Mask = mSL_Dyn_Mask_def; | GamePlayer.jsfx-inc:24661 |
| `i` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // install in clip and save right now | GamePlayer.jsfx-inc:24602 |
| `m` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 2; | GamePlayer.jsfx-inc:24626 |
| `p` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  65; | GamePlayer.jsfx-inc:24557 |
| `p` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 1; | GamePlayer.jsfx-inc:24623 |
| `q` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  66; | GamePlayer.jsfx-inc:24560 |
| `r` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  67; | GamePlayer.jsfx-inc:24563 |
| `s` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  68; | GamePlayer.jsfx-inc:24566 |
| `s` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // save right now | GamePlayer.jsfx-inc:24594 |
| `t` |  | module | paramètres dynamiques (show_Dyn_pars) | // alternate "show mode" | GamePlayer.jsfx-inc:24674 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste to currpad | GamePlayer.jsfx-inc:24549 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste to clip if valid | GamePlayer.jsfx-inc:24587 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste "65" | GamePlayer.jsfx-inc:24941 |
| `x` |  | module | paramètres dynamiques (show_Dyn_pars) | // alternate "show mode" | GamePlayer.jsfx-inc:24666 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  0; | GamePlayer.jsfx-inc:24554 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs1, 0); | GamePlayer.jsfx-inc:24634 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs2, 0); | GamePlayer.jsfx-inc:24642 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_And_Mask = 0; | GamePlayer.jsfx-inc:24650 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_Or_Mask = 0; | GamePlayer.jsfx-inc:24658 |
| `Left` |  | module | paramètres dynamiques (show_Dyn_pars) | iKPar = (iKPar + paramDynCnt - 1) % paramDynCnt; | GamePlayer.jsfx-inc:24847 |
| `Right` |  | module | paramètres dynamiques (show_Dyn_pars) | iKPar = (iKPar + 1) % paramDynCnt; | GamePlayer.jsfx-inc:24848 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | GamePlayer.jsfx-inc:27093 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | GamePlayer.jsfx-inc:27065 |
| `Backspace` |  | onglet | commandes d'onglet (do_Generic_Commands) | flagStopOne += 1; | GamePlayer.jsfx-inc:18778 |
| `"` |  | onglet | commandes d'onglet (do_Generic_Commands) | parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:18773 |
| `#` |  | onglet | commandes d'onglet (do_Generic_Commands) | ui_GFXdoNow \|= 1; ui_GFXReason = 38; | GamePlayer.jsfx-inc:18739 |
| `$` |  | onglet | commandes d'onglet (do_Generic_Commands) | setRModeRec(); | GamePlayer.jsfx-inc:18753 |
| `&` |  | onglet | commandes d'onglet (do_Generic_Commands) | setPlayMark(-1, psKPlaying, recOptMarkReplay ? psKReplaying : 0, 0); | GamePlayer.jsfx-inc:18749 |
| `'` |  | onglet | commandes d'onglet (do_Generic_Commands) | setRModeSwitch(); | GamePlayer.jsfx-inc:18760 |
| `;` |  | onglet | commandes d'onglet (do_Generic_Commands) | DynParamsReset(); | GamePlayer.jsfx-inc:18757 |
| `<` |  | onglet | commandes d'onglet (do_Generic_Commands) | switchAuto(); ui_GFXdoNow \|= 1; ui_GFXReason = 38; | GamePlayer.jsfx-inc:18732 |
| `>` |  | onglet | commandes d'onglet (do_Generic_Commands) | ui_GFXdoNow \|= 1; parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:18735 |
| `@` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 11\|ActFlg1, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:18743 |
| `\|` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '\|' : switch to previous tabulation | GamePlayer.jsfx-inc:18794 |
| `}` |  | onglet | commandes d'onglet (do_Generic_Commands) | // switch tabulations | GamePlayer.jsfx-inc:18802 |
| `~` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '~' : switch to next tabulation | GamePlayer.jsfx-inc:18798 |
| `Del` |  | onglet | commandes d'onglet (do_Generic_Commands) | studPrefDispPanes = 1 + (studPrefDispPanes % 4) ; | GamePlayer.jsfx-inc:18781 |
| `0x80` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18729 |
| `0x90` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18729 |
| `à` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 11\|ActFlg1, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:18743 |
| `0xF9` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18729 |
| `0x42A` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '~' : switch to next tabulation | GamePlayer.jsfx-inc:18798 |
| `Del` |  | onglet | commandes d'onglet (do_Generic_Commands) | // clearCmd(); | GamePlayer.jsfx-inc:18724 |
| `End` |  | onglet | commandes d'onglet (do_Generic_Commands) | Kbtp = cmdClMdBase + GvPlayTypGrLoop; | GamePlayer.jsfx-inc:18770 |
| `F10` |  | onglet | commandes d'onglet (do_Generic_Commands) | // switch tabulations | GamePlayer.jsfx-inc:18802 |
| `F11` |  | onglet | commandes d'onglet (do_Generic_Commands) | uix_switch += 1; | GamePlayer.jsfx-inc:18786 |
| `F12` |  | onglet | commandes d'onglet (do_Generic_Commands) | studPrefDispPanes = 1 + (studPrefDispPanes % 4) ; | GamePlayer.jsfx-inc:18781 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:586 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:587 |
| `a` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 0 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25556 |
| `c` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispClip; | GamePlayer.jsfx-inc:25577 |
| `d` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 10 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25566 |
| `e` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 2 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25558 |
| `f` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 11 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25567 |
| `g` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 12 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25568 |
| `h` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 13 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25569 |
| `i` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 7 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25563 |
| `j` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 14 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25570 |
| `k` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 15 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25571 |
| `l` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispRng; | GamePlayer.jsfx-inc:25575 |
| `m` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispErr; | GamePlayer.jsfx-inc:25576 |
| `q` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 8 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25564 |
| `r` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 3 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25559 |
| `s` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 9 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25565 |
| `t` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 4 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25560 |
| `u` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 6 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25562 |
| `v` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispGrp; | GamePlayer.jsfx-inc:25573 |
| `w` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispPar; | GamePlayer.jsfx-inc:25572 |
| `x` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispGBk; | GamePlayer.jsfx-inc:25574 |
| `y` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 5 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25561 |
| `z` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 1 \| FLdoForcePlay; | GamePlayer.jsfx-inc:25557 |

## FilePlayer

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris → panneau → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys).

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:108 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:110 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:109 |
| `+` |  | module | File Player Status (do_local_Control) | gfx_col_width = min(560, gfx_col_width + 10) ; | FilePlayer.jsfx-inc:7154 |
| `-` |  | module | File Player Status (do_local_Control) | gfx_col_width = max(260, gfx_col_width - 10) ; | FilePlayer.jsfx-inc:7155 |
| `=` |  | module | File Player Status (do_local_Control) | gfx_col_width = gfx_col_def_width ; | FilePlayer.jsfx-inc:7156 |
| `A` |  | module | File Player Status (do_local_Control) | info_config(0, 4, 5, 6, 7, 8, 1, 2, 3, 9, 10, 11); | FilePlayer.jsfx-inc:7152 |
| `Z` |  | module | File Player Status (do_local_Control) | info_config(0, 1, 2, 3); | FilePlayer.jsfx-inc:7153 |
| `a` |  | module | File Player Status (do_local_Control) | nbligMax = min(glIsizCnt, nbligMax+1) ; | FilePlayer.jsfx-inc:7157 |
| `s` |  | module | File Player Status (do_local_Control) | nbligMax = max(1, nbligMax-1); memset(glIsizTab, 0, glIsizCnt); | FilePlayer.jsfx-inc:7158 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | FilePlayer.jsfx-inc:7330 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | FilePlayer.jsfx-inc:7330 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | FilePlayer.jsfx-inc:7342 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | FilePlayer.jsfx-inc:7343 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | FilePlayer.jsfx-inc:7344 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | FilePlayer.jsfx-inc:7345 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | FilePlayer.jsfx-inc:7346 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | FilePlayer.jsfx-inc:7347 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | FilePlayer.jsfx-inc:7348 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | FilePlayer.jsfx-inc:7349 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | FilePlayer.jsfx-inc:7351 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | FilePlayer.jsfx-inc:7335 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | FilePlayer.jsfx-inc:7334 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | FilePlayer.jsfx-inc:7332 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | FilePlayer.jsfx-inc:7331 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | FilePlayer.jsfx-inc:7350 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | FilePlayer.jsfx-inc:7336 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | FilePlayer.jsfx-inc:7333 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | FilePlayer.jsfx-inc:7338 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | FilePlayer.jsfx-inc:7339 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | FilePlayer.jsfx-inc:7340 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | FilePlayer.jsfx-inc:7341 |
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
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | ScriptMaster.jsfx-inc:2563 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | ScriptMaster.jsfx-inc:2563 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | ScriptMaster.jsfx-inc:2575 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | ScriptMaster.jsfx-inc:2576 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | ScriptMaster.jsfx-inc:2577 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | ScriptMaster.jsfx-inc:2578 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | ScriptMaster.jsfx-inc:2579 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | ScriptMaster.jsfx-inc:2580 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | ScriptMaster.jsfx-inc:2581 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | ScriptMaster.jsfx-inc:2582 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | ScriptMaster.jsfx-inc:2584 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | ScriptMaster.jsfx-inc:2568 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | ScriptMaster.jsfx-inc:2567 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | ScriptMaster.jsfx-inc:2565 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | ScriptMaster.jsfx-inc:2564 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | ScriptMaster.jsfx-inc:2583 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | ScriptMaster.jsfx-inc:2569 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | ScriptMaster.jsfx-inc:2566 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | ScriptMaster.jsfx-inc:2571 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | ScriptMaster.jsfx-inc:2572 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | ScriptMaster.jsfx-inc:2573 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | ScriptMaster.jsfx-inc:2574 |
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
| `h` |  | module | Space 3D (la vue) (show_Space3D_Pad) | s3d_style = !s3d_style; ui_GFXdoNow \|= 4;  // balls, or crosses and halos | Diffusion-3-Space3D.jsfx-inc:748 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Diffusion-3.jsfx-inc:5718 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Diffusion-3.jsfx-inc:5718 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | Diffusion-3.jsfx-inc:5730 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | Diffusion-3.jsfx-inc:5731 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | Diffusion-3.jsfx-inc:5732 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | Diffusion-3.jsfx-inc:5733 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | Diffusion-3.jsfx-inc:5734 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | Diffusion-3.jsfx-inc:5735 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | Diffusion-3.jsfx-inc:5736 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | Diffusion-3.jsfx-inc:5737 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | Diffusion-3.jsfx-inc:5739 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | Diffusion-3.jsfx-inc:5723 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | Diffusion-3.jsfx-inc:5722 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | Diffusion-3.jsfx-inc:5720 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | Diffusion-3.jsfx-inc:5719 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | Diffusion-3.jsfx-inc:5738 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | Diffusion-3.jsfx-inc:5724 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | Diffusion-3.jsfx-inc:5721 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | Diffusion-3.jsfx-inc:5726 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | Diffusion-3.jsfx-inc:5727 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | Diffusion-3.jsfx-inc:5728 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | Diffusion-3.jsfx-inc:5729 |
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
| `$` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_opt = s3d_opt ~ s3d_oLevels; | Diffusion-3.jsfx-inc:6110 |
| `%` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_opt = s3d_opt ~ s3d_oGains; | Diffusion-3.jsfx-inc:6113 |
| `,` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_dist = min(12, s3d_dist * 1.02); | Diffusion-3.jsfx-inc:6104 |
| `/` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_lbg = !sx_lbg; | Diffusion-3.jsfx-inc:6116 |
| `:` |  | module | écran Live : boîte sous la souris (mouse_hover) | HP_Dr_updsize(mh_cur_box, max(10, floor(mh_cur_box[bx_sfact]  * 0.96))); | Diffusion-3.jsfx-inc:6097 |
| `;` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_dist = max(1.8, s3d_dist * 0.98); | Diffusion-3.jsfx-inc:6101 |
| `=` |  | module | écran Live : boîte sous la souris (mouse_hover) | HP_Dr_updsize(mh_cur_box, max(mh_cur_box[bx_sfact] + 1, ceil(mh_cur_box[bx_sfact]  * 1.04))); | Diffusion-3.jsfx-inc:6094 |
| `?` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_SetView((sx_view + 1) % 4); | Diffusion-3.jsfx-inc:6107 |
| `Up` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_el += 0.05; | Diffusion-3.jsfx-inc:6123 |
| `Down` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_el -= 0.05; | Diffusion-3.jsfx-inc:6126 |
| `Home` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_SetView(sx_view); | Diffusion-3.jsfx-inc:6119 |
| `Left` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_az -= 0.05; | Diffusion-3.jsfx-inc:6129 |
| `Right` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_az += 0.05; | Diffusion-3.jsfx-inc:6132 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:791 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:763 |
| `-` |  | onglet | écran Live : commandes (do_live_actions) | check_graph = 1 - check_graph; | Diffusion-3.jsfx-inc:5284 |
| `.` |  | onglet | écran Live : commandes (do_live_actions) | mk_display_box(1, "*", 1, -1, 180); | Diffusion-3.jsfx-inc:5287 |
| `C` |  | onglet | écran Live : commandes (do_live_actions) | coloriterate = coloriterate ? 0: 1; | Diffusion-3.jsfx-inc:5232 |
| `a` |  | onglet | écran Live : commandes (do_live_actions) | wrefresh = 1; | Diffusion-3.jsfx-inc:5225 |
| `b` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(7, 0, actpars); | Diffusion-3.jsfx-inc:5263 |
| `c` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5228 |
| `g` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5217 |
| `i` |  | onglet | écran Live : commandes (do_live_actions) | HP_Box[bx_activ] & bx__drawbox ? HP_Box[bx_activ] &= 0x7FFFFFFF - bx__drawbox : HP_Box[bx_activ] \|= bx__drawb… | Diffusion-3.jsfx-inc:5281 |
| `j` |  | onglet | écran Live : commandes (do_live_actions) | HP_ViewN = (HP_ViewN + 1) % 4; | Diffusion-3.jsfx-inc:5276 |
| `k` |  | onglet | écran Live : commandes (do_live_actions) | statkeyd = statkeyd ? 0 : 1; | Diffusion-3.jsfx-inc:5248 |
| `l` |  | onglet | écran Live : commandes (do_live_actions) | // Clear non permanent boxes | Diffusion-3.jsfx-inc:5269 |
| `m` |  | onglet | écran Live : commandes (do_live_actions) | show_mouse = 1 - show_mouse; | Diffusion-3.jsfx-inc:5241 |
| `p` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5259 |
| `r` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = 1; | Diffusion-3.jsfx-inc:5244 |
| `s` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5221 |
| `t` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5251 |
| `u` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1;  // next tabulation (Tab, Shift + Tab : see do_Plugin_Keys) | Diffusion-3.jsfx-inc:5255 |
| `v` |  | onglet | écran Live : commandes (do_live_actions) | show_used = 1 - show_used; | Diffusion-3.jsfx-inc:5238 |
| `w` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(8, 0, actpars); | Diffusion-3.jsfx-inc:5273 |
| `x` |  | onglet | écran Live : commandes (do_live_actions) | wrefresh = 3; | Diffusion-3.jsfx-inc:5235 |
| `z` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(10, 0, actpars); | Diffusion-3.jsfx-inc:5266 |
| `S` |  | plugin | commandes de Diffusion-3 (do_Plugin_Keys) | togglesliders(-1); | Diffusion-3.jsfx-inc:5301 |
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
| `Ctrl+A..Ctrl+D` |  | module | ? (its_Mod_LawMenu) | (xx !== a) ? ( p[its_Mod_Depth] = (xx === da) ? d0 : its_ModA_Dep[xx]; ); | Interstys.jsfx-inc:14241 |
| `Ctrl+E..Ctrl+G` |  | module | ? (its_Mod_LawMenu) | f = f - (f & 0x3F60) + 32 * (xx - 5); | Interstys.jsfx-inc:14245 |
| `Backspace..G` |  | module | ? (its_Mod_LawMenu) | f = f - (f & 0x3F60) + 32 * its_ModS_Crv + 256 * (xx - 8); | Interstys.jsfx-inc:14246 |
| `K..M` |  | module | ? (its_Mod_LawMenu) | f = f - (f & (its_ModF_NoSl \| its_ModF_Att)) + ((xx === 75) ? its_ModF_NoSl : (xx === 77) ? its_ModF_Att : 0)… | Interstys.jsfx-inc:14250 |
| `Ctrl+A` | Cmd | module | ? (show_Curves_Pad) | i = 0; loop(b[its_Crv_N], its_CrvSelF[i] = 1; i += 1;); | Interstys.jsfx-inc:17752 |
| `Ctrl+A..Ctrl+E` |  | module | ? (show_Curves_Pad) | its_Crv_Pre(k); its_Crv_Commit();  // (Undo) | Interstys.jsfx-inc:17832 |
| `Ctrl+A..Ctrl+E` |  | module | ? (show_Curves_Pad) | // a new curve (the one shown, replaced) | Interstys.jsfx-inc:17833 |
| `a` | Cmd | module | ? (show_Curves_Pad) | i = 0; loop(b[its_Crv_N], its_CrvSelF[i] = 1; i += 1;); | Interstys.jsfx-inc:17752 |
| `d` |  | module | ? (show_Curves_Pad) | its_Crv_Dump(k) | Interstys.jsfx-inc:17748 |
| `s` |  | module | ? (show_Curves_Pad) | its_Crv_SetSus(b, k, -2) | Interstys.jsfx-inc:17750 |
| `d` |  | module | ? (show_Effect_Pad) | GM_Dump(fx, its_Efx_BlkSize, sprintf(#, "Effect %d", fxn+1)) | Interstys.jsfx-inc:16237 |
| `d` |  | module | Line (show_Line_Pad) | GM_Dump(lcbl, its_Lin_BlkSize, sprintf(#, "Line %d", lnr+1)) | Interstys.jsfx-inc:15556 |
| `d` |  | module | Reader (show_Reader_Pad) | GM_Dump(rcbl, its_Rdr_BlkSize, sprintf(#, "Reader %d", rdr+1)) | Interstys.jsfx-inc:14539 |
| `r` |  | module | Reader (show_Reader_Pad) | // toggle run/pause state | Interstys.jsfx-inc:15186 |
| `t` |  | module | Reader (show_Reader_Pad) | RDBL[6] = (RDBL[6] + 1) % 3; | Interstys.jsfx-inc:15190 |
| `d` |  | module | Writer (show_Writer_Pad) | GM_Dump(wcbl, its_Wrt_BlkSize, sprintf(#, "Writer %d", wrt+1)) | Interstys.jsfx-inc:16513 |
| `+` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = min(its_WaveHMax, h + its_WaveHStep); | Interstys.jsfx-inc:1357 |
| `-` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = max(its_WaveHMin, h - its_WaveHStep); | Interstys.jsfx-inc:1361 |
| `=` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = min(its_WaveHMax, h + its_WaveHStep); | Interstys.jsfx-inc:1357 |
| `v` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | fp[0] = fp[0] ~ its_WaveOver; | Interstys.jsfx-inc:1365 |
| `w` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | fp[0] = fp[0] ~ its_WaveHide; | Interstys.jsfx-inc:1354 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Interstys.jsfx-inc:13699 |
| `Space` |  | module | log système (show_SysLog) | mSL_log(box, " "); | Interstys.jsfx-inc:13699 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | Interstys.jsfx-inc:13711 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | Interstys.jsfx-inc:13712 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | Interstys.jsfx-inc:13713 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | Interstys.jsfx-inc:13714 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | Interstys.jsfx-inc:13715 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | Interstys.jsfx-inc:13716 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | Interstys.jsfx-inc:13717 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | Interstys.jsfx-inc:13718 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of GMAuxiliary.eel, to copy it | Interstys.jsfx-inc:13720 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | Interstys.jsfx-inc:13704 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | Interstys.jsfx-inc:13703 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | Interstys.jsfx-inc:13701 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | Interstys.jsfx-inc:13700 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | Interstys.jsfx-inc:13719 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | Interstys.jsfx-inc:13705 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | Interstys.jsfx-inc:13702 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | Interstys.jsfx-inc:13707 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | Interstys.jsfx-inc:13708 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | Interstys.jsfx-inc:13709 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | Interstys.jsfx-inc:13710 |
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
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | Interstys.jsfx-inc:18815 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | Interstys.jsfx-inc:18787 |
| `S` |  | plugin | commandes d'Interstys (do_Plugin_Keys) | // the generic sliders in the panel of REAPER | Interstys.jsfx-inc:13104 |
| `U` |  | plugin | commandes d'Interstys (do_Plugin_Keys) | gui_show_UI = gui_show_UI ? 0 : 1; | Interstys.jsfx-inc:13101 |
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
