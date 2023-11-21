import random

def check(nb,  chiffre_un, chiffre_de):
    try:
        int(nb)
        it_is = True
    except ValueError:
        it_is = False
        print("donne un chiffre et non un chaine de charactere")
    while it_is == False:
        nb = input("Donne un bon nombre stp : ")
        try:
            int(nb)
            it_is = True
            nb = int(nb)
        except ValueError:
            it_is = False
            print("donne un chiffre et non un chaine de charactere")
    
    if nb > chiffre_de:
        while nb > chiffre_de or nb < chiffre_un:
            print("Nombre pas comprit entre 1 et 100, redonne un nombre")
            nb = int(input("Donne ton nombre : "))

    return nb


def jeu(nb, essai,  chiffre_un, chiffre_de):
    nb_joueur = input("Donne ton nombre : ")
    nb_joueur = check(nb_joueur,  chiffre_un, chiffre_de)
    if essai >= 9:
        print("perdu")
        rep = input("gg a toi bg, tu veux recommencer une partie : ")
        if rep == "y":
            start()
        else:
            print("ok")
            return 
    else:
        if nb_joueur>nb:
            print("ton chiifre est tro grand")
            essai = essai + 1
            jeu(nb, essai, chiffre_un, chiffre_de)
        elif nb_joueur<nb:
            print("ton chiifre est tro petit")
            essai = essai + 1
            jeu(nb, essai, chiffre_un, chiffre_de)
        else:
            rep = input("gg a toi bg, tu veux recommencer une partie : ")
            if rep == "y":
                start()
            else:
                print("ok")
                return

def start():    
    ask = input("Veut-tu fixer des bornes du nombre a deviner ? (y/n)")
    essai = 0
    chiffre_un = 1
    chiffre_de = 100
    if ask == "y":
        chiffre_un = int(input("Donne ton 1er chiffre : "))
        chiffre_de = int(input("Donne ton 1er chiffre : "))
        nb = random.randint(chiffre_un,chiffre_de)
        print(nb)
    else:
        nb = random.randint(1,100)

    jeu(nb, essai, chiffre_un, chiffre_de)

start()