# Touches du clavier dans CMGS

*Fichier produit par `CMGS-aux/tools/keys_table.py` : ne pas le modifier à la main, relancer le script.*

Pour chaque plugin, les touches testées par le code `@gfx`, par niveau dans l'ordre où les niveaux voient la touche pendant une trame. « Modif. » : les modificateurs testés sur la même ligne (vide : non testés, la touche agit avec ou sans modificateur ; « none » : sans modificateur). L'action est le début du code exécuté. Les bibliothèques partagées (mSL_Dbg_Memory…) apparaissent dans chaque plugin qui les inclut.

## Conflits

### GamePlayer

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (18)

- `$` : commandes d'onglet (GamePlayer.jsfx-inc:18835), pas au-dessus de : Scripts / Settings
- `Backspace` : commandes d'onglet (GamePlayer.jsfx-inc:18860), pas au-dessus de : ?, Scripts / Settings
- `S` : raccourcis de l'utilisateur, puis S : les sliders Ctl (sans raccourci sur S) (GamePlayer.jsfx-inc:27795), pas au-dessus de : Clips selection
- `Shift+Down` : largeur des colonnes (GamePlayer.jsfx-inc:27598), pas au-dessus de : mémoire (débogueur)
- `Shift+Left` : largeur des colonnes (GamePlayer.jsfx-inc:27567), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (GamePlayer.jsfx-inc:27539), pas au-dessus de : mémoire (débogueur)
- `Shift+Tab` : onglet suivant / précédent (ui-lib-JJ-GUI.jsfx-inc:680), pas au-dessus de : ?
- `Shift+Up` : largeur des colonnes (GamePlayer.jsfx-inc:27598), pas au-dessus de : mémoire (débogueur)
- `Tab` : onglet suivant / précédent (ui-lib-JJ-GUI.jsfx-inc:681), pas au-dessus de : ?
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

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (11)

- `Shift+Down` : largeur des colonnes (mSL_Panes.jsfx-inc:918), pas au-dessus de : mémoire (débogueur)
- `Shift+Left` : largeur des colonnes (mSL_Panes.jsfx-inc:887), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (mSL_Panes.jsfx-inc:859), pas au-dessus de : mémoire (débogueur)
- `Shift+Up` : largeur des colonnes (mSL_Panes.jsfx-inc:918), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `s` : commandes système (mSL_System_Keys.jsfx-inc:37), pas au-dessus de : File Player Status
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : log système

### ScriptMaster

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (10)

- `Shift+Down` : largeur des colonnes (mSL_Panes.jsfx-inc:918), pas au-dessus de : mémoire (débogueur)
- `Shift+Left` : largeur des colonnes (mSL_Panes.jsfx-inc:887), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (mSL_Panes.jsfx-inc:859), pas au-dessus de : mémoire (débogueur)
- `Shift+Up` : largeur des colonnes (mSL_Panes.jsfx-inc:918), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : log système

### Diffusion-3

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (18)

- `S` : commandes de Diffusion-3 (Diffusion-3.jsfx-inc:5856), pas au-dessus de : ?
- `Shift+Down` : largeur des colonnes (mSL_Panes.jsfx-inc:918), pas au-dessus de : mémoire (débogueur)
- `Shift+Left` : largeur des colonnes (mSL_Panes.jsfx-inc:887), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (mSL_Panes.jsfx-inc:859), pas au-dessus de : mémoire (débogueur)
- `Shift+Tab` : onglet suivant / précédent (ui-lib-JJ-GUI.jsfx-inc:680), pas au-dessus de : ?
- `Shift+Up` : largeur des colonnes (mSL_Panes.jsfx-inc:918), pas au-dessus de : mémoire (débogueur)
- `Tab` : onglet suivant / précédent (ui-lib-JJ-GUI.jsfx-inc:681), pas au-dessus de : ?
- `a` : écran Live : commandes (Diffusion-3.jsfx-inc:5780), pas au-dessus de : écran Live : boîte sous la souris
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : ?, mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : ?, mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : ?, log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : ?, log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : ?, Edit A ... D (éditeurs de points), log système, mémoire (débogueur)
- `n` : commandes système (mSL_System_Keys.jsfx-inc:27), pas au-dessus de : ?
- `o` : commandes système (mSL_System_Keys.jsfx-inc:36), pas au-dessus de : ?
- `r` : commandes système (mSL_System_Keys.jsfx-inc:30), pas au-dessus de : ?
- `s` : commandes système (mSL_System_Keys.jsfx-inc:37), pas au-dessus de : ?
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : ?, log système

### Interstys

**Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la même touche : c'est la règle, mais à éviter pour les commandes importantes)** (10)

