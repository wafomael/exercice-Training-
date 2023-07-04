from random import *

alphabet = [
    'b', 'c', 'd','f', 'g', 'h',
    'j', 'k', 'l', 'm', 'n', 'p', 'q',
    'r', 's', 't', 'v', 'w', 'x','z',
    'a', 'e', 'i', 'o', 'u', 'y'
]

consonne = [
    'b', 'c', 'd','f', 'g', 'h',
    'j', 'k', 'l', 'm', 'n', 'p', 'q',
    'r', 's', 't', 'v', 'w', 'x','z'
]

voyelle = [
    'a', 'e', 'i', 'o', 'u', 'y'
]

voyellesP = [
    "Je pense que c'est une voyelle.",
    "Cette lettre ressemble à une voyelle.",
    "Les voyelles sont souvent présentes dans les mots.",
    "Je dirais que c'est une voyelle.",
    "Les voyelles apportent de la fluidité aux mots.",
    "Cela ressemble à une voyelle pour moi.",
    "Les voyelles sont essentielles dans la prononciation.",
    "Hmm, je détecte une voyelle ici.",
    "Je parie que c'est une voyelle.",
    "Les voyelles sont les mélodies des mots."
]

consonnesP = [
    "Cette lettre ressemble à une consonne.",
    "Les consonnes forment souvent le squelette des mots.",
    "Je dirais que c'est une consonne.",
    "Les consonnes ont généralement un son distinctif.",
    "Cela ressemble à une consonne pour moi.",
    "Les consonnes ajoutent du rythme aux mots.",
    "Hmm, je détecte une consonne ici.",
    "Je parie que c'est une consonne.",
    "Les consonnes sont les blocs de construction des mots.",
    "Cette lettre a l'air d'être une consonne."
]

phrases_demande_autre_partie = [
    "C'était amusant ! On joue encore une partie !",
    "Je veux une revanche ! On continue à jouer !",
    "Cette partie était géniale, jouons-en une autre !",
    "Je ne peux pas m'arrêter là, on en fait une autre !",
    "J'ai hâte de rejouer, on fait une autre partie !",
    "C'était tellement divertissant, jouons encore !",
    "Je suis partant(e) pour une autre partie, et vous !",
    "On s'amuse bien, continuons à jouer, d'accord !",
    "Je veux essayer encore, on joue une autre fois !",
    "C'était trop court, je veux une autre partie !"
]


print("Nous allons joeur \n\nje dois deviner si la lettre que vous me donner est une voyelle ou une consonne")
print("NB! \nsi vous vouler arreter pour eteindre completement taper 'STOP'\n\n")

choix = input("On commence, donner moi une lettre : ->")
while choix.lower() != "stop":

    if choix.lower() == "stop":
        break

    while not choix.lower() in alphabet or len(choix) != 1:
        choix = input("Entrer une voyelle ou une consone : ->")
        if choix.lower() == "stop":
            break

    if choix.lower() in consonne:
        print(consonnesP[randint(0, 9)])
    elif choix.lower() in voyelle:
        print(voyellesP[randint(0, 9)])

    print(phrases_demande_autre_partie[randint(0, 9)])

    choix = input("Donner moi une lettre : ->")






