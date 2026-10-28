#menu
#   lancer jeu
#   afficher le classement
#   quitter
#demande le pseudo 
#   boucle infinie
#       demander un pseudo
#       si le pseudo est valide return
#       sinon fonction erreur 
#choisir l'equipe
#   recup les heros de cote_lumineux
#   tant que l'equipe a pas 3 heros on laisse la selection des heros afficher 
#       affiche l'equipe selectionné avec les heros numeroté
#       choix avec numero des heros
#       si il est deja dans l'equipe on ajoute pas
#       sinon on ajoute 
#   return l'equipe
#jouer
#   on reprend le pseudo entré
#   on reprend l'equipe selctionné
#   lance la partie
#   save le score 
#   afficher le score
#choix
#   1 jour
#   2 afficher le score
#   3 sys.exit
import sys
from game import lancer_partie
from utils import afficher_menu, afficher_heros, afficher_equipe, afficher_scores
from utils import choix, erreur, lire_heros, pseudo_valide, sauver_score
MENU = ["Lance le jeu", "afficher les scores", "quitter"]

def demander_pseudo():
    while True:
        pseudo = input("ton pseudo: ").string()
        if pseudo_valide(pseudo):
            return pseudo
        print("psuedo invalide, avce que des lettres entre 3 et 18 stp")

def choisir_equipe():
    heros = lire_heros()
    numero = []
    for i in range(1, len(heros) + 1):
        numero.append(str(i))
    equipe = []
    while len(equipe) < 3:
        afficher_equipe(equipe)
        afficher_heros
        numero = int (choix(numero, erreur))
        perso = heros[numero - 1]
        if perso in equipe :
            print("ce hero est deja dans l'equipe")
        else:
            equipe.append(perso)
        return equipe

def jouer():
    pseudo = demander_pseudo()
    equipe = choisir_equipe()
    vagues = lancer_partie
    sauver_score(pseudo, vagues)
    print(f"\n{pseudo} a fait {vagues} vagues")
    afficher_scores()

def process(reponse):
    if reponse == "1":
        jouer()
    elif reponse == "2":
        afficher_scores()
    elif reponse == "3":
        sys.exit()

if __name__=="__main__":
    while True:
        afficher_menu(MENU)
        process(choix(["1", "2", "3"], erreur))