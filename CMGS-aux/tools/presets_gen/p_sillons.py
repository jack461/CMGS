from common import level, vca, output

NAMES = dict(INS='sillons', INSIN='sillin', ALGIN='SillIn', NOM='sillons', TITRE='Preset-Sillons')
FILE = 'Preset-Sillons.mSL'

TITLE = 'print("Preset-Sillons. Des boucles de bande qui se reenregistrent, a vitesse variable ; 10 minutes, mono, dans le buffer de sortie.");'

DOC = r'''
/*
  PRESET "SILLONS" : les boucles, le reenregistrement, le phonogene
  Deux lecteurs Brage prelevent des fragments au hasard dans le buffer d'entree (a l'endroit, a l'envers, transposes) ;
  ils s'enregistrent dans trois boucles courtes (de 0.7 a 9 s, des longueurs tirees au hasard, sans commune mesure), en
  s'ajoutant a ce qu'elles contiennent deja (overdub) : chaque boucle accumule ses passages, s'epaissit, s'efface.
  Chaque boucle est relue a sa vitesse (de -2 a 2 : a l'envers, transposee) qui glisse parfois (glissandos, arrets de
  bande), et se reinjecte un peu dans la suivante. Les ouvertures et les fermetures des enregistrements sont parfois des
  coupures franches (des "punch-in") ; une boucle peut se figer (un sillon ferme : elle repete sans fin ce qu'elle a)
  ou s'effacer d'un passage. Un chorus aleatoire imite le pleurage de la bande, un filtre change de couleur par
  paliers, une petite piece (Matrix) rapproche le tout.
  La forme : des sections de 8 s a 40 s, des evenements toutes les 1.5 a 5 s (arrets de bande, effacements,
  fluctuations de vitesse, nouveaux fragments).
'''

BODY1 = r'''
// ======================================================================================================================
// Sillons : les modules
// ======================================================================================================================
/*
  L'instance sillons : les lecteurs de fragments f1, f2 (Brage) sur le buffer d'entree (sillin:src), leur somme mono fo ;
  trois boucles b1, b2, b3 (des lignes courtes), leurs writers w1, w2, w3 (mode Sum : overdub, le sens d'ecriture tire au
  hasard) dont l'entree i1, i2, i3 recoit les fragments et un peu de la boucle precedente, et dont le gain suit les
  niveaux l4 s4, l5 s5, l6 s6 ; leurs lecteurs r1, r2, r3 (leur volume : l1 s1, l2 s2, l3 s3 ; leur vitesse glisse :
  k1 q1, k2 q2, k3 q3, en octaves) ; les fragments directs (l7 s7 e7 v7) ; la somme mx, le chorus fl (pleurage), le
  filtre tn (ts : sa couleur par paliers), la piece rm ; le niveau general (lm sm em vm) ; res, wo ; l'ecoute m0, m1.
*/
var KM = 7;                                   // le niveau general (0-2 : les boucles, 3-5 : leurs enregistrements, 6 : direct)
var MAST = -4;
var NVl = array(`l1, `l2, `l3, `l4, `l5, `l6, `l7, `lm);
var NVs = array(`s1, `s2, `s3, `s4, `s5, `s6, `s7, `sm);
var NVc = malloc(8);
var NVd = malloc(8);
'''

def glide(k):
    return (f"        Effect k{k}  type LFO  chan 1  freq 0.01  amp 0  offset 0\n"
            f"        Effect q{k}  type Math  chan 1  source Effect k{k}  mode Slew  attack 1000  release 1000\n")

def wloop(k, prev):
    return (f"        Effect i{k}  type Mixer  chan 1  src1 Effect fo  gain1 0  src2 Reader r{prev}  gain2 -120\n"
            f"        Writer w{k}  line b{k}  source Effect i{k}  mode Sum  overdub 75  direction @{4 + k}@\n"
            f"                   mod Gain Effect s{3 + k}  depth 80  law dB  status Writing\n"
            f"        Reader r{k}  line b{k}  loop loop  xfade 30  out Own  speed @{7 + k}@  mod Volume Effect s{k}  depth 80  law dB\n"
            f"                   mod Speed Effect q{k}  depth 1  law Oct  status Reading\n")

