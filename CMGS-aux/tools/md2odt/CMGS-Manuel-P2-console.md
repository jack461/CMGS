---
title: "CMGS — fragment console"
lang: fr-FR
---

# Les modules communs

## mSL Console

Le module **mSL Console** exécute aussitôt une ligne de mSL tapée au clavier, sans passer par un fichier : pour
essayer une expression, consulter ou modifier les variables d'un script en cours, appeler ses fonctions, envoyer des
réglages (*settings*) au plug-in, ou demander l'explication d'une erreur. Il existe dans les cinq plug-ins (Game
Master, FilePlayer, ScriptMaster, Diffusion-3, Interstys) ; on l'ajoute à un panneau par le menu des modules
(Shift + clic droit).

En bas du module se trouve la ligne de saisie ; au-dessus, les dernières lignes de la console, la plus récente en bas.

### Taper une ligne

Un clic dans la ligne de saisie lui donne le clavier : toutes les touches vont alors à la console, et plus aux autres
modules ni aux commandes du plug-in. Échap, ou un clic ailleurs, rend le clavier au plug-in.

| Touche | Effet |
|--------------|----------------------------------------|
| Entrée | exécute la ligne |
| `▲`, `▼` | rappelle la ligne précédente ou la suivante (les 32 dernières lignes exécutées) |
| `◀`, `▶`, Début, Fin | déplacent le curseur d'un caractère vers la gauche ou vers la droite, au début ou à la fin de la ligne |
| Retour arrière, Suppr | effacent le caractère avant ou après le curseur |
| Échap | rend le clavier au plug-in |

La souris sur le module, quand la ligne de saisie n'a pas le clavier : `+` (ou `=`) et `-` augmentent ou réduisent
la hauteur du module ; la molette fait défiler les lignes affichées vers les plus anciennes ou vers les plus récentes.

Chaque ligne est compilée et exécutée comme un petit script, dans son propre processus. Elle peut contenir plusieurs
instructions séparées par des points-virgules. Une erreur dans une ligne n'arrête que cette ligne ; les scripts en
cours continuent (§ 13.3).

### Les modes

Le premier caractère d'une ligne peut choisir le mode de la console. Le nouveau mode reste en vigueur jusqu'au
changement suivant, et le reste de la ligne, s'il y en a un, est exécuté dans ce mode. Le texte tapé prend la couleur
du mode courant, ou celle du mode qu'annonce son premier caractère.

| Début | Mode | Couleur | Effet |
|------|----------|-------|------------------------------------|
| `>` | mSL, avec traces | violet | la ligne est écrite dans le journal (`> ligne`), puis la valeur de sa dernière expression (`= valeur`) |
| `.` | mSL, silencieux | vert | ni la ligne ni sa valeur ne sont écrites ; les impressions de la ligne (`print`…) et ses erreurs le sont |
| `<` | réglages | orange | le texte est le contenu d'un `settings(data( … ))` du plug-in : `< hppos 3 Off` équivaut à `settings(data( hppos 3 Off ));` |
| `=` | (inchangé) | | la valeur de l'expression qui suit, quel que soit le mode : `= 2 * 3` |
| `?` | (inchangé) | bleu | l'aide, l'explication d'une erreur, la liste des noms (voir plus loin) |

Le mode mSL avec traces est le mode par défaut. La valeur d'une ligne est celle de sa dernière expression ; elle
n'est pas écrite quand la ligne se termine par un point-virgule ou par une accolade fermante, ni après la définition
d'une fonction. Une chaîne de caractères s'écrit entre guillemets, une fonction sous la forme `= function nom`
(`= function (lambda)` pour une fonction anonyme, § 12.6). Un `.` suivi d'un chiffre est un nombre (`.5 * x`), et
non un changement de mode. La définition d'une fonction, quand elle termine la ligne, peut se passer du
point-virgule final.

```
> 2 + 3
= 5
> function carre(x) (x * x)
> carre(12)
= 144
> var t = array(sin, cos);
> t[1](0)
= 1
< hppos 3 Off
```

Sur un fond clair, les couleurs des modes sont plus foncées que sur un fond sombre. Avec l'apparence *soft* (§ 5.5),
la ligne de saisie est affichée en vidéo inverse, comme une cellule de pad étendue sur toute la largeur du module.

