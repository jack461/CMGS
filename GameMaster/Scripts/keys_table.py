#!/usr/bin/env python3
"""Keys table of CMGS : the keyboard keys used by the @gfx code of the plugins.

    python3 -I Scripts/keys_table.py [-raw] [-o output.md]

All the plugins follow the same scheme (see GM-Libs/mSL_ui_LibJJ.jsfx-inc, Keyboard) : one key per frame
(GM_key_frame), taken by the first level that uses it (GM_key_take), in the same order everywhere :
the module under the mouse (its keys, then its pads) -> the pane -> the tab -> the commands of the plugin
-> the system commands -> the Studio pad (GamePlayer).

Scans GM-Libs/*.jsfx-inc for the key tests (GM_key_take('m'), or a key variable such as u_ch, zzch, gwk
compared with a character constant), finds the function that holds them, and writes a Markdown table :
one line per key and handler, with its level (see HANDLERS), the plugins, the modifiers seen on the line,
the action, and file:line. It then lists :
  - the keys tested twice in the same handler (the second test is never reached) ;
  - the commands masked over a module : a key of a later level (pane, tab, plugin, system, Studio pad)
    that a module also uses (over this module, the module wins : the command does not run) ;
  - the system commands of the plugins, to check that a key means the same thing everywhere.
Without -o, the table goes to ../Documents/CMGS-Keys.md (relative to GameMaster/).
-raw prints the raw extraction (one line per test) instead.
"""
import re, os, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
GM = os.path.dirname(HERE)                      # GameMaster/
LIBS = os.path.join(GM, 'GM-Libs')

# The variables that hold a key in the keyboard handlers
KEY_VARS = r'(key|u_ch|ch|zzch|k|KeyedT|Keyed|gwk|xx|inKey)'
# Files (or parts of names) that are not keyboard code : parsers, archives, generated files
SKIP = ('mSL_Comp_lib', 'Diffusion-3-XML', 'mSL_Utilities', 'ZZZ', 'unused', 'The_Obsolete',
        'Diffusion-3-Set-Table', 'Diffusion-3-Utils', 'mSL_string_list', 'mSL_ui_Menus', 'mSL_GM_Vars', 'mSL_FR_Vars')
# Functions that compare such variables with characters but do not handle keys (string parsing...)
NOT_KEYS = {('GamePlayer.jsfx-inc', f) for f in ('getClipName', 'rebuildAllaliases', 'installClipSet',
            'SetClipsList', 'updClSel')} | {('FilePlayer.jsfx-inc', 'checkRCB')} | \
           {('mSL_ui_LibJJ.jsfx-inc', f) for f in ('GM_key_frame', 'GM_key_end', 'GM_key_peek', 'GM_key_take',
                                                   'GM_key_take_in', 'GM_key_mods')}
READERS = set()

# Plugins and the shared files they include (see the imports of each plugin)
PLUGINS = ['GamePlayer', 'FilePlayer', 'ScriptMaster', 'Diffusion-3', 'Interstys']
SHARED = {
    'mSL_Dbg_Memory.jsfx-inc': PLUGINS,
    'mSL_Panes.jsfx-inc': ['Diffusion-3'],
    'mSL_ui_Pads.jsfx-inc': ['GamePlayer'],              # interactive leds : GamePlayer only
    'ScriptMaster_Utilities.jsfx-inc': ['ScriptMaster', 'Interstys'],
    'mSL_System_Keys.jsfx-inc': ['FilePlayer', 'ScriptMaster', 'Diffusion-3', 'Interstys'],
    'ui-lib-JJ-GUI.jsfx-inc': PLUGINS,                    # GM_Tab_Keys (Tab, Shift + Tab)
}

