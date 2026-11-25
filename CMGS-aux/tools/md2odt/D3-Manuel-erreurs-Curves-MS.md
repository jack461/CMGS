---
title: "Espaces — erreurs des courbes et des MetaSurfaces"
lang: fr-FR
---

# Les codes d'erreur

## Les courbes et les MetaSurfaces

Ces erreurs sont notées dans le journal sous la forme « ERR: 2443 Espaces settings (word n) : … » pour les blocs
Curve et MetaSurface des settings (comme pour la configuration, rien n'est changé), et « ERR: 1656 Curves : export : … »
pour les exports.

| Code | Sens |
|--------|--------------------------------------------------------------|
| 1650 | Curve : un numéro de courbe (1 à 64) ou un nom est attendu ; ou plus de courbe libre pour un nouveau nom |
| 1651 | Curve, name : un nom de 1 à 31 caractères, sans guillemet, est attendu ; ou ce nom est celui d'une autre courbe |
| 1652 | Curve : type Env, Wave, HEnv, QWave ou HWave ; periodic On ou Off |
| 1653 | Curve, points : des points x y c (2 à 128), x de 0 à 1 sans décroître, c de −1 à 1 |
| 1654 | Curve, points : un y hors de la plage du type (0 à 1 pour Env et HEnv, −1 à 1 pour les formes d'onde) |
| 1655 | Curve, sustain : un numéro de point de la courbe, ou Off ; seule une enveloppe (Env) a un point de sustain |
| 1656 | export des courbes : pas de courbe, le script CMGS-auxiliary.eel ne tourne pas, est trop ancien ou est occupé, le texte est trop long, ou le fichier n'a pas pu être écrit |
| 2441 | MetaSurface : un numéro de MetaSurface (1 à 32) est attendu |
| 2443 | MetaSurface : une valeur hors de sa plage (réglages, zone, place, glide, cycle, depth) |
| 2444 | MetaSurface : un mot de la liste de la clé est attendu (surface, rule, brush, mode, speed, chain, flip, dyn) |
| 2445 | MetaSurface, name : un « texte » est attendu |
| 2446 | MetaSurface, zone : plus de 32 diffusions |
| 2447 | MetaSurface, dyn, modrot, modspeed, modmix : Curve n (1 à 64) ou Curve "nom" (une courbe du projet, ou d'un bloc Curve placé avant) est attendu |
| 2448 | MetaSurface : une trajectoire est attendue après A, B, C ou D (None, Circle, Square, Star, Spiral, Central, Edit A à D, T1 à T128) |
| 2449 | MetaSurface : place ou flip sans A, B, C, D ou path avant |
| 2450 | export des MetaSurfaces : aucune MetaSurface utilisée, le script CMGS-auxiliary.eel ne tourne pas, est trop ancien ou est occupé, ou le texte est trop long : rien n'est écrit |
| 2451 | export des MetaSurfaces : le fichier n'a pas pu être écrit |
