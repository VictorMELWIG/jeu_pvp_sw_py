from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.jeu_pvp_sw_py
collection = db.cote_lumineux
collection.drop()
collection.insert_many([
    {
        "name": "luke",
        "attack": 30,
        "defense": 12,
        "hp": 280
    },
    {
        "name": "leia",
        "attack": 22,
        "defense": 10,
        "hp": 110
    },
    {
        "name": "han slo",
        "attack": 29,
        "defense": 6,
        "hp": 90
    },
    {
        "name": "obiwan",
        "attack": 26,
        "defense": 7,
        "hp": 85
    },
    {
        "name": "yoda",
        "attack": 32,
        "defense": 4,
        "hp": 75
    },
    {
        "name": "chewbacca",
        "attack": 24,
        "defense": 8,
        "hp": 100
    },
    {
        "name": "r2d2",
        "attack": 22,
        "defense": 9,
        "hp": 95
    },
    {
        "name": "rey",
        "attack": 28,
        "defense": 5,
        "hp": 80
    },
    {
        "name": "c3po",
        "attack": 23,
        "defense": 8,
        "hp": 90
    },
    {
        "name": "ahsoka",
        "attack": 21,
        "defense": 9,
        "hp": 100
    }
])
collection = db.cote_obscur
collection.drop()
collection.insert_many([
    {
        "name": "dark vador",
        "attack": 10,
        "defense": 6,
        "hp": 150
    },
    {
        "name": "palpatine",
        "attack": 10,
        "defense": 8,
        "hp": 180
    },
    {
        "name": "dark maul",
        "attack": 10,
        "defense": 12,
        "hp": 200
    },
    {
        "name": "kylo ren",
        "attack": 10,
        "defense": 7,
        "hp": 160
    },
    {
        "name": "dooku",
        "attack": 10,
        "defense": 10,
        "hp": 190
    },
    {
        "name": "grievous",
        "attack": 24,
        "defense": 6,
        "hp": 170
    },
    {
        "name": "jabba",
        "attack": 21,
        "defense": 14,
        "hp": 210
    },
    {
        "name": "boba fett",
        "attack": 26,
        "defense": 9,
        "hp": 175
    },
    {
        "name": "tarkin",
        "attack": 24,
        "defense": 8,
        "hp": 185
    },
    {
        "name": "thrawn",
        "attack": 19,
        "defense": 7,
        "hp": 155
    }
])
collection = db.scores

collection.drop()
collection.insert_many([
    {
        "player_name": "j1",
        "waves": 6
    },
    {
        "player_name": "j2",
        "waves": 9
    },
    {
        "player_name": "j3",
        "waves": 6
    },
    {
        "player_name": "j4",
        "waves": 10
    },
    {
        "player_name": "j5",
        "waves": 35
    },
    {
        "player_name": "j6",
        "waves": 14
    },
    {
        "player_name": "j7",
        "waves": 54
    },
    {
        "player_name": "j8",
        "waves": 51
    }
])
print("Base jeu_pvp_sw_py initialisée : 10 perso du coté lumineux, 10 perso du coté obscur, 8 scores.")