# Levels, in the order they see the key during a frame : each level only gets the keys the previous ones left
#   module    : the mouse is in the module (its own keys, then the keys of its pads)
#   pane      : genericItemsPos, the pane under the mouse (Shift + arrows : column sizes)
#   tab       : the commands of the tab or of the screen (do_Generic_Commands, Live screen of Diffusion-3)
#   plugin    : the commands of the plugin (do_Plugin_Keys)
#   system    : the system commands (do_System_Keys, mSL_System_Keys.jsfx-inc)
#   last      : the Studio pad of GamePlayer, when it is displayed
#   editor    : number editors, called by the modules with the key they got (not in the conflicts)
LEVELS = ['module', 'pane', 'tab', 'plugin', 'system', 'last', 'editor']
LEVEL_FR = {'module': 'module', 'pane': 'panneau', 'tab': 'onglet', 'plugin': 'plugin', 'system': 'système',
            'last': 'pad Studio', 'editor': 'éditeur'}
ORDER = {
    'GamePlayer': "module sous la souris (puis ses pads) → panneau → commandes d'onglet (do_Generic_Commands) → "
                  "raccourcis de l'utilisateur (do_Plugin_Keys) → pad Studio, s'il est affiché (do_StudioPadKeyboard) ; "
                  "pendant l'apprentissage d'un raccourci, la touche va d'abord à celui-ci",
    'FilePlayer': "module sous la souris → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys)",
    'ScriptMaster': "module sous la souris → commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys)",
    'Diffusion-3': "module sous la souris (écran Live : la boîte sous la souris) → panneau → écran Live (do_live_actions) "
                   "→ commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys)",
    'Interstys': "module sous la souris (puis ses pads) → panneau → commandes d'onglet (do_Generic_Commands) → "
                 "commandes du plugin (do_Plugin_Keys) → commandes système (do_System_Keys)",
}

# HANDLERS[(file, function)] = (level, description) ; the plugins come from the file (or SHARED)
HANDLERS = {
    ('Interstys.jsfx-inc', 'do_Plugin_Keys'): ('plugin', 'commandes d\'Interstys'),
    ('Interstys.jsfx-inc', 'do_Generic_Commands'): ('tab', 'commandes d\'onglet'),
    ('Interstys.jsfx-inc', 'genericItemsPos'): ('pane', 'largeur des colonnes'),
    ('Interstys.jsfx-inc', 'show_SysLog'): ('module', 'log système'),
    ('Interstys.jsfx-inc', 'show_Reader_Pad'): ('module', 'Reader'),
    ('Interstys.jsfx-inc', 'show_Line_Pad'): ('module', 'Line'),
    ('Interstys.jsfx-inc', 'show_Writer_Pad'): ('module', 'Writer'),
    ('GamePlayer.jsfx-inc', 'do_Generic_Commands'): ('tab', 'commandes d\'onglet'),
    ('GamePlayer.jsfx-inc', 'genericItemsPos'): ('pane', 'largeur des colonnes'),
    ('GamePlayer.jsfx-inc', 'show_Generator'): ('module', 'Generator'),
    ('GamePlayer.jsfx-inc', 'show_Sensors'): ('module', 'Sensors'),
    ('GamePlayer.jsfx-inc', 'show_SysLog'): ('module', 'log système / log utilisateur'),
    ('GamePlayer.jsfx-inc', 'show_Clips_Selection'): ('module', 'Clips selection'),
    ('GamePlayer.jsfx-inc', 'show_Units'): ('module', 'Units'),
    ('GamePlayer.jsfx-inc', 'doBanksInteract'): ('module', 'Banks'),
    ('GamePlayer.jsfx-inc', 'show_Scripts'): ('module', 'Scripts / Settings'),
    ('GamePlayer.jsfx-inc', 'show_PlayLog'): ('module', 'Play log'),
    ('GamePlayer.jsfx-inc', 'show_Dyn_pars'): ('module', 'paramètres dynamiques'),
    ('GamePlayer.jsfx-inc', 'show_Studio_Play_Pad'): ('module', 'pad Studio'),
    ('GamePlayer.jsfx-inc', 'do_StudioPadKeyboard'): ('last', 'pad Studio : jeu au clavier (aussi au survol du pad)'),
    ('GamePlayer.jsfx-inc', 'show_Play_Control'): ('module', 'Play control'),
    ('FilePlayer.jsfx-inc', 'do_local_Control'): ('module', 'File Player Status'),
    ('FilePlayer.jsfx-inc', 'do_Plugin_Keys'): ('plugin', 'commandes de FilePlayer'),
    ('ScriptMaster.jsfx-inc', 'do_Plugin_Keys'): ('plugin', 'commandes de ScriptMaster'),
    ('FilePlayer.jsfx-inc', 'show_SysLog'): ('module', 'log système'),
    ('ScriptMaster.jsfx-inc', 'show_SysLog'): ('module', 'log système'),
    ('Diffusion-3.jsfx-inc', 'do_live_actions'): ('tab', 'écran Live : commandes'),
    ('Diffusion-3.jsfx-inc', 'mouse_hover'): ('module', 'écran Live : boîte sous la souris'),
    ('Diffusion-3.jsfx-inc', 'do_Plugin_Keys'): ('plugin', 'commandes de Diffusion-3'),
    ('Diffusion-3.jsfx-inc', 'show_SysLog'): ('module', 'log système'),
    ('mSL_Dbg_Memory.jsfx-inc', 'show_Memory'): ('module', 'mémoire (débogueur)'),
    ('mSL_Panes.jsfx-inc', 'genericItemsPos'): ('pane', 'largeur des colonnes'),
    ('mSL_ui_Pads.jsfx-inc', 'show_jled'): ('module', 'LED interactive'),
    ('mSL_System_Keys.jsfx-inc', 'do_System_Keys'): ('system', 'commandes système'),
    ('ui-lib-JJ-GUI.jsfx-inc', 'GM_Tab_Keys'): ('plugin', 'onglet suivant / précédent'),
}
# The commands of the plugins (plugin and system levels), compared between plugins
SYSTEM = [('Interstys', 'Interstys.jsfx-inc', 'do_Plugin_Keys'), ('Diffusion-3', 'Diffusion-3.jsfx-inc', 'do_Plugin_Keys'),
          ('FilePlayer', None, None), ('ScriptMaster', None, None)]


