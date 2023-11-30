import random
import math

def AskInt(message: str):
    while True:
        try:
            value: int = int(input(message))
            return value

        except:
            print("Please type a number and not a character")

def ShowPlayfield(playfield, tab_lenght):
    for i in range(len(playfield)):
        print('\n')
        print(playfield[i], end = " ")
    print('\n')
    print('______________________')
    print('\n')     

def IsEmptyCell(playfield, user_choice, tab_lenght):
    if 0 <= user_choice < len(playfield)*len(playfield):
            x:int = user_choice % tab_lenght
            y:int = user_choice // tab_lenght
            if playfield[y][x] == ".":
                return True
    return False

def PlayerMove(playfield, tab_lenght):
    user_choice:int = AskInt(f"Where do you want to place you symbole ? (between 1 and {len(playfield)*len(playfield)}): ")
    user_choice-=1
    while IsEmptyCell(playfield, user_choice, tab_lenght) == False:
        user_choice:int = AskInt("Where do you want to place you symbole, do not put a symobole on a taken area ? : ")
        user_choice-=1
    x:int = user_choice % tab_lenght
    y:int = user_choice // tab_lenght
    playfield[y][x] = "X"

def GetPlayfieldWinCombination(playfield, tab_lenght):
    lines: list[list[str]] = []
    # DIAGS

    diag1:list[str] = []
    diag2:list[str] = []

    for i in range(len(playfield)):
        diag1.append(i*len(playfield) + i)
    lines.append(diag1)
    for i in range(len(playfield)):
        diag2.append(len(playfield) - 1 - i + len(playfield)*i)
    lines.append(diag2)

    # Lines
    
    for i in range(len(playfield)):
        line_d:list[str] = []
        for j in range(len(playfield)):
            line_d.append(j + i*len(playfield))
        lines.append(line_d)

    # COL
    
    for i in range(len(playfield)):
        col:list[str] = []
        for x in range(len(playfield)):
            col.append(x*len(playfield) + i)
        lines.append(col)
    return lines

def GetIaMove(playfield:list, lines, letters:list = ["O", "X"]):
    for k in range(len(letters)):
        for i in range(len(playfield)):
            for j in range(len(playfield)):
                check = IsEmptyCell(playfield, i*len(playfield) + j, len(playfield))
                if check == True:
                    playfield[i][j] = letters[k]
                    res = TestWin(playfield, lines, letters[k])
                
                    if res == True:
                        playfield[i][j] = "."
                        return i*len(playfield) + j
                
                    playfield[i][j] = "."
    num:int = random.randint(0,len(playfield)*len(playfield))
    return num

def RandomPlacement(playfield):       
    num:int = random.randint(0,len(playfield)*len(playfield))
    return num

def IaMoveInitializer(playfield, tab_lenght, lines):
    ia:int = GetIaMove(playfield, lines)

    while IsEmptyCell(playfield, ia, tab_lenght) == False:
        ia = RandomPlacement(playfield)
        
    x:int = ia % tab_lenght
    y:int = ia // tab_lenght

    playfield[y][x] = "O"

def TestWin(playfield, lines, letter) -> bool:  
    for i in range(len(lines)):
        symbol_aligned_count = 0  
        for j in range(len(lines[i])):
            x:int = lines[i][j] % len(playfield)
            y:int = lines[i][j] // len(playfield)
            if playfield[y][x] == letter != ".":
                symbol_aligned_count += 1
        if symbol_aligned_count == len(playfield):
            return True
    return False
    
def Init():
    playfield:list[list[str]] = []
    tab_lenght: int = AskInt("What size of TicTacToe do you want ? : ")
    for i in range(0, tab_lenght):
        line: list[str] = []
        for j in range(0, tab_lenght):
            line.append(".")
        playfield.append(line)
    return playfield

def StartGame():
    playfield = Init()
    tab_lenght = len(playfield)
    winner:str = " "
    run:bool = True
    while run == True:
        PlayerMove(playfield, tab_lenght)
        ShowPlayfield(playfield, tab_lenght)
        lines:list[list[str]] = GetPlayfieldWinCombination(playfield, tab_lenght)
        if TestWin(playfield, lines, "X") == True:   
            winner = "Player"
            run = False
        else:
            counter = 0
            for i in range(len(playfield)):
                for j in range(len(playfield)):
                    if playfield[i][j] != ".":
                        counter += 1
            if counter == len(playfield)*len(playfield):
                print(f"It's a Tie !")
                return False
            IaMoveInitializer(playfield, tab_lenght, lines)
            ShowPlayfield(playfield, tab_lenght)
            if TestWin(playfield, lines, "O") == True: 
                winner = "Bot"
                run = False

    print(f"The {winner} won the game !")
    
StartGame()


'''for i in range(len(playfield)):
            for j in range(len(playfield)):
                check = CheckPlacement(playfield, playfield[i][j], len(playfield))
                if check == True:
                    playfield[i][j] = letters[k]
                    res = TestWin(playfield, lines, letters[k])
                    if res == True:
                        playfield[i][j] = "."
                        return playfield[i][j]
                        
                        
                        
                        
    for i in range(len(lines)):
            symbol_aligned_count:int = 0
            dot_count:int = 0
            for j in range(len(lines[i])):
                x:int = lines[i][j] % len(playfield)
                y:int = lines[i][j] // len(playfield)
                if playfield[y][x] == letters[k]:
                    symbol_aligned_count += 1
                elif playfield[y][x] == ".":
                    IaPlace:int = y*len(playfield) + x
                    dot_count +=1
            if symbol_aligned_count == len(playfield)-1 and dot_count == 1:
                return IaPlace'''