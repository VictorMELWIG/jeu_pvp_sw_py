class Personnage:
    def __init__(self, nom, atk, defense, pv):
        self.nom = nom
        self.atk = atk
        self.defense = defense
        self.pv = pv
        self.pv_max = pv

    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, cible):
        degats = max(1, self.atk - cible.defense)
        cible.pv = max(0, cible.pv - degats)
        return degats

    def __str__(self):
        return f"{self.nom} - {self.atk} ATK - {self.defense} DEF - {self.pv} PV"

class Hero(Personnage):
    pass

class Mechant(Personnage):
    pass