TCRE = (r'''
var TCRE = data(
    Interstys
    Algorithm Sillons
        Line res  length @1@  chan 1
        Line b1  length @2@  chan 1
        Line b2  length @3@  chan 1
        Line b3  length @4@  chan 1
''' + level(1) + level(2) + level(3) + level(4) + level(5) + level(6) + level(7) + level('m')
    + glide(1) + glide(2) + glide(3) + r'''        Reader f1  line sillin:src  mode Brage  outchan 2  loop loop  out Own  block 400  overlap 25  search 0  transp 0
                   speed 1  status Reading
        Reader f2  line sillin:src  mode Brage  outchan 2  loop loop  out Own  block 900  overlap 25  search 0  transp 0
                   speed -1  status Reading
        Effect fo  type Mixer  chan 1  src1 Reader f1:0  gain1 -3  src2 Reader f1:1  gain2 -3  src3 Reader f2:0  gain3 -3
                   src4 Reader f2:1  gain4 -3
''' + wloop(1, 3) + wloop(2, 1) + wloop(3, 2) + vca(7, 'Effect fo') + r'''        Effect mx  type Mixer  chan 1  src1 Reader r1  gain1 0  src2 Reader r2  gain2 0  src3 Reader r3  gain3 0
                   src4 Effect v7  gain4 0
        Effect fl  type Chorus  chan 1  source Effect mx  delay 12  sweep 3  rate 0.6  wave Random  voices 1  jitter 0.5
                   glide 1  mix 100
        Effect ts  type Random  chan 1  mode Step  dist Uniform  rate 0.08  jitter 0.6  steps 6  glide 0.8  amp 1  offset 0
        Effect tn  type Filter  chan 1  source Effect fl  mode LP  stages 2  freq 3200  q 0.9  mod Cutoff Effect ts  depth 1.6
        Effect rm  type Matrix  chan 1  source Effect tn  mode Householder  lines 8  delays Random  seed @11@  dmin 11
                   dmax 47  decay 0.9  damp 6000  mix 22
''' + vca('m', 'Effect rm', '  limiter On') + output('Effect vm', 12) + r'''    End
    Instance sillons Sillons
);
''')

