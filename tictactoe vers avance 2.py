import random
import math

def ShowPlayfield(playfield, tab_lenght):
    for i in range(len(playfield)):
        print('\n')
        print(playfield[i], end = " ")
    print('\n')
    print('______________________')
    print('\n')     

def CheckPlacement(playfield, user_choice, tab_lenght):
    if 0 <= user_choice <= len(playfield)*tab_lenght:
            x:int = user_choice % tab_lenght
            y:int = user_choice // tab_lenght
            if playfield[y][x] == ".":
                return True
    return False

def PlayerMove(playfield, tab_lenght):
    user_choice:int = int(input(f"Where do you want to place you symbole ? (between 1 and {len(playfield)}): "))
    user_choice-=1
    while CheckPlacement(playfield, user_choice, tab_lenght) == False:
        user_choice:int = int(input("Where do you want to place you symbole, do not put a symobole on a taken area ? : "))
    x:int = user_choice % tab_lenght
    y:int = user_choice // tab_lenght
    playfield[y][x] = "X"

def GetPlayfieldLines(playfield, tab_lenght):
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

    line1:list[str] = []
    line2:list[str] = []
    line3:list[str] = []
    line4:list[str] = []

    for i in range(len(playfield)):
        line1.append(i)
    lines.append(line1)

    for i in range(len(playfield)):
        line2.append(i + len(playfield))
    lines.append(line2)

    for i in range(len(playfield)):
        line3.append(i + 2*len(playfield))
    lines.append(line3)

    for i in range(len(playfield)):
        line4.append(i + 3*len(playfield))
    lines.append(line4)

    # COL

    col1:list[str] = []
    col2:list[str] = []
    col3:list[str] = []
    col4:list[str] = []

    for i in range(len(playfield)):
        col1.append(i*len(playfield))
    lines.append(col1)

    for i in range(len(playfield)):
        col2.append(i*len(playfield) + 1)
    lines.append(col2)

    for i in range(len(playfield)):
        col3.append(i*len(playfield)+ 2)
    lines.append(col3)

    for i in range(len(playfield)):
        col4.append(i*len(playfield) + 3)
    lines.append(col4)
    return lines
    

def GetIaMove(playfield:list, lines, letters:list = ["O", "X"]):
    for k in range(len(letters)):
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
                return IaPlace
    num:int = random.randint(0,len(playfield)*len(playfield))
    print(num)
    return num

def IaMoveInitializer(playfield, tab_lenght, lines):
    ia:int = GetIaMove(playfield, lines)

    while CheckPlacement(playfield, ia, tab_lenght) == False:
        counter = 0
        ia = GetIaMove(playfield, lines)
        
    x:int = ia % tab_lenght
    y:int = ia // tab_lenght

    playfield[y][x] = "O"

def TestWin(playfield, lines, letter:str = ["O", "X"]) -> bool:  
    print("test win")
    for k in range(len(letter)):
        for i in range(len(lines)):
            symbol_aligned_count = 0  
            for j in range(len(lines[i])):
                    x:int = lines[i][j] % len(playfield)
                    y:int = lines[i][j] // len(playfield)
                    if playfield[y][x] == letter[k] != ".":
                        symbol_aligned_count += 1
            if symbol_aligned_count == len(playfield):
                return True
    return False
    

def StartGame():
    playfield:list[list[str]] = []
    tab_lenght: int = int(input("What size of TicTacToe do you want ? : "))
    for i in range(0, tab_lenght):
        line: list[str] = []
        for j in range(0, tab_lenght):
            line.append(".")
        playfield.append(line)
    print(playfield)
    winner:str = " "
    run:bool = True
    while run == True:
        PlayerMove(playfield, tab_lenght)
        ShowPlayfield(playfield, tab_lenght)
        lines = GetPlayfieldLines(playfield, tab_lenght)
        if TestWin(playfield, lines) == True:   
            winner = "Player"
            run = False
        else:
            IaMoveInitializer(playfield, tab_lenght, lines)
            ShowPlayfield(playfield, tab_lenght)
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