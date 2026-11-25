---
title: "CMGS — Partie III"
lang: fr-FR
---

# Premiers pas

**mSL** (*micro Script Language*) est le langage de script de CMGS. Il est intégré à chacun des plug-ins : il sert à
décrire des configurations (le Profile du Game Master, les configurations d'Espaces, les patchs d'Interstys), à
écrire des algorithmes de jeu, à automatiser des réglages, et à mettre au point les plug-ins eux-mêmes. Ce chapitre
en présente les éléments essentiels, à travers de petits exemples ; le chapitre suivant décrit le langage plus
complètement. Les fonctions propres à chaque plug-in sont décrites dans son manuel.

mSL est écrit en JSFX, et il en reprend largement la syntaxe : le lecteur qui connaît JSFX (ou le langage C) s'y
retrouvera vite.

## Écrire et lancer un script

Les plug-ins ne contiennent pas d'éditeur de texte : on écrit un script avec n'importe quel éditeur (VS Code,
TextEdit, Vim…) et on l'enregistre dans un fichier d'extension **`.mSL`**. Pour l'exécuter, il suffit de **faire
glisser le fichier dans la fenêtre d'un plug-in** de CMGS. ScriptMaster, conçu pour cela, est le plus commode pour
essayer des scripts ; dans le Game Master, ne le déposez pas sur la case *Profile* du module *Scripts Settings*, qui
en ferait le Profile du projet.

Le plug-in **compile** d'abord le texte : il vérifie sa syntaxe et le traduit en un code prêt à être exécuté. S'il
trouve une erreur, il l'indique dans le journal (module *System Log*) par un numéro d'erreur, un numéro de ligne et une
position dans la ligne. Sinon, il crée un **processus** qui **exécute** ce code. Une erreur peut encore survenir à
l'exécution ; elle arrête alors le processus, et elle est elle aussi signalée dans le journal.

## Un premier programme

Écrivons dans un fichier `test1.mSL` :

```
print("Calcul de la somme des dix premiers entiers.");
var s = (10 * (10 + 1)) / 2;
print(sprintf(0, "s vaut %d", s));
```

et déposons-le dans la fenêtre d'un plug-in. Le journal affiche :

```
Calcul de la somme des dix premiers entiers.
s vaut 55
```

