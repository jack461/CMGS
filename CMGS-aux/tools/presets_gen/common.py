# Parties communes des cinq presets d'Interstys (CMGS-scripts/Presets/Preset-*.mSL)
# Jetons : @INS@ (instance principale), @INSIN@ (instance du buffer d'entree), @ALGIN@ (son algorithme),
# @NOM@ (nom du processus), @TITRE@ (titre), @k@ (k-ieme valeur d'une table modele : 7700000000 + k)

USAGE = r'''
  Utilisation (la meme pour les cinq presets : Nuee, Glacier, Sillons, Resonances, Vertige)
    - Regler les variables de "Reglages" ci-dessous, puis deposer ce fichier dans la fenetre d'Interstys. Une session
      vierge suffit : le preset cree ses buffers et ses modules, dans deux instances (@INSIN@ : le buffer d'entree ;
      @INS@ : le traitement et le buffer de sortie), sans toucher aux autres modules.
    - Sans fichier (fichier = "") : le son de la piste est enregistre dans le buffer d'entree (In:0, et In:1 si canaux
      vaut 2) pendant "duree" secondes. Lancer d'abord la lecture de la piste (une nappe, un son de plusieurs minutes),
      puis deposer le preset : la generation commence apres 6 secondes d'enregistrement, et ne puise que dans la part
      deja enregistree. Avec un fichier : il est lu dans le buffer d'entree (mono ou stereo ; un nom relatif au dossier
      du projet, CMGS-auxiliary.eel en marche, ou un chemin complet), et "duree" doit valoir sa duree (ou moins : au-dela,
      les positions reviennent au debut du fichier).
    - La generation dure "sortie" secondes, en temps reel : REAPER doit faire tourner la piste (lecture en cours, ou
      piste armee avec le monitoring). Le resultat, mono, s'ecrit dans le buffer de sortie (la ligne "res" de l'instance
      @INS@, "@INS@:res" dans une table) et s'entend sur Out:0 et Out:1 (niveau "ecoute"). Le journal suit les sections.
    - Le hasard decide de tout (les positions dans le buffer, les durees, les textures, les hauteurs, les enchainements) :
      chaque execution est differente. Redeposer le fichier relance une generation (la precedente s'arrete, ses buffers
      sont refaits). Presets-Stop.mSL arrete les generations en cours (un fondu ; les buffers restent) ;
      Presets-Free.mSL retire tout.
    - La premiere fois, le journal note deux erreurs (2787, 2757) : les instances a retirer n'existent pas encore.
'''

SETTINGS = r'''
// ======================================================================================================================
// Reglages
// ======================================================================================================================
var fichier = "";     // un fichier son pour le buffer d'entree ; "" : le son de la piste (In:0) est enregistre
var duree = 180;      // la duree du buffer d'entree (s, au plus 1300) : celle de l'enregistrement, ou celle du fichier
var canaux = 2;       // les canaux enregistres : 1 (In:0) ou 2 (In:0 et In:1) ; un fichier donne les siens
var continu = 0;      // 1 : l'enregistrement continue (le buffer garde les "duree" dernieres secondes) ; 0 : il s'arrete
var sortie = 600;     // la duree produite dans le buffer de sortie (s)
var ecoute = -6;      // le niveau d'ecoute du resultat sur Out:0 et Out:1 (dB ; -120 : muet)
'''