- `Shift+Down` : largeur des colonnes (Interstys.jsfx-inc:29497), pas au-dessus de : mémoire (débogueur)
- `Shift+Left` : largeur des colonnes (Interstys.jsfx-inc:29466), pas au-dessus de : mémoire (débogueur)
- `Shift+Right` : largeur des colonnes (Interstys.jsfx-inc:29438), pas au-dessus de : mémoire (débogueur)
- `Shift+Up` : largeur des colonnes (Interstys.jsfx-inc:29497), pas au-dessus de : mémoire (débogueur)
- `c` : commandes système (mSL_System_Keys.jsfx-inc:28), pas au-dessus de : mémoire (débogueur)
- `g` : commandes système (mSL_System_Keys.jsfx-inc:24), pas au-dessus de : mémoire (débogueur)
- `k` : commandes système (mSL_System_Keys.jsfx-inc:25), pas au-dessus de : log système, mémoire (débogueur)
- `l` : commandes système (mSL_System_Keys.jsfx-inc:29), pas au-dessus de : log système, mémoire (débogueur)
- `m` : commandes système (mSL_System_Keys.jsfx-inc:26), pas au-dessus de : log système, mémoire (débogueur)
- `t` : commandes système (mSL_System_Keys.jsfx-inc:35), pas au-dessus de : log système

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
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:128 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:130 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `Backspace` |  | module | ? (uix_jp_make) | min(3, ui_jvariant) : (ui_jstyle != 0) | ui-lib-JJ-GUI.jsfx-inc:1277 |
| `Backspace` |  | module | ? (uix_jp_measure) | (k = 10); d = uix_jp_dist(t[8 * k], uix_jp_bgc); (d < uix_jp_mBg) ? (uix_jp_mBg = d; uix_jp_mBgR = k;); k += 1… | ui-lib-JJ-GUI.jsfx-inc:1234 |
| `Backspace` |  | module | ? (uix_jrole_name) | "Information" : (k === 9) ? "Empty" : (k === 10) ? "Alert" : "Role"; | mSL_ui_Pads.jsfx-inc:702 |
| `Tab` |  | module | ? (uix_jrole_name) | "Empty" : (k === 10) ? "Alert" : "Role"; | mSL_ui_Pads.jsfx-inc:702 |
| `g` |  | module | Banks (doBanksInteract) | GM_key_take('g'); | GamePlayer.jsfx-inc:23006 |
| `g` |  | module | Banks (doBanksInteract) | BnkGrpLock(); | GamePlayer.jsfx-inc:23007 |
| `Ctrl+C` |  | module | Clips selection (show_Clips_Selection) | i = curB; loop(100,  // ^C | GamePlayer.jsfx-inc:21684 |
| `Enter` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // Enter : play (not Space : play / stop in REAPER) | GamePlayer.jsfx-inc:21569 |
| `Enter` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // Enter : play (not Space : play / stop in REAPER) | GamePlayer.jsfx-inc:21619 |
| `Ctrl+Z` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? ( | GamePlayer.jsfx-inc:21692 |
| `!` |  | module | Clips selection (show_Clips_Selection) | gmem[clClAlias+xcell] = 0;  // remove the alias and clear the entry | GamePlayer.jsfx-inc:21586 |
| `%` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs - 1 + showStates) % showStates ; | GamePlayer.jsfx-inc:21652 |
| `+` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? (  // validate/unvalidate all entries | GamePlayer.jsfx-inc:21639 |
| `/` |  | module | Clips selection (show_Clips_Selection) | i = curB; loop(100,  // clear all entries | GamePlayer.jsfx-inc:21631 |
| `0..9` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 1 | GamePlayer.jsfx-inc:21573 |
| `0..9` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 0 - 9 | GamePlayer.jsfx-inc:21623 |
| `:` |  | module | Clips selection (show_Clips_Selection) | gmem[clInfStart+xcell] = 0;  // clear the entry | GamePlayer.jsfx-inc:21581 |
| `=` |  | module | Clips selection (show_Clips_Selection) | (gmem[clInfStart+xcell] < -10000) ? (  // (un)validate the entry | GamePlayer.jsfx-inc:21592 |
| `A..Z` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 10 - N | GamePlayer.jsfx-inc:21627 |
| `a..z` |  | module | Clips selection (show_Clips_Selection) | GM_key_take(zzch);  // play clip with partial 10 - N | GamePlayer.jsfx-inc:21577 |
| `0xA0` |  | module | Clips selection (show_Clips_Selection) | GvPlayCl3 = cellAlt;  // alt+' '  => play | GamePlayer.jsfx-inc:21663 |
| `Up` | none | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 1) % 10; | GamePlayer.jsfx-inc:21449 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 100 - 10) % 100; | GamePlayer.jsfx-inc:21608 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs + 1) % showStates ; | GamePlayer.jsfx-inc:21655 |
| `Up` |  | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 1) % 10; | GamePlayer.jsfx-inc:21676 |
| `Down` | none | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 10 - 1) % 10; | GamePlayer.jsfx-inc:21446 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 10) % 100; | GamePlayer.jsfx-inc:21605 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | showClNbrs = (showClNbrs - 1 + showStates) % showStates ; | GamePlayer.jsfx-inc:21652 |
| `Down` |  | module | Clips selection (show_Clips_Selection) | slBankset = (slBankset + 10 - 1) % 10; | GamePlayer.jsfx-inc:21673 |
| `Home` | none | module | Clips selection (show_Clips_Selection) | slBankset = slGroupNum = 0; | GamePlayer.jsfx-inc:21452 |
| `Home` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB; | GamePlayer.jsfx-inc:21611 |
| `Left` | none | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 10 - 1) % 10; | GamePlayer.jsfx-inc:21443 |
| `Left` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 100 - 1) % 100; | GamePlayer.jsfx-inc:21602 |
| `Left` |  | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 10 - 1) % 10; | GamePlayer.jsfx-inc:21670 |
| `Right` | none | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 1) % 10; | GamePlayer.jsfx-inc:21440 |
| `Right` |  | module | Clips selection (show_Clips_Selection) | cellAlt = curB + (cellAlt + 1) % 100; | GamePlayer.jsfx-inc:21599 |
| `Right` |  | module | Clips selection (show_Clips_Selection) | slGroupNum = (slGroupNum + 1) % 10; | GamePlayer.jsfx-inc:21667 |
| `Up` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + readerCount - 8) % readerCount; | GamePlayer.jsfx-inc:20207 |
| `Down` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + 8) % readerCount; | GamePlayer.jsfx-inc:20201 |
| `Left` | none | module | Generator (show_Generator) | unitbkl[0] = (unitbkl[0] - 1 + 4) % 4; | GamePlayer.jsfx-inc:20193 |
| `Left` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + readerCount - 1) % readerCount; | GamePlayer.jsfx-inc:20204 |
| `Right` | none | module | Generator (show_Generator) | unitbkl[0] = (unitbkl[0] + 1) % 4; | GamePlayer.jsfx-inc:20190 |
| `Right` | none | module | Generator (show_Generator) | unitbkl[2] = upla = (upla + 1) % readerCount; | GamePlayer.jsfx-inc:20198 |
| `x` |  | module | LED interactive (show_jled) | led[ui_jled_status] = led[ui_jled_status] > 0.5 ? 0 : 1; | mSL_ui_Pads.jsfx-inc:118 |
| `*` |  | module | Play control (show_Play_Control) | // very slow stop all... | GamePlayer.jsfx-inc:26406 |
| `a` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypAnyClip | GamePlayer.jsfx-inc:26403 |
| `b` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypBank | GamePlayer.jsfx-inc:26402 |
| `c` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypClip | GamePlayer.jsfx-inc:26397 |
| `g` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypGroup | GamePlayer.jsfx-inc:26401 |
| `p` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypPartial | GamePlayer.jsfx-inc:26400 |
| `r` |  | module | Play control (show_Play_Control) | GvPlayTyp = GvPlayTypRange | GamePlayer.jsfx-inc:26399 |
| `s` |  | module | Play control (show_Play_Control) | GvPlayTyp = 0 | GamePlayer.jsfx-inc:26398 |
| `Left` |  | module | Play control (show_Play_Control) | GvPlayTyp = (GvPlayTyp + menuActModeCnt - 1) % menuActModeCnt | GamePlayer.jsfx-inc:26404 |
| `Right` |  | module | Play control (show_Play_Control) | GvPlayTyp = (GvPlayTyp + 1) % menuActModeCnt | GamePlayer.jsfx-inc:26405 |
| `Backspace` |  | module | Scripts / Settings (show_Scripts) | (v !== 0\|v) ? (  // backspace | GamePlayer.jsfx-inc:23544 |
| `$` |  | module | Scripts / Settings (show_Scripts) | ssnd = 1; | GamePlayer.jsfx-inc:23563 |
| `+` |  | module | Scripts / Settings (show_Scripts) | v = v + 1; | GamePlayer.jsfx-inc:23532 |
| `-` |  | module | Scripts / Settings (show_Scripts) | v = v + u - 1; | GamePlayer.jsfx-inc:23535 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23510 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23514 |
| `0..9` |  | module | Scripts / Settings (show_Scripts) | // goto marker "n" | GamePlayer.jsfx-inc:24618 |
| `=` |  | module | Scripts / Settings (show_Scripts) | v = v + 1; | GamePlayer.jsfx-inc:23532 |
| `A..F` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23522 |
| `X` |  | module | Scripts / Settings (show_Scripts) | padSettingC7fmt = padSettingC7fmt === 0; | GamePlayer.jsfx-inc:23529 |
| `Z` |  | module | Scripts / Settings (show_Scripts) | v = 0; | GamePlayer.jsfx-inc:23526 |
| `_` |  | module | Scripts / Settings (show_Scripts) | v = v + u - 1; | GamePlayer.jsfx-inc:23535 |
| `a..f` |  | module | Scripts / Settings (show_Scripts) | GM_key_take(zzch); | GamePlayer.jsfx-inc:23518 |
| `a` |  | module | Scripts / Settings (show_Scripts) | parSet(p_GvAutoMd, ! paramValues[p_GvAutoMd]); | GamePlayer.jsfx-inc:24560 |
| `e` |  | module | Scripts / Settings (show_Scripts) | playSkipSlnc = ! playSkipSlnc ; | GamePlayer.jsfx-inc:24615 |
| `g` |  | module | Scripts / Settings (show_Scripts) | recOptMarkReplay = ! recOptMarkReplay ; | GamePlayer.jsfx-inc:24580 |
| `h` |  | module | Scripts / Settings (show_Scripts) | setRModeStop(); | GamePlayer.jsfx-inc:24600 |
| `i` |  | module | Scripts / Settings (show_Scripts) | // invert read direction | GamePlayer.jsfx-inc:24583 |
| `j` |  | module | Scripts / Settings (show_Scripts) | playJmpLoop = ! playJmpLoop ; | GamePlayer.jsfx-inc:24574 |
| `k` |  | module | Scripts / Settings (show_Scripts) | playAndLock ? SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:24566 |
| `l` |  | module | Scripts / Settings (show_Scripts) | playRepeatMd = ! playRepeatMd ; | GamePlayer.jsfx-inc:24577 |
| `m` |  | module | Scripts / Settings (show_Scripts) | replayUnMute = ! replayUnMute; | GamePlayer.jsfx-inc:24604 |
| `o` |  | module | Scripts / Settings (show_Scripts) | recOptLockSnds = ! recOptLockSnds; | GamePlayer.jsfx-inc:24607 |
| `p` |  | module | Scripts / Settings (show_Scripts) | setPModeSwitch(); | GamePlayer.jsfx-inc:24553 |
| `q` |  | module | Scripts / Settings (show_Scripts) | playReeval = 1; | GamePlayer.jsfx-inc:24556 |
| `r` |  | module | Scripts / Settings (show_Scripts) | setRModeSwitch(); | GamePlayer.jsfx-inc:24563 |
| `s` |  | module | Scripts / Settings (show_Scripts) | playModeStep = ! playModeStep ; | GamePlayer.jsfx-inc:24593 |
| `t` |  | module | Scripts / Settings (show_Scripts) | recOptRecReplay = ! recOptRecReplay ; | GamePlayer.jsfx-inc:24597 |
| `u` |  | module | Scripts / Settings (show_Scripts) | playAndUnLock = ! playAndUnLock ; | GamePlayer.jsfx-inc:24570 |
| `w` |  | module | Scripts / Settings (show_Scripts) | // various play speed | GamePlayer.jsfx-inc:24588 |
| `x` |  | module | Scripts / Settings (show_Scripts) | padSettingC7fmt = padSettingC7fmt === 0; | GamePlayer.jsfx-inc:23529 |
| `z` |  | module | Scripts / Settings (show_Scripts) | v = 0; | GamePlayer.jsfx-inc:23526 |
| `z` |  | module | Scripts / Settings (show_Scripts) | parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:24610 |
| `Up` |  | module | Scripts / Settings (show_Scripts) | Settings_F_Sel = (Settings_F_Sel - 1 + FlagsCount) % FlagsCount; | GamePlayer.jsfx-inc:23560 |
| `Up` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? 10 : (jmc === 0x04) ? 60 : (jmc === 0x10) ? 300 : (jmc === 0x14) ? 1800 : 0; | GamePlayer.jsfx-inc:24629 |
| `Down` |  | module | Scripts / Settings (show_Scripts) | Settings_F_Sel = (Settings_F_Sel + 1) % FlagsCount; | GamePlayer.jsfx-inc:23557 |
| `Down` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? -10 : (jmc === 0x04) ? -60 : (jmc === 0x10) ? -300 : (jmc === 0x14) ? -1800 : 0; | GamePlayer.jsfx-inc:24632 |
| `Left` | none | module | Scripts / Settings (show_Scripts) | v = (padSettingC7fmt === 0) ? v << 4 : v * 10; | GamePlayer.jsfx-inc:23538 |
| `Left` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? -1 : (jmc === 0x04) ? -0.1 : (jmc === 0x10) ? -0.01 : (jmc === 0x14) ? -0.001 : 0; | GamePlayer.jsfx-inc:24623 |
| `Right` | none | module | Scripts / Settings (show_Scripts) | v = (padSettingC7fmt === 0) ? v >> 4 : (v / 10); | GamePlayer.jsfx-inc:23541 |
| `Right` |  | module | Scripts / Settings (show_Scripts) | inc = (jmc === 0x00) ? 1 : (jmc === 0x04) ? 0.1 : (jmc === 0x10) ? 0.01 : (jmc === 0x14) ? 0.001 : 0; | GamePlayer.jsfx-inc:24626 |
| `+` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += 1; | GamePlayer.jsfx-inc:20561 |
| `-` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += MIDI_States_siz - 1; | GamePlayer.jsfx-inc:20564 |
| `0..9` |  | module | Sensors (show_Sensors) | GM_key_take(zzch); | GamePlayer.jsfx-inc:20567 |
| `2` |  | module | Sensors (show_Sensors) | setSensorSize(zzch) | GamePlayer.jsfx-inc:20624 |
| `3` |  | module | Sensors (show_Sensors) | setSensorSize(zzch) | GamePlayer.jsfx-inc:20624 |
| `=` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += MIDI_States_siz - 1; | GamePlayer.jsfx-inc:20564 |
| `_` |  | module | Sensors (show_Sensors) | MIDI_Sens_mode += 1; | GamePlayer.jsfx-inc:20561 |
| `!` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 2.5, 0, 0); | GamePlayer.jsfx-inc:22377 |
| `E` |  | module | Units (show_Units) | gmem[Un+RCB_State_Changed] \|= i_M_Rst; | GamePlayer.jsfx-inc:22352 |
| `E` |  | module | Units (show_Units) | gmem[Un+RCB_Cl_Flgs] = 1;  // also Lock entry (the key is already taken) | GamePlayer.jsfx-inc:22355 |
| `a` |  | module | Units (show_Units) | BplayerA[2] = rd; | GamePlayer.jsfx-inc:22336 |
| `b` |  | module | Units (show_Units) | BplayerB[2] = rd; | GamePlayer.jsfx-inc:22340 |
| `c` |  | module | Units (show_Units) | BplayerC[2] = rd; | GamePlayer.jsfx-inc:22344 |
| `d` |  | module | Units (show_Units) | BplayerD[2] = rd; | GamePlayer.jsfx-inc:22348 |
| `e` |  | module | Units (show_Units) | gmem[Un+RCB_State_Changed] \|= i_M_Rst; | GamePlayer.jsfx-inc:22352 |
| `f` |  | module | Units (show_Units) | SchedAddTask(5, 8, -1, -1, 1, 0, 0); | GamePlayer.jsfx-inc:22361 |
| `g` |  | module | Units (show_Units) | parSet(p_GvAutoMd, ! paramValues[p_GvAutoMd]); | GamePlayer.jsfx-inc:22333 |
| `h` |  | module | Units (show_Units) | SchedAddTask(5, 8, -1, -1, 0.20, 0, 0); | GamePlayer.jsfx-inc:22364 |
| `i` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 3.5, 0, 0); | GamePlayer.jsfx-inc:22380 |
| `j` |  | module | Units (show_Units) | Kbtp = cmdClMdBase + GvPlayTypGrLoop; | GamePlayer.jsfx-inc:22402 |
| `k` |  | module | Units (show_Units) | SchedAddTask(5, 7, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22367 |
| `l` |  | module | Units (show_Units) | SchedAddTask(5, 1\|ActFlg1, 1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22330 |
| `m` |  | module | Units (show_Units) | SchedAddTask(5, 6, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22312 |
| `n` |  | module | Units (show_Units) | lmode = ! lmode ; | GamePlayer.jsfx-inc:22383 |
| `o` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 5, 0, 0); | GamePlayer.jsfx-inc:22389 |
| `p` |  | module | Units (show_Units) | SchedAddTask(5, 9, -1, -1, 8, 0, 0); | GamePlayer.jsfx-inc:22392 |
| `q` |  | module | Units (show_Units) | qmode = ! qmode ; | GamePlayer.jsfx-inc:22386 |
| `r` |  | module | Units (show_Units) | SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22395 |
| `s` |  | module | Units (show_Units) | SchedAddTask(5, 5\|ActFlg1, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22316 |
| `t` |  | module | Units (show_Units) | SchedAddTask(5, 3, rd, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22370 |
| `u` |  | module | Units (show_Units) | SchedAddTask(5, 1, 1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22327 |
| `v` |  | module | Units (show_Units) | gDispPlay = rd; | GamePlayer.jsfx-inc:22374 |
| `w` |  | module | Units (show_Units) | SchedAddTask(5, 2, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22399 |
| `z` |  | module | Units (show_Units) | SchedAddTask(5, 1\|ActFlg1, 3, -1, 0, 0, 0); | GamePlayer.jsfx-inc:22324 |
| `Enter` |  | module | log système / log utilisateur (show_SysLog) | mSL_log(box, " ");  // Enter : a blank line (not Space : play / stop in REAPER) | GamePlayer.jsfx-inc:20734 |
| `1` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 1; | GamePlayer.jsfx-inc:20746 |
| `2` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 2; | GamePlayer.jsfx-inc:20747 |
| `3` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 3; | GamePlayer.jsfx-inc:20748 |
| `4` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 4; | GamePlayer.jsfx-inc:20749 |
| `5` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 5; | GamePlayer.jsfx-inc:20750 |
| `6` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 6; | GamePlayer.jsfx-inc:20751 |
| `7` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 7; | GamePlayer.jsfx-inc:20752 |
| `8` |  | module | log système / log utilisateur (show_SysLog) | box[5] = 8; | GamePlayer.jsfx-inc:20753 |
| `P` |  | module | log système / log utilisateur (show_SysLog) | sysout(SysLogBox, 31);  // the log in the console of CMGS-auxiliary.eel, to copy it | GamePlayer.jsfx-inc:20755 |
| `j` |  | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+1) % box[2]; | GamePlayer.jsfx-inc:20739 |
| `k` |  | module | log système / log utilisateur (show_SysLog) | box[7] = max(0, box[7]-1); | GamePlayer.jsfx-inc:20738 |
| `l` |  | module | log système / log utilisateur (show_SysLog) | box[6] = max(0, box[6]-1); | GamePlayer.jsfx-inc:20736 |
| `m` |  | module | log système / log utilisateur (show_SysLog) | box[6] = min(20, box[6]+1); | GamePlayer.jsfx-inc:20735 |
| `p` |  | module | log système / log utilisateur (show_SysLog) | sysout(SysLogBox); | GamePlayer.jsfx-inc:20754 |
| `t` |  | module | log système / log utilisateur (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | GamePlayer.jsfx-inc:20740 |
| `v` |  | module | log système / log utilisateur (show_SysLog) | ShowConfig(); | GamePlayer.jsfx-inc:20741 |
| `z` |  | module | log système / log utilisateur (show_SysLog) | box[7] = 0; | GamePlayer.jsfx-inc:20737 |
| `Up` |  | module | log système / log utilisateur (show_SysLog) | box[7] = max(0, box[7]-10); | GamePlayer.jsfx-inc:20742 |
| `Down` |  | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+10) % box[2]; | GamePlayer.jsfx-inc:20743 |
| `Left` | none | module | log système / log utilisateur (show_SysLog) | box[7] = 0; | GamePlayer.jsfx-inc:20744 |
| `Right` | none | module | log système / log utilisateur (show_SysLog) | box[7] = (box[7]+100) % box[2]; | GamePlayer.jsfx-inc:20745 |
| `+` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `-` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = max(hmin, hneed - 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:855 |
| `=` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:247 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:298 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:243 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:294 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:253 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:304 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:307 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:262 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:265 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:259 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:256 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:250 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:301 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:219 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:237 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:282 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:222 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:240 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:285 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:225 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:231 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:288 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:228 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:234 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:291 |
| `+` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact += max(0.1, padStGFact * 0.1); | GamePlayer.jsfx-inc:26169 |
| `-` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact = max(0, padStGFact - padStGFact * 0.1); | GamePlayer.jsfx-inc:26172 |
| `=` |  | module | pad Studio (show_Studio_Play_Pad) | padStGFact = 2; | GamePlayer.jsfx-inc:26175 |
| `+` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell + 1)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:25003 |
| `+` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = (currCpMode + 1) % 3; | GamePlayer.jsfx-inc:25063 |
| `-` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:25006 |
| `:` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:25006 |
| `=` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell + 1)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:25003 |
| `=` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = (currCpMode + 1) % 3; | GamePlayer.jsfx-inc:25063 |
| `A` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 2, 0) | GamePlayer.jsfx-inc:24833 |
| `E` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 10, 0) | GamePlayer.jsfx-inc:24835 |
| `I` |  | module | paramètres dynamiques (show_Dyn_pars) | interType = 1; | GamePlayer.jsfx-inc:24839 |
| `R` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 25, 0) | GamePlayer.jsfx-inc:24836 |
| `T` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 50, 0) | GamePlayer.jsfx-inc:24837 |
| `X` |  | module | paramètres dynamiques (show_Dyn_pars) | interType = 2; | GamePlayer.jsfx-inc:24846 |
| `Y` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 75, 0) | GamePlayer.jsfx-inc:24838 |
| `Z` |  | module | paramètres dynamiques (show_Dyn_pars) | DynParamModulate(0, 5, 0) | GamePlayer.jsfx-inc:24834 |
| `_` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell = (max(0, currcell - 1 + padDynPrstSizT)) % (padDynPrstSizT); | GamePlayer.jsfx-inc:25006 |
| `a` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // abend edit | GamePlayer.jsfx-inc:25045 |
| `a` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 0; | GamePlayer.jsfx-inc:25054 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy current currpad | GamePlayer.jsfx-inc:24978 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy if valid | GamePlayer.jsfx-inc:25014 |
| `c` |  | module | paramètres dynamiques (show_Dyn_pars) | // copy to "65" | GamePlayer.jsfx-inc:25369 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs1, mSL_Dyn_Flg1_def); | GamePlayer.jsfx-inc:25071 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs2, mSL_Dyn_Flg2_def); | GamePlayer.jsfx-inc:25079 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_And_Mask = mSL_Dyn_Mask_def; | GamePlayer.jsfx-inc:25087 |
| `f` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_Or_Mask = mSL_Dyn_Mask_def; | GamePlayer.jsfx-inc:25095 |
| `i` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // install in clip and save right now | GamePlayer.jsfx-inc:25036 |
| `m` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 2; | GamePlayer.jsfx-inc:25060 |
| `p` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  65; | GamePlayer.jsfx-inc:24991 |
| `p` |  | module | paramètres dynamiques (show_Dyn_pars) | currCpMode = 1; | GamePlayer.jsfx-inc:25057 |
| `q` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  66; | GamePlayer.jsfx-inc:24994 |
| `r` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  67; | GamePlayer.jsfx-inc:24997 |
| `s` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  68; | GamePlayer.jsfx-inc:25000 |
| `s` |  | module | paramètres dynamiques (show_Dyn_pars) | (currVal && (currDPars < 0)) ? (  // save right now | GamePlayer.jsfx-inc:25028 |
| `t` |  | module | paramètres dynamiques (show_Dyn_pars) | // alternate "show mode" | GamePlayer.jsfx-inc:25108 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste to currpad | GamePlayer.jsfx-inc:24983 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste to clip if valid | GamePlayer.jsfx-inc:25021 |
| `v` |  | module | paramètres dynamiques (show_Dyn_pars) | // paste "65" | GamePlayer.jsfx-inc:25377 |
| `x` |  | module | paramètres dynamiques (show_Dyn_pars) | // alternate "show mode" | GamePlayer.jsfx-inc:25100 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | currcell =  0; | GamePlayer.jsfx-inc:24988 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs1, 0); | GamePlayer.jsfx-inc:25068 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_set_par(currpad, p_Dyn_Flgs2, 0); | GamePlayer.jsfx-inc:25076 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_And_Mask = 0; | GamePlayer.jsfx-inc:25084 |
| `z` |  | module | paramètres dynamiques (show_Dyn_pars) | dyn_Or_Mask = 0; | GamePlayer.jsfx-inc:25092 |
| `Left` |  | module | paramètres dynamiques (show_Dyn_pars) | iKPar = (iKPar + paramDynCnt - 1) % paramDynCnt; | GamePlayer.jsfx-inc:25282 |
| `Right` |  | module | paramètres dynamiques (show_Dyn_pars) | iKPar = (iKPar + 1) % paramDynCnt; | GamePlayer.jsfx-inc:25283 |
| `Up` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | GamePlayer.jsfx-inc:27598 |
| `Down` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | GamePlayer.jsfx-inc:27598 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | GamePlayer.jsfx-inc:27567 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | GamePlayer.jsfx-inc:27539 |
| `Backspace` |  | onglet | commandes d'onglet (do_Generic_Commands) | flagStopOne += 1; | GamePlayer.jsfx-inc:18860 |
| `"` |  | onglet | commandes d'onglet (do_Generic_Commands) | parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:18855 |
| `#` |  | onglet | commandes d'onglet (do_Generic_Commands) | ui_GFXdoNow \|= 1; ui_GFXReason = 38; | GamePlayer.jsfx-inc:18821 |
| `$` |  | onglet | commandes d'onglet (do_Generic_Commands) | setRModeRec(); | GamePlayer.jsfx-inc:18835 |
| `&` |  | onglet | commandes d'onglet (do_Generic_Commands) | setPlayMark(-1, psKPlaying, recOptMarkReplay ? psKReplaying : 0, 0); | GamePlayer.jsfx-inc:18831 |
| `'` |  | onglet | commandes d'onglet (do_Generic_Commands) | setRModeSwitch(); | GamePlayer.jsfx-inc:18842 |
| `;` |  | onglet | commandes d'onglet (do_Generic_Commands) | DynParamsReset(); | GamePlayer.jsfx-inc:18839 |
| `<` |  | onglet | commandes d'onglet (do_Generic_Commands) | switchAuto(); ui_GFXdoNow \|= 1; ui_GFXReason = 38; | GamePlayer.jsfx-inc:18814 |
| `>` |  | onglet | commandes d'onglet (do_Generic_Commands) | ui_GFXdoNow \|= 1; parSet(p_GvAutoMd, 0); | GamePlayer.jsfx-inc:18817 |
| `@` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 11\|ActFlg1, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:18825 |
| `\|` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '\|' : switch to previous tabulation | GamePlayer.jsfx-inc:18876 |
| `}` |  | onglet | commandes d'onglet (do_Generic_Commands) | // switch tabulations | GamePlayer.jsfx-inc:18884 |
| `~` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '~' : switch to next tabulation | GamePlayer.jsfx-inc:18880 |
| `Del` |  | onglet | commandes d'onglet (do_Generic_Commands) | studPrefDispPanes = 1 + (studPrefDispPanes % 4) ; | GamePlayer.jsfx-inc:18863 |
| `0x80` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18811 |
| `0x90` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18811 |
| `à` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 11\|ActFlg1, -1, -1, 0, 0, 0); | GamePlayer.jsfx-inc:18825 |
| `0xF9` |  | onglet | commandes d'onglet (do_Generic_Commands) | SchedAddTask(5, 1\|ActFlg1, 1, -1, -1, 0, 0);  // ù '☒' ou F17 | GamePlayer.jsfx-inc:18811 |
| `0x42A` |  | onglet | commandes d'onglet (do_Generic_Commands) | // '~' : switch to next tabulation | GamePlayer.jsfx-inc:18880 |
| `Del` |  | onglet | commandes d'onglet (do_Generic_Commands) | // clearCmd(); | GamePlayer.jsfx-inc:18806 |
| `End` |  | onglet | commandes d'onglet (do_Generic_Commands) | Kbtp = cmdClMdBase + GvPlayTypGrLoop; | GamePlayer.jsfx-inc:18852 |
| `F10` |  | onglet | commandes d'onglet (do_Generic_Commands) | // switch tabulations | GamePlayer.jsfx-inc:18884 |
| `F11` |  | onglet | commandes d'onglet (do_Generic_Commands) | uix_switch += 1; | GamePlayer.jsfx-inc:18868 |
| `F12` |  | onglet | commandes d'onglet (do_Generic_Commands) | studPrefDispPanes = 1 + (studPrefDispPanes % 4) ; | GamePlayer.jsfx-inc:18863 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:680 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:681 |
| `S` |  | plugin | raccourcis de l'utilisateur, puis S : les sliders Ctl (sans raccourci sur S) (do_Plugin_Keys) | gsl_Show(-1); | GamePlayer.jsfx-inc:27795 |
| `a` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 0 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26003 |
| `c` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispClip; | GamePlayer.jsfx-inc:26024 |
| `d` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 10 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26013 |
| `e` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 2 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26005 |
| `f` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 11 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26014 |
| `g` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 12 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26015 |
| `h` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 13 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26016 |
| `i` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 7 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26010 |
| `j` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 14 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26017 |
| `k` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 15 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26018 |
| `l` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispRng; | GamePlayer.jsfx-inc:26022 |
| `m` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispErr; | GamePlayer.jsfx-inc:26023 |
| `q` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 8 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26011 |
| `r` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 3 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26006 |
| `s` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 9 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26012 |
| `t` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 4 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26007 |
| `u` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 6 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26009 |
| `v` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispGrp; | GamePlayer.jsfx-inc:26020 |
| `w` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispPar; | GamePlayer.jsfx-inc:26019 |
| `x` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | StdnumLastM = lastTime; StdnumUnchkd = padStDispGBk; | GamePlayer.jsfx-inc:26021 |
| `y` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 5 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26008 |
| `z` |  | pad Studio | pad Studio : jeu au clavier (aussi au survol du pad) (do_StudioPadKeyboard) | Kbtp = cmdPadBase + 1 \| FLdoForcePlay; | GamePlayer.jsfx-inc:26004 |

