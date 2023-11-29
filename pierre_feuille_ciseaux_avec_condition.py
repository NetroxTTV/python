import random   

def Game():
    check:bool = True
    while check == True:
        choice: str = str(input("Choose Rock, Paper or Scissors : "))
        player:int = 0
        check:bool = True
        tab:list = ["rock", "paper", "scissors"]
        while check == True:
            for i in range(len(tab)):
                if choice == tab[i]:
                    player = i + 1
                    check = False
            if check == True:
                print("Put a Valid Answer")
                joueur:str = str(input("Choose Rock, Paper or Scissors : "))
            
        bot:int = random.randint(1,3)

        if bot == 1 and player == 3 or bot == 2 and player == 1 or bot == 3 and player == 2:
            print("The Bot WON")
        elif bot == player:
            print("TIE")
        else:
            print("YOU WON")
        anws:str=input("Do you want to play again ? (yes/no)")
        if anws == "yes" or anws == "y":
            check = True
        else:
            print("ok")
            check = False
            return

Game()