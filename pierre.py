import random   

def restart():
    anws=input("Joueur a gagner, veut tu re-jouer ? (yes/no)")
    if anws == "yes":
        start()
    else:
        print("ok")
        return

def jeu(joueur, val_joueur):
    if joueur == "pierre" or joueur == "p":
        val_joueur = 1
    elif joueur == "feuille" or joueur == "f":
        val_joueur = 2
    elif joueur == "ciseaux" or joueur == "c":
        val_joueur = 3
    else:
        print("donne une réponse valide")
        start()
    ordi = random.randint(1,3)

    if ordi == 1 and val_joueur == 3:
        print("ordi a gagner")
        restart()
    elif ordi == 2 and val_joueur == 1:
        print("ordi a gagner")
        restart()
    elif ordi == 3 and val_joueur == 2:
        print("ordi a gagner")
        restart()
    elif ordi == val_joueur:
        print("egalité")
        restart()
    else:
        print("joueur a gagné")
        restart()

def start():
    joueur = str(input("Choisi entre pierre, feuille et ciseaux : "))
    val_joueur = 0
    jeu(joueur, val_joueur)

start()