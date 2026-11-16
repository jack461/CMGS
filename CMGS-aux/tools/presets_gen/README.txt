Generateur des presets d'Interstys (CMGS-scripts/Presets/Preset-*.mSL).
  common.py      les parties communes (reglages, outils, niveaux, demarrage, fin) ; jetons @INS@ ... et @k@ (7700000000 + k)
  p_*.py         le corps de chaque preset (doc, modules, chef d'orchestre)
  build.py       python3 -I build.py <dossier>   : ecrit les cinq Preset-*.mSL
  check.py       python3 -I check.py <fichiers>  : parentheses, noms <= 8 caracteres, nombre de valeurs de chaque tab(),
                 modules definis / designes dans les algorithmes, mots reserves
Presets-Stop.mSL, Presets-Free.mSL et README.md sont ecrits a la main (dans CMGS-scripts/Presets).
