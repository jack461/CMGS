---
title: "CMGS — fragment erreurs"
lang: fr-FR
---

# Exécution des scripts

## Les erreurs d'un processus

Une erreur d'exécution (écriture hors d'un bloc, mémoire épuisée, nombre d'arguments incorrect, `error(code)`…)
arrête le processus qui l'a commise, et lui seul : les autres processus du plug-in continuent. C'est le comportement
par défaut, adapté au concert : un script en défaut ne doit pas interrompre les autres. Le journal donne le numéro
de l'erreur ; dans la console mSL (§ 8.6), `? n` en donne l'explication et le détail de sa dernière occurrence.

Pour la mise au point, `` call(`errLock, 1); `` fait revenir au mode de verrouillage : la première erreur arrête alors
tous les processus du plug-in, jusqu'à la fin du prochain passage du ramasse-miettes, ou jusqu'à *Unlock Scripts*
dans le module Processes Manager (§ 8.5). `` call(`errLock, 0); `` rétablit le comportement par défaut, et
`` call(`errLock) `` rend la valeur courante. Un script qui provoque des erreurs à dessein peut ainsi s'assurer du mode :

```
var avant = call(`errLock, 0);     // une erreur n'arrête que son processus
// ... les essais qui produisent des erreurs ...
call(`errLock, avant);              // le mode d'avant
```

Une erreur de compilation (un script déposé, une ligne de la console) n'arrête aucun processus : le script fautif
n'est simplement pas lancé.
