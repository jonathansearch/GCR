# GCR — Grand Collisionneur de Ratiss (univers virtuel uniquement)
Collision de 2 murs tanh dans nappe auto-gravitante (micro-loi S03 : coeur
Planck k=0.108 = raideur du tissu). Détecteur : beta1 exact (Euler sur
complexe alpha, alpha=0.5) + E_kin + drop (maille étirée). Brutalité
B' = v*A/(w*gamma). Unités jouet (capacité à déformer, PAS de GeV).

## Résultat V3 (stable : 0 clips, vmax saines)
- ÉTINCELLES (trous b1=2-4, vie 0.2-0.8tu) si gamma=0.05, A>=10, v>=3 (B'>~500).
- 2 modes de breakup : DÉCHIRURE (gamma bas : trous) vs ÉTIREMENT (gamma haut :
  drop 0.23, b1<=1, lisse). A=3 : élastique (survit).
- Destin : fragmentation irréversible (r_rms 2->13, ouvert, pas de re-cuisson).
- V1 INVALIDÉE (explosion numérique ekin~10^6) ; V2 stable mais non équilibrée.
Détails : JOURNAL.md · ticket : tickets/ETINCELLE_TOPOLOGIQUE.md
QPU (le testeur) : voir synchrotron-24/qpu-bigbang (PAS ici : GCR = virtuel).
