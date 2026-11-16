from common import level, vca, output

NAMES = dict(INS='vertige', INSIN='vertin', ALGIN='VertIn', NOM='vertige', TITRE='Preset-Vertige')
FILE = 'Preset-Vertige.mSL'

TITLE = 'print("Preset-Vertige. Des spirales de decalages de frequence dans des boucles de retard ; 10 minutes, mono, dans le buffer de sortie.");'

DOC = r'''
/*
  PRESET "VERTIGE" : les spirales
  Des fragments du buffer d'entree, surtout a l'envers (Brage), et des grains sont injectes par bouffees dans deux
  boucles de retard (un retard court et un long, tires au hasard) ; a chaque tour, un decaleur de frequence (Ring, mode
  Up ou Down) deplace tout le spectre de quelques Hz : le son monte ou descend sans fin, en spirale, se dedouble, devient
  inharmonique, se perd dans les aigus ou dans les graves (des filtres dans la boucle l'y eteignent). Le decalage erre
  (une marche aleatoire) et change de regime d'une section a l'autre : des battements lents (moins de 1 Hz), des
  spirales (2 a 14 Hz), des cascades metalliques (20 a 160 Hz). Un phaser a balayage sans fin (barber pole) tourne
  par-dessus, une petite piece (Matrix) rapproche le tout.
  La forme : des sections de 10 s a 45 s ; toutes les 1 a 4 s, une bouffee d'entree, une chute (les entrees se taisent,
  les boucles tournent longtemps), une coupure (les boucles se vident), ou un nouveau decalage.
'''

BODY1 = r'''
// ======================================================================================================================
// Vertige : les modules
// ======================================================================================================================
/*
  L'instance vertige : les lecteurs rv (Brage, surtout a l'envers) et gr (Grains) sur le buffer d'entree (vertin:src),
  leurs niveaux (l1 s1, l2 s2), leur somme fo ; deux boucles A et B : la ligne (ya, yb : 4 s), son writer (xa, xb) qui
  ecrit l'entree (ia, ib : fo et le retour), le lecteur en retard (ra, rb), le decaleur (fa, fb : Ring Up ou Down ; wa,
  wb : la marche aleatoire de son decalage), un passe-haut et un passe-bas (ha, ka ; hb, kb), le retour (ga za, gb zb :
  son gain, lineaire ; fa2, fb2) ; les sorties des boucles (l3 s3 e3 v3, l4 s4 e4 v4) et les fragments directs (l5 s5
  e5 v5), leur somme ou, le phaser bp (barber pole), la piece sp ; le niveau general (lm sm em vm) ; res, wo ; m0, m1.
*/
var KM = 5;                                   // le niveau general (0, 1 : les entrees, 2, 3 : les boucles, 4 : direct)
var MAST = -4;
var NVl = array(`l1, `l2, `l3, `l4, `l5, `lm);
var NVs = array(`s1, `s2, `s3, `s4, `s5, `sm);
var NVc = malloc(6);
var NVd = malloc(6);
'''

# une boucle : x la lettre (a, b), d le retard (argument), m le mode du decaleur (argument), r la vitesse de sa marche
def spiral(x, d, m, r):
    return (f"        Effect g{x}  type LFO  chan 1  freq 0.01  amp 0  offset 0\n"
            f"        Effect z{x}  type Math  chan 1  source Effect g{x}  mode Slew  attack 1000  release 1000\n"
            f"        Effect w{x}  type Random  chan 1  mode Walk  dist Uniform  rate {r}  walk 0.15  glide 0.5  amp 0.5  offset 0\n"
            f"        Effect i{x}  type Mixer  chan 1  src1 Effect fo  gain1 0  src2 Effect f{x}2  gain2 0\n"
            f"        Writer x{x}  line y{x}  source Effect i{x}  status Writing\n"
            f"        Reader r{x}  writer x{x}  delay @{d}@  out Own  status Reading\n"
            f"        Effect f{x}  type Ring  chan 1  source Reader r{x}  mode @{m}@  freq 3  wave Sine  mix 100\n"
            f"                   mod Freq Effect w{x}  depth 1\n"
            f"        Effect h{x}  type Filter  chan 1  source Effect f{x}  mode HP  stages 1  freq 70  q 0.707\n"
            f"        Effect k{x}  type Filter  chan 1  source Effect h{x}  mode LP  stages 1  freq 6500  q 0.707\n"
            f"        Effect f{x}2  type Math  chan 1  source Effect k{x}  src2 Effect z{x}  mode Mul\n")

