nom = input("quelle est votre nom ? ->")
prenom = input("quelle est votre prenom ? ->")
age = float(input("quelle est votre age ? ->"))
ville = input("Dans quelle ville vivez vous ? ->")
pasword = input("quelle est votre mot de passe ? ->")
id = float(input("quelle est votre identifiant ? ->"))

print("Se connecter\n\n\n\n")
nomV = input("nom: -> ")
prenomV = input("prenom: -> ")
ageV = float(input("age: -> "))
villeV = input("ville: -> ")
paswordV = input("pasword: -> ")
idV = float(input("id: -> "))

verification = 0

while verification < 6:
    if nomV != nom:
        print("le nom n'est pas corecte")
        nomV = input("nom: -> ")
    else:
        verification += 1
    if prenomV != prenom:
        print("le prenom n'est pas corecte")
        prenomV = input("prenom: -> ")
    else:
        verification += 1
    if ageV != age:
        print("l'age n'est pas corecte")
        ageV = float(input("age: -> "))
    else:
        verification += 1
    if villeV != ville:
        print("la ville n'est pas corecte")
        villeV = input("ville: -> ")
    else:
        verification += 1
    if paswordV != pasword:
        print("le mot de passe n'est pas corecte")
        paswordV = input("pasword: -> ")
    else:
        verification += 1
    if idV != id:
        print("le prenom n'est pas corecte")
        idV = float(input("id: -> "))
    else:
        verification += 1
    if verification < 6:
        verification = 0

print("Conection reussit  ;)")



