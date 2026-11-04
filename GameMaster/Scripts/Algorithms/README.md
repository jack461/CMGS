# Bibliothèque d'algorithmes d'Interstys

Des recettes prêtes à l'emploi, pensées pour la création sonore : chaque fichier `.mSL` se dépose dans la
fenêtre d'Interstys et installe aussitôt un algorithme complet, branché sur la piste.

## Utilisation

- **Déposer** un fichier `Matrix-….mSL` dans Interstys : le son de la piste (`In:0`) passe dans
  l'algorithme, le son sec et le son traité sortent vers `Out:0`.
- **Régler** : les paramètres sont sur la ligne `Instance` en bas de chaque fichier (le nombre de canaux
  `nch`, les durées, les fréquences, les niveaux `dry` et `wet`). Modifier la ligne, puis redéposer le
  fichier : l'instance est refaite. Les autres réglages se changent à la main dans les pads des effets
  de l'instance (le module Instances la montre).
- **Essayer sans matériau** : `Sources.mSL` met des clics (ou un buzz) sur le bus 64, que toutes les
  recettes écoutent en plus de leur entrée. `Sources-Stop.mSL` l'arrête.
- **Tout retirer** : `Free-All.mSL`.
- **Plusieurs canaux** : mettre `nch` au nombre de canaux de la piste (jusqu'à 128). Sur une piste
  stéréo, `nch 2`.

La première fois qu'on dépose un fichier, le journal note une erreur 2787 : le fichier retire d'abord une
instance précédente, qui n'existe pas encore. C'est sans conséquence.

## Les recettes de la Matrix (réseau de retards bouclés)

| Fichier | Ce qu'il fait |
|---|---|
| `Matrix-Espace` | Un espace dense : toutes les lignes mélangées à chaque passage (Hadamard) |
| `Matrix-Traines` | Des traînes locales : chaque canal garde la sienne, qui déborde lentement (Householder) |
| `Matrix-Metal` | Un métal accordé : toutes les lignes au même retard, un seul peigne résonant |
| `Matrix-Accord` | Un accord métallique : des retards multiples d'une période |
| `Matrix-Masse` | Une masse qui enfle : la boucle croît (Grow) et sature |
| `Matrix-Pompe` | Un pompage collectif : un couplage négatif entre les lignes |
| `Matrix-Souffle` | Une traîne qui respire : sa durée balayée par un LFO très lent |
| `Matrix-Tenue` | Une pédale de tenue : la durée de la traîne sur un curseur Ctl (automatisable, MIDI) |
| `Matrix-Repandu` | Une source mono sur tous les canaux : le canal 0 dans toutes les lignes |
| `Matrix-Anneau` | Un anneau : chaque écho passe au haut-parleur voisin, le son tourne (Ring) |
| `Matrix-Ondule` | Une traîne qui ondule : les retards modulés lentement, déphasés d'une ligne à l'autre |
| `Matrix-Vrille` | Une vrille métallique : des retards courts modulés à vitesse audio |

Chaque recette se compose de trois effets : `pre` (l'entrée et le bus d'essai), `fdn` (la Matrix),
`post` (le mélange sec et traité vers la sortie) ; `Matrix-Souffle` y ajoute un LFO.
