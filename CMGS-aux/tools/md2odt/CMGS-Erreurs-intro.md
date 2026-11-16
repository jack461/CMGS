---
title: "CMGS — Partie IV"
lang: fr-FR
---

# Liste des erreurs

## Lire un message d'erreur

Les plug-ins de CMGS vérifient autant que possible les données et les opérations qu'on leur confie. Lorsqu'un
problème est détecté, ils le signalent par un **code d'erreur**, un nombre de quatre chiffres, accompagné le plus
souvent d'un message, dans le journal (module *System Log*), sous la forme :

```
ERR: 2474    Space : the library of trajectories is full (128) : "Spirale" not kept
```

Certains modules affichent aussi le code de la dernière erreur dans une de leurs cellules (par exemple la cellule 13 du
module *Play Control* du Game Master).

Chaque code est **unique** dans l'ensemble des sources de CMGS : on peut le chercher tel quel dans ce chapitre, et le
développeur peut le retrouver dans le code. Les codes sont classés ici par ordre numérique ; la colonne « Application »
indique le plug-in qui le produit (« tous » : les bibliothèques communes, en particulier le langage mSL, présentes dans
tous les plug-ins).

**Erreurs de scripts.** Une erreur de **compilation** est signalée avec le numéro de la ligne et la position dans la
ligne où le compilateur s'est arrêté. Une erreur d'**exécution** arrête le processus qui l'a commise (et, par défaut,
les autres processus du plug-in : voir la Partie III). Un script peut signaler lui-même une erreur par la fonction
`error(n)` : le code affiché est alors **10000 + n**.

**Erreurs internes.** Les erreurs marquées « erreur interne » ou « erreur système » ne devraient pas se produire :
elles révèlent un défaut du logiciel ou une mémoire endommagée. Si l'une d'elles apparaît, notez les circonstances,
exportez le journal (touche `p`) et signalez-la à l'auteur ; il est en général prudent de recharger le projet.

## Les familles de codes

| Codes | Domaine |
|----------------------|------------------------------------------------------------------------------|
| 0100 à 0199 | mémoire statique, configurations de haut-parleurs du Game Master |
| 0200 à 0299 | tables de Diffusion-3, listes d'actions du Game Master |
| 0300 à 0399 | configurations de haut-parleurs et banques du Game Master |
| 0400 à 0499 | fichiers son, écran « Live » |
| 0500 à 0599 | lecture des clips (Game Master) |
| 0600 à 0699 | blocs de commande des lecteurs (FilePlayer), paramètres |
| 0700 à 0899 | tables du Game Master, matrices de Diffusion-3, modules définis par `gui` |
| 1000 à 1999 | compilateur, mémoire dynamique, exécution des scripts |
| 2000 à 2499 | syntaxe de mSL, lancement des scripts, tables de Diffusion-3 |
| 2600 à 2999 | Interstys |
| 3000 à 4999 | compilateur, ramasse-miettes, ordonnanceur, erreurs internes de Diffusion-3 |
| 6000 à 7999 | script auxiliaire, playlog, actions différées |
| 9000 à 9999 | erreurs internes et d'initialisation |
| 10000 et plus | erreurs signalées par les scripts (`error(n)`) |

Les codes de l'ancien manuel du Game Master qui ne figurent pas ici (par exemple 0310 à 0357, ou 0606 à 0610) ne sont
plus utilisés : ils concernaient les anciens fichiers de configuration séparés, remplacés par le Profile.
