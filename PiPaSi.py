from random import *

activation = True

pointJ = 0
pointO = 0
print("Vous allez jouer à Pierre , Papapier, Ciseaux.\nPour sortir taper 'END'")
while activation:
    joueur = input("Choisiser un nombre\n1.Pierre\n2.Papier\n3.Ciseaux\n-> ")
    ordinateur = str(choice(range(1 , 4)))

    if joueur == ordinateur:
        print("Match null")
    elif joueur == "1" and ordinateur == "2":
        print("L'ordinateur Gagne")
        pointO += 1
    elif joueur == "2" and ordinateur == "1":
        print("Le joueur Gagne")
        pointJ += 1
    elif joueur == "3" and ordinateur == "1":
        print("L'ordinateur Gagne")
        pointO += 1
    elif joueur == "1" and ordinateur == "3":
        print("Le joueur Gagne")
        pointJ += 1
    elif joueur == "2" and ordinateur == "3":
        print("L'ordinateur Gagne")
        pointO += 1
    elif joueur == "3" and ordinateur == "2":
        print("Le joueur Gagne")
        pointJ += 1
    elif joueur.lower() == "end":
        activation = False
    """elif ordinateur == "4":
            activation = False"""

    print(f"Ordinateur:{pointO}                                       Joueur:{pointJ}")


    if pointO == 2:
        print("\nL'ordinateur Gagne la partie\n")
        pointO = 0
        pointJ = 0
    elif pointJ == 2:
        print("\nLe joueuer Gagne la partie\n")
        pointO = 0
        pointJ = 0

