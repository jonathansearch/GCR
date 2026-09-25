"""Tests GCR : témoin + étincelle + étirement + pont Omni (mise à jour). MIT."""
import sys
sys.path.insert(0, '/home/user/GCR/univers')
sys.path.insert(0, '/home/user/RATISS-Omni')


def test_temoin_elastique():
    from collision import run, etincelle
    s, eq, _ = run(0.0, 0.5, A=0.0)
    an = etincelle(s)
    assert an['b1_max'] <= 1, an
    assert not an['etincelle']


def test_etincelle_topologique():
    from collision import run, etincelle
    s, eq, _ = run(5.0, 0.5, A=10.0, gamma=0.05)
    an = etincelle(s)
    assert an['etincelle'], an
    assert 2 <= an['b1_max'] <= 4, an  # trous b1=2-4 (découverte)


def test_etirement_pas_dechire():
    from collision import run, etincelle
    s, eq, _ = run(5.0, 0.5, A=10.0, gamma=0.3)
    an = etincelle(s)
    assert not an['etincelle'], an  # gamma haut : étire, ne déchire pas


def test_pont_Omni_maj(tmp_path):
    from collision import run, etincelle
    from ratiss_core.bus import OmniBus
    from ratiss_core.control import control_step
    s, eq, _ = run(5.0, 0.5, A=10.0, gamma=0.05)
    an = etincelle(s)
    b = OmniBus(str(tmp_path / 'gcr_bus.dat'), create=True)
    b.write(E_turb=max(p['ekin'] for p in s), T2_us=223.7,
            Q_fus=an['b1_max'])
    a = control_step(b)
    assert 1e-10 <= a <= 2e-9, a  # GCR pilote le drive via Omni
