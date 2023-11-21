import random

def CheckIfINT(nb,  chiffre_un, chiffre_de):
    try:
        int(nb)
        it_is:bool = True
        nb = int(nb)
    except ValueError:
        it_is:bool = False
        print("donne un chiffre et non un chaine de charactere")
    while it_is == False:
        nb:str = input("Donne un bon nombre stp : ")
        try:
            int(nb)
            it_is:bool = True
            nb = int(nb)
        except ValueError:
            it_is:bool = False
            print("donne un chiffre et non un chaine de charactere")
    
    if nb > chiffre_de:
        while nb > chiffre_de or nb < chiffre_un:
            print("Nombre pas comprit entre 1 et 100, redonne un nombre")
            nb = int(input("Donne ton nombre : "))

    return nb


def Game(nb, essai,  chiffre_un, chiffre_de):
    while essai != 10:
        nb_joueur:str = input("Donne ton nombre : ")
        nb_joueur:str = CheckIfINT(nb_joueur,  chiffre_un, chiffre_de)
        if nb_joueur>nb:
            print("ton chiifre est tro grand")
            essai = essai + 1
        elif nb_joueur<nb:
            print("ton chiifre est tro petit")
            essai = essai + 1
        else:
            rep:str = input("gg a toi bg, tu veux recommencer une partie ? (y/n) ")
            if rep == "y" or rep == "yes":
                Start()
            else:
                print("ok")
                essai = 10
                return

def Start():    
    ask:str = input("Veut-tu fixer des bornes du nombre a deviner ? (y/n)")
    essai:int = 0
    chiffre_un:int = 1
    chiffre_de:int = 100
    if ask == "y":
        chiffre_un:int = int(input("Donne ton 1er chiffre : "))
        chiffre_de:int = int(input("Donne ton 2e chiffre : "))
        nb = random.randint(chiffre_un,chiffre_de)
    else:
        nb:int = random.randint(1,100)

    Game(nb, essai, chiffre_un, chiffre_de)

Start()