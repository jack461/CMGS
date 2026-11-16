from common import level, vca, output

NAMES = dict(INS='reson', INSIN='resonin', ALGIN='ResonIn', NOM='reson', TITRE='Preset-Resonances')
FILE = 'Preset-Resonances.mSL'

TITLE = 'print("Preset-Resonances. Le son excite des corps accordes qui changent d\'accord ; 10 minutes, mono, dans le buffer de sortie.");'

DOC = r'''
/*
  PRESET "RESONANCES" : des corps resonants
  Le buffer d'entree ne s'entend plus : il devient l'excitation de resonateurs. Des grains brefs et des segments (Brage),
  pris au hasard dans le buffer, frappent deux bancs de six filtres passe-bande tres etroits (accordes sur un spectre
  tire au hasard : harmoniques, harmoniques impaires, partiels d'une barre ou d'une cloche, accords justes, une grappe
  serree, les partiels aigus d'un son grave, ou au hasard ; parfois etires) et un reseau de retards accorde (Matrix :
  des retards multiples d'une periode, ou egaux : un peigne), qui sonne comme une corde, un tube, une plaque. D'une
  section a l'autre, l'accord mute (un banc remplace l'autre, en fondu ou d'un coup) ou glisse (tout le banc monte ou
  descend d'un intervalle) ; le peigne se reaccorde en glissant. Un decaleur de frequence fait battre et deriver les
  partiels ; des frappes soudaines (une rafale de grains) relancent les resonances.
  La forme : des sections de 12 s a 1 min ; des evenements toutes les 1.5 a 6 s.
'''

BODY1 = r'''
// ======================================================================================================================
// Resonances : les modules
// ======================================================================================================================
/*
  L'instance reson : les excitateurs gx (Grains) et bx (Brage) sur le buffer d'entree (resonin:src), leurs niveaux
  (l1 s1, l2 s2), leur somme ex ; le banc A (filtres a1 ... a6, somme ma, niveau l3 s3 e3 v3, accord ka ta : le
  glissement de tout le banc, en octaves), le banc B (b1 ... b6, mb, l4 s4 e4 v4, kb tb) ; leur somme ab, le decaleur
  fs (Ring : Up ou Down) ; le peigne cm (Matrix accordee), son niveau (l5 s5 e5 v5) ; la somme su, l'espace sp ; le
  niveau general (lm sm em vm) ; res, wo ; l'ecoute m0, m1.
*/
var KM = 5;                                   // le niveau general (0, 1 : les excitateurs, 2, 3 : les bancs A, B, 4 : le peigne)
var MAST = -4;
var NVl = array(`l1, `l2, `l3, `l4, `l5, `lm);
var NVs = array(`s1, `s2, `s3, `s4, `s5, `sm);
var NVc = malloc(6);
var NVd = malloc(6);
'''

def tune(b):
    return (f"        Effect k{b}  type LFO  chan 1  freq 0.01  amp 0  offset 0\n"
            f"        Effect t{b}  type Math  chan 1  source Effect k{b}  mode Slew  attack 1000  release 1000\n")

def bank(b):
    s = ""
    for j in range(1, 7):
        s += (f"        Effect {b}{j}  type Filter  chan 1  source Effect ex  mode BP  stages 2  freq {110 * j}  q 60"
              f"  mod Cutoff Effect t{b}  depth 1\n")
    s += f"        Effect m{b}  type Mixer  chan 1"
    for j in range(1, 7):
        s += f"  src{j} Effect {b}{j}  gain{j} 20"
        if j == 3:
            s += "\n                  "
    return s + "\n"

TCRE = (r'''
var TCRE = data(
    Interstys
    Algorithm Reson
        Line res  length @1@  chan 1
''' + level(1) + level(2) + level(3) + level(4) + level(5) + level('m') + tune('a') + tune('b')
    + r'''        Reader gx  line resonin:src  mode Grains  outchan 1  loop loop  out Own  size 20  density 10  plateau 0  fadein 30
                   mod Volume Effect s1  depth 80  law dB  status Reading
        Reader bx  line resonin:src  mode Brage  outchan 2  loop loop  out Own  block 120  overlap 20  search 0  transp 0
                   speed 1  mod Volume Effect s2  depth 80  law dB  status Reading
        Effect ex  type Mixer  chan 1  src1 Reader gx  gain1 0  src2 Reader bx:0  gain2 -3  src3 Reader bx:1  gain3 -3
''' + bank('a') + bank('b') + vca(3, 'Effect ma') + vca(4, 'Effect mb') + r'''        Effect ab  type Mixer  chan 1  src1 Effect v3  gain1 0  src2 Effect v4  gain2 0
        Effect fs  type Ring  chan 1  source Effect ab  mode @2@  freq 1.5  wave Sine  mix 40
        Effect cm  type Matrix  chan 1  source Effect ex  mode Hadamard  lines 8  delays Harmonic  dmin 9  dmax 160  decay 6
                   damp 6000  glide 4  mix 100
''' + vca(5, 'Effect cm') + r'''        Effect su  type Mixer  chan 1  src1 Effect fs  gain1 0  src2 Effect v5  gain2 0
        Effect sp  type Matrix  chan 1  source Effect su  mode Householder  lines 12  delays Random  seed @3@  dmin 19
                   dmax 120  decay 2.5  damp 8000  wow 2  rate 0.3  mix 30
''' + vca('m', 'Effect sp', '  limiter On') + output('Effect vm', 4) + r'''    End
    Instance reson Reson
);
''')

