import random

def ShowPlayfield(playfield):
    for i in range(len(playfield)):
        if i%3 == 0:
            print('\n')
        print(playfield[i], end = " ")
    print('\n')
    print('______________________')
    print('\n')

def CheckPlacement(playfield, user_choice):
    if 0 <= user_choice <= 8:
        if playfield[user_choice] == ".":
            return True
    return False

def PlayerMove(playfield):
    placement = int(input("Where do you want to place you symbole ? : "))
    while CheckPlacement(playfield, placement) == False:
        placement = int(input("Where do you want to place you symbole, do not put a symobole on a taken area ? : "))
    playfield[placement] = "X"

def BotMove(playfield):
    bot = random.randint(0,8)

    while CheckPlacement(playfield, bot) == False:
        bot = random.randint(0,8)
    
    playfield[bot] = "O"

def Wins(playfield):    
    a = 0
    for i in range(len(playfield)):
        if playfield[i] != ".":
            a += 1
    if len(playfield) == a:
        return True
    
    if (playfield[0] == playfield[1] == playfield[2] and playfield[0] != "." or 
        playfield[3] == playfield[4] == playfield[5] and playfield[3] != "." or 
        playfield[6] == playfield[7] == playfield[8] and playfield[6] != "." or 
        playfield[0] == playfield[3] == playfield[6] and playfield[0] != "." or 
        playfield[1] == playfield[4] == playfield[7] and playfield[1] != "." or 
        playfield[2] == playfield[5] == playfield[8] and playfield[2] != "." or 
        playfield[0] == playfield[4] == playfield[8] and playfield[0] != "." or 
        playfield[2] == playfield[4] == playfield[6] and playfield[2] != "."):
        return True
    else:
        return False

def StartGame():
    playfield:list = [".",".",".",".",".",".",".",".","."]   
    winner:str = " "
    run:bool = True
    while run == True:
        PlayerMove(playfield)
        ShowPlayfield(playfield)

        if Wins(playfield) == True:
            winner = "Player"
            run = False
        else:
            BotMove(playfield)
            ShowPlayfield(playfield)
            if Wins(playfield) == True:
                winner = "Bot"
                run = False

    print(f"The {winner} won the game !")

StartGame()