import random

def moi():
    nbr = random.choice(range(0, 500))

    devine = float(input("Devine mon nombre ......"))

    while devine != nbr:

        if devine < nbr:
            print("plus grand")
            devine = float(input("recomence"))
        elif devine > nbr:
            print("plus petit")
            devine = float(input("recomence"))
        elif devine == nbr:
            return 1