def handler_of(f, fn):
    if (f, fn) in HANDLERS: return HANDLERS[(f, fn)]
    if fn.startswith('upd') or fn == 'updtBNumber': return ('editor', 'éditeur de nombre')
    return ('module', '?')


def plugins_of(f):
    if f in SHARED: return SHARED[f]
    for p in PLUGINS:
        if f.startswith(p + '.') or f.startswith(p + '-'): return [p]
    return []


KEY_NAMES = {8: 'Backspace', 9: 'Tab', 13: 'Enter', 27: 'Esc', 32: 'Space', 127: 'Del'}
LIT_NAMES = {'left': 'Left', 'rght': 'Right', 'up': 'Up', 'down': 'Down', 'home': 'Home', 'end': 'End',
             'pgup': 'PgUp', 'pgdn': 'PgDn', 'del': 'Del', 'insr': 'Ins'}
LIT_NAMES.update({'f%d' % i: 'F%d' % i for i in range(1, 25)})


def lit_value(lit):
    """The numeric value of an EEL2 constant : 'x', 'left' (multi-char), 9, 0x09"""
    if lit == "'\\''": return 39
    if lit.startswith("'"):
        v = 0
        for c in lit[1:-1]:
            v = v * 256 + ord(c)
        return v
    return int(lit, 16) if lit.lower().startswith('0x') else int(lit)


def key_name(lit):
    if lit == "'\\''": return "'"
    if lit.startswith("'"):
        s = lit[1:-1]
        if s in LIT_NAMES: return LIT_NAMES[s]
        if len(s) == 1:
            return 'Space' if s == ' ' else s
        return s
    v = lit_value(lit)
    if v in KEY_NAMES: return KEY_NAMES[v]
    if 1 <= v <= 26: return 'Ctrl+' + chr(64 + v)
    if 32 < v < 127: return chr(v)
    return '0x%02X' % v


