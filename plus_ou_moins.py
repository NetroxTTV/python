import random

def AskInt(message: str, min: int, max: int):
    while True:
        try:
            value: int = int(input(message))

            if value >= min and value <= max:
                return value

            print("Not in range")

        except:
            print("Please type a number and not a character") 
 

def jeu(nb, tries,  min, max):
    while tries != 10:
        nb_joueur = AskInt("Please type a number : ", min, max)

        if nb_joueur>nb:
            print("My number is smaller")
            tries = tries + 1
        elif nb_joueur<nb:
            print("My number is bigger")
            tries = tries + 1
        else:
            rep:str = input("Good job, do you want to replay ? (y/n) ")
            if rep == "y":
                start()
            else:
                print("ok")
                return
            
    print("You Lost")
    rep:str = input("Good job, do you want to replay ? : ")
    if rep == "y":
        start()
    else:
        print("See ya")
        return 

def start():
    ask:str = input("Do you want to To fix the range ? (y/n)")
    tries:int = 0
    min:int = 1
    max:int = 100
    if ask == "y":
        min:int = int(input("Type your number : "))
        max:int = int(input("Type your number : "))
        nb = random.randint(min,max)
        print(nb)
    else:
        nb:int = random.randint(1,100)

    jeu(nb, tries, min, max)

start()