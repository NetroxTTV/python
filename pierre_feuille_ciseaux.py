import random   

def Game():
    rewind = True
    while rewind == True:
        joueur: str = str(input("Choisi entre pierre, feuille et ciseaux : "))
        valeur_joueur = 0
        a: bool = True
        while a == True:
            if joueur == "pierre" or joueur == "p":
                valeur_joueur = 1
                a = False
            elif joueur == "feuille" or joueur == "f":
                valeur_joueur = 2
                a = False
            elif joueur == "ciseaux" or joueur == "c":
                valeur_joueur = 3
                a = False
            else:
                print("donne une réponse valide")
                joueur = str(input("Choisi entre pierre, feuille et ciseaux : "))
            
        ordi = random.randint(1,3)

        if ordi == 1 and valeur_joueur == 3 or ordi == 2 and valeur_joueur == 1 or ordi == 3 and valeur_joueur == 2:
            print("ordi a gagner")
        elif ordi == valeur_joueur:
            print("egalité")
        else:
            print("joueur a gagné")
        anws=input("Joueur a gagner, veut tu re-jouer ? (yes/no)")
        if anws == "yes" or anws == "y":
            rewind = True
        else:
            print("ok")
            rewind = False
            return

Game()