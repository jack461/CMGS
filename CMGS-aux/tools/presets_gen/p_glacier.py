from common import level, vca, output

NAMES = dict(INS='glacier', INSIN='glacin', ALGIN='GlacIn', NOM='glacier', TITRE='Preset-Glacier')
FILE = 'Preset-Glacier.mSL'

TITLE = 'print("Preset-Glacier. Le temps dilate : des etirements extremes, des gels, des halos transposes ; 10 minutes, mono, dans le buffer de sortie.");'

DOC = r'''
/*
  PRESET "GLACIER" : l'etirement et le gel
  Deux lecteurs en mode Stretch avancent dans le buffer d'entree 8 a 250 fois plus lentement que le temps reel (parfois
  a reculons), chacun dans une region tiree au hasard, transposes (deux octaves en dessous ... une octave au-dessus,
  parfois a l'envers) : le son devient une masse lente, granuleuse. Un lecteur Brage y jette des fragments (a l'endroit
  ou a l'envers). Un reseau de retards (Matrix) les prolonge ; par moments il se fige (loop Freeze) : il garde un
  instant du son, un accord immobile qui ondule, pendant que les couches mouvantes s'en vont, ou se taisent d'un coup.
  Un Shimmer les entoure d'un halo transpose (octaves, quintes, ou des intervalles infimes qui derivent), un chorus lent
  les epaissit, un passe-bas respire.
  La forme : des sections de 18 s a 80 s ; dans chacune, les etirements changent de vitesse, les regions derivent, les
  hauteurs basculent ; un gel sur deux sections environ.
'''

BODY1 = r'''
// ======================================================================================================================
// Glacier : les modules
// ======================================================================================================================
/*
  L'instance glacier : deux lecteurs Stretch t1, t2 et un lecteur Brage bg sur le buffer d'entree (glacin:src), leurs
  niveaux (l1 s1, l2 s2, l3 s3) ; leur somme mono mo ; un chorus ch ; un reseau de retards fz (le gel), son niveau
  (l4 s4 e4 v4) ; un Shimmer ha (le halo), son niveau (l5 s5 e5 v5) ; la somme su, un passe-bas lo que fait respirer un
  Random (rb) ; le niveau general (lm sm em vm) ; le buffer de sortie res et son writer wo ; l'ecoute m0, m1.
*/
var KM = 5;                                   // le niveau general (0, 1 : les etirements, 2 : les fragments, 3 : le gel, 4 : le halo)
var MAST = -4;
var NVl = array(`l1, `l2, `l3, `l4, `l5, `lm);
var NVs = array(`s1, `s2, `s3, `s4, `s5, `sm);
var NVc = malloc(6);
var NVd = malloc(6);
'''

TCRE = (r'''
var TCRE = data(
    Interstys
    Algorithm Glacier
        Line res  length @1@  chan 1
''' + level(1) + level(2) + level(3) + level(4) + level(5) + level('m') + r'''        Reader t1  line glacin:src  mode Stretch  outchan 2  loop loop  out Own  block 300  overlap 50  search 15  transp 0
                   stretch 0.05  speed 1  mod Volume Effect s1  depth 80  law dB  status Reading
        Reader t2  line glacin:src  mode Stretch  outchan 2  loop loop  out Own  block 400  overlap 50  search 15  transp 0
                   stretch 0.03  speed 0.5  mod Volume Effect s2  depth 80  law dB  status Reading
        Reader bg  line glacin:src  mode Brage  outchan 2  loop loop  out Own  block 600  overlap 40  search 0  transp 0
                   speed 1  mod Volume Effect s3  depth 80  law dB  status Reading
        Effect mo  type Mixer  chan 1  src1 Reader t1:0  gain1 -3  src2 Reader t1:1  gain2 -3  src3 Reader t2:0  gain3 -3
                   src4 Reader t2:1  gain4 -3  src5 Reader bg:0  gain5 -3  src6 Reader bg:1  gain6 -3
        Effect ch  type Chorus  chan 1  source Effect mo  delay 25  sweep 8  rate 0.12  wave Random  voices 3  jitter 0.5
                   glide 2  mix 40
        Effect fz  type Matrix  chan 1  source Effect mo  mode Hadamard  lines 16  delays Random  seed @2@  dmin 40
                   dmax 260  decay 20  damp 5000  wow 6  rate 0.13  mix 100  loop Decay
''' + vca(4, 'Effect fz') + r'''        Effect ha  type Shimmer  chan 1  source Effect mo  mode Hadamard  lines 8  decay 8  shimmer 50  shift 12  shift2 7
                   grain 120  damp 7000  hp 100  mix 100
''' + vca(5, 'Effect ha') + r'''        Effect su  type Mixer  chan 1  src1 Effect ch  gain1 0  src2 Effect v4  gain2 0  src3 Effect v5  gain3 0
        Effect rb  type Random  chan 1  mode Smooth  dist Gauss  rate 0.04  jitter 0.5  amp 1  offset 0
        Effect lo  type Filter  chan 1  source Effect su  mode LP  stages 2  freq 4500  q 0.7  mod Cutoff Effect rb  depth 1.5
''' + vca('m', 'Effect lo', '  limiter On') + output('Effect vm', 3) + r'''    End
    Instance glacier Glacier
);
''')

