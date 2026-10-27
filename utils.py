#on se co a la bdd
#aller chercher les heros avec find sur cote_lunimeux- fait + test ok
#tirer un mechant au hasard sur cote_obscur- fait + test ok
#save le score avec pseudo vague dans la bdd avec un insert_one dans scores - fait + test ok
#voir le top3 avec find et un tri sur waves 
#afficher le menu MENU boucle sur chaque option>num+texte
#choix (option, erreur)
#   tant que c'est vrai on a la saisit du joueur
#   dans option on return
#   sinon def erreur
#erreur affiche choix invalide
#numero+hero pour valider la selection
#afficher les heros choisit par le joueur 
#afficher le top3 qu'on a recup au dessus
from pymongo import MongoClient
from models import Hero, Mechant
import random

client = MongoClient("mongodb://localhost:27017")
db = client.jeu_pvp_sw_py

def lire_heros():
    heros = []
    for doc in db.cote_lumineux.find():
        heros.append(Hero(doc["name"], doc["attack"], doc["defense"], doc["hp"]))
    return heros

def tirer_mechant():
    mechants = list(db.cote_obscur.find())
    doc = random.choice(mechants)
    return Mechant(doc["name"], doc["attack"], doc["defense"], doc["hp"])

def sauver_score(pseudo, vagues):
    db.scores.insert_one({"player_name" : pseudo, "waves" : vagues})

def lire_top3():
    return list(db.scores.find().sort("waves"))