TOOLS = r'''
// ======================================================================================================================
// Outils (les memes dans les cinq presets)
// ======================================================================================================================
var NOM = `@NOM@;                    // le nom du processus : un nouveau depot de ce preset arrete celui-ci
var TITRE = "@TITRE@";
var PH = 7700000000;                 // dans une table modele, le mot PH + k est remplace par la k-ieme valeur (tab)
var arret = 0;                       // 1 : arret demande (Presets-Stop.mSL : un fondu), 2 : arret immediat
var T0 = 0;                          // le debut de la generation (ptime)
var Trec = 0;                        // le debut de l'enregistrement du buffer d'entree
var recfin = 0;                      // 1 : l'enregistrement est termine
var avecfic = (strlen(fichier) > 0); // 1 : le buffer d'entree vient d'un fichier
var FIN = 8;                         // le fondu final (s)
var E = 0.4;                         // l'energie (0 ... 1) : elle erre, et choisit les sections
var NS = 0;                          // les sections

// le hasard : le generateur de rand() avance d'un nombre de pas tire de l'horloge, chaque execution est differente
var k0 = floor(1000000 * (ptime() - floor(ptime())));
loop(1 + (k0 % 7919), rand(1));

function alea(a, b) ( a + rand(b - a); );                       // un reel dans [a, b]
function aleal(a, b) ( a * pow(b / a, rand(1)); );              // dans [a, b] (a, b > 0), en echelle logarithmique
function proba(p) ( rand(1) < p; );                             // vrai avec la probabilite p
function signe(p) ( (rand(1) < p) ? -1 : 1; );                  // -1 avec la probabilite p, sinon 1
function borne(x, a, b) ( max(a, min(b, x)); );
function pioche(t) ( t[min(t[-1] - 1, floor(rand(t[-1])))]; );  // un element d'un tableau, au hasard
function tps() ( ptime() - T0; );                               // le temps de la generation (s)

// un indice tire selon les poids du tableau w
function tirage(w) local(s, i, u, k)
(
    s = 0; i = 0; while (i < w[-1]) ( s += w[i]; i += 1; );
    u = rand(s); k = 0; s = w[0];
    while ((k < w[-1] - 1) && (u >= s)) ( k += 1; s += w[k]; );
    k;
);

// la table modele m (un data), ses mots PH + 1, PH + 2... remplaces par les valeurs v1, v2... : tab(m, v1, v2...) ;
// m n'est pas modifiee ; une instance qui n'existe plus (retiree a la main) arrete la generation
function tab(n; v) local(m, c, i, w, r)
(
    r = -1;
    (arret !== 2) ? (
        m = v[0]; c = malloc(m[-1]);
        i = 0; while (i < m[-1]) (
            w = m[i];
            ((w > PH) && (w < PH + n)) ? (w = v[w - PH]);
            c[i] = w; i += 1;
        );
        r = table(c);
        mfree(c);
        (r !== 0) ? (
            print(sprintf(0, "%s : erreur %04d dans une table", TITRE, r));
            ((r === 2757) || (r === 2787)) ? (arret = 2);
        );
    );
    r;
);

// attendre d secondes ; un message "stop" (Presets-Stop.mSL, ou un nouveau depot du preset) arrete la generation
function attend(d) local(t1, m)
(
    t1 = ptime() + d;
    while ((arret === 0) && (ptime() < t1 - 0.005)) (
        (t1 - ptime() >= 1) ? (
            m = event(`wait, t1 - ptime());
            (m > 0) ? (
                (m[2] === `stop) ? (arret = (m[14] === 1) ? 2 : 1);
                event(`recycle, m);
            );
        ) : (
            wait(t1 - ptime());
        );
    );
);

// la fin : attendre d secondes ; seul un nouveau depot du preset (un arret immediat) interrompt
function attfin(d) local(t1, m)
(
    t1 = ptime() + d;
    while ((arret !== 2) && (ptime() < t1 - 0.005)) (
        (t1 - ptime() >= 1) ? (
            m = event(`wait, t1 - ptime());
            (m > 0) ? (
                ((m[2] === `stop) && (m[14] === 1)) ? (arret = 2);
                event(`recycle, m);
            );
        ) : (
            wait(t1 - ptime());
        );
    );
);

// la duree utilisable du buffer d'entree (s) : la part deja enregistree, ou la duree du fichier
function dispo() local(e)
(
    avecfic ? duree : (
        e = ptime() - Trec;
        (e >= duree) ? duree : max(2, e - 0.5);
    );
);

// l'energie erre autour d'un arc (faible au debut et a la fin, forte au milieu)
function energie() local(x, arc)
(
    x = borne(tps() / sortie, 0, 1);
    arc = 0.2 + 0.6 * sin($pi * x);
    E = borne(0.5 * E + 0.5 * (arc + alea(-0.35, 0.35)), 0, 1);
);

// la duree d'une transition : une coupure (20 %), un fondu court (50 %) ou long (30 %)
function transit() local(u)
(
    u = rand(1);
    (u < 0.2) ? alea(0.03, 0.15) : ((u < 0.7) ? alea(0.8, 4) : alea(5, 14));
);
'''

LEVELS = r'''
// les niveaux : une cible (un LFO constant "l...") et une pente (un Math Slew "s..." : de -80 a 0 dB, par pas de
// 0.8 dB) ; ils modulent le volume d'un reader, le gain d'un writer, ou (Math Exp "e...", Math Mul "v...") un son ;
// niv(k, dB, s) : le niveau k va vers dB en s secondes (au plus 10 s par 0.8 dB) ; ils partent de -80 dB
var TNIV = data(Interstys  Effect @INS@:@3@  offset @1@  Effect @INS@:@4@  attack @2@  release @2@);
function niv(k, db, s) local(t, d, a)
(
    t = borne(1 + db / 80, 0, 1);
    d = 100 * abs(t - NVc[k]);
    a = borne(1000 * s / max(0.01, d), 1, 10000);
    NVc[k] = t; NVd[k] = db;
    tab(TNIV, t, a, NVl[k], NVs[k]);
);
var k1 = 0;
loop(KM + 1, NVd[k1] = -80; k1 += 1;);

// le buffer d'entree (l'instance @INSIN@ : la ligne src et le writer rec, qui l'enregistre depuis In:0)
var TIN = data(
    Interstys
    Algorithm @ALGIN@
        Line src  length @1@  chan @2@
        Writer rec  line src  source In:0  status Paused
        Display Line src
    End
    Instance @INSIN@ @ALGIN@
);
var TFIC = data(Interstys  Line @INSIN@:src  file @1@);
var TREC = data(Interstys  Writer @INSIN@:rec  status @1@);
var TWS = data(Interstys  Writer @INS@:@1@  status @2@);
var TRST = data(Interstys  Reader @INS@:@1@  status @2@);

// l'enregistrement s'arrete quand le buffer d'entree est plein (sauf "continu")
function finrec()
(
    (!avecfic && !continu && !recfin && (ptime() - Trec >= duree)) ? (
        tab(TREC, `Paused); recfin = 1;
        print(sprintf(0, "%s : le buffer d'entree est complet (%d s)", TITRE, duree));
    );
);
'''