BODY2 = TCRE + r'''
// les modules : la graine des retards du gel, l'ecoute
function creer() ( tab(TCRE, sortie + 30, floor(rand(99999)), borne(ecoute, -120, 40)); );

var TN = array(`t1, `t2);                     // les etirements
var TST = data(Interstys  Reader glacier:@1@  from @2@  to @3@  stretch @4@  speed @5@  transp @6@  block @7@  overlap @8@
    search @9@);
var TSS = data(Interstys  Reader glacier:@1@  stretch @2@);
var TSP = data(Interstys  Reader glacier:@1@  speed @2@);
var TWIN = data(Interstys  Reader glacier:@1@  from @2@  to @3@);
var TBR = data(Interstys  Reader glacier:bg  from @1@  to @2@  block @3@  speed @4@  transp @5@  overlap @6@);
var TFZ = data(Interstys  Effect glacier:fz  loop @1@  decay @2@);
var THA = data(Interstys  Effect glacier:ha  shift @1@  shift2 @2@  shimmer @3@  decay @4@);
var TCH = data(Interstys  Effect glacier:ch  rate @1@  sweep @2@  delay @3@  Effect glacier:rb  rate @4@);

var PIT = array(0.25, 0.5, 0.5, 0.75, 1, 1, 1, 1.5, 2);   // les vitesses de lecture des blocs (la hauteur)
var HAL1 = array(12, 12, -12, 7, 0.15, 24, 5, 19);         // les halos : les transpositions des lignes paires
var HAL2 = array(12, 7, -12, -5, -0.15, 12, -7, 12);       // et impaires (demi-tons)
var WA = malloc(2);                           // les regions des etirements (s)
var WB = malloc(2);
var STv = malloc(2);                          // leurs etirements (la progression)
var SPv = malloc(2);                          // leurs vitesses (la hauteur)
var GELE = 0;                                 // 1 : le reseau est fige

// l'etirement i : une region de w secondes au hasard, sa progression st (0.004 : 250 fois plus lent ; < 0 : a reculons),
// sa hauteur sp (< 0 : les blocs a l'envers) et tr (demi-tons), ses blocs (ms)
function etire(i, w, st, sp, tr, blk) local(d, a)
(
    d = dispo(); w = borne(w, min(d, 1), d); a = rand(max(0, d - w));
    WA[i] = a; WB[i] = a + w; STv[i] = st; SPv[i] = sp;
    tab(TST, TN[i], a, a + w, borne(st, -32, 32), borne(sp, -32, 32), borne(tr, -24, 24), borne(blk, 10, 5000),
        floor(alea(30, 50)), alea(8, 25));
);

// les fragments : une region de w secondes, des segments de blk ms, leur vitesse, leur transposition
function brage(w, blk, sp, tr) local(d, a)
(
    d = dispo(); w = borne(w, min(d, 0.5), d); a = rand(max(0, d - w));
    tab(TBR, a, a + w, borne(blk, 10, 5000), borne(sp, -32, 32), borne(tr, -24, 24), floor(alea(20, 50)));
);

// le halo : ses transpositions, sa part transposee, sa duree
function halo() local(k)
(
    k = floor(rand(7.999));
    tab(THA, HAL1[k], HAL2[k], alea(30, 80), aleal(4, 20));
);

// la region de l'etirement i derive (de 2 a 20 % du buffer)
function derive(i) local(d, w, a)
(
    d = dispo(); w = min(WB[i] - WA[i], d);
    a = borne(WA[i] + signe(0.5) * aleal(0.02, 0.2) * d, 0, max(0, d - w));
    WA[i] = a; WB[i] = a + w;
    tab(TWIN, TN[i], a, a + w);
);

// un gel de h secondes : le reseau garde ce qu'il contient ; parfois les couches mouvantes se taisent d'un coup
function gel(h) local(cut, a, b, c)
(
    print(sprintf(0, "%s %d:%02d  gel (%d s)", TITRE, floor(tps() / 60), floor(tps()) % 60, floor(h + 0.5)));
    cut = proba(0.4);
    GELE = 1;
    tab(TFZ, `Freeze, 30);
    niv(3, alea(-5, -1), alea(1, 5));
    a = NVd[0]; b = NVd[1]; c = NVd[2];
    cut ? (
        niv(0, -80, alea(0.03, 0.4)); niv(1, -80, alea(0.03, 0.4)); niv(2, -80, alea(0.03, 0.4));
    );
    attend(h);
    cut ? (
        niv(0, a, alea(3, 12)); niv(1, b, alea(3, 12)); niv(2, c, alea(3, 12));
    );
    tab(TFZ, `Decay, aleal(8, 40));
    niv(3, alea(-20, -12), aleal(8, 20));
    GELE = 0;
);

// une section dure D secondes : toutes les 3 a 9 s, un etirement change de vitesse, de region ou de hauteur ; un gel
// une fois sur deux, apres le premier quart
function vivre(D) local(tf, u, i, g)
(
    tf = ptime() + D;
    g = proba(0.55);
    while ((arret === 0) && (ptime() < tf - 0.3) && (tps() < sortie - FIN)) (
        attend(min(alea(3, 9), max(0.1, tf - ptime())));
        finrec();
        ((arret === 0) && (ptime() < tf - 1) && (tps() < sortie - FIN)) ? (
            (g && (ptime() > tf - 0.75 * D)) ? (
                g = 0;
                gel(min(aleal(6, 30), max(3, sortie - FIN - tps() - 2)));
            ) : (
                i = floor(rand(1.999));
                (NVd[i] > -60) ? (
                    u = rand(1);
                    (u < 0.35) ? (
                        STv[i] = borne(STv[i] * aleal(0.6, 1.6), -32, 32);
                        tab(TSS, TN[i], STv[i]);
                    ) : ((u < 0.6) ? derive(i) : ((u < 0.72) ? (
                        SPv[i] = sign(SPv[i]) * pioche(PIT);
                        tab(TSP, TN[i], SPv[i]);
                    ) : 0));
                );
            );
        );
    );
);

function section() local(D, tr)
(
    energie();
    NS += 1;
    D = aleal(18, 80);
    tr = proba(0.25) ? alea(0.05, 0.4) : alea(3, 14);
    print(sprintf(0, "%s %d:%02d  section %d : %d s (energie %.2f)", TITRE, floor(tps() / 60), floor(tps()) % 60, NS,
        floor(D + 0.5), E));
    etire(0, aleal(6, 60), signe(0.25) * aleal(0.004, 0.12), signe(0.12) * pioche(PIT), (proba(0.3) ? alea(-0.5, 0.5) : 0),
        aleal(120, 600));
    niv(0, (proba(0.85) ? alea(-6, -2) : -80), tr);
    proba(0.45 + 0.4 * E) ? (
        etire(1, aleal(6, 60), signe(0.25) * aleal(0.004, 0.12), signe(0.12) * pioche(PIT),
            (proba(0.3) ? alea(-0.5, 0.5) : 0), aleal(120, 600));
        niv(1, alea(-9, -4), tr);
    ) : niv(1, -80, tr);
    proba(0.2 + 0.5 * E) ? (
        brage(aleal(2, 20), aleal(150, 2500), signe(0.4) * pioche(PIT), (proba(0.3) ? alea(-3, 3) : 0));
        niv(2, alea(-14, -5), tr);
    ) : niv(2, -80, tr);
    proba(0.6) ? (
        halo();
        niv(4, alea(-14, -4), 2 * tr + 2);
    ) : niv(4, -80, 2 * tr + 2);
    (!GELE) ? niv(3, alea(-20, -10), tr);
    tab(TCH, aleal(0.03, 0.4), alea(3, 12), alea(15, 40), aleal(0.015, 0.1));
    vivre(D);
);

// la fin : les lecteurs s'arretent
function arreter() ( tab(TRST, `t1, `Paused); tab(TRST, `t2, `Paused); tab(TRST, `bg, `Paused); );
'''
