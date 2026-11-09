# Presets d'Interstys

Cinq presets de génération, de conceptions différentes. Chacun transforme en profondeur un son d'entrée (une nappe très
stable suffit), sans distorsion, par des modulations, des textures qui évoluent et un hasard omniprésent : il prélève
le son à des positions aléatoires dans un buffer d'entrée de plusieurs minutes (mono ou stéréo) et écrit une dizaine de
minutes de résultat, mono, dans un buffer de sortie. Chaque exécution est différente.

| Fichier | Conception |
|---|---|
| `Preset-Nuee.mSL` | La granulation : trois couches de grains (fins, moyens, longs), chacune dans une fenêtre qui saute dans le buffer, avec son champ de hauteurs (octaves, quintes, tritons, micro-intervalles, glissements) ; un phaser, un passe-bas qui respire, un réseau de retards. Sections : poussière, essaim, nuage, traînées, tutti, silences. |
| `Preset-Glacier.mSL` | L'étirement et le gel : deux lecteurs Stretch avancent 8 à 250 fois plus lentement que le temps réel (parfois à reculons), transposés ; des fragments Brage ; un réseau de retards qui se fige par moments (un accord immobile qui ondule, pendant que le reste se tait) ; un halo Shimmer (octaves, quintes, désaccords infimes). |
| `Preset-Sillons.mSL` | Les boucles et le réenregistrement : des fragments s'enregistrent dans trois boucles courtes (overdub) relues à vitesse variable (à l'envers, transposées, glissandos, arrêts de bande) ; sillons fermés, effacements, réinjection d'une boucle dans l'autre, pleurage. |
| `Preset-Resonances.mSL` | Des corps résonants : le son n'est plus qu'une excitation (grains brefs, segments) de deux bancs de filtres très étroits accordés sur des spectres tirés au hasard (harmoniques, barre, cloche, accords justes, grappe…) et d'un peigne accordé ; les accords mutent ou glissent, un décaleur fait battre les partiels, des frappes relancent les résonances. |
| `Preset-Vertige.mSL` | Les spirales : des fragments (surtout à l'envers) injectés par bouffées dans deux boucles de retard où un décaleur de fréquence déplace le spectre à chaque tour (battements, spirales, cascades métalliques) ; un phaser à balayage sans fin. |
| `Presets-Stop.mSL` | Arrête les générations en cours (un fondu) ; les buffers restent. |
| `Presets-Free.mSL` | Retire tout : les instances des presets, leurs buffers, leurs modèles. |

## Utilisation

1. Régler les variables en tête du fichier (`Reglages`) :

   | Variable | Rôle |
   |---|---|
   | `fichier` | un fichier son pour le buffer d'entrée (relatif au dossier du projet, GMAuxiliary.eel en marche, ou un chemin complet) ; `""` : le son de la piste est enregistré |
   | `duree` | la durée du buffer d'entrée (s, au plus 1300) : celle de l'enregistrement, ou celle du fichier (au-delà, les positions reviennent au début du fichier) |
   | `canaux` | les canaux enregistrés : 1 (In:0) ou 2 (In:0 et In:1) ; un fichier donne les siens |
   | `continu` | 1 : l'enregistrement continue (le buffer garde les `duree` dernières secondes) ; 0 : il s'arrête |
   | `sortie` | la durée produite (s ; 600 par défaut) |
   | `ecoute` | le niveau d'écoute du résultat sur Out:0 et Out:1 (dB ; -120 : muet) |

2. Sans fichier : lancer la lecture de la piste (le son à transformer), puis déposer le preset dans la fenêtre
   d'Interstys. Le buffer d'entrée s'enregistre depuis In:0 ; la génération commence après 6 secondes et ne puise que
   dans la part déjà enregistrée. Avec un fichier : il est lu dans le buffer d'entrée, la génération commence aussitôt.
3. La génération se fait en temps réel : REAPER doit faire tourner la piste pendant `sortie` secondes (lecture en
   cours, ou piste armée avec le monitoring). Le journal suit les sections et les événements.
4. Le résultat est dans la ligne `res` de l'instance (`nuee:res`, `glacier:res`, `sillons:res`, `reson:res`,
   `vertige:res`) : le module Line la montre. Il s'entend aussi sur Out:0 et Out:1 : pour en faire un fichier,
   enregistrer la sortie de la piste dans REAPER pendant la génération.

Redéposer un preset relance une génération (la précédente s'arrête, ses buffers sont refaits). Plusieurs presets
différents peuvent tourner en même temps. La première fois, le journal note deux erreurs (2787, 2757) : les instances à
retirer n'existent pas encore.

## Fonctionnement

Chaque preset crée deux instances : `<nom>in` (le buffer d'entrée `src` et le writer `rec` qui l'enregistre) et `<nom>`
(le traitement, le buffer de sortie `res` et son writer `wo`). Puis le script reste actif : un « chef d'orchestre »
enchaîne des sections de durées aléatoires (en coupures ou en fondus), d'après une « énergie » qui erre autour d'un arc
(faible au début et à la fin), et modifie les modules par des tables (`Reader nuee:g1 from … to …`). Les valeurs
tirées au hasard sont glissées dans des tables modèles (`data(...)`) dont les mots `7700000001`, `7700000002`… sont
remplacés à chaque appel (fonction `tab`).

Les niveaux ne sautent jamais : chaque niveau est une cible (un LFO constant) suivie d'une pente (Math Slew, de -80 à
0 dB par pas de 0.8 dB), qui module le volume d'un lecteur, le gain d'un writer, ou un son (Math Exp, puis Math Mul).
Le niveau général finit par le limiteur automatique (`limiter On`), en garde-fou.

## Remarques

- Mémoire : le buffer de sortie fait `sortie` + 30 s, le buffer d'entrée `duree` s (par canal). À 48 kHz, 600 s de
  sortie et 180 s stéréo en entrée occupent environ 47 millions de mots (Interstys en a 128) ; à 96 kHz, le double.
- Un fichier lu dans une ligne d'instance (`Line nueein:src file …`) remplace la ligne ; la nouvelle ligne appartient
  toujours à l'instance (depuis le 2026-11-09), et `Free Instance` la libère. Le `Free Line <nom>in:src` qui précède
  `Free Instance` dans les presets n'est donc plus nécessaire ; il est sans effet nuisible.
- Les noms des modules et des modèles ont au plus 8 caractères ; `out` est un mot réservé (d'où `res`).