LIT = r"('\\''|'[^']{1,4}'|0x[0-9A-Fa-f]+|\d+)"
CMP = re.compile(r"\b" + KEY_VARS + r"\s*(===|!==|==|!=|>=|<=|>|<)\s*" + LIT)
TAKE = re.compile(r"\b(GM_key_take(?:_in)?)\s*\(\s*" + LIT + r"\s*\)")
FN = re.compile(r'^\s*function\s+([A-Za-z_][\w.]*)\s*\(')
MODS = re.compile(r'(shfCap|cmdCap|altCap|ctlCap|winCap|GM_key_mods\(\)\s*[=!&]+=?\s*\w+|Kmouse_cap\s*[=!&]+=?\s*\w+|ui_jmouse_cap\s*[=!&]+=?\s*\w+|'
                  r'mouse_cap\s*&\s*\w+|zzmmd\s*[=!&]+=?\s*\w+|jmc\s*&\s*\w+)')
CAPS = {'8': 'Shift', '4': 'Cmd', '16': 'Alt', '32': 'Ctrl', '0': 'none', 'shfCap': 'Shift', 'cmdCap': 'Cmd',
        'altCap': 'Alt', 'ctlCap': 'Ctrl', 'winCap': 'Win'}


def mods_of(line):
    out = []
    for m in MODS.finditer(line):
        t = m.group(1)
        last = re.split(r'[^\w]+', t)[-1]
        neg = '!' in t
        name = CAPS.get(last, t)
        out.append(('not ' if neg else '') + name)
    return ', '.join(dict.fromkeys(out))


def strip_block_comments(lines):
    """The lines without the /* ... */ comments (the code of the line is kept, the comment is blanked)"""
    out = []; inc = False
    for l in lines:
        r = ''; i = 0
        while i < len(l):
            if inc:
                j = l.find('*/', i)
                if j < 0: i = len(l)
                else: inc = False; i = j + 2
            else:
                j = l.find('/*', i); k = l.find('//', i)
                if j < 0 or (0 <= k < j): r += l[i:]; i = len(l)
                else: r += l[i:j]; inc = True; i = j + 2
        out.append(r)
    return out


def scan(path):
    """Yields (line number, function or 'top @section', line text, lines) for each line of the file
    (the lines are given without their /* */ comments)"""
    lines = strip_block_comments(open(path, encoding='utf-8', errors='replace').read().splitlines())
    cur = None; sect = '(no section)'; pend = False
    for n, l in enumerate(lines, 1):
        s = l.rstrip()
        if re.match(r'^@\w+', s): sect = s.split()[0]; cur = None
        m = FN.match(s)
        if m: cur = m.group(1)
        elif re.match(r'^\s*function\s*$', s): pend = True
        elif pend:
            m = re.match(r'^\s*([A-Za-z_][\w.]*)\s*\(', s); pend = False
            if m: cur = m.group(1)
        yield n, cur or ('top ' + sect), l, lines
        if cur and re.match(r'^\);', s): cur = None


def action_of(lines, n, code, end):
    """The action after the test : the code after the '?' that ends the condition (it may be on a next line,
    for the lists of '||'), else the next code line ; plus the comment of the line"""
    act = None
    rest = code[end:]
    for j in range(n - 1, min(n + 6, len(lines))):
        t = rest if j == n - 1 else lines[j].split('//')[0]
        k = t.find('?')
        if k >= 0:
            act = t[k + 1:]; n2 = j + 1
            break
    if act is None: act = ''; n2 = n
    act = act.strip().strip(':').strip()
    act = re.sub(r'\)\s*;$', ')', act).strip()
    while act.startswith('(') and act.endswith(')') and act.count('(') == act.count(')'):
        act = act[1:-1].strip()
    act = re.sub(r'\)\s*:$', '', act).strip().rstrip(':').strip()
    if act in ('', '('):
        j = n2
        while j < len(lines):
            t = lines[j].split('//')[0].strip()
            c = lines[j].split('//', 1)[1].strip() if '//' in lines[j] else ''
            j += 1
            if t or c:
                act = t if t else '// ' + c
                break
    com = lines[n - 1].split('//', 1)[1].strip() if '//' in lines[n - 1] else ''
    if com and com not in act: act = (act + '  // ' + com).strip()
    act = act.replace('|', '\\|')
    return act[:110] + ('…' if len(act) > 110 else '')


