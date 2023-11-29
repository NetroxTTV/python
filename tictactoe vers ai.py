import random

def AskInt(message: str):
    while True:
        try:
            value: int = int(input(message))
            return value

        except:
            print("Please type a number and not a character")

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
    placement:int = AskInt("Where do you want to place you symbole ? (between 1 and 9): ")
    placement-=1
    while CheckPlacement(playfield, placement) == False:
        placement:int = AskInt("Where do you want to place you symbole, do not put a symobole on a taken area ? : ")
        placement-=1
    playfield[placement] = "X"

def GetIaMove(playfield:list, lines, letters:list = ["O", "X"]):
    for x in range(len(letters)):
        for i in range(len(lines)): # 0 a 8
            symbol_aligned_count:int = 0
            dot_count:int = 0

            for j in range(len(lines[i])): ###### CHECK SI LIGNE PEUT ETRE GAGNANTE/BLOQUER
                if playfield[lines[i][j]] == letters[x]:
                    symbol_aligned_count += 1
                elif playfield[lines[i][j]] == ".": 
                    IaPlace:int = lines[i][j]
                    dot_count +=1

            if symbol_aligned_count == 2 and dot_count == 1: #### BLOQUE/WIN 
                playfield[IaPlace] = letters[x]
                if TestWin(playfield, lines) == True:
                    print("win")
                    playfield[IaPlace] = "."
                    return IaPlace
                return IaPlace
    num:int = random.randint(0,8)
    return num

def IaMoveInitializer(playfield, lines):

    bot:int = GetIaMove(playfield, lines)

    while CheckPlacement(playfield, bot) == False:
        counter = 0
        for i in range(len(playfield)):
            if playfield[i] != ".":
                counter += 1
            if counter == 9:
                return
        bot = GetIaMove(playfield, lines)
        
    
    playfield[bot] = "O"

def TestWin(playfield, lines) -> bool:    
    for i in range(len(lines)):
        if playfield[lines[i][0]] == playfield[lines[i][1]] == playfield[lines[i][2]] != ".":
            print(playfield[lines[i][0]], playfield[lines[i][1]] , playfield[lines[i][2]])
            return True
    return False
    

def StartGame():
    playfield:list = [".",".",".",".",".",".",".",".","."] 
    lines:list[list] = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]  
    winner:str = " "
    run:bool = True
    while run == True:
        PlayerMove(playfield)
        ShowPlayfield(playfield)

        if TestWin(playfield, lines) == True:
            winner = "Player"
            run = False
        else:
            IaMoveInitializer(playfield, lines)
            ShowPlayfield(playfield)
            if TestWin(playfield, lines) == True:
                winner = "Bot"
                run = False
        counter = 0
        for i in range(len(playfield)):
            if playfield[i] != ".":
                counter += 1
            if counter == 9:
                print(f"It's a Tie !")
                run = False
                return

    print(f"The {winner} won the game !")

StartGame()