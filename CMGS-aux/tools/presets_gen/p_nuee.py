from common import level, vca, output

NAMES = dict(INS='nuee', INSIN='nueein', ALGIN='NueeIn', NOM='nuee', TITRE='Preset-Nuee')
FILE = 'Preset-Nuee.mSL'

TITLE = 'print("Preset-Nuee. Des nuees de grains preleves au hasard dans le buffer d\'entree : 10 minutes, mono, dans le buffer de sortie.");'

DOC = r'''
/*
  PRESET "NUEE" : la granulation
  Trois couches de grains puisent dans le buffer d'entree, a des positions tirees au hasard dans une fenetre qui saute
  d'une region a l'autre : des grains fins (une poussiere, un essaim), moyens (un nuage), longs (des trainees). Chaque
  couche a son champ de hauteurs, tire au hasard (unisson, octaves, quintes, douziemes, tritons, quartes, tierces,
  micro-intervalles, glissements continus), ses grains a l'endroit ou a l'envers, plus ou moins reguliers. Un phaser que
  balaye un mouvement aleatoire lent, un passe-bas qui respire et un reseau de retards (Matrix) qui diffuse et prolonge
  achevent de dissoudre le son d'origine.
  La forme : des sections de 6 s a 1 min (poussiere, essaim, nuage, trainees, tutti, silences), enchainees en coupures
  ou en fondus, choisies d'apres une "energie" qui erre (faible au debut et a la fin) ; dans chaque section, les
  fenetres derivent, les densites accelerent ou ralentissent, des accents surgissent.
'''

BODY1 = r'''
// ======================================================================================================================
// Nuee : les modules
// ======================================================================================================================
/*
  L'instance nuee : trois couches de grains g1 (fins), g2 (moyens), g3 (longs) qui lisent le buffer d'entree (nueein:src) ;
  leurs niveaux (l1 s1, l2 s2, l3 s3) ; leurs champs de hauteurs p1, p2, p3 (des Random qui modulent leur vitesse, en
  octaves : des paliers, ou une marche) ; leur melange mx ; un phaser ph, balaye par un Random lent (rf) ; un passe-bas
  lo qui respire (rb) ; un reseau de retards mt ; le niveau general (lm sm em vm) ; le buffer de sortie res et son
  writer wo ; l'ecoute m0, m1 (vers Out:0, Out:1).
*/
var KM = 3;                                   // le niveau general (0, 1, 2 : les couches)
var MAST = -4;                                // son niveau (dB)
var NVl = array(`l1, `l2, `l3, `lm);
var NVs = array(`s1, `s2, `s3, `sm);
var NVc = malloc(4);
var NVd = malloc(4);
'''

TCRE = (r'''
var TCRE = data(
    Interstys
    Algorithm Nuee
        Line res  length @1@  chan 1
''' + level(1) + level(2) + level(3) + level('m') + r'''        Effect p1  type Random  chan 1  mode Step  dist Uniform  rate 12  jitter 0.7  steps 0  amp 0  offset 0
        Effect p2  type Random  chan 1  mode Step  dist Uniform  rate 6  jitter 0.7  steps 0  amp 0  offset 0
        Effect p3  type Random  chan 1  mode Walk  dist Uniform  rate 2  walk 0.3  glide 0.3  amp 0  offset 0
        Effect rf  type Random  chan 1  mode Smooth  dist Uniform  rate 0.2  jitter 0.5  amp 1  offset 0
        Effect rb  type Random  chan 1  mode Smooth  dist Gauss  rate 0.06  jitter 0.5  amp 1  offset 0
        Reader g1  line nueein:src  mode Grains  outchan 1  loop loop  out Own  size 40  density 5  plateau 10  fadein 50
                   mod Volume Effect s1  depth 80  law dB  mod Speed Effect p1  depth 1  law Oct  status Reading
        Reader g2  line nueein:src  mode Grains  outchan 1  loop loop  out Own  size 400  density 4  plateau 40  fadein 50
                   mod Volume Effect s2  depth 80  law dB  mod Speed Effect p2  depth 1  law Oct  status Reading
        Reader g3  line nueein:src  mode Grains  outchan 1  loop loop  out Own  size 2000  density 1  plateau 50  fadein 40
                   mod Volume Effect s3  depth 80  law dB  mod Speed Effect p3  depth 1  law Oct  status Reading
        Effect mx  type Mixer  chan 1  src1 Reader g1  gain1 0  src2 Reader g2  gain2 0  src3 Reader g3  gain3 0
        Effect ph  type Phaser  chan 1  source Effect mx  mode @2@  stages @3@  freq 700  sweep 3  rate 0.05  feedback 0.5
                   q 3  glide 3  mix 50  mod Freq Effect rf  depth 1.5
        Effect lo  type Filter  chan 1  source Effect ph  mode LP  stages 2  freq 5000  q 0.8  mod Cutoff Effect rb  depth 1.2
        Effect mt  type Matrix  chan 1  source Effect lo  mode Householder  lines 12  delays Random  seed @4@  dmin 17
                   dmax 110  decay 3  damp 7000  wow 3  rate 0.4  mix @5@
''' + vca('m', 'Effect mt', '  limiter On') + output('Effect vm', 6) + r'''    End
    Instance nuee Nuee
);
''')