def extract():
    rows = []
    for path in sorted(glob.glob(os.path.join(LIBS, '*.jsfx-inc'))):
        f = os.path.basename(path)
        if any(s in f for s in SKIP): continue
        for n, ctx, l, lines in scan(path):
            if (f, ctx) in NOT_KEYS or ctx in READERS: continue
            code = l.split('//')[0]
            found = list(CMP.finditer(code))
            takes = list(TAKE.finditer(code))
            if not found and not takes: continue
            ind = len(l) - len(l.lstrip())
            base = dict(file=f, fn=ctx, line=n, mods=mods_of(code), indent=ind)
            for m in takes:
                rows.append(dict(base, var=m.group(1), key=key_name(m.group(2)), val=lit_value(m.group(2)),
                                 act=action_of(lines, n, code, m.end())))
            # ranges : v >= 'a' && v <= 'z'
            lo = {m.group(1): m for m in found if m.group(2) == '>='}
            hi = {m.group(1): m for m in found if m.group(2) == '<='}
            done = set()
            for v in lo:
                if v in hi:
                    a, b = lo[v].group(3), hi[v].group(3)
                    rows.append(dict(base, var=v, key=key_name(a) + '..' + key_name(b),
                                     val=('range', lit_value(a), lit_value(b)),
                                     act=action_of(lines, n, code, max(lo[v].end(), hi[v].end()))))
                    done |= {lo[v], hi[v]}
            for m in found:
                if m in done or m.group(2) not in ('===', '=='): continue
                v, op, lit = m.groups()
                if lit[0] != "'":
                    # numbers : not for the menu results (xx), and only the control keys for the general variables
                    if v == 'xx' or lit_value(lit) == 0: continue
                    if v in ('k', 'key', 'ch') and lit_value(lit) not in KEY_NAMES: continue
                rows.append(dict(base, var=v, key=key_name(lit), val=lit_value(lit),
                                 act=action_of(lines, n, code, m.end())))
    for r in rows:
        r['level'], r['desc'] = handler_of(r['file'], r['fn'])
        r['plugins'] = plugins_of(r['file'])
    return rows


def values(r):
    v = r['val']
    return set(range(v[1], v[2] + 1)) if isinstance(v, tuple) else {v}


def mods_set(r):
    return set(x.strip() for x in r['mods'].split(',') if x.strip())


def mods_meet(a, b):
    """Can the two tests be true for the same modifiers ? (no modifier test : any modifier)"""
    ma, mb = mods_set(a), mods_set(b)
    if not ma or not mb: return True
    if ('none' in ma and mb - {'none'} and not any(x.startswith('not ') for x in mb)) or \
       ('none' in mb and ma - {'none'} and not any(x.startswith('not ') for x in ma)): return False
    return True


def cond_rest(line):
    """The condition of a line without the key tests (to see if two tests have the same other conditions)"""
    t = CMP.sub('', line.split('//')[0])
    t = t.split('?')[0]
    return re.sub(r'[()|\s]', '', t)


def same_chain(lines, a, b):
    """Are the two tests in the same chain of ' ? ... : ' (same indentation, nothing less indented between),
    in two different branches (a '?' between them), with the same other conditions ?"""
    if a['indent'] != b['indent']: return False
    if '?' not in ''.join(l.split('//')[0] for l in lines[a['line'] - 1:b['line'] - 1]): return False
    if cond_rest(lines[a['line'] - 1]) != cond_rest(lines[b['line'] - 1]): return False
    for j in range(a['line'], b['line'] - 1):
        t = lines[j]
        if t.strip() and not t.strip().startswith('//') and len(t) - len(t.lstrip()) < a['indent']: return False
    return True


