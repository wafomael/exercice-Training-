from random import *

planetes = [
    "mercure", "venus", "terre",
    "mars", "jupiter", "saturne",
    "uranus", "neptune", "pluton"
]

activation = True

print("tu doit deviner qu'elle est la planete\nPour sortire du jeux , taper 'end'")

while activation:
    alea = planetes.index(choice(planetes)) + 1

    planete = input(f"Quelle est la {alea} planete du systeme scolaire (〃￣︶￣)-> ")

    if planete.lower() == planetes[alea - 1]:
        print(f"Bien joué, ^0^ {planetes[alea - 1]} est la {alea} planete du systeme solaire ^_-")
    elif not planete.lower() in planetes:
        if planete != "end":
            print(f"{planete} n'est pas une planete du systeme solaire (┬┬﹏┬┬)")
    else:
        print(f"{planete} n'est pas la {alea} planete du systeme solaire -_- c'est {planetes[alea - 1]} la {alea} planete du systeme solaire  ~_~")

    if planete.lower() == "end":
        activation = False
        print("game OFF")