TCRE = (r'''
var TCRE = data(
    Interstys
    Algorithm Vertige
        Line res  length @1@  chan 1
        Line ya  length 4  chan 1
        Line yb  length 4  chan 1
''' + level(1) + level(2) + level(3) + level(4) + level(5) + level('m')
    + r'''        Reader rv  line vertin:src  mode Brage  outchan 2  loop loop  out Own  block 900  overlap 30  search 0  transp 0
                   speed -1  mod Volume Effect s1  depth 80  law dB  status Reading
        Reader gr  line vertin:src  mode Grains  outchan 1  loop loop  out Own  size 120  density 8  plateau 30  fadein 50
                   mod Volume Effect s2  depth 80  law dB  status Reading
        Effect fo  type Mixer  chan 1  src1 Reader rv:0  gain1 -3  src2 Reader rv:1  gain2 -3  src3 Reader gr  gain3 0
''' + spiral('a', 2, 4, 0.4) + spiral('b', 3, 5, 0.25) + vca(3, 'Effect ka') + vca(4, 'Effect kb') + vca(5, 'Effect fo')
    + r'''        Effect ou  type Mixer  chan 1  src1 Effect v3  gain1 0  src2 Effect v4  gain2 0  src3 Effect v5  gain3 0
        Effect bp  type Phaser  chan 1  source Effect ou  mode @6@  stages 10  freq 900  sweep 4  rate 0.05  feedback 0.55
                   glide 3  mix 55
        Effect sp  type Matrix  chan 1  source Effect bp  mode Householder  lines 10  delays Random  seed @7@  dmin 13
                   dmax 90  decay 1.8  damp 7000  mix 25
''' + vca('m', 'Effect sp', '  limiter On') + output('Effect vm', 8) + r'''    End
    Instance vertige Vertige
);
''')

