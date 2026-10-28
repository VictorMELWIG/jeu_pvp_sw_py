#tant que l'equipe a un hero en vie 
#   on tire un mechant 
#   tant que le mechant est en vie et l'equipe aussi
#       tout les heros en vie attaque le mechant 
#       si le mechant meurt on le sort 
#       sinon il frappe un hero en vie
#       en boucle jusqu'a ce que les heros ou mechnat sortent
#on commence a la vague 0
#   tant que les heros sont en vie on tire un mechnat et frappe
#   +1 sur vague si le mehcnat sort 
#   return vague
import random
from utils import tirer_mechant

def heros_en_vie(equipe):
    vivants = []
    for heros in equipe:
        if heros.est_vivant():
            vivants.append(heros)
    return vivants

def equipe_en_vie(equipe):
    return len(heros_en_vie(equipe)) > 0

def tour_de_combat(equipe, mechant):
    for heros in heros_en_vie(equipe):
        degats = heros.attaquer(mechant)
        print(f"{heros.nom} inflige {degats} dégâts à {mechant.nom}")
        if not mechant.est_vivant():
            return
    cible = random.choice(heros_en_vie(equipe))
    degats = mechant.attaquer(cible)
    print(f"{mechant.nom} inflige {degats} dégâts à {cible.nom}")
    if not cible.est_vivant():
        print(f"{cible.nom} est tombé !")

def combattre_vague(equipe, mechant):
    while mechant.est_vivant() and equipe_en_vie(equipe):
        tour_de_combat(equipe, mechant)

def lancer_partie(equipe):
    vagues = 0
    while equipe_en_vie(equipe):
        mechant = tirer_mechant()
        print(f"\nVague {vagues + 1} : {mechant}")
        combattre_vague(equipe, mechant)
        if not mechant.est_vivant():
            vagues += 1
            print(f"{mechant.nom} est vaincu !")
    return vagues