MAIN = r'''
// ======================================================================================================================
// Demarrage, generation, fin (les memes dans les cinq presets)
// ======================================================================================================================
// un depot precedent de ce preset : son chef d'orchestre s'arrete (ses modules sont refaits ci-dessous)
(thread(`count, NOM) > 0) ? (
    loop(thread(`count, NOM), event(`notify, 0, 0, 0, 0, NOM, `stop, 0, 10, 0, 0, 0, 1, 0));
    wait(1.5);
);
thread(`name, NOM);
// les instances precedentes (la ligne d'abord : lue d'un fichier, elle n'appartient plus a son instance)
table(data( Free Instance @INS@ ));
table(data( Free Line @INSIN@:src  Free Instance @INSIN@ ));
var r = tab(TIN, (avecfic ? 1 : borne(duree, 2, 1300)), (avecfic ? 1 : borne(canaux, 1, 2)));
((r === 0) && avecfic) ? (r = tab(TFIC, fichier));
(r === 0) ? (r = creer());
(r !== 0) ? (
    print(sprintf(0, "%s : les modules n'ont pas pu etre crees (erreur %04d), rien n'est genere.", TITRE, r));
    arret = 2;
);
(arret === 0) ? (
    Trec = ptime();
    avecfic ? (
        print(sprintf(0, "%s : le buffer d'entree vient du fichier %s (%d s utilisees)", TITRE, fichier, duree));
    ) : (
        tab(TREC, `Writing);
        print(sprintf(0, "%s : enregistrement du buffer d'entree depuis In:0 (%d s, %d canal(aux))", TITRE, duree, canaux));
        attend(min(duree, 6));
    );
);
(arret === 0) ? (
    T0 = ptime();
    tab(TWS, `wo, `Writing);
    niv(KM, MAST, 3);
    print(sprintf(0, "%s : generation de %d s dans le buffer de sortie (@INS@:res)", TITRE, sortie));
);
while ((arret === 0) && (tps() < sortie - FIN)) ( section(); );
(arret !== 2) ? (
    niv(KM, -80, (arret === 1) ? 3 : FIN);
    attfin((arret === 1) ? 3.5 : (FIN + 0.5));
);
(arret !== 2) ? (
    tab(TWS, `wo, `Paused);
    arreter();
    (!avecfic && !recfin) ? tab(TREC, `Paused);
    print(sprintf(0, "%s : fin, %d s dans le buffer de sortie (@INS@:res)", TITRE, ((T0 > 0) ? floor(tps()) : 0)));
);
'''

# un niveau : la cible l<k> (LFO constant) et sa pente s<k> (Math Slew, de -1 a 0 : -80 ... 0 dB)
def level(k):
    return (f"        Effect l{k}  type LFO  chan 1  freq 0.01  amp 0  offset 0\n"
            f"        Effect s{k}  type Math  chan 1  source Effect l{k}  gain 40  mode Slew  attack 1000  release 1000  amp 0.01  offset -1\n")

# un niveau qui agit sur un son (VCA) : e<k> (Math Exp : 10^(80 u / 20)), v<k> (Math Mul : le son <src> fois e<k>)
def vca(k, src, extra=""):
    return (f"        Effect e{k}  type Math  chan 1  source Effect s{k}  gain 38.0618  mode Exp\n"
            f"        Effect v{k}  type Math  chan 1  source {src}  src2 Effect e{k}  mode Mul{extra}\n")

# la sortie : le buffer res (l'argument @1@ : sa duree), son writer wo, l'ecoute (m0, m1 : l'argument @k@, en dB)
def output(src, kecoute):
    return (f"        Writer wo  line res  source {src}  status Paused\n"
            f"        Effect m0  type Mixer  chan 1  src1 {src}  gain1 @{kecoute}@  out Out:0\n"
            f"        Effect m1  type Mixer  chan 1  src1 {src}  gain1 @{kecoute}@  out Out:1\n"
            f"        Display Line res\n")

def expand(text, names):
    import re
    for k, v in names.items():
        text = text.replace('@' + k + '@', v)
    return re.sub(r'@(\d+)@', lambda m: str(7700000000 + int(m.group(1))), text)