### L'aide, les erreurs et les noms

| Ligne | Effet |
|--------|------------------------------------------|
| `?` | l'aide de la console, dans le journal |
| `? n` | l'explication de l'erreur n (`? 3418`), suivie du détail de sa dernière occurrence : l'identificateur non déclaré et sa position, le mot refusé par des réglages… |
| `? vars` | les noms des variables `var` du contexte de la console (voir plus loin), triés, en colonnes ; `nom()` désigne une variable dont la valeur est une fonction |
| `? locs` | les noms des variables `loc` du contexte |
| `? exts` | les noms des variables `ext` du plug-in, partagées par tous ses scripts (§ 12.3) |

Les explications des erreurs viennent du fichier `CMGS-data/CMGS-Erreurs.tsv` (la liste de la Partie IV), lu dans le
dossier `Data` de REAPER : il est installé avec le dossier `CMGS-data`.

```
> b = 3
? 3419
? 3419 (tous) : Identificateur non déclaré (affecté : il manque var, loc ou ext) …
?   the last one : b (line 1, column 1)
```

### Le menu de la console

Un clic droit dans le module (sans Shift : Shift + clic droit ouvre, comme partout, le menu des modules) ouvre le
menu de la console :

- *mSL with traces*, *mSL, silent*, *Settings* : choisissent le mode, comme `>`, `.` et `<` ;
- *Immediate*, *Incremental* : le traitement des variables d'une ligne à l'autre (voir plus loin) ;
- *Clear the context* : oublie le contexte de la console (son nombre de noms est indiqué) ;
- *Columns* : affiche les lignes sur 1 à 4 colonnes ; la plus récente est en bas de la colonne de gauche, juste
  au-dessus de la ligne de saisie, et les plus anciennes continuent en bas de la colonne suivante, vers la droite ;
- *Show the whole System Log* : la console affiche tout le journal du plug-in, et non ses seules lignes ;
- *Help* : l'aide, comme `?`.

### Les lignes de la console

La console garde ses propres lignes, les 160 dernières : ce qui est tapé, et tout ce que les lignes écrivent pendant
leur compilation et leur exécution (leurs valeurs, leurs impressions, leurs erreurs). L'activité du reste du
plug-in (une série de tests déposée, les autres scripts) ne les chasse donc pas. Tout est aussi écrit dans le
System Log, et l'enregistrement du journal par la touche `p` (§ 8.2) le conserve.

Les lignes tapées et les valeurs sont en violet, les réglages en orange, l'aide en bleu, les erreurs en rouge. Les
processus créés par une ligne (`` thread(`new, …) ``) ne sont pas suivis par la console : leurs impressions vont
seulement dans le System Log.

### Immédiat et incrémental

En mode *Immediate* (par défaut), chaque ligne est compilée seule : ses variables disparaissent avec elle. En mode
*Incremental*, les variables déclarées par une ligne (`var`, `loc`) restent connues des lignes suivantes, avec leurs
valeurs, ainsi que les noms déclarés `ext` et les fonctions (le nom d'une fonction est une variable dont la valeur
est la fonction) : c'est le **contexte** de la console. Le titre du module indique le nombre de ses noms ;
*Clear the context* l'oublie, et l'on repart d'un contexte vide.

```
> var a = 2;
> a * 10
= 20
> function plus_a(x) (x + a)
> plus_a(1)
= 3
? vars
? vars : 2 names (the context of the console)
?   a       plus_a()
```

### Déposer un script dans la console

Un fichier `.mSL` déposé sur le module est compilé et exécuté comme ailleurs, et il devient le contexte de la
console : les lignes tapées ensuite partagent ses variables et ses fonctions, pendant qu'il s'exécute (par exemple
pendant un `wait`) comme après sa fin. On peut ainsi lire ou modifier ses variables, appeler ses fonctions, suivre
son travail. La console passe en mode *Incremental* et son titre donne le nom du fichier ; les impressions et les
erreurs du script s'affichent aussi dans la console.

```
// compteur.mSL, déposé sur la console
var compteur = 0;
function remise() ( compteur = 0; );
while (compteur < 1000) ( compteur += 1; wait(1); );
```

```
> compteur
= 12
> remise();
> compteur
= 0
```

Les variables déclarées ensuite dans la console sont vues aussi par le script en cours.
