from random import *

"""nb = int(input("Entrer un nombre"))

for i in range(1, nb):
    nb = nb + i
    print(f"{nb-i} + {i} = {nb}")

print(f"Le resultat de ces calcules est {nb}")"""


"""def noteRepeat(liste):
    return list(set(liste))


liste = [1, 2, 4, 9, 7, 7, 4, 4, 6, 3, 9, 3, 1, 3, 2, 4, 5, 6, 7, 53, 3]
print(liste)

print(noteRepeat(liste))"""


"""voyelle = [
    'a', 'e', 'i', 'o', 'u', 'y'
]

mot = input("Entrer un mot -> ")
nbVoyelle = 0

for i in range(len(mot)):
    if mot[i] in voyelle:
        nbVoyelle += 1

print(f"il y a {nbVoyelle} voyelle dans {mot}")"""


"""def ordober(liste):
    liste.sort()
    return liste


liste = [1, 2, 4, 9, 7, 7, 4, 4, 6, 3, 9, 3, 1, 3, 2, 4, 5, 6, 7, 53, 3]
print(liste)

print(ordober(liste))"""


"""cpt = 1
phrase = input("Entrer une phrase ->")


for i in range(len(phrase)):
    if phrase[i] == " " and phrase[i+1] != " ":
        
        cpt +=1

print(f"Il y a {cpt} mot dans la phrase '{phrase}'")"""


"""def reverse(mot):
    return mot[::-1]


mot = input("Entrer un mot -> ")
print(mot)

print(reverse(mot))"""

"""maj = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
]
min = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z'
]

nb = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

alea = 0

password = []

for i in range(5):
    alea = choice(range(1 , 4))

    if alea == 1:
        password.append(maj[choice(range(len(maj)))])
    elif alea == 2:
        password.append(min[choice(range(len(min)))])
    elif alea == 3:
        password.append(nb[choice(range(len(nb)))])

password.append(maj[choice(range(len(maj)))])
password.append(min[choice(range(len(min)))])
password.append(nb[choice(range(len(nb)))])

shuffle(password)

print(''.join(password))"""

"""def arondir(liste):
    mediane = round(len(liste) / 2)
    return liste[mediane]


liste = [1, 2, 4, 9, 7, 7, 4, 4, 6, 3, 9, 3, 1, 3, 2, 4, 5, 6, 7, 53, 3]


print(arondir(liste))"""









