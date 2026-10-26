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

