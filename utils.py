#on se co a la bdd
#aller chercher les heros avec find sur cote_lunimeux
#tirer un mechant au hasard sur cote_obscur- fait + test ok
#save le score avec pseudo vague dans la bdd avec un insert_one dans scores
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
import random
from pymongo import MongoClient
from models import Hero, Mechant

client : MongoClient = MongoClient('mongodb://localhost:27017/')
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
    db.scores.insert_one({"player_name": pseudo, "waves": vagues})

def lire_top3():
    return list(db.scores.find().sort("waves", -1).limit(3))

def pseudo_existe(pseudo):
    return db.scores.count_documents({"player_name": pseudo}) > 0

def pseudo_valide(pseudo):
    if len(pseudo) <= 3 or len(pseudo) >= 10:
        return False
    if not pseudo.isalpha():
        return False
    if pseudo_existe(pseudo):
        return False
    return True

def afficher_menu(options):
    numero = 1
    for texte in options:
        print(f"{numero}. {texte}")
        numero += 1

def erreur():
    print("choix invalide recommence")

def choix(options, erreur):
    while True:
        saisie = input("ton choix:").strip()
        if saisie in options:
            return saisie
        erreur()

def afficher_heros(heros):
    print("\nheros disponible :")
    numero = 1
    for perso in heros:
        print(f"{numero}. {perso}")
        numero += 1

def afficher_equipe(equipe):
    print("\nton équipe:")
    for perso in equipe:
        print(perso)

def afficher_scores():
    print("\ntop3")
    for score in lire_top3():
        print(f"{score['player_name']} - {score['waves']} vagues")