## FilePlayer

Ordre : Cmd + - + = 0 (taille d'affichage) → module sous la souris → panneau → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys).

| Touche | Modif. | Niveau | Module | Action | Source |
|---|---|---|---|---|---|
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:128 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:130 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `Backspace` |  | module | ? (uix_jp_make) | min(3, ui_jvariant) : (ui_jstyle != 0) | ui-lib-JJ-GUI.jsfx-inc:1277 |
| `Backspace` |  | module | ? (uix_jp_measure) | (k = 10); d = uix_jp_dist(t[8 * k], uix_jp_bgc); (d < uix_jp_mBg) ? (uix_jp_mBg = d; uix_jp_mBgR = k;); k += 1… | ui-lib-JJ-GUI.jsfx-inc:1234 |
| `+` |  | module | File Player Status (do_local_Control) | gfx_col_width = min(560, gfx_col_width + 10) ; | FilePlayer.jsfx-inc:7266 |
| `-` |  | module | File Player Status (do_local_Control) | gfx_col_width = max(260, gfx_col_width - 10) ; | FilePlayer.jsfx-inc:7267 |
| `=` |  | module | File Player Status (do_local_Control) | gfx_col_width = gfx_col_def_width ; | FilePlayer.jsfx-inc:7268 |
| `A` |  | module | File Player Status (do_local_Control) | info_config(0, 4, 5, 6, 7, 8, 1, 2, 3, 9, 10, 11); | FilePlayer.jsfx-inc:7264 |
| `Z` |  | module | File Player Status (do_local_Control) | info_config(0, 1, 2, 3); | FilePlayer.jsfx-inc:7265 |
| `a` |  | module | File Player Status (do_local_Control) | nbligMax = min(glIsizCnt, nbligMax+1) ; | FilePlayer.jsfx-inc:7269 |
| `s` |  | module | File Player Status (do_local_Control) | nbligMax = max(1, nbligMax-1); memset(glIsizTab, 0, glIsizCnt); | FilePlayer.jsfx-inc:7270 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " ");  // Enter : a blank line (not Space : play / stop in REAPER) | FilePlayer.jsfx-inc:7443 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | FilePlayer.jsfx-inc:7455 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | FilePlayer.jsfx-inc:7456 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | FilePlayer.jsfx-inc:7457 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | FilePlayer.jsfx-inc:7458 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | FilePlayer.jsfx-inc:7459 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | FilePlayer.jsfx-inc:7460 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | FilePlayer.jsfx-inc:7461 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | FilePlayer.jsfx-inc:7462 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of CMGS-auxiliary.eel, to copy it | FilePlayer.jsfx-inc:7464 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | FilePlayer.jsfx-inc:7448 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | FilePlayer.jsfx-inc:7447 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | FilePlayer.jsfx-inc:7445 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | FilePlayer.jsfx-inc:7444 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | FilePlayer.jsfx-inc:7463 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | FilePlayer.jsfx-inc:7449 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | FilePlayer.jsfx-inc:7446 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | FilePlayer.jsfx-inc:7451 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | FilePlayer.jsfx-inc:7452 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | FilePlayer.jsfx-inc:7453 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | FilePlayer.jsfx-inc:7454 |
| `+` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `-` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = max(hmin, hneed - 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:855 |
| `=` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:247 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:298 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:243 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:294 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:253 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:304 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:307 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:262 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:265 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:259 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:256 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:250 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:301 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:219 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:237 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:282 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:222 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:240 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:285 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:225 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:231 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:288 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:228 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:234 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:291 |
| `Up` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | mSL_Panes.jsfx-inc:918 |
| `Down` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | mSL_Panes.jsfx-inc:918 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:887 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:859 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:680 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:681 |
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
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:128 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:130 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `Backspace` |  | module | ? (uix_jp_make) | min(3, ui_jvariant) : (ui_jstyle != 0) | ui-lib-JJ-GUI.jsfx-inc:1277 |
| `Backspace` |  | module | ? (uix_jp_measure) | (k = 10); d = uix_jp_dist(t[8 * k], uix_jp_bgc); (d < uix_jp_mBg) ? (uix_jp_mBg = d; uix_jp_mBgR = k;); k += 1… | ui-lib-JJ-GUI.jsfx-inc:1234 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " ");  // Enter : a blank line (not Space : play / stop in REAPER) | ScriptMaster.jsfx-inc:2636 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | ScriptMaster.jsfx-inc:2648 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | ScriptMaster.jsfx-inc:2649 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | ScriptMaster.jsfx-inc:2650 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | ScriptMaster.jsfx-inc:2651 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | ScriptMaster.jsfx-inc:2652 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | ScriptMaster.jsfx-inc:2653 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | ScriptMaster.jsfx-inc:2654 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | ScriptMaster.jsfx-inc:2655 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of CMGS-auxiliary.eel, to copy it | ScriptMaster.jsfx-inc:2657 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | ScriptMaster.jsfx-inc:2641 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | ScriptMaster.jsfx-inc:2640 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | ScriptMaster.jsfx-inc:2638 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | ScriptMaster.jsfx-inc:2637 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | ScriptMaster.jsfx-inc:2656 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | ScriptMaster.jsfx-inc:2642 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | ScriptMaster.jsfx-inc:2639 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | ScriptMaster.jsfx-inc:2644 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | ScriptMaster.jsfx-inc:2645 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | ScriptMaster.jsfx-inc:2646 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | ScriptMaster.jsfx-inc:2647 |
| `+` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `-` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = max(hmin, hneed - 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:855 |
| `=` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:247 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:298 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:243 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:294 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:253 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:304 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:307 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:262 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:265 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:259 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:256 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:250 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:301 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:219 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:237 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:282 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:222 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:240 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:285 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:225 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:231 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:288 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:228 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:234 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:291 |
| `Up` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | mSL_Panes.jsfx-inc:918 |
| `Down` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | mSL_Panes.jsfx-inc:918 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:887 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:859 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:680 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:681 |
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
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:128 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:130 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `Ctrl+C..Ctrl+E` |  | module | ? (ce_OpsDo) | ce_Normalize(k - 3) | Diffusion-3-ConfEditor.jsfx-inc:1236 |
| `Ctrl+A..0x84` |  | module | ? (ms_TrNext) | r = k; | Diffusion-3-MetaSurface.jsfx-inc:2106 |
| `Backspace` |  | module | ? (uix_jp_make) | min(3, ui_jvariant) : (ui_jstyle != 0) | ui-lib-JJ-GUI.jsfx-inc:1277 |
| `Backspace` |  | module | ? (uix_jp_measure) | (k = 10); d = uix_jp_dist(t[8 * k], uix_jp_bgc); (d < uix_jp_mBg) ? (uix_jp_mBg = d; uix_jp_mBgR = k;); k += 1… | ui-lib-JJ-GUI.jsfx-inc:1234 |
| `Backspace` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | (ce_Wt(ce_row, ce_col) > 0) ? (ce_Keep(); ce_Set(ce_row, ce_col, 0);); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2560 |
| `+` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_Keep(); ce_Set(ce_row, ce_col, ce_Wt(ce_row, ce_col) + 1); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2558 |
| `-` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | (ce_Wt(ce_row, ce_col) > 0) ? (ce_Keep(); ce_Set(ce_row, ce_col, ce_Wt(ce_row, ce_col) - 1);); ui_GFXdoNow \|=… | Diffusion-3-ConfEditor.jsfx-inc:2559 |
| `<` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_mode = !ce_mode; ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2555 |
| `=` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_Keep(); ce_Set(ce_row, ce_col, ce_Wt(ce_row, ce_col) + 1); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2558 |
| `>` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_pres = (ce_pres + 1) % 6; ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2554 |
| `a` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_Level3(); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2552 |
| `a` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_mode = !ce_mode; ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2555 |
| `e` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | (ce_Wt(ce_row, ce_col) > 0) ? (ce_Keep(); ce_Set(ce_row, ce_col, 0);); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2560 |
| `v` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_SetView3((ce_View3Of() + 1) % 4); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2553 |
| `v` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_opt = ce_opt ~ ce_oNo3D; ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2556 |
| `z` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_Undo(); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2557 |
| `Up` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_row = max(0, ce_row - 1); ce_Show(); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2564 |
| `Del` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | (ce_Wt(ce_row, ce_col) > 0) ? (ce_Keep(); ce_Set(ce_row, ce_col, 0);); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2560 |
| `Down` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_row = min(ce_N - 1, ce_row + 1); ce_Show(); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2565 |
| `Left` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_col = max(0, ce_col - 1); ce_Show(); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2562 |
| `Right` |  | module | Conf Editor (éditeur de configurations) (show_ConfEditor_Pad) | ce_col = min(ce_P - 1, ce_col + 1); ce_Show(); ui_GFXdoNow \|= 4; | Diffusion-3-ConfEditor.jsfx-inc:2563 |
| `Ctrl+A` | Cmd | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_SelOp(e, 0); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2551 |
| `Ctrl+E` | Cmd | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_SelOp(e, 1); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2552 |
| `Backspace` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_DelSelK(e); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2560 |
| `<` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | st[ed_sMode] = (st[ed_sMode] + 1) % 3; ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2557 |
| `>` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | st[ed_sGrid] = (st[ed_sGrid] + 1) % 6; ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2558 |
| `a` | Cmd | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_SelOp(e, 0); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2551 |
| `a` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_Level(e); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2554 |
| `e` | Cmd | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_SelOp(e, 1); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2552 |
| `m` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | st[ed_sMode] = 1; ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2555 |
| `p` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | st[ed_sMode] = 2; ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2556 |
| `v` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | !st[ed_sLock] ? ed_SetView(e, (max(-1, st[ed_sView]) + 1) % 4); ui_GFXdoNow \|= 4;  // (Lock 2D : no) | Diffusion-3-Edit.jsfx-inc:2553 |
| `z` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_Undo(e); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2559 |
| `Up` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_Sel1(e, 0); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2564 |
| `Del` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_DelSelK(e); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2560 |
| `Down` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_Sel1(e, n - 1); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2565 |
| `Left` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_Sel1(e, (cur <= 0) ? n - 1 : cur - 1); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2562 |
| `Right` |  | module | Edit A ... D (éditeurs de points) (show_Edit_Pad) | ed_Sel1(e, (cur + 1) % n); ui_GFXdoNow \|= 4; | Diffusion-3-Edit.jsfx-inc:2563 |
| `<` |  | module | Space A ... D (la vue) (show_Space_Pad) | s3d_mtarget = !s3d_mtarget; ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1565 |
| `>` |  | module | Space A ... D (la vue) (show_Space_Pad) | s3d_PresSet((s3d_PresCur() + 1) % 6); ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1566 |
| `a` |  | module | Space A ... D (la vue) (show_Space_Pad) | s3d_level(); ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1570 |
| `h` |  | module | Space A ... D (la vue) (show_Space_Pad) | s3d_style = !s3d_style; ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1564 |
| `v` |  | module | Space A ... D (la vue) (show_Space_Pad) | sx_SetView((sx_view + 1) % 4); ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1569 |
| `w` |  | module | Space A ... D (la vue) (show_Space_Pad) | s3d_opt = s3d_opt ~ s3d_oClamp; ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1568 |
| `x` |  | module | Space A ... D (la vue) (show_Space_Pad) | s3d_opt = s3d_opt ~ s3d_oTraj; ui_GFXdoNow \|= 4; | Diffusion-3-Space3D.jsfx-inc:1567 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " ");  // Enter : a blank line (not Space : play / stop in REAPER) | Diffusion-3.jsfx-inc:6274 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | Diffusion-3.jsfx-inc:6286 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | Diffusion-3.jsfx-inc:6287 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | Diffusion-3.jsfx-inc:6288 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | Diffusion-3.jsfx-inc:6289 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | Diffusion-3.jsfx-inc:6290 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | Diffusion-3.jsfx-inc:6291 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | Diffusion-3.jsfx-inc:6292 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | Diffusion-3.jsfx-inc:6293 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of CMGS-auxiliary.eel, to copy it | Diffusion-3.jsfx-inc:6295 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | Diffusion-3.jsfx-inc:6279 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | Diffusion-3.jsfx-inc:6278 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | Diffusion-3.jsfx-inc:6276 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | Diffusion-3.jsfx-inc:6275 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | Diffusion-3.jsfx-inc:6294 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | Diffusion-3.jsfx-inc:6280 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | Diffusion-3.jsfx-inc:6277 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | Diffusion-3.jsfx-inc:6282 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | Diffusion-3.jsfx-inc:6283 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | Diffusion-3.jsfx-inc:6284 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | Diffusion-3.jsfx-inc:6285 |
| `+` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `-` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = max(hmin, hneed - 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:855 |
| `=` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:247 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:298 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:243 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:294 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:253 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:304 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:307 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:262 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:265 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:259 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:256 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:250 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:301 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:219 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:237 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:282 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:222 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:240 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:285 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:225 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:231 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:288 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:228 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:234 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:291 |
| `$` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_opt = s3d_opt ~ s3d_oLevels; | Diffusion-3.jsfx-inc:6698 |
| `%` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_opt = s3d_opt ~ s3d_oGains; | Diffusion-3.jsfx-inc:6701 |
| `,` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_dist = min(12, s3d_dist * 1.02); | Diffusion-3.jsfx-inc:6685 |
| `/` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_lbg = !sx_lbg; | Diffusion-3.jsfx-inc:6704 |
| `:` |  | module | écran Live : boîte sous la souris (mouse_hover) | HP_Dr_updsize(mh_cur_box, max(10, floor(mh_cur_box[bx_sfact]  * 0.96))); | Diffusion-3.jsfx-inc:6677 |
| `;` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_dist = max(1.8, s3d_dist * 0.98); | Diffusion-3.jsfx-inc:6682 |
| `=` |  | module | écran Live : boîte sous la souris (mouse_hover) | HP_Dr_updsize(mh_cur_box, max(mh_cur_box[bx_sfact] + 1, ceil(mh_cur_box[bx_sfact]  * 1.04))); | Diffusion-3.jsfx-inc:6674 |
| `>` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_PresSet((s3d_PresCur() + 1) % 6); | Diffusion-3.jsfx-inc:6695 |
| `?` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_SetView((sx_view + 1) % 4); | Diffusion-3.jsfx-inc:6688 |
| `a` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_basis(); s3d_LevelStart(5); | Diffusion-3.jsfx-inc:6691 |
| `Up` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_el += 0.05; | Diffusion-3.jsfx-inc:6711 |
| `Down` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_el -= 0.05; | Diffusion-3.jsfx-inc:6714 |
| `Home` |  | module | écran Live : boîte sous la souris (mouse_hover) | sx_SetView(sx_view); | Diffusion-3.jsfx-inc:6707 |
| `Left` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_az -= 0.05; | Diffusion-3.jsfx-inc:6717 |
| `Right` |  | module | écran Live : boîte sous la souris (mouse_hover) | s3d_az += 0.05; | Diffusion-3.jsfx-inc:6720 |
| `Up` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | mSL_Panes.jsfx-inc:918 |
| `Down` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | mSL_Panes.jsfx-inc:918 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:887 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | mSL_Panes.jsfx-inc:859 |
| `-` |  | onglet | écran Live : commandes (do_live_actions) | check_graph = 1 - check_graph; | Diffusion-3.jsfx-inc:5839 |
| `.` |  | onglet | écran Live : commandes (do_live_actions) | mk_display_box(1, "*", 1, -1, 180); | Diffusion-3.jsfx-inc:5842 |
| `C` |  | onglet | écran Live : commandes (do_live_actions) | coloriterate = coloriterate ? 0: 1; | Diffusion-3.jsfx-inc:5787 |
| `a` |  | onglet | écran Live : commandes (do_live_actions) | wrefresh = 1; | Diffusion-3.jsfx-inc:5780 |
| `b` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(7, 0, actpars); | Diffusion-3.jsfx-inc:5818 |
| `c` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5783 |
| `g` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5772 |
| `i` |  | onglet | écran Live : commandes (do_live_actions) | HP_Box_Show(-1); | Diffusion-3.jsfx-inc:5836 |
| `j` |  | onglet | écran Live : commandes (do_live_actions) | HP_ViewN = (HP_ViewN + 1) % 4; | Diffusion-3.jsfx-inc:5831 |
| `k` |  | onglet | écran Live : commandes (do_live_actions) | statkeyd = statkeyd ? 0 : 1; | Diffusion-3.jsfx-inc:5803 |
| `l` |  | onglet | écran Live : commandes (do_live_actions) | // Clear non permanent boxes | Diffusion-3.jsfx-inc:5824 |
| `m` |  | onglet | écran Live : commandes (do_live_actions) | show_mouse = 1 - show_mouse; | Diffusion-3.jsfx-inc:5796 |
| `p` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5814 |
| `r` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = 1; | Diffusion-3.jsfx-inc:5799 |
| `s` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5776 |
| `t` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1; | Diffusion-3.jsfx-inc:5806 |
| `u` |  | onglet | écran Live : commandes (do_live_actions) | actpars[0] = -1;  // next tabulation (Tab, Shift + Tab : see do_Plugin_Keys) | Diffusion-3.jsfx-inc:5810 |
| `v` |  | onglet | écran Live : commandes (do_live_actions) | show_used = 1 - show_used; | Diffusion-3.jsfx-inc:5793 |
| `w` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(8, 0, actpars); | Diffusion-3.jsfx-inc:5828 |
| `x` |  | onglet | écran Live : commandes (do_live_actions) | wrefresh = 3; | Diffusion-3.jsfx-inc:5790 |
| `z` |  | onglet | écran Live : commandes (do_live_actions) | perform_action(10, 0, actpars); | Diffusion-3.jsfx-inc:5821 |
| `S` |  | plugin | commandes de Diffusion-3 (do_Plugin_Keys) | togglesliders(-1); | Diffusion-3.jsfx-inc:5856 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:680 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:681 |
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
| `+` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `-` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK - 1); 1 | ui-lib-JJ-GUI.jsfx-inc:128 |
| `0` |  | début de trame | taille d'affichage (GM_Size_Keys) | (ui_jzoom_set(ui_jzoomDef); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:130 |
| `=` |  | début de trame | taille d'affichage (GM_Size_Keys) | ui_jzoom_set(ui_jzoomK + 1); 1 | ui-lib-JJ-GUI.jsfx-inc:129 |
| `Backspace` |  | module | ? (uix_jp_make) | min(3, ui_jvariant) : (ui_jstyle != 0) | ui-lib-JJ-GUI.jsfx-inc:1277 |
| `Backspace` |  | module | ? (uix_jp_measure) | (k = 10); d = uix_jp_dist(t[8 * k], uix_jp_bgc); (d < uix_jp_mBg) ? (uix_jp_mBg = d; uix_jp_mBgR = k;); k += 1… | ui-lib-JJ-GUI.jsfx-inc:1234 |
| `Ctrl+A` | Cmd | module | Curves (show_Curves_Pad) | i = 0; loop(b[its_Crv_N], its_CrvSelF[i] = 1; i += 1;); | Interstys.jsfx-inc:28244 |
| `a` | Cmd | module | Curves (show_Curves_Pad) | i = 0; loop(b[its_Crv_N], its_CrvSelF[i] = 1; i += 1;); | Interstys.jsfx-inc:28244 |
| `d` |  | module | Curves (show_Curves_Pad) | its_Crv_Dump(k) | Interstys.jsfx-inc:28240 |
| `h` |  | module | Curves (show_Curves_Pad) | its_Crv_SetSus(b, k, -2) | Interstys.jsfx-inc:28242 |
| `d` |  | module | Effect (show_Effect_Pad) | GM_Dump(fx, its_Efx_BlkSize, sprintf(#, "Effect %d", fxn+1)) | Interstys.jsfx-inc:24897 |
| `+` |  | module | Effect : hauteur du graphique (VU meter, Limiter) (its_FxGraph_Keys) | hp[0] = max(its_FxGraphHMin, min(its_FxGraphHMax, h + its_FxGraphHStep)); | Interstys.jsfx-inc:24814 |
| `-` |  | module | Effect : hauteur du graphique (VU meter, Limiter) (its_FxGraph_Keys) | hp[0] = max(its_FxGraphHMin, min(its_FxGraphHMax, min(h, hs) - its_FxGraphHStep)); | Interstys.jsfx-inc:24817 |
| `=` |  | module | Effect : hauteur du graphique (VU meter, Limiter) (its_FxGraph_Keys) | hp[0] = max(its_FxGraphHMin, min(its_FxGraphHMax, h + its_FxGraphHStep)); | Interstys.jsfx-inc:24814 |
| `d` |  | module | Line (show_Line_Pad) | GM_Dump(lcbl, its_Lin_BlkSize, sprintf(#, "Line %d", lnr+1)) | Interstys.jsfx-inc:22902 |
| `d` |  | module | Reader (show_Reader_Pad) | GM_Dump(rcbl, its_Rdr_BlkSize, sprintf(#, "Reader %d", rdr+1)) | Interstys.jsfx-inc:21871 |
| `e` |  | module | Reader (show_Reader_Pad) | RDBL[6] = (RDBL[6] + 1) % 3;  // 'e' (extent, étendue) : the length shown of the region, Full / 10 s / 1 s | Interstys.jsfx-inc:22533 |
| `j` |  | module | Reader (show_Reader_Pad) | Rd_Set_Status(rdr, -1);  // 'j' (joue) : toggle run/pause state | Interstys.jsfx-inc:22530 |
| `d` |  | module | Writer (show_Writer_Pad) | GM_Dump(wcbl, its_Wrt_BlkSize, sprintf(#, "Writer %d", wrt+1)) | Interstys.jsfx-inc:25225 |
| `+` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = min(its_WaveHMax, h + its_WaveHStep); | Interstys.jsfx-inc:1685 |
| `-` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = max(its_WaveHMin, h - its_WaveHStep); | Interstys.jsfx-inc:1689 |
| `=` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | hp[0] = min(its_WaveHMax, h + its_WaveHStep); | Interstys.jsfx-inc:1685 |
| `v` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | fp[0] = fp[0] ~ its_WaveOver; | Interstys.jsfx-inc:1693 |
| `w` |  | module | forme d'onde (Line, Reader, Writer) (its_Wave_Keys) | fp[0] = fp[0] ~ its_WaveHide; | Interstys.jsfx-inc:1682 |
| `Enter` |  | module | log système (show_SysLog) | mSL_log(box, " ");  // Enter : a blank line (not Space : play / stop in REAPER) | Interstys.jsfx-inc:20656 |
| `1` |  | module | log système (show_SysLog) | box[5] = 1; | Interstys.jsfx-inc:20668 |
| `2` |  | module | log système (show_SysLog) | box[5] = 2; | Interstys.jsfx-inc:20669 |
| `3` |  | module | log système (show_SysLog) | box[5] = 3; | Interstys.jsfx-inc:20670 |
| `4` |  | module | log système (show_SysLog) | box[5] = 4; | Interstys.jsfx-inc:20671 |
| `5` |  | module | log système (show_SysLog) | box[5] = 5; | Interstys.jsfx-inc:20672 |
| `6` |  | module | log système (show_SysLog) | box[5] = 6; | Interstys.jsfx-inc:20673 |
| `7` |  | module | log système (show_SysLog) | box[5] = 7; | Interstys.jsfx-inc:20674 |
| `8` |  | module | log système (show_SysLog) | box[5] = 8; | Interstys.jsfx-inc:20675 |
| `P` |  | module | log système (show_SysLog) | sysout(box, 31);  // the log in the console of CMGS-auxiliary.eel, to copy it | Interstys.jsfx-inc:20677 |
| `j` |  | module | log système (show_SysLog) | box[7] = (box[7]+1) % box[2]; | Interstys.jsfx-inc:20661 |
| `k` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-1); | Interstys.jsfx-inc:20660 |
| `l` |  | module | log système (show_SysLog) | box[6] = max(0, box[6]-1); | Interstys.jsfx-inc:20658 |
| `m` |  | module | log système (show_SysLog) | box[6] = min(20, box[6]+1); | Interstys.jsfx-inc:20657 |
| `p` |  | module | log système (show_SysLog) | sysout(box);  // log in a text file (see mSL_show_Utilities) | Interstys.jsfx-inc:20676 |
| `t` |  | module | log système (show_SysLog) | nowTime(); mSL_log(SysLogBox, #nowis); | Interstys.jsfx-inc:20662 |
| `z` |  | module | log système (show_SysLog) | box[7] = 0; | Interstys.jsfx-inc:20659 |
| `Up` |  | module | log système (show_SysLog) | box[7] = max(0, box[7]-10); | Interstys.jsfx-inc:20664 |
| `Down` |  | module | log système (show_SysLog) | box[7] = (box[7]+10) % box[2]; | Interstys.jsfx-inc:20665 |
| `Left` | none | module | log système (show_SysLog) | box[7] = 0; | Interstys.jsfx-inc:20666 |
| `Right` | none | module | log système (show_SysLog) | box[7] = (box[7]+100) % box[2]; | Interstys.jsfx-inc:20667 |
| `+` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `-` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = max(hmin, hneed - 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:855 |
| `=` |  | module | mSL Console (la ligne de saisie n'a pas le clavier) (show_Console) | mcon_Hgt = min(1200, max(hmin, hneed) + 40); ui_GFXdoNow \|= 4; | mSL_Console.jsfx-inc:854 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:247 |
| `:` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 1; | mSL_Dbg_Memory.jsfx-inc:298 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:243 |
| `=` |  | module | mémoire (débogueur) (show_Memory) | // set this location as relative zero | mSL_Dbg_Memory.jsfx-inc:294 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[7] + knb * u_ms_y; | mSL_Dbg_Memory.jsfx-inc:253 |
| `c` |  | module | mémoire (débogueur) (show_Memory) | memoryBoxAdd = membox[16]; | mSL_Dbg_Memory.jsfx-inc:304 |
| `g` |  | module | mémoire (débogueur) (show_Memory) | membox[16] = memoryBoxAdd; | mSL_Dbg_Memory.jsfx-inc:307 |
| `j` |  | module | mémoire (débogueur) (show_Memory) | act = 3; | mSL_Dbg_Memory.jsfx-inc:262 |
| `k` |  | module | mémoire (débogueur) (show_Memory) | act = 4; | mSL_Dbg_Memory.jsfx-inc:265 |
| `l` |  | module | mémoire (débogueur) (show_Memory) | act = 2; | mSL_Dbg_Memory.jsfx-inc:259 |
| `m` |  | module | mémoire (débogueur) (show_Memory) | act = 1; | mSL_Dbg_Memory.jsfx-inc:256 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 4; | mSL_Dbg_Memory.jsfx-inc:250 |
| `x` |  | module | mémoire (débogueur) (show_Memory) | membox[14] = membox[14] ~ 8; | mSL_Dbg_Memory.jsfx-inc:301 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:219 |
| `Up` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 256; | mSL_Dbg_Memory.jsfx-inc:237 |
| `Up` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb; | mSL_Dbg_Memory.jsfx-inc:282 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:222 |
| `Down` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 256; | mSL_Dbg_Memory.jsfx-inc:240 |
| `Down` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb; | mSL_Dbg_Memory.jsfx-inc:285 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:225 |
| `Left` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - knb * 32; | mSL_Dbg_Memory.jsfx-inc:231 |
| `Left` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] - 1; | mSL_Dbg_Memory.jsfx-inc:288 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:228 |
| `Right` | Shift | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + knb * 32; | mSL_Dbg_Memory.jsfx-inc:234 |
| `Right` | none | module | mémoire (débogueur) (show_Memory) | membox[7] = membox[7] + 1; | mSL_Dbg_Memory.jsfx-inc:291 |
| `Up` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | Interstys.jsfx-inc:29497 |
| `Down` | Shift | panneau | largeur des colonnes (genericItemsPos) | p = serialBlock + Pr7_StudRat + 4 * TabIdt; | Interstys.jsfx-inc:29497 |
| `Left` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | Interstys.jsfx-inc:29466 |
| `Right` | Shift | panneau | largeur des colonnes (genericItemsPos) | // try to increase colum size | Interstys.jsfx-inc:29438 |
| `S` |  | plugin | commandes d'Interstys (do_Plugin_Keys) | // the generic sliders in the panel of REAPER | Interstys.jsfx-inc:20061 |
| `U` |  | plugin | commandes d'Interstys (do_Plugin_Keys) | gui_show_UI = gui_show_UI ? 0 : 1; | Interstys.jsfx-inc:20058 |
| `Tab` | Shift | plugin | onglet suivant / précédent (GM_Tab_Keys) | ui_jtab_step(uix_jG_menuscr, -1); 1 | ui-lib-JJ-GUI.jsfx-inc:680 |
| `Tab` |  | plugin | onglet suivant / précédent (GM_Tab_Keys) | (ui_jtab_step(uix_jG_menuscr, 1); 1) : 0; | ui-lib-JJ-GUI.jsfx-inc:681 |
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
| mcon_Key | mSL_Console.jsfx-inc | `Backspace` `Del` `Left` `Right` `Home` `End` `Up` `Down` `Enter` `Esc` |
