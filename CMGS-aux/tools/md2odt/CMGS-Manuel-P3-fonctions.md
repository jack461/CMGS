---
title: "CMGS — fragment fonctions"
lang: fr-FR
---

# Le langage en détail

## Fonctions

### Fonctions anonymes

Une **fonction anonyme** (ou lambda-expression) s'écrit comme une définition de fonction, sans nom :
`function (paramètres) (corps)`. C'est une expression, dont la valeur est la fonction : on peut la ranger dans une
variable, la passer en argument, ou l'appeler aussitôt, en plaçant ses arguments juste après elle.

```
var carre = function (x) (x * x);
carre(5);                                   // 25
function deux_fois(f, x) ( f(f(x)); );
deux_fois(function (x) (x + 10), 1);        // 21
function (x) (x + 1) (3);                   // 4 : appelée aussitôt
(function (x, y) (x * y))(5, 6);            // 30
```

Comme pour une fonction nommée, des groupes `local(…)` peuvent suivre les paramètres ; le corps est toujours entre
parenthèses. Une fonction anonyme n'a pas de nom caché : elle n'existe que tant qu'une variable, un tableau ou un
code en cours la désigne, puis le ramasse-miettes la récupère. Elle n'a pas de fermeture (*closure*) : son corps voit
les variables globales (`var`, `ext`), ses paramètres et ses variables locales, mais pas les paramètres ni les
variables locales de la fonction qui la contient. Un même texte peut contenir au plus 62 fonctions anonymes (erreur
2258).

### La fonction elle-même : _

Dans le corps d'une fonction, nommée ou non, l'identificateur `_` désigne la fonction elle-même : c'est le moyen
d'écrire une fonction anonyme récursive. Il ne dépend d'aucune variable : si la fonction est rangée ailleurs, ou si
son nom reçoit une autre valeur, `_` désigne toujours la même fonction. Dans des fonctions imbriquées, `_` désigne
la plus proche. En dehors d'une fonction, `_` est un identificateur ordinaire.

```
var fib = function (n) ( (n < 2) ? n : _(n - 1) + _(n - 2); );
fib(10);                                    // 55
function fact(n) ( (n <= 1) ? 1 : n * _(n - 1); );
var f2 = fact;
fact = 0;
f2(5);                                      // 120 : _ est toujours la fonction de f2
```

### Appeler ou indexer une expression

Toute expression dont la valeur est une fonction peut être appelée, en plaçant ses arguments entre parenthèses juste
après elle ; de même, toute expression dont la valeur est un bloc peut être indexée.

```
function donne() (sin);
donne()(0);                                 // 0 : sin(0)
var w;
(w = donne())(0);                           // 0, et w vaut la fonction sin
var t = array(sin, cos);
t[1](0);                                    // 1 : cos(0)
function table() (t);
table()[1](0);                              // 1 : une expression indexée, puis appelée
var m = array(array(1, 2), array(3, 4));
m[1][0];                                    // 3
```

La tête d'une définition (`function f(x)` suivie de son corps) n'est pas un appel ; deux expressions entre
parenthèses placées l'une après l'autre, en revanche, en forment un : `(a)(b)` appelle la valeur de `a`.
