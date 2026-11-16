import re, sys, os

RESERVED = set("""Algorithm All Bus Check Clear Control Created Ctl Curve Display Dump Effect End EofMark Export Free Global In Instance
Interstys Line Out Own Paused Reader Reading Ready Remove Set Tab Undefined View Writer Writing action adaa amount amp att attack
bchan bias block bypass chan chaos clock color corr cross curve damp decay delay delays density depth desync detect detune
diffusion direction display dist dmax dmin doppler drive fade fadein fadernd feedback file first follow freq from gain gain1 gain2
gain3 gain4 gain5 gain6 gain7 gain8 glide grain gvol harm hp inject input jitter law length limiter line lines loop looplen
loopspeed mix mod mode mute name none offset onsetrnd order os out outchan output overdub overlap param periodic phase plateau
platrnd points polarity power q rate release rfreq rumble samples search seed shape shift shift2 shimmer size sizernd solo source
spacing speed speedrnd spls spread src1 src2 src3 src4 src5 src6 src7 src8 stages status steps stretch sustain sweep thresh tilt
to transp type used value voices vol volrnd wait walk wave wow writer xfade
Gain Overdub Fade Plateau Wait Dir Desync Offset Speed Volume LoopSpd Cutoff Reso Drive Bias Order Decay Damping Diffusion Delay
Rate Feedback Freq Level Density Corr Amp Jitter Value Amount Mix On Off Bypass
Undefined None Mixer AutoMix Mover Action Script LFO Filter Saturation Matrix Flanger Chorus Phaser Shimmer Noise Random Math Ring""".split())

KEYWORDS_LONG = set("""direction function Interstys Algorithm Instance Householder Hadamard Geometric Harmonic Resonant BarberUp BarberDown Backward
recycle""".split())

def strip(text):
    # retire les commentaires et le contenu des chaines (garde la structure)
    out = []; i = 0; n = len(text)
    while i < n:
        c = text[i]
        if text.startswith('//', i):
            j = text.find('\n', i); j = n if j < 0 else j
            out.append(' ' * (j - i)); i = j
        elif text.startswith('/*', i):
            j = text.find('*/', i) + 2
            out.append(re.sub(r'[^\n]', ' ', text[i:j])); i = j
        elif c == '"':
            j = text.find('"', i + 1) + 1
            out.append('"' + ' ' * (j - i - 2) + '"'); i = j
        else:
            out.append(c); i += 1
    return ''.join(out)

def check(path):
    text = open(path).read()
    s = strip(text)
    errs = []
    # parentheses
    depth = 0
    for ln, line in enumerate(s.split('\n'), 1):
        for c in line:
            if c == '(': depth += 1
            elif c == ')':
                depth -= 1
                if depth < 0: errs.append(f'{ln}: ) en trop'); depth = 0
    if depth: errs.append(f'parentheses non fermees : {depth}')
    # identifiants de plus de 8 caracteres
    longs = sorted(set(w for w in re.findall(r'[A-Za-z_][A-Za-z0-9_]*', s) if len(w) > 8) - KEYWORDS_LONG)
    if longs: errs.append('identifiants > 8 : ' + ' '.join(longs))
    # les tables modeles : leur plus grand marqueur
    datas = {}
    for m in re.finditer(r'var\s+(\w+)\s*=\s*data\(', s):
        name = m.group(1); start = m.end(); d = 1; j = start
        while d:
            if s[j] == '(': d += 1
            elif s[j] == ')': d -= 1
            j += 1
        body = s[start:j - 1]
        ph = [int(x) - 7700000000 for x in re.findall(r'77000000\d\d', body)]
        datas[name] = (max(ph) if ph else 0, body)
    # les appels tab(NOM, ...) : le nombre d'arguments
    for m in re.finditer(r'(?<!function )\btab\((\w+)', s):
        name = m.group(1); j = m.start() + 4; d = 1; args = 1; k = j
        while d:
            c = s[k]
            if c == '(': d += 1
            elif c == ')': d -= 1
            elif c == ',' and d == 1: args += 1
            k += 1
        if name not in datas:
            errs.append(f'tab({name}) : pas de table modele'); continue
        need = datas[name][0]
        if args - 1 != need:
            ln = s[:m.start()].count('\n') + 1
            errs.append(f'{ln}: tab({name}) : {args - 1} valeurs, {need} attendues')
    # les modules definis dans les algorithmes, et ceux qu'ils designent
    for name, (mx, body) in datas.items():
        if 'Algorithm' not in body: continue
        words = body.split()
        defs = {}
        for i, w in enumerate(words[:-1]):
            if w in ('Line', 'Effect', 'Reader', 'Writer') and (i == 0 or words[i - 1] not in
                    ('source', 'src1', 'src2', 'src3', 'src4', 'src5', 'src6', 'src7', 'src8', 'Display')) \
                    and not words[i - 1].startswith('src') and words[i - 1] not in ('mod',) and \
                    not (i >= 2 and words[i - 2] == 'mod'):
                nm = words[i + 1]
                if ':' in nm: continue
                if nm in defs and defs[nm] != w: errs.append(f'{name} : {nm} est un {defs[nm]} et un {w}')
                defs.setdefault(nm, w)
        for nm in defs:
            if nm in RESERVED: errs.append(f'{name} : {nm} est un mot reserve')
            if len(nm) > 8: errs.append(f'{name} : {nm} a plus de 8 caracteres')
        # les references : apres source, srcN, mod X, line, writer
        for i, w in enumerate(words):
            ref = None
            if w in ('Effect', 'Reader') and i > 0 and (words[i - 1] in ('source',) or words[i - 1].startswith('src')
                                                         or (i >= 2 and words[i - 2] == 'mod')):
                ref = (w, words[i + 1].split(':')[0])
            if w in ('line', 'writer') and i + 1 < len(words):
                ref = ('Line' if w == 'line' else 'Writer', words[i + 1].split(':')[0])
            if ref and ':' not in ' '.join(words[i + 1:i + 2]) or (ref and words[i + 1].count(':') == 1 and
                                                                  words[i + 1].split(':')[1].isdigit()):
                ty, nm = ref
                if nm not in defs: errs.append(f'{name} : {ty} {nm} n\'est pas defini')
                elif defs[nm] != ty: errs.append(f'{name} : {nm} est un {defs[nm]}, pas un {ty}')
        print(f'  {name} : {len(defs)} modules')
    return errs

for p in sys.argv[1:]:
    e = check(p)
    print(os.path.basename(p), 'OK' if not e else '')
    for x in e: print('   ', x)