BODY2 = TCRE + r'''
var BN = array(`r1, `r2, `r3);                // les lecteurs des boucles
var WN = array(`w1, `w2, `w3);                // leurs writers
var XN = array(`i1, `i2, `i3);                // leurs entrees (la reinjection de la boucle precedente : gain2)
var KN = array(`k1, `k2, `k3);                // les glissements de leur vitesse : la cible
var QN = array(`q1, `q2, `q3);                // et la pente
var FN = array(`f1, `f2);                     // les lecteurs de fragments
var SPD = array(-2, -1, -0.5, 0.5, 0.75, 1, 1, 1.5, 2);    // les vitesses des boucles (< 0 : a l'envers)
var SB = malloc(3);                           // la vitesse de chaque boucle
var GO = malloc(3);                           // son glissement (octaves)
var OV = malloc(3);                           // son overdub (%)
var LB = malloc(3);                           // sa longueur (s)

// le sens d'ecriture d'une boucle : en avant, en arriere, ou les deux
function sens() local(u) ( u = rand(1); (u < 0.6) ? `Forward : ((u < 0.85) ? `Backward : `Both); );

// les modules : la duree du buffer de sortie, les longueurs des boucles, leurs sens, leurs vitesses, la graine, l'ecoute
function creer() local(k)
(
    k = 0; loop(3, LB[k] = aleal(0.7, 9); SB[k] = pioche(SPD); OV[k] = 75; k += 1;);
    print(sprintf(0, "%s : boucles de %.2f, %.2f et %.2f s", TITRE, LB[0], LB[1], LB[2]));
    tab(TCRE, sortie + 30, LB[0], LB[1], LB[2], sens(), sens(), sens(), SB[0], SB[1], SB[2], floor(rand(99999)),
        borne(ecoute, -120, 40));
);

var TFR = data(Interstys  Reader sillons:@1@  from @2@  to @3@  block @4@  speed @5@  overlap @6@  transp @7@);
var TOV = data(Interstys  Writer sillons:@1@  overdub @2@);
var TSB = data(Interstys  Reader sillons:@1@  speed @2@);
var TXF = data(Interstys  Effect sillons:@1@  gain2 @2@);
var TGL = data(Interstys  Effect sillons:@1@  offset @2@  Effect sillons:@3@  attack @4@  release @4@);
var TTN = data(Interstys  Effect sillons:ts  rate @1@  Effect sillons:fl  rate @2@  sweep @3@);

// le lecteur de fragments i : une region au hasard, des segments de 60 a 1500 ms, une vitesse, une transposition
function frag(i) local(d, w, a)
(
    d = dispo(); w = borne(aleal(0.5, 20), min(d, 0.3), d); a = rand(max(0, d - w));
    tab(TFR, FN[i], a, a + w, aleal(60, 1500), pioche(SPD), floor(alea(10, 40)), (proba(0.3) ? alea(-5, 5) : 0));
);

// la vitesse de la boucle k glisse vers oc octaves (par rapport a sa vitesse) en s secondes
function glisse(k, oc, s) local(a)
(
    a = borne(1000 * s / max(0.01, abs(oc - GO[k])), 1, 10000);
    GO[k] = oc;
    tab(TGL, KN[k], borne(oc, -10, 10), QN[k], a);
);

// la boucle k : son overdub (%) et ce qu'elle recoit de la boucle precedente (dB) : son gain reste sous 0.95
function boucle(k, ov, xg)
(
    xg = ((ov / 100 + pow(10, xg / 20)) > 0.95) ? 20 * log10(max(0.00001, 0.95 - ov / 100)) : xg;
    OV[k] = ov;
    tab(TOV, WN[k], ov);
    tab(TXF, XN[k], borne(xg, -120, 40));
);

// un arret de bande sur la boucle k : la vitesse tombe (-6 octaves), puis repart
function bande(k) local(g, s)
(
    (NVd[k] > -60) ? (
        print(sprintf(0, "%s %d:%02d  arret de bande (boucle %d)", TITRE, floor(tps() / 60), floor(tps()) % 60, k + 1));
        g = GO[k]; s = alea(0.5, 2.5);
        glisse(k, -6, s);
        attend(s + alea(0.3, 1.5));
        glisse(k, g, (proba(0.4) ? 0.05 : alea(0.3, 2)));
    );
);

// un effacement : la boucle k se remplit de neuf pendant un passage (si elle enregistre)
function efface(k) local(o)
(
    (NVd[3 + k] > -60) ? (
        print(sprintf(0, "%s %d:%02d  effacement (boucle %d)", TITRE, floor(tps() / 60), floor(tps()) % 60, k + 1));
        o = OV[k];
        tab(TOV, WN[k], 0);
        attend(LB[k] * 1.05);
        tab(TOV, WN[k], o);
    );
);

// une section dure D secondes : toutes les 1.5 a 5 s, un arret de bande, un effacement, une fluctuation de vitesse,
// ou de nouveaux fragments
function vivre(D) local(tf, u, k)
(
    tf = ptime() + D;
    while ((arret === 0) && (ptime() < tf - 0.3) && (tps() < sortie - FIN)) (
        attend(min(alea(1.5, 5), max(0.1, tf - ptime())));
        finrec();
        ((arret === 0) && (ptime() < tf - 1) && (tps() < sortie - FIN)) ? (
            k = floor(rand(2.999)); u = rand(1);
            (u < 0.12) ? bande(k) : ((u < 0.22) ? efface(k) :
            ((u < 0.42) ? glisse(k, GO[k] + alea(-0.06, 0.06), alea(0.5, 2)) : ((u < 0.65) ? frag(floor(rand(1.999))) : 0)));
        );
    );
);

function section() local(D, tr, k, f)
(
    energie();
    NS += 1;
    D = aleal(8, 40);
    tr = transit();
    print(sprintf(0, "%s %d:%02d  section %d : %d s (energie %.2f)", TITRE, floor(tps() / 60), floor(tps()) % 60, NS,
        floor(D + 0.5), E));
    frag(0); frag(1);
    k = 0;
    loop(3,
        // l'enregistrement s'ouvre ou se ferme (une coupure franche une fois sur deux)
        f = proba(0.3 + 0.45 * E);
        niv(3 + k, (f ? alea(-6, 0) : -80), (proba(0.5) ? 0.02 : alea(0.3, 3)));
        ((!f) && proba(0.3)) ? (
            boucle(k, 100, -120);
            print(sprintf(0, "%s %d:%02d  sillon ferme (boucle %d)", TITRE, floor(tps() / 60), floor(tps()) % 60, k + 1));
        ) : boucle(k, alea(50, 90), (proba(0.35) ? alea(-20, -12) : -120));
        proba(0.4) ? ( SB[k] = pioche(SPD); tab(TSB, BN[k], SB[k]); );
        proba(0.3) ? glisse(k, (proba(0.5) ? 0 : alea(-1, 1)), aleal(2, 15));
        niv(k, (proba(0.75) ? alea(-12, -3) : -80), tr);
        k += 1;
    );
    niv(6, (proba(0.25) ? alea(-16, -6) : -80), tr);
    tab(TTN, aleal(0.03, 0.4), aleal(0.2, 3), alea(1, 6));
    vivre(D);
);

// la fin : les lecteurs et les writers des boucles s'arretent
function arreter()
(
    tab(TRST, `f1, `Paused); tab(TRST, `f2, `Paused);
    tab(TRST, `r1, `Paused); tab(TRST, `r2, `Paused); tab(TRST, `r3, `Paused);
    tab(TWS, `w1, `Paused); tab(TWS, `w2, `Paused); tab(TWS, `w3, `Paused);
);
'''