La première ligne appelle la **fonction** `print`, qui écrit une **chaîne de caractères** (un texte placé entre
guillemets droits `"`) dans le journal ; `GM_Log` est un autre nom de la même fonction. La deuxième ligne **déclare**
une **variable** `s` (mot-clé `var`) et lui **affecte** (signe `=`) la valeur d'une **expression**. La troisième
ligne fabrique un texte avec la fonction `sprintf` : le format `"s vaut %d"` indique où et comment insérer la valeur
de `s` (`%d` : sous forme d'un entier) ; le premier paramètre, `0`, demande à `sprintf` d'utiliser une chaîne
temporaire, qu'elle rend comme résultat.

Chaque instruction se termine par un point-virgule. Les espaces et les passages à la ligne sont libres, sauf entre
deux mots. Les commentaires s'écrivent comme en C : de `//` à la fin de la ligne, ou entre `/*` et `*/`.

## Variables et expressions

mSL ne connaît qu'un seul type de données : le **nombre flottant** sur 64 bits, qui représente aussi bien les entiers
que les décimaux. Les chaînes de caractères, les tableaux et les fonctions sont eux-mêmes désignés par des nombres
(leur numéro ou leur adresse).

Toutes les variables doivent être **déclarées**, par `var` (ou `loc`, voir le chapitre suivant). Une déclaration peut
regrouper plusieurs variables et leur donner une valeur initiale : `var a, b = 3, c;`. Cette obligation évite qu'une
faute de frappe crée silencieusement une nouvelle variable.

Les expressions utilisent les opérateurs habituels : `+`, `-`, `*`, `/`, `%` (reste), `^` (puissance), les
comparaisons `<`, `<=`, `==`, `!=`, `>=`, `>`, les opérateurs logiques `&&`, `||`, `!`, et les parenthèses. Les
priorités sont celles des mathématiques (la multiplication avant l'addition) ; dans le doute, on ajoute des
parenthèses, qui ne coûtent rien. Ainsi le trinôme a·x² + b·x + c s'écrit `a*x^2 + b*x + c`.

## Boucles et conditions

La boucle **`while`** répète des instructions tant qu'une condition est vraie (différente de zéro). Pour calculer
autrement la somme des dix premiers entiers :

```
var s = 0, i = 0;
while (i < 10) (
    i = i + 1;
    s = s + i;
);
print(sprintf(0, "s vaut %d", s));
```

Les deux couples de parenthèses (la condition, puis le corps de la boucle) et le point-virgule final font partie de la
syntaxe. La boucle **`loop`** répète des instructions un nombre de fois donné : `loop(10, i += 1; s += i;);`.

L'**instruction conditionnelle** s'écrit avec `?` et, éventuellement, `:` :

```
(x < 0) ? (signe = -1;) : (signe = 1;);
(a > b) ? (max = a;);
```

## Tableaux

Un **tableau** (ou **bloc**) est une suite de valeurs rangées en mémoire, numérotées à partir de 0. On en crée un :

- par `data(…)`, qui contient des valeurs fixées dans le texte du programme : `var liste = data(7 11 43 0 2 1 1 637 -7 13);` ;
- par `array(e1, e2, …)`, qui calcule ses valeurs à l'exécution ;
- par `malloc(n)`, qui crée un tableau de `n` éléments.

On consulte et l'on modifie un élément par **indexation** : `liste[0]` vaut 7, `liste[3] = 5;` change le quatrième
élément. La fonction `size(t)` rend le nombre d'éléments d'un tableau ; `mfree(t)` libère un tableau créé par
`malloc` ou `array` lorsqu'on n'en a plus besoin. Pour trouver le plus grand élément de `liste` :

```
var liste = data(7 11 43 0 2 1 1 637 -7 13);
var s = liste[0], i = 1;
while (i < size(liste)) (
    s = max(s, liste[i]);
    i += 1;
);
print(sprintf(0, "s vaut %d", s));     // s vaut 637
```

Par sécurité, l'écriture indexée (`t[i] = v`) n'est permise qu'à l'intérieur d'un tableau, pour un indice compris entre
0 et sa taille moins 1 : écrire au-delà provoque une erreur (voir le chapitre suivant).

## Fonctions

On regroupe un algorithme dans une **fonction**, que l'on peut ensuite appeler aussi souvent que l'on veut :

```
function somme(T)
local (i, s)
(
    i = s = 0;
    while (i < size(T)) ( s += T[i]; i += 1; );
    s;
);
print(sprintf(0, "somme : %d", somme(data(1 2 3 4))));   // somme : 10
```

Le mot-clé `function` est suivi du nom de la fonction et de ses **paramètres** entre parenthèses ; `local` déclare ses
**variables locales**, qui n'existent que pendant l'appel ; le corps de la fonction est entre parenthèses. Le
**résultat** de la fonction est la valeur de la dernière expression évaluée (ici `s`) ; la fonction `return(v)`
permet aussi d'en sortir à tout moment. Les fonctions peuvent être récursives :

```
function fib(n) ( (n < 2) ? n : fib(n-1) + fib(n-2); );
print(sprintf(0, "fib(25) = %d", fib(25)));   // fib(25) = 75025
```

Une fonction est aussi une valeur, que l'on peut ranger dans une variable ou passer à une autre fonction :

```
function reduce(A, f, N)
local (i, r)
( r = N; i = 0; while (i < size(A)) ( r = f(r, A[i]); i += 1; ); r; );
var T = data(3 -6 30 8);
print(sprintf(0, "max = %d, somme = %d", reduce(T, max, -(10^300)), reduce(T, (+), 0)));
```

`max` est une fonction prédéfinie, et `(+)`, un opérateur placé entre parenthèses, se comporte comme une fonction.
(On écrit `-(10^300)` et non `-10^300` : le moins unaire est plus prioritaire que la puissance, et `-10^300` vaudrait
`(-10)^300`, un nombre positif.)

## Chaînes de caractères

Une chaîne écrite dans le programme (`"bonjour"`) est une **constante**. Pour fabriquer un texte, on utilise une chaîne
**modifiable**, obtenue par `stralloc()` (à libérer par `strfree(s)` quand on n'en a plus besoin) ou, pour un usage
immédiat, par `strtmp()`, ou encore le `0` de `sprintf(0, …)`. La fonction `sprintf(dest, format, valeurs…)` place
dans `dest` le texte du format, où chaque `%` introduit l'édition d'une valeur : `%d` un entier, `%f` ou `%.2f` un
décimal, `%x` un nombre hexadécimal, `%s` une chaîne.

```
var str = stralloc();
sprintf(str, "%s : %d clips, %.2f s", "Groupe 3", 12, 37.5);
print(str);                              // Groupe 3 : 12 clips, 37.50 s
strfree(str);
```

## Les erreurs

Une erreur de **syntaxe** est signalée dès la compilation : le journal donne son numéro, la ligne et la position où le
compilateur s'est arrêté (souvent un peu après la faute réelle : une parenthèse ou un point-virgule oublié). Une erreur
d'**exécution** (écriture hors d'un tableau, mémoire épuisée, erreur signalée par le script lui-même avec `error(code)`…) arrête le
processus qui l'a commise. Par défaut, une erreur arrête aussi les autres processus du plug-in ; après
`` call(`errLock, 0); ``, seul le processus fautif s'arrête. La Partie IV donne la liste de toutes les erreurs.

# Le langage en détail

Ce chapitre décrit mSL plus complètement. mSL est très proche de JSFX (EEL2) ; les différences sont signalées.

## Identificateurs et symboles

Un **identificateur** (nom de variable ou de fonction) commence par une lettre ou le caractère `_`, suivi de lettres,
de chiffres et de `_`. Les majuscules et les minuscules sont distinctes : `abc`, `Abc` et `ABC` sont trois noms
différents. Les noms de plus de 8 caractères sont acceptés, mais ils sont « compactés » en interne sur 8 caractères :
deux noms longs différents peuvent, très rarement, se confondre. Certains plug-ins demandent explicitement des noms de
8 caractères au plus (par exemple les noms d'algorithmes et d'instances d'Interstys).

Un **symbole** est un identificateur précédé d'une apostrophe inversée : `` `hello ``. Sa valeur est un nombre qui
code ce nom ; les symboles servent de mots-clés dans les appels de fonctions (`` thread(`new, f) ``) et dans les
tables de données.

Les **constantes symboliques** commencent par `$` : `$pi` et `$e` (les constantes mathématiques), `$undef` (valeur
« indéfinie »), `$endmark`, `$usep` ; chaque plug-in peut en définir d'autres.

## Valeurs

| Notation | Exemple | Valeur |
|---|---|---|
| entier, décimal | `42`, `-3.25`, `1.5e-3` | le nombre |
| hexadécimal | `0x1F`, `0X3ffA27342C5` | le nombre en base 16 |
| binaire | `0b1011` | le nombre en base 2 |
| caractères | `'A'`, `'Game'` | le code de 1 à 4 caractères (comme en JSFX) |
| symbole | `` `hello `` | le code du symbole |
| constante | `$pi` | la valeur de la constante |
| chaîne | `"texte"` | le numéro d'une chaîne constante |

## Déclarations

| Mot-clé | Portée |
|---|---|
| `var` | variable du script, partagée par tous les processus créés par ce script ; les fonctions définies sont aussi de ce type |
| `loc` | variable « semi-locale » : chaque processus créé par le script en a sa propre copie |
| `ptr` | variable « pointeur » : elle contient une adresse, et c'est le mot situé à cette adresse qui est lu ou écrit |
| `ext` | variable « externe » : elle subsiste après la fin du script, et tout script exécuté ensuite la retrouve en la déclarant à son tour (voir ci-dessous) |
| `local (…)` | dans une fonction, ses variables locales (dans la pile, non initialisées) |

Les déclarations valent pour tout le texte du script : une variable peut être utilisée avant d'être déclarée, pourvu
qu'elle le soit quelque part.

Les variables `ext` sont *rémanentes* : une fois définie, une telle variable subsiste en mémoire après la fin du
script qui l'a créée, pendant toute la session de REAPER, et tout script exécuté ensuite dans le même plug-in la
retrouve en la déclarant à son tour par `ext`. Un script préparatoire peut ainsi définir des fonctions que l'on
associe, par exemple, aux touches d'un pad : elles sont aussitôt exécutables, sans qu'il faille charger ni compiler
un fichier `.mSL`. Les tests `Ex-0003` et `Ex-0004` en donnent l'exemple :

```
// premier script : définit la fonction fibo et la rend disponible sous le nom fib
function fibo(n) ( (n <= 1) ? 1 : fibo(n-1) + fibo(n-2); );
ext fib = fibo;

// second script, exécuté plus tard : retrouve fib et l'appelle
ext fib;
print(sprintf(0, "fib(8) vaut %d", fib(8)));   // fib(8) vaut 34
```

## Opérateurs et priorités

| Niveau | Opérateurs | Associativité | Nature |
|---|---|---|---|
| 1 | `( )` `[ ]` | — | parenthèses, appels de fonctions, indexation |
| 2 | `-` `+` `!` `~` | de droite à gauche | opérateurs unaires |
| 3 | `^` | de gauche à droite | puissance |
| 4 | `*` `/` `%` | de gauche à droite | multiplicatifs |
| 5 | `+` `-` | de gauche à droite | additifs |
| 6 | `<<` `>>` | de gauche à droite | décalages |
| 7 | `<` `<=` `>=` `>` | non associatifs | comparaisons |
| 8 | `===` `==` `!=` `!==` | non associatifs | égalités |
| 9 | `&` `~` | de gauche à droite | « et », « ou exclusif » bit à bit |
| 10 | \| | de gauche à droite | « ou » bit à bit |
| 11 | `&&` | de gauche à droite | « et » logique |
| 12 | \|\| | de gauche à droite | « ou » logique |
| 13 | `? :` | de droite à gauche | condition |
| 14 | `=` `+=` `-=` `*=` `/=` `%=` `&=` \|= | de droite à gauche | affectations |
| 15 | `;` | de gauche à droite | suite d'instructions |
| 16 | `,` | de gauche à droite | suite de valeurs |

Deux différences avec JSFX :

- `&&` et `||` ont la sémantique du langage C : `2 && 3` vaut 3 (et non 1). Dans un test, le sens est le même ;
- les affectations sont **moins prioritaires** que la condition `? :` : il faut parfois des parenthèses, comme dans
  `(x > 0) ? (y = 1) : (y = 2);`.

## Instructions de contrôle

- `while (condition) (corps);` répète le corps tant que la condition est vraie. C'est la seule forme de `while`.
- `loop(n, corps);` répète le corps `n` fois.
- `(condition) ? (si_vrai) : (si_faux);` exécute l'une des deux branches ; la branche `: (…)` est facultative.
- `return(v)` sort de la fonction courante avec le résultat `v` ; `exit(v)` termine le processus.

## Fonctions

```
function nom(p1, p2, …)
local (v1, v2, …)
( instructions );
```

Contrairement à JSFX, les virgules entre paramètres et entre variables locales sont obligatoires, et :

- les fonctions peuvent être **récursives**, y compris de façon croisée, et être appelées avant leur définition ;
- les paramètres et les variables locales sont alloués dans la pile à chaque appel : ils ne gardent pas leur valeur
  d'un appel à l'autre, et les variables locales ne sont **pas initialisées** ;
- le nombre de paramètres d'une fonction est fixe, et un nom ne désigne qu'une fonction. Une fonction **variadique**,
  qui accepte un nombre quelconque d'arguments, se déclare avec un point-virgule : dans `function f(n; args)`, `n`
  reçoit le nombre d'arguments et `args` un tableau qui les contient (valable seulement pendant l'appel) ;
- les fonctions sont des **valeurs** comme les autres : on peut les ranger dans une variable ou un tableau, les passer
  en paramètre, les rendre comme résultat. Les fonctions prédéfinies aussi (`var f = sin;`), et les opérateurs placés
  entre parenthèses (`var plus = (+); plus(2, 3);` vaut 5) ;
- l'interprète optimise la **récursivité terminale** : un appel placé en dernière position d'une fonction ne consomme
  pas de pile, si bien qu'une fonction peut s'appeler des millions de fois.

## Tableaux et mémoire

Un **bloc** est une zone de mémoire précédée d'un en-tête : si `t` est un bloc de `N` éléments, `t[-2]` est son
**type** (une valeur de 4 caractères, `'data'` par défaut), `t[-1]` sa **taille** `N`, et `t[0]` à `t[N-1]` ses
éléments. Les blocs se créent par :

| Opération | Effet |
|---|---|
| `data(…)`, ou `` `(…) `` | bloc créé une fois pour toutes à la compilation, avec des valeurs constantes |
| `array(e1, …, eN)` | nouveau bloc à chaque exécution, avec les valeurs des expressions |
| `malloc(n)` | nouveau bloc de `n` éléments ; rend 0 si la mémoire manque |
| `mfree(t)` | libère un bloc créé par `array` ou `malloc` |
| `size(t)`, `isblock(t)` | taille d'un bloc (−1 si ce n'en est pas un), test |

Un bloc peut servir de **table associative** : les éléments de rang pair sont des clés, les suivants leurs valeurs, et
`` t[`clé] `` rend la valeur associée à la clé (les clés doivent être des nombres plus grands que la taille du bloc,
ce qui est le cas des symboles).

**Lecture et écriture.** On peut lire n'importe quel mot de la mémoire du plug-in (`a[i]`), et de la mémoire partagée
entre plug-ins (`gmem[i]`). En revanche, l'écriture indexée `t[i] = v` (et `+=`, `*=`…) n'est permise que :

- dans un bloc, pour un indice compris entre 0 et sa taille moins 1 ;
- dans le tableau des arguments d'une fonction variadique.

Toute autre écriture arrête le processus avec une erreur (1629 ou 1630). Pour écrire à une adresse quelconque, en
connaissance de cause, on utilise `poke(adresse, valeur)` ou `poke(adresse, décalage, valeur)`. La fonction
`memcpy(destination, source, n)` copie `n` mots en respectant la taille des blocs (une adresse négative désigne la
mémoire partagée) et rend le nombre de mots copiés.

La mémoire dynamique est gérée par un **ramasse-miettes** (*garbage collector*) conservatif, qui récupère les blocs
devenus inaccessibles, en particulier ceux qui sont partagés entre plusieurs processus.

## La syntaxe de `data`

La directive `data` est suivie d'une liste de **constantes** entre parenthèses, séparées par des espaces, des
tabulations, des passages à la ligne ou des virgules ; on peut y placer des commentaires. Les éléments sont :

- des nombres, sous toutes les notations vues plus haut, et des chaînes entre guillemets ;
- des **identificateurs**, qui y valent leur symbole : dans `data(Table PlModes PMd 3)`, `Table` et `PlModes` sont des
  symboles. Attention, la casse compte : `FdIn` et `FDin` sont deux mots différents ;
- des notations propres à `data` : `-v` (l'opposé d'une valeur), `a+b` (la somme), `a|b` (le « ou » bit à bit),
  `a&b` (le « et »), et `a/b/c`, qui désigne l'entier dont les bits de numéros `a`, `b` et `c` sont à 1 (`6/2/0` vaut
  67).

C'est avec `data` que s'écrivent les **tables** de configuration des plug-ins, passées à la fonction `table` :

```
table(data(
    Table PlModes
    PMd 32
        Kmd KmdLoop
        Speed 0.4 0.7 0.8
        Gsize 0.2 0.45
    End
));
```

Le vocabulaire des tables (ici `Table`, `PMd`, `Kmd`, `Speed`…) est propre à chaque plug-in et décrit dans son manuel.

## Chaînes de caractères

Les chaînes sont prises dans une réserve gérée par le plug-in. Une chaîne constante (`"texte"`) est allouée par le
compilateur ; `stralloc()` fournit une chaîne modifiable, à rendre par `strfree(s)` ; `strtmp()` fournit une chaîne
temporaire, qui n'a pas besoin d'être libérée mais ne reste valable que pour les quelques instructions qui suivent. Il
n'y a pas de récupération automatique des chaînes : une chaîne obtenue par `stralloc` et jamais libérée reste occupée.

| Fonction | Effet |
|---|---|
| `sprintf(d, format, v1, …)` | édite les valeurs dans la chaîne `d` (ou dans une chaîne temporaire si `d` vaut 0), et rend cette chaîne |
| `strlen(s)` | longueur |
| `strcpy(d, s)`, `strcat(d, s)` | copie, concaténation |
| `strcmp(a, b)`, `stricmp(a, b)` | comparaison, avec ou sans distinction des majuscules |
| `strgetch(s, i)`, `strsetch(s, i, c)` | lit, écrit le caractère de rang `i` |
| `symbol(s)` | le symbole correspondant au texte de la chaîne |
| `edn(s, v)` | écrit dans `s` la représentation la plus lisible de la valeur `v` |
| `isstring(x)` | teste si `x` est une chaîne |

## Les fonctions prédéfinies

| Domaine | Fonctions |
|---|---|
| mathématiques | `sin` `cos` `tan` `asin` `acos` `atan` `atan2` `pow` `sqr` `sqrt` `invsqrt` `exp` `log` `log10` `abs` `sign` `floor` `ceil` `int` `min` `max` |
| sommes | `sum(x1, …)`, `prod(x1, …)` : somme, produit de leurs arguments |
| hasard | `rand(x)` : décimal dans [0, x[ ; `irand(n)` : entier dans [0, n-1] |
| tests | `isint` `isfun` `isstring` `isblock` |
| temps et audio | `time()` (secondes), `ptime()` (temps précis, `time_precise` de JSFX), `srate()`, `num_ch()`, `tempo()` |
| mémoire | `malloc` `mfree` `array` `size` `memcpy` `poke` `memtop()` |
| chaînes | `stralloc` `strfree` `strtmp` `sprintf` `strlen` `strcpy` `strcat` `strcmp` `stricmp` `strgetch` `strsetch` `symbol` `edn` |
| contrôle | `return(v)` `exit(v)` `error(code)` (signale une erreur et arrête le processus) |
| compilation | `compile(s)` : compile le texte `s` en une fonction sans paramètre, qui s'exécute plus tard : après `var c = compile("var a=3; 2*a+1;");`, `c()` vaut 7 |
| processus | `thread` `wait` `yield` `event` (voir le chapitre suivant) |
| plug-ins | `print` (ou `GM_Log`), `get`, `set`, `call`, `table`, `action`, `GM_Addr`… : leur effet dépend du plug-in |

mSL n'a pas de fonctions graphiques.

**Paramètres.** Les paramètres des plug-ins (ceux que l'on règle avec des sliders) portent des numéros de 0 à 1023,
avec une plage par application : 0 à 255 pour le Game Master, 256 à 511 pour Interstys, 512 à 639 pour Espaces,
640 à 703 pour ScriptMaster, 704 à 767 pour MIDI_In et MIDIduino. `` get(`pval, n) `` lit la valeur du paramètre `n`,
quelle que soit l'application ; `` set(`pval, n, v) `` le modifie, s'il appartient au plug-in où s'exécute le script
(sinon, une erreur), et rend la valeur précédente.

## Importer un fichier

Un script peut inclure le texte d'un autre fichier, d'extension `.mSL` ou `.txt` : `import "fichier.mSL";`. Les
importations peuvent se mêler aux autres instructions.

# Exécution des scripts

## Processus légers

Chaque script s'exécute dans un **processus léger** (*thread*). Un plug-in peut faire tourner des centaines de
processus en même temps ; ils partagent la mémoire du plug-in, mais chacun a sa pile et ses variables `loc`. Un seul
processus travaille à un instant donné : l'**ordonnanceur** (module *Scheduler*) passe de l'un à l'autre, soit à leur
demande, soit d'office au bout d'un certain temps (la commutation est **préemptive** : aucun processus ne peut bloquer
le plug-in). Après une commutation, un processus est assuré de pouvoir exécuter un nombre minimal d'instructions
(plus de 4000) sans être interrompu, ce qui permet de modifier sans risque, pendant ce temps, des données partagées.

Les scripts s'exécutent dans la partie graphique des plug-ins (la section `@gfx` de JSFX), par petites tranches de
temps, et non dans la partie audio : ils ne perturbent donc pas le son. Ils continuent de s'exécuter lorsque la fenêtre
du plug-in est fermée. (Dans le Game Master, si la partie graphique s'arrête, la partie audio prend le relais.)

## Créer et gérer des processus

| Opération | Effet |
|---|---|
| `` thread(`new, f, p1, …) `` | crée un processus qui exécutera la fonction `f` avec les paramètres `p1…` ; rend son identifiant |
| `` thread(`run, t) `` | lance le processus `t` |
| `` thread(`idt) `` | identifiant du processus courant |
| `` thread(`name, `nom) `` | donne un nom au processus courant (pour lui adresser des messages) |
| `` thread(`status, t) ``, `` thread(`find, …) ``, `` thread(`count) `` | état d'un processus, recherche, nombre de processus |
| `wait(s)` | met le processus en attente pendant `s` secondes |
| `yield()` | cède la main aux autres processus |
| `exit(v)` | termine le processus ; `v` est sa valeur de sortie |

Les processus créés par un même script partagent ses variables `var`, mais chacun a ses propres variables `loc`.

```
var total = 0;
function travail(n) ( wait(0.5); total += n; );
thread(`run, thread(`new, travail, 10));
thread(`run, thread(`new, travail, 20));
wait(1);
print(sprintf(0, "total = %d", total));   // total = 30
```

## Les messages

Les processus d'un même plug-in s'échangent des **messages** (ou *événements*) par la fonction `event`. Un message
porte un nom (un symbole), un délai, une durée de vie et des paramètres ; il est adressé à un processus par son
identifiant ou par son nom.

| Opération | Effet |
|---|---|
| `` event(`notify, 0, 0, 0, dest, nomDest, `evt, délai, durée, 0, 0, seq, p1, p2) `` | envoie le message `evt` au processus `dest` (ou, si `dest` vaut 0, au processus nommé `nomDest`), après `délai` secondes ; il expire au bout de `durée` secondes |
| `` event(`wait, s) `` | attend un message, au plus `s` secondes ; rend le message, ou −1 |
| `` event(`check) `` | indique si un message attend |
| `` event(`count) `` | nombre de messages en attente |
| `` event(`recycle, m) `` | rend le message `m` après usage |
| `` event(`clearall) `` | supprime les messages en attente |

Dans un message reçu `m`, `m[2]` est le nom de l'événement, `m[13]` le numéro `seq` et `m[14]` le premier paramètre.

```
var moi = thread(`idt);
function envoi() ( wait(0.5); event(`notify, 0, 0, 0, moi, 0, `hello, 0, 10, 0, 0, 1, 42, 0); );
thread(`run, thread(`new, envoi));
var m = event(`wait, 5);
(m > 0) ? ( print(sprintf(0, "reçu %d", m[14])); event(`recycle, m); );   // reçu 42
```

Les plug-ins entre eux communiquent par la **mémoire partagée** (`gmem`) et par les **paramètres** (voir plus haut) ;
le Game Master pilote ainsi ses lecteurs, et un script peut lire les paramètres de tous les plug-ins du projet.

## Les séries de tests

Le dossier `CMGS-scripts/Tests` contient des scripts de test, `Ex-NNNN.mSL`, qui vérifient le langage et les plug-ins.
Leurs numéros indiquent leur domaine : `Ex-0NNN` le langage (ils doivent réussir dans tous les plug-ins), `Ex-1NNN`
Interstys, `Ex-2NNN` le Game Master, `Ex-3NNN` Espaces.

Chaque script annonce ce qu'il doit écrire dans le journal, par des commentaires :

```
// Expected "Ex-0022. lu 1, inchange 1"
// Expected error 1629
// Allowed error 0621
```

`Expected "…"` attend un message (les formats de `sprintf`, comme `%d`, y sont permis), `Expected error NNNN` une
erreur, `Allowed error NNNN` une erreur qui peut apparaître ou non. Pour passer une série :

1. déposez les scripts dans la fenêtre du plug-in ;
2. quand ils ont fini, enregistrez le journal avec la touche `p` (le script auxiliaire doit être lancé) : le fichier
   `syslog-<plug-in>-<date>.txt` est écrit dans le dossier du projet ;
3. vérifiez-le avec : `python3 -I CMGS-scripts/Tests/check_scripts.py [fichier ou dossier] [-a]`

`check_scripts.py` lit par défaut le journal le plus récent des projets de `~/Music/REAPER-Projects`, et indique pour
chaque script s'il est correct, en échec, ou s'il a produit une erreur inattendue. Le journal ne garde que ses derniers
messages (environ 800 lignes) : une série trop bavarde doit être passée en plusieurs fois.
