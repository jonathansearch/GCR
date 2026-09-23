#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""GCR-V batterie v3 : equilibre puis tir (A x gamma x v)."""
import json, sys
import numpy as np
sys.path.insert(0, 'univers')
from collision import run, etincelle
res = {'runs': {}}
s, e0 = run(0.0, 0.5, A=0.0)
res['runs']['temoin'] = {'series': s, 'eq_ekin': e0, **etincelle(s)}
print(f"TEMOIN: eq_ekin={e0:.1f} b1max={max(p['b1'] for p in s)}")
print(f"{'v':>4s} {'A':>4s} {'gam':>5s} {'b1max':>6s} {'dropmax':>8s} {'Emax/Eq':>8s} {'vmax':>6s} {'clips':>5s} verdict")
for v, A, gam in ((2.0,3.0,0.3),(2.0,10.0,0.3),(2.0,10.0,0.05),
                  (3.0,3.0,0.3),(3.0,10.0,0.3),(3.0,10.0,0.05),
                  (5.0,3.0,0.3),(5.0,10.0,0.3),(5.0,10.0,0.05),
                  (5.0,20.0,0.05)):
    log = []
    s, eq = run(v, 0.5, A=A, gamma=gam, Fmax_log=log)
    an = etincelle(s)
    emax = max(p['ekin'] for p in s); vmax = max(p['vmax'] for p in s)
    dmax = max(p['drop'] for p in s if np.isfinite(p['drop']))
    nc = sum(log)
    res['runs'][f'v{v}_A{A}_g{gam}'] = {'series': s, 'eq_ekin': eq, 'clips': nc, **an}
    ok = 'SUSPECT' if (nc or vmax > 30 or emax > 2e5) else ('ETINCELLE' if an['etincelle'] else 'elastique')
    print(f"{v:>4.1f} {A:>4.0f} {gam:>5.2f} {an['b1_max']:>6.0f} {dmax:>8.3f} "
          f"{emax/max(eq,1e-9):>8.1f} {vmax:>6.2f} {nc:>5d} {ok}")
json.dump(res, open('resultats/gcr_v1.json', 'w'))
print('[gcr-v3] resultats/gcr_v1.json OK')