BODY2 = TCRE + r'''
// les modules : le decaleur vers le haut ou vers le bas, la graine de l'espace, l'ecoute
function creer() ( tab(TCRE, sortie + 30, (proba(0.5) ? `Up : `Down), floor(rand(99999)), borne(ecoute, -120, 40)); );

var TBK = data(Interstys
    Effect reson:@1@  freq @7@  q @13@  Effect reson:@2@  freq @8@  q @13@  Effect reson:@3@  freq @9@  q @13@
    Effect reson:@4@  freq @10@  q @13@  Effect reson:@5@  freq @11@  q @13@  Effect reson:@6@  freq @12@  q @13@
    Effect reson:@14@  gain1 @15@  gain2 @15@  gain3 @15@  gain4 @15@  gain5 @15@  gain6 @15@);
var TTU = data(Interstys  Effect reson:@1@  offset @2@  Effect reson:@3@  attack @4@  release @4@);
var TCM = data(Interstys  Effect reson:cm  dmin @1@  delays @2@  decay @3@  damp @4@);
var TFS = data(Interstys  Effect reson:fs  freq @1@);
var TGX = data(Interstys  Reader reson:gx  from @1@  to @2@  size @3@  density @4@  speed @5@  onsetrnd @6@  direction @7@
    sizernd @8@  speedrnd @9@);
var TBX = data(Interstys  Reader reson:bx  from @1@  to @2@  block @3@  speed @4@  transp @5@);
var TDX = data(Interstys  Reader reson:gx  density @1@);

var BKA = array(`a1, `a2, `a3, `a4, `a5, `a6);
var BKB = array(`b1, `b2, `b3, `b4, `b5, `b6);
// les spectres (rapports a la fondamentale) ; le dernier (hasard) est tire a chaque fois
var R0 = array(1, 2, 3, 4, 5, 6);
var R1 = array(1, 3, 5, 7, 9, 11);
var R2 = array(1, 2.756, 5.404, 8.933, 13.345, 18.64);
var R3 = array(0.56, 0.92, 1.19, 1.71, 2.74, 3.76);
var R4 = array(1, 1.25, 1.5, 2, 2.5, 3);
var R5 = array(1, 1.2, 1.5, 1.8, 2.4, 3.6);
var R6 = array(1, 1.029, 1.059, 1.122, 1.189, 1.26);
var R7 = array(8, 9, 10, 11, 13, 15);
var RS = array(R0, R1, R2, R3, R4, R5, R6, R7);
var RNOM = array("harmoniques", "impaires", "barre", "cloche", "majeur", "mineur", "grappe", "aigus", "hasard");
var GLI = array(-1, -0.5833, -0.4167, -0.1667, -0.0833, 0.0833, 0.1667, 0.4167, 0.5833, 1);   // les glissements (octaves)
var SPX = array(0.5, 1, 1, 2);                // les vitesses des grains
var SPB = array(-1, -0.5, 0.5, 1, 1, 2);      // celles des segments
var FQ = malloc(6);                           // les frequences d'un banc
var TU = malloc(2);                           // le glissement de chaque banc (octaves)
var CUR = 0;                                  // le banc qui sonne (0 : A, 1 : B)

// un accord pour le banc bk : un spectre (etire une fois sur trois), une fondamentale de 40 a 300 Hz, des filtres plus
// ou moins etroits (q de 30 a 400 : plus il est grand, plus ils resonnent), leur gain compense ; le banc ne glisse plus
function accord(bk) local(k, j, rs, f0, x, q, g, nm)
(
    k = floor(rand(8.999));
    rs = (k < 8) ? RS[k] : 0;
    f0 = aleal(40, 300);
    x = proba(0.3) ? alea(0.97, 1.08) : 1;
    j = 0;
    loop(6,
        FQ[j] = borne(f0 * ((k < 8) ? pow(rs[j], x) : aleal(1, 9)), 30, 12000);
        j += 1;
    );
    q = aleal(30, 400);
    g = borne(10 * log10(q) + 4, 0, 40);
    nm = (bk === 0) ? BKA : BKB;
    print(sprintf(0, "%s %d:%02d  banc %s : %s sur %d Hz, q %d", TITRE, floor(tps() / 60), floor(tps()) % 60,
        ((bk === 0) ? "A" : "B"), RNOM[k], floor(f0), floor(q)));
    tab(TBK, nm[0], nm[1], nm[2], nm[3], nm[4], nm[5], FQ[0], FQ[1], FQ[2], FQ[3], FQ[4], FQ[5], q,
        ((bk === 0) ? `ma : `mb), g);
    tab(TTU, ((bk === 0) ? `ka : `kb), 0, ((bk === 0) ? `ta : `tb), 1);
    TU[bk] = 0;
);

// une mutation : l'autre banc recoit un nouvel accord, puis les bancs s'echangent en tf secondes
function mutation(tf) local(o)
(
    o = 1 - CUR;
    accord(o);
    niv(2 + o, alea(-6, -1), tf);
    niv(2 + CUR, -80, tf * alea(0.7, 1.5));
    CUR = o;
);

// un glissement : le banc qui sonne monte ou descend d'un intervalle, en s secondes
function gliss(s) local(t)
(
    t = borne(TU[CUR] + pioche(GLI), -2, 2);
    tab(TTU, ((CUR === 0) ? `ka : `kb), t, ((CUR === 0) ? `ta : `tb), borne(1000 * s / max(0.01, abs(t - TU[CUR])), 1, 10000));
    TU[CUR] = t;
);

// le peigne se reaccorde (en glissant) : sa periode, des retards multiples ou egaux, sa duree, son amortissement
function peigne() local(f)
(
    f = aleal(35, 400);
    tab(TCM, borne(1000 / f, 2.5, 28), (proba(0.65) ? `Harmonic : `Equal), aleal(2, 14), aleal(2500, 9000));
);

// les excitateurs : des regions au hasard, des grains de 10 a 40 ms (plus denses avec l'energie), des segments
function excite() local(d, w, a)
(
    d = dispo();
    w = borne(aleal(0.5, 30), min(d, 0.3), d); a = rand(max(0, d - w));
    tab(TGX, a, a + w, aleal(10, 40), aleal(2, 10 + 60 * E), pioche(SPX), alea(0, 1), alea(-1, 1), alea(1, 2.5), alea(1, 1.5));
    w = borne(aleal(0.5, 30), min(d, 0.3), d); a = rand(max(0, d - w));
    tab(TBX, a, a + w, aleal(30, 400), pioche(SPB), (proba(0.3) ? alea(-7, 7) : 0));
);

// une frappe : une rafale de grains
function frappe() local(v)
(
    v = NVd[0];
    tab(TDX, 100);
    niv(0, alea(-4, 0), 0.02);
    attend(alea(0.1, 0.6));
    tab(TDX, aleal(2, 10 + 60 * E));
    niv(0, v, alea(0.5, 3));
);

// une section dure D secondes : toutes les 1.5 a 6 s, une frappe, un glissement, un nouveau decalage, de nouveaux
// excitateurs
function vivre(D) local(tf, u)
(
    tf = ptime() + D;
    while ((arret === 0) && (ptime() < tf - 0.3) && (tps() < sortie - FIN)) (
        attend(min(alea(1.5, 6), max(0.1, tf - ptime())));
        finrec();
        ((arret === 0) && (ptime() < tf - 1) && (tps() < sortie - FIN)) ? (
            u = rand(1);
            (u < 0.2) ? frappe() : ((u < 0.35) ? gliss(aleal(3, 12)) :
            ((u < 0.5) ? tab(TFS, aleal(0.1, 20)) : ((u < 0.65) ? excite() : 0)));
        );
    );
);

function section() local(D, tr)
(
    energie();
    NS += 1;
    D = aleal(12, 60);
    tr = transit();
    print(sprintf(0, "%s %d:%02d  section %d : %d s (energie %.2f)", TITRE, floor(tps() / 60), floor(tps()) % 60, NS,
        floor(D + 0.5), E));
    ((NS === 1) || proba(0.65)) ? mutation((proba(0.2) ? 0.05 : aleal(1.5, 10))) : gliss(aleal(4, 20));
    excite();
    niv(0, (proba(0.8) ? alea(-6, 0) : -80), tr);
    niv(1, (proba(0.5) ? alea(-10, -2) : -80), tr);
    proba(0.6) ? (
        peigne();
        niv(4, alea(-14, -4), tr);
    ) : niv(4, -80, tr);
    tab(TFS, (proba(0.6) ? aleal(0.1, 3) : aleal(3, 25)));
    vivre(D);
);

// la fin : les excitateurs s'arretent
function arreter() ( tab(TRST, `gx, `Paused); tab(TRST, `bx, `Paused); );
'''