BODY2 = TCRE + r'''
// les modules : les retards des boucles (un court, un long), le sens de leurs decaleurs (souvent opposes), le sens du
// phaser, la graine de la piece, l'ecoute
function creer() local(m)
(
    m = proba(0.5) ? `Up : `Down;
    tab(TCRE, sortie + 30, aleal(0.07, 0.6), aleal(0.6, 3.2), m, (proba(0.6) ? ((m === `Up) ? `Down : `Up) : m),
        (proba(0.5) ? `BarberUp : `BarberDown), floor(rand(99999)), borne(ecoute, -120, 40));
);

var TFB = data(Interstys  Effect vertige:@1@  offset @2@  Effect vertige:@3@  attack @4@  release @4@);
var TRG = data(Interstys  Effect vertige:@1@  freq @2@  Effect vertige:@3@  amp @4@  rate @5@);
var TRV = data(Interstys  Reader vertige:rv  from @1@  to @2@  block @3@  speed @4@  overlap @5@  transp @6@);
var TGV = data(Interstys  Reader vertige:gr  from @1@  to @2@  size @3@  density @4@  speed @5@  direction @6@  speedrnd @7@);
var TBP = data(Interstys  Effect vertige:bp  rate @1@  feedback @2@  Effect vertige:sp  decay @3@);

var GA = array(`ga, `gb);                     // le retour des boucles : sa cible
var ZA = array(`za, `zb);                     // et sa pente
var FA = array(`fa, `fb);                     // les decaleurs
var WK = array(`wa, `wb);                     // leurs marches
var SPV = array(-1, -1, -0.5, -2, 1, 0.5);    // les vitesses des fragments (surtout a l'envers)
var SPG = array(0.5, 1, 1, 2);                // celles des grains
var FBv = malloc(2);                          // le retour de chaque boucle (gain lineaire)

// le retour de la boucle k va vers g (0 ... 0.97) en s secondes
function retour(k, g, s) local(a)
(
    g = borne(g, 0, 0.97);
    a = borne(1000 * s / max(0.001, abs(g - FBv[k])), 1, 10000);
    FBv[k] = g;
    tab(TFB, GA[k], g, ZA[k], a);
);

// un regime de decalage (Hz) : des battements, des spirales, des cascades
function regime() local(u)
(
    u = rand(1);
    (u < 0.3 - 0.15 * E) ? aleal(0.05, 1.2) : ((u < 0.75) ? aleal(1.5, 14) : aleal(18, 160));
);

// le decalage de la boucle k : sa frequence, l'etendue (octaves) et la vitesse de son errance
function decal(k) ( tab(TRG, FA[k], regime(), WK[k], alea(0.1, 1), aleal(0.05, 0.8)); );

// les entrees : des fragments (une region au hasard, des segments de 250 ms a 2.5 s) et des grains
function entree() local(d, w, a)
(
    d = dispo();
    w = borne(aleal(1, 30), min(d, 0.5), d); a = rand(max(0, d - w));
    tab(TRV, a, a + w, aleal(250, 2500), pioche(SPV), floor(alea(20, 45)), (proba(0.3) ? alea(-5, 5) : 0));
    w = borne(aleal(0.5, 20), min(d, 0.3), d); a = rand(max(0, d - w));
    tab(TGV, a, a + w, aleal(40, 400), aleal(2, 25), pioche(SPG), alea(-1, 1), alea(1, 1.3));
);

// une bouffee : une entree s'ouvre, puis se referme
function bouffee() local(k)
(
    k = floor(rand(1.999));
    niv(k, alea(-6, 0), alea(0.02, 0.5));
    attend(aleal(0.3, 4));
    niv(k, -80, alea(0.05, 2));
);

// une chute : les entrees se taisent, les boucles tournent longtemps
function chute()
(
    print(sprintf(0, "%s %d:%02d  chute", TITRE, floor(tps() / 60), floor(tps()) % 60));
    niv(0, -80, 0.3); niv(1, -80, 0.3);
    retour(0, alea(0.9, 0.95), alea(0.5, 2)); retour(1, alea(0.9, 0.95), alea(0.5, 2));
);

// une coupure : les boucles se vident, puis repartent sur une bouffee
function coupure() local(a, b)
(
    print(sprintf(0, "%s %d:%02d  coupure", TITRE, floor(tps() / 60), floor(tps()) % 60));
    a = FBv[0]; b = FBv[1];
    retour(0, 0, alea(0.02, 0.4)); retour(1, 0, alea(0.02, 0.4));
    attend(alea(0.5, 3));
    retour(0, a, alea(0.5, 3)); retour(1, b, alea(0.5, 3));
    bouffee();
);

// une section dure D secondes : toutes les 1 a 4 s, une bouffee, une chute, une coupure ou un nouveau decalage
function vivre(D) local(tf, u)
(
    tf = ptime() + D;
    while ((arret === 0) && (ptime() < tf - 0.3) && (tps() < sortie - FIN)) (
        attend(min(alea(1, 4), max(0.1, tf - ptime())));
        finrec();
        ((arret === 0) && (ptime() < tf - 1) && (tps() < sortie - FIN)) ? (
            u = rand(1);
            (u < 0.35) ? bouffee() : ((u < 0.45) ? chute() : ((u < 0.52) ? coupure() :
            ((u < 0.67) ? decal(floor(rand(1.999))) : 0)));
        );
    );
);

function section() local(D, tr, k)
(
    energie();
    NS += 1;
    D = aleal(10, 45);
    tr = transit();
    print(sprintf(0, "%s %d:%02d  section %d : %d s (energie %.2f)", TITRE, floor(tps() / 60), floor(tps()) % 60, NS,
        floor(D + 0.5), E));
    entree();
    k = 0;
    loop(2,
        decal(k);
        retour(k, alea(0.55, 0.93), alea(0.5, 4));
        niv(2 + k, (proba(0.85) ? alea(-8, -2) : -80), tr);
        k += 1;
    );
    niv(4, (proba(0.3) ? alea(-16, -8) : -80), tr);
    tab(TBP, aleal(0.01, 0.25), alea(0.3, 0.8), aleal(1, 4));
    bouffee();
    vivre(D);
);

// la fin : les lecteurs et les writers s'arretent
function arreter()
(
    tab(TRST, `rv, `Paused); tab(TRST, `gr, `Paused); tab(TRST, `ra, `Paused); tab(TRST, `rb, `Paused);
    tab(TWS, `xa, `Paused); tab(TWS, `xb, `Paused);
);
'''