def conflicts(rows):
    out = collections.defaultdict(list)   # plugin -> [(kind, text)]
    cache = {}
    def lines_of(f):
        if f not in cache: cache[f] = strip_block_comments(open(os.path.join(LIBS, f), encoding='utf-8', errors='replace').read().splitlines())
        return cache[f]
    # 1. the same key twice in the same chain : the second test is never reached
    by_fn = collections.defaultdict(list)
    for r in rows:
        by_fn[(r['file'], r['fn'])].append(r)
    for (f, fn), rs in by_fn.items():
        for i, a in enumerate(rs):
            for b in rs[i + 1:]:
                if b['line'] == a['line'] or not (values(a) & values(b)) or a['mods'] != b['mods']: continue
                if same_chain(lines_of(f), a, b):
                    for p in a['plugins']:
                        out[p].append(('inaccessible', f"`{b['key']}` testée deux fois dans {fn} "
                                       f"({f}:{a['line']} et {b['line']}) : la seconde branche n'est jamais exécutée"))
    # 2. the commands masked over a module : a later level uses a key that a module also uses
    for p in PLUGINS:
        rs = [r for r in rows if p in r['plugins'] and r['level'] != 'editor']
        masked = collections.OrderedDict()
        studio = collections.OrderedDict()
        for c in rs:
            if c['level'] in ('module', 'editor'): continue
            for m in rs:
                if m['level'] != 'module' or not (values(c) & values(m)) or not mods_meet(c, m): continue
                if c['level'] == 'pane' and 'Shift' not in mods_set(m): continue
                if c['level'] == 'last' and m['fn'] in ('show_Studio_Play_Pad',): continue
                # the Live screen of Diffusion-3 : only the boxes under the mouse, no modules
                if c['fn'] == 'do_live_actions' and m['fn'] != 'mouse_hover': continue
                if c['level'] == 'last':
                    studio.setdefault((c['desc'], c['file'], m['desc']), set()).add(c['key'])
                    continue
                k = (c['key'], c['mods'], c['desc'], c['file'], c['line'])
                masked.setdefault(k, set()).add(m['desc'])
        for (key, mods, desc, f, line), ms in masked.items():
            kk = (mods + '+' if mods and mods != 'none' else '') + key
            out[p].append(('masquée', f"`{kk}` : {desc} ({f}:{line}), pas au-dessus de : " + ', '.join(sorted(ms))))
        for (desc, f, mdesc), ks in sorted(studio.items()):
            out[p].append(('masquée', f"{desc} ({f}), pas au-dessus de {mdesc} : " + ' '.join('`' + k + '`' for k in sorted(ks))))
    return out


def md_table(rows):
    t = ['| Touche | Modif. | Niveau | Module | Action | Source |', '|---|---|---|---|---|---|']
    for r in rows:
        t.append(f"| `{r['key'] if r['key'] != '|' else chr(92) + '|'}` | {r['mods']} | {LEVEL_FR[r['level']]} | "
                 f"{r['desc']} ({r['fn']}) | {r['act']} | {r['file']}:{r['line']} |")
    return t


def sort_key(r):
    v = r['val'][1] if isinstance(r['val'], tuple) else r['val']
    return (LEVELS.index(r['level']), r['desc'], r['fn'], v, r['line'])


