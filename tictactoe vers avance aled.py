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
    placement:int = int(input("Where do you want to place you symbole ? (between 1 and 9): "))
    placement-=1
    while CheckPlacement(playfield, placement) == False:
        placement:int = int(input("Where do you want to place you symbole, do not put a symobole on a taken area ? : "))
    playfield[placement] = "X"

def GetIaMove(playfield:list, lines:list[list] = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]], letters:list = ["O", "X"]):
    for x in range(len(letters)):
        for i in range(len(lines)): # 0 a 8
            symbol_aligned_count:int = 0
            dot_count:int = 0
            for j in range(len(lines[i])): # 0 a 2
                if playfield[lines[i][j]] == letters[x]:
                    symbol_aligned_count += 1
                elif playfield[lines[i][j]] == ".": 
                    IaPlace:int = lines[i][j]
                    dot_count +=1
            if symbol_aligned_count == 2 and dot_count == 1:
                return IaPlace
    num:int = random.randint(0,8)
    return num

def IaMoveInitializer(playfield):
    bot:int = GetIaMove(playfield)

    while CheckPlacement(playfield, bot) == False:
        counter = 0
        for i in range(len(playfield)):
            if playfield[i] != ".":
                counter += 1
            if counter == 9:
                return
        bot = GetIaMove(playfield)
        
    
    playfield[bot] = "O"

def TestWin(playfield) -> str:    
    
    if (playfield[0] == playfield[1] == playfield[2] and playfield[0] != "." or 
        playfield[3] == playfield[4] == playfield[5] and playfield[3] != "." or 
        playfield[6] == playfield[7] == playfield[8] and playfield[6] != "." or 
        playfield[0] == playfield[3] == playfield[6] and playfield[0] != "." or 
        playfield[1] == playfield[4] == playfield[7] and playfield[1] != "." or 
        playfield[2] == playfield[5] == playfield[8] and playfield[2] != "." or 
        playfield[0] == playfield[4] == playfield[8] and playfield[0] != "." or 
        playfield[2] == playfield[4] == playfield[6] and playfield[2] != "."):
        return "win"
    else:
        return "lost"
    

def StartGame():
    playfield:list = [".",".",".",".",".",".",".",".","."]   
    winner:str = " "
    run:bool = True
    while run == True:
        PlayerMove(playfield)
        ShowPlayfield(playfield)

        if TestWin(playfield) == "win":
            winner = "Player"
            run = False
        else:
            IaMoveInitializer(playfield)
            ShowPlayfield(playfield)
            if TestWin(playfield) == "win":
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