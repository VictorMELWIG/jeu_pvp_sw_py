# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
# Process
#    JEU
#       on commenvce a la vague 0
#       tant que l'equipe a un hero en vie 
#           on tire un mechant 
#           tant que le mechant est en vie et l'equipe aussi
#               tout les heros en vie attaque le mechant 
#               si le mechant meurt on le sort 
#               le mechnat attaque un hero en vie 
#       si le mechant meurt le compteur de vague passe a +1
#renvoie le nombre de vague
#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#    Quitter
#       sys.exit()