def report(rows):
    out = ['# Touches du clavier dans CMGS', '',
           '*Fichier produit par `Scripts/keys_table.py` : ne pas le modifier à la main, relancer le script.*', '',
           'Pour chaque plugin, les touches testées par le code `@gfx`, par niveau dans l\'ordre où les niveaux '
           'voient la touche pendant une trame. « Modif. » : les modificateurs testés sur la même ligne '
           '(vide : non testés, la touche agit avec ou sans modificateur ; « none » : sans modificateur). '
           'L\'action est le début du code exécuté. Les bibliothèques partagées (mSL_Dbg_Memory…) apparaissent '
           'dans chaque plugin qui les inclut.', '']
    conf = conflicts(rows)
    out += ['## Conflits', '']
    names = {'inaccessible': 'Branches jamais exécutées',
             'masquée': 'Commandes masquées au-dessus de certains modules (le module, qui passe avant, utilise la '
                        'même touche : c\'est la règle, mais à éviter pour les commandes importantes)'}
    for p in PLUGINS:
        cs = conf.get(p, [])
        out += [f'### {p}', '']
        if not cs: out += ['Aucun conflit détecté.', '']; continue
        for kind in names:
            ks = sorted(set(t for k, t in cs if k == kind))
            if ks: out += [f'**{names[kind]}** ({len(ks)})', ''] + ['- ' + t for t in ks] + ['']
    # the commands of the plugins (plugin and system levels)
    out += ['## Commandes des plugins : comparaison', '',
            'Les commandes du plugin (do_Plugin_Keys : Tab, affichages) et les commandes système (do_System_Keys, '
            'communes à FilePlayer, ScriptMaster, Diffusion-3 et Interstys). Majuscules pour les affichages, minuscules '
            'pour les commandes. GamePlayer : ses commandes de concert sont au niveau de l\'onglet, et ses '
            'raccourcis sont définis par l\'utilisateur.', '']
    keys = collections.OrderedDict()
    cols = [p for p in PLUGINS if p != 'GamePlayer']
    for p in cols:
        for r in rows:
            if p in r['plugins'] and r['level'] in ('plugin', 'system'):
                keys.setdefault(r['key'], {}).setdefault(p, r['act'][:50])
    out += ['| Touche | ' + ' | '.join(cols) + ' |', '|---|' + '---|' * len(cols)]
    for k in sorted(keys, key=lambda x: (x.lower(), x)):
        out.append(f'| `{k}` | ' + ' | '.join(keys[k].get(p, '') for p in cols) + ' |')
    out.append('')
    # per plugin tables
    for p in PLUGINS:
        rs = sorted([r for r in rows if p in r['plugins'] and r['level'] != 'editor'], key=sort_key)
        out += [f'## {p}', '', 'Ordre : ' + ORDER[p] + '.', ''] + md_table(rs) + ['']
    # editors and unused handlers
    out += ['## Éditeurs de nombres', '',
            'Appelés par les modules avec la touche qu\'ils ont reçue (hors analyse des conflits).', '',
            '| Fonction | Fichier | Touches |', '|---|---|---|']
    eds = collections.OrderedDict()
    for r in rows:
        if r['level'] == 'editor':
            eds.setdefault((r['fn'], r['file']), []).append(r['key'])
    for (fn, f), ks in eds.items():
        ks = list(dict.fromkeys(ks))
        out.append(f"| {fn} | {f} | " + ' '.join('`' + (k if k != '|' else chr(92) + '|') + '`' for k in ks) + ' |')
    out.append('')
    return '\n'.join(out)


def main():
    args = sys.argv[1:]
    rows = extract()
    if '-raw' in args:
        for r in rows:
            print(f"{r['file']}:{r['line']}\t{r['fn']}\t{r['level']}\t{r['var']}\t{r['key']}\t{r['mods']}\t{r['act']}")
        return
    dest = args[args.index('-o') + 1] if '-o' in args else os.path.join(os.path.dirname(GM), 'Documents', 'CMGS-Keys.md')
    open(dest, 'w', encoding='utf-8').write(report(rows))
    conf = conflicts(rows)
    print(f"{len(rows)} tests de touches ; conflits : " +
          ', '.join(f"{p} {len(set(conf.get(p, [])))}" for p in PLUGINS) + f"\n-> {dest}")


if __name__ == '__main__':
    main()
