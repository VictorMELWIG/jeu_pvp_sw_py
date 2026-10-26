from models import Hero, Mechant
from utils import lire_heros, tirer_mechant

#test l'affichage au bon format
def test_affichage():
    yoda = Hero("yoda", 20, 5, 80)
    assert str(yoda) == "yoda - 20 ATK - 5 DEF - 80 PV"

#test que les attaques font des degats 
def test_attaquer_retire_des_pv():
    yoda = Hero("yoda", 20, 5, 80)
    vador = Mechant("vador", 25, 10, 100)
    degats = yoda.attaquer(vador)
    assert degats == 10
    assert vador.pv == 90

#test degat minimum
def test_degats_minimum_1():
    rey = Hero("rey", 5, 5, 50)
    palpatine = Mechant("palpatine", 30, 25, 250)
    assert rey.attaquer(palpatine) == 1

#test que les pv descendent pas en dessous de 0 et que le mechant meurt 
def test_pv_jamais_negatifs():
    yoda = Hero("yoda", 100, 5, 50)
    maul = Mechant("maul", 10, 5, 20)
    yoda.attaquer(maul)
    assert maul.pv == 0
    assert not maul.est_vivant()

#test que les 10 heros sont bien lus depuis la bdd
def test_lire_heros():
    heros = lire_heros()
    assert len(heros) == 10

#test qu'on tire bien un mechant vivant
def test_tirer_mechant():
    mechant = tirer_mechant()
    assert mechant.est_vivant()

if __name__ == "__main__":
    test_affichage()
    test_attaquer_retire_des_pv()
    test_degats_minimum_1()
    test_pv_jamais_negatifs()
    test_lire_heros()
    test_tirer_mechant()
    print("tout est bon")