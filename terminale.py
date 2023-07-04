"""class Disk:
    def __init__(self, nom, taille, libre):
        self.nom = nom
        self.taille = taille
        self.statut = "En ligne"
        self.libre = libre
        self.select = False

Disks = [Disk("Systeme", 200, 50), Disk("MeData", 420, 122), Disk("Me-USB", 100, 39)]


#for disk in Disks:
    #print(disk.nom, disk.taille)


print("Microsoft Windows [version 10.0.22000.1936]\n(c) Microsoft Corporation. Tous droits réservés.")

commande = None

while commande != "stop":
    commande = input("C:\Windows\system32>")
    if commande == "diskpart":
        print("Microsoft DiskPart version 10.0.22000.653\nCopyright (C) Microsoft Corporation.\nSur l’ordinateur : ASSUS")
        while commande != "exit":
            commande = input("DISKPART>")

            if commande == "list disk":
                print("Numéro    Statut     Taille    Libre    Dyn   GPT\n-------------------------------------------------")

                for disk in Disks:
                    print(f"Disque{Disks.index(disk)}  {disk.statut}    {disk.taille}Go    {disk.libre}Go")

            if len(commande) == 13 and commande[0:6] == "select" and commande[7:11] == "disk":
                for disk in Disks:
                    if int(commande[-1]) == Disks.index(disk):
                        if disk.select == True:
                            disk.select = False
                        disk.select = True
                        print(f"Le disque {Disks.index(disk)} est maintenant le disque sélectionné.")



                    #print(disk.select)"""



print("Microsoft Windows [version 10.0.22000.1936]\n(c) Microsoft Corporation. Tous droits réservés.")

commande = None
selection = False

while commande != "stop":
    commande = input("C:\Windows\system32>")
    if commande == "diskpart":
        print("Microsoft DiskPart version 10.0.22000.653\nCopyright (C) Microsoft Corporation.\nSur l’ordinateur : ASSUS")
        while commande != "exit":
            commande = input("DISKPART>")
            if commande == "list disk":
                print("\n\nNuméro    Statut     Taille    Libre    Dyn   GPT\n-------------------------------------------------")
                print(f"Disque0  En ligne    320Go    100Go\n")
            elif commande == "select disk 0":
                print("Le disque0 est maintenant le disque sélectionné.")
                selection = True
            elif commande == "clean" and selection:
                print("Le disque est nettoyé")
            elif commande == "create partition primary" and selection:
                print("La partition a été créée avec succès.")
            elif commande == "active" and selection:
                print("La partition a été activé avec succès.")
            elif commande == "format fs=ntfs" and selection:
                print("Le formatage du volume en NTFS est en cours...\nLe formatage du volume est terminé.")
            elif commande == "assign"  and selection:
                print("La lettre 'E' a été attribuée avec succès.")