BODY2 = TCRE + r'''
// les modules : le phaser Classic ou Resonant, ses etages, la graine des retards, la part du reseau, l'ecoute
function creer()
(
    tab(TCRE, sortie + 30, (proba(0.5) ? `Classic : `Resonant), floor(alea(6, 16)), floor(rand(99999)), alea(30, 55),
        borne(ecoute, -120, 40));
);

var TGR = data(Interstys  Reader nuee:@1@  from @2@  to @3@  size @4@  sizernd @5@  plateau @6@  fadein @7@
    density @8@  onsetrnd @9@  direction @10@  speedrnd @11@  speed @12@  volrnd @13@  gvol @14@);
var TWIN = data(Interstys  Reader nuee:@1@  from @2@  to @3@);
var TDEN = data(Interstys  Reader nuee:@1@  density @2@);
var TPF = data(Interstys  Effect nuee:@1@  mode @2@  amp @3@  steps @4@  rate @5@);
var TPH = data(Interstys  Effect nuee:ph  freq @1@  feedback @2@  rate @3@  sweep @4@  Effect nuee:rf  rate @5@
    Effect nuee:rb  rate @6@);
var TMT = data(Interstys  Effect nuee:mt  decay @1@  damp @2@);

var GN = array(`g1, `g2, `g3);                // les couches
var PN = array(`p1, `p2, `p3);                // leurs champs de hauteurs
var WA = malloc(3);                           // leurs fenetres (s)
var WB = malloc(3);
var GD = malloc(3);                           // leurs densites (/s)
// les champs de hauteurs : l'etendue (octaves de part et d'autre) et les paliers (0 : continu)
var CHA = array(0, 1, 0.5833, 1.5833, 2, 1, 0.08, 1.5, 0.8333, 0.6667);
var CHP = array(0, 3, 3, 3, 5, 5, 0, 0, 5, 5);
var CHHAR = array(1, 2, 3, 4, 8, 9);          // les champs "harmoniques"
var CHMIC = array(0, 6, 2);                   // unisson, micro-intervalles, quintes
var BASES = array(0.25, 0.5, 0.5, 0.75, 1, 1, 1, 1.5, 2);
var BASESL = array(0.25, 0.5, 0.5, 0.75, 1);
var NOMSEC = array("poussiere", "essaim", "nuage", "trainees", "tutti", "silence");
// les poids des sections, selon l'energie (faible, moyenne, forte)
var W1 = array(30, 8, 25, 27, 0, 10);
var W2 = array(15, 20, 22, 18, 16, 9);
var W3 = array(8, 30, 12, 10, 36, 4);
// les facteurs aleatoires des grains (taille, volume, vitesse : 1 ... 5) et l'irregularite des attaques (0 ... 1)
var Fsz = 1.5;
var Fvol = 1.5;
var Fsp = 1;
var Fon = 1;

// la couche i : taille (ms), densite (/s), plateau et attaque (%), sens (-1 a l'envers ... 1 a l'endroit), vitesse (la
// hauteur), largeur de sa fenetre (s) ; la fenetre au hasard dans le buffer ; le gain des grains selon leur nombre
function couche(i, sz, dn, pl, fi, dir, sp, w) local(d, a, ov, gv)
(
    d = dispo();
    w = borne(w, min(d, 0.05 + 3 * sz * sp / 1000), d);
    a = rand(max(0, d - w));
    ov = dn * sz / 1000;
    gv = borne(-10 * log10(max(1, ov)), -20, 6);
    WA[i] = a; WB[i] = a + w; GD[i] = dn;
    tab(TGR, GN[i], a, a + w, borne(sz, 10, 10000), borne(Fsz, 1, 5), floor(borne(pl, 0, 100)), floor(borne(fi, 0, 100)),
        borne(dn, 0.01, 100), borne(Fon, 0, 1), borne(dir, -1, 1), borne(Fsp, 1, 5), borne(sp, 0.05, 8), borne(Fvol, 1, 5), gv);
);

// le champ de hauteurs k de la couche i : son mode (Step : des paliers, Walk : une marche), sa vitesse (Hz)
function champ(i, k, md, rt) ( tab(TPF, PN[i], md, CHA[k], CHP[k], rt); );

// poussiere : des grains fins et rares, des accents, de longs echos
function sec0(tr)
(
    Fsz = alea(1, 2.5); Fvol = alea(1.5, 4); Fsp = alea(1, 1.3); Fon = 1;
    couche(0, aleal(6, 45), aleal(1.5, 14), alea(0, 25), alea(10, 60), alea(-1, 1), pioche(BASES), aleal(0.5, 30));
    champ(0, floor(rand(9.99)), `Step, aleal(4, 25));
    niv(0, alea(-4, 0), tr);
    niv(1, -80, tr);
    proba(0.3) ? (
        Fsz = 1.5; Fvol = 1.5; Fsp = 1.2; Fon = 1;
        couche(2, aleal(900, 4000), aleal(0.3, 1), 40, 50, alea(-1, 1), pioche(BASESL), aleal(5, 40));
        champ(2, 7, `Walk, aleal(0.5, 3));
        niv(2, alea(-20, -12), tr);
    ) : niv(2, -80, tr);
    tab(TMT, aleal(3, 14), aleal(5000, 12000));
);

// essaim : des grains fins et serres, une hauteur presque unique, battante
function sec1(tr)
(
    Fsz = alea(1.2, 2); Fvol = alea(1, 1.6); Fsp = aleal(1.003, 1.06); Fon = alea(0.2, 1);
    couche(0, aleal(12, 90), aleal(25, 95), alea(20, 50), alea(30, 60), (proba(0.7) ? 1 : alea(-1, 1)), pioche(BASES),
        aleal(0.3, 8));
    champ(0, pioche(CHMIC), `Step, aleal(10, 40));
    niv(0, alea(-6, -2), tr);
    proba(0.4) ? (
        Fsz = 1.5; Fvol = 1.5; Fsp = 1; Fon = 0.7;
        couche(1, aleal(150, 600), aleal(2, 6), 40, 50, 1, pioche(BASES), aleal(2, 15));
        champ(1, pioche(CHHAR), `Step, aleal(1, 5));
        niv(1, alea(-16, -10), tr);
    ) : niv(1, -80, tr);
    niv(2, -80, tr);
    tab(TMT, aleal(1, 4), aleal(4000, 9000));
);

// nuage : des grains moyens, un accord (octaves, quintes...), plus ou moins dense
function sec2(tr)
(
    Fsz = alea(1.3, 2.5); Fvol = alea(1, 2); Fsp = aleal(1, 1.02); Fon = alea(0.5, 1);
    couche(1, aleal(150, 1400), aleal(3, 18), alea(20, 60), alea(30, 70), alea(0, 1), pioche(BASES), aleal(2, 25));
    champ(1, pioche(CHHAR), `Step, aleal(2, 12));
    niv(1, alea(-5, -1), tr);
    proba(0.3) ? (
        Fsz = 2; Fvol = 3; Fsp = 1.1; Fon = 1;
        couche(0, aleal(8, 30), aleal(2, 8), 10, 40, alea(-1, 1), pioche(BASES), aleal(1, 20));
        champ(0, floor(rand(9.99)), `Step, 8);
        niv(0, alea(-18, -12), tr);
    ) : niv(0, -80, tr);
    proba(0.3) ? (
        Fsz = 1.5; Fvol = 1.3; Fsp = 1.1; Fon = 0.5;
        couche(2, aleal(1000, 5000), aleal(0.3, 1.2), 50, 40, alea(-1, 1), pioche(BASESL), aleal(5, 40));
        champ(2, pioche(CHHAR), `Step, aleal(0.2, 1));
        niv(2, alea(-14, -9), tr);
    ) : niv(2, -80, tr);
    tab(TMT, aleal(2, 7), aleal(4000, 10000));
);

// trainees : de longs grains rares, leur hauteur erre (une marche), a l'endroit et a l'envers
function sec3(tr)
(
    Fsz = alea(1.2, 2); Fvol = alea(1, 1.5); Fsp = alea(1, 1.5); Fon = alea(0.3, 1);
    couche(2, aleal(900, 7000), aleal(0.3, 2.5), alea(30, 70), alea(25, 60), alea(-1, 1), pioche(BASESL), aleal(5, 60));
    champ(2, 7, `Walk, aleal(0.5, 4));
    niv(2, alea(-5, -1), tr);
    proba(0.4) ? (
        Fsz = 2; Fvol = 3; Fsp = 1.2; Fon = 1;
        couche(0, aleal(6, 25), aleal(1, 6), 0, 30, alea(-1, 1), pioche(BASES), aleal(1, 30));
        champ(0, floor(rand(9.99)), `Step, 6);
        niv(0, alea(-22, -14), tr);
    ) : niv(0, -80, tr);
    niv(1, -80, tr);
    tab(TMT, aleal(4, 12), aleal(3000, 8000));
);

// tutti : les trois couches
function sec4(tr)
(
    Fsz = 1.8; Fvol = 2; Fsp = 1.05; Fon = 0.8;
    couche(0, aleal(10, 60), aleal(15, 60), 30, 50, alea(-1, 1), pioche(BASES), aleal(0.5, 10));
    couche(1, aleal(150, 900), aleal(3, 12), 40, 50, alea(0, 1), pioche(BASES), aleal(2, 20));
    couche(2, aleal(800, 5000), aleal(0.4, 2), 50, 40, alea(-1, 1), pioche(BASESL), aleal(5, 40));
    champ(0, floor(rand(9.99)), `Step, aleal(5, 30));
    champ(1, pioche(CHHAR), `Step, aleal(2, 8));
    champ(2, floor(rand(9.99)), `Walk, aleal(0.5, 3));
    niv(0, alea(-9, -5), tr);
    niv(1, alea(-9, -5), tr);
    niv(2, alea(-9, -5), tr);
    tab(TMT, aleal(2, 6), aleal(5000, 11000));
);

// la fenetre de la couche i derive (de 2 a 20 % du buffer)
function derive(i) local(d, w, a)
(
    d = dispo(); w = min(WB[i] - WA[i], d);
    a = borne(WA[i] + signe(0.5) * aleal(0.02, 0.2) * d, 0, max(0, d - w));
    WA[i] = a; WB[i] = a + w;
    tab(TWIN, GN[i], a, a + w);
);

// la densite de la couche i accelere ou ralentit
function densite(i, f) ( GD[i] = borne(GD[i] * f, 0.05, 100); tab(TDEN, GN[i], GD[i]); );

// un accent sur la couche i
function accent(i) local(v)
(
    v = NVd[i];
    niv(i, min(0, v + alea(4, 9)), alea(0.05, 0.4));
    attend(alea(0.3, 1.5));
    niv(i, v, alea(1, 4));
);

// une section dure D secondes : toutes les 1.5 a 6 s, une couche qui sonne derive, accelere, ralentit ou s'accentue
function vivre(D) local(tf, u, i)
(
    tf = ptime() + D;
    while ((arret === 0) && (ptime() < tf - 0.3) && (tps() < sortie - FIN)) (
        attend(min(alea(1.5, 6), max(0.1, tf - ptime())));
        finrec();
        ((arret === 0) && (ptime() < tf - 1) && (tps() < sortie - FIN)) ? (
            i = floor(rand(2.999));
            (NVd[i] > -60) ? (
                u = rand(1);
                (u < 0.45) ? derive(i) : ((u < 0.75) ? densite(i, aleal(0.5, 2)) : ((u < 0.88) ? accent(i) : 0));
            );
        );
    );
);

function section() local(ty, D, tr)
(
    energie();
    ty = tirage((E < 0.35) ? W1 : ((E < 0.7) ? W2 : W3));
    NS += 1;
    tr = transit();
    D = (ty === 5) ? alea(1, 5) : ((ty === 4) ? aleal(6, 25) : aleal(10, 55));
    print(sprintf(0, "%s %d:%02d  section %d : %s, %d s (energie %.2f)", TITRE, floor(tps() / 60), floor(tps()) % 60, NS,
        NOMSEC[ty], floor(D + 0.5), E));
    (ty === 5) ? (
        niv(KM, -80, alea(0.03, 1.5));
        attend(D);
        niv(KM, MAST, alea(0.05, 3));
    ) : (
        (ty === 0) ? sec0(tr) : ((ty === 1) ? sec1(tr) : ((ty === 2) ? sec2(tr) : ((ty === 3) ? sec3(tr) : sec4(tr))));
        tab(TPH, aleal(250, 3000), alea(-0.6, 0.85), aleal(0.01, 0.4), alea(1, 5), aleal(0.03, 0.6), aleal(0.02, 0.2));
        vivre(D);
    );
);

// la fin : les couches s'arretent
function arreter() ( tab(TRST, `g1, `Paused); tab(TRST, `g2, `Paused); tab(TRST, `g3, `Paused); );
'''
