import keyboard
import random
import time
import os


def decimal(question: str):
    while True:
        answer: str = input(question)
        if answer.isdecimal():
            deci: int = int(answer)
            return deci
        else:
            print("please choose a number and not a letter")
            continue

def ask_replay():
    while True:
        replay:int=decimal("Do you want to replay ? Choose 1 to replay and 2 to stop the game ")
        if replay == 1 :
            return True
        elif replay == 2 :
            return False
        else :
            print("Please choose 1 or 2 : 1 to replay and 2 to stop the game :  ")

def generer_grille(N:int):
    playfield:list = []
    for i in range(N):
        ligne:list = []
        for j in range(N):
            ligne.append(".")
        playfield.append(ligne)
    return playfield

def afficher_grille(playfield:list[list]):
    print('___________')
    print('\n')  
    for i in range(len(playfield)):
        for j in range(len(playfield)):
            print(playfield[i][j], end = " ")
        print('\n')
    print('___________')
    print('\n')       
    
def generer_nombre():
    return 2 if random.random() < 0.9 else 4

def aleatoire_placement(playfield:list[list], nombre):
    check:bool = True
    if_plein = 0
    for y in range(len(playfield)):
        for x in range(len(playfield)):
            if playfield[x][y] != ".":
                if_plein += 1
    if if_plein == len(playfield)*len(playfield):
        return True
    while check == True:
        x_random:int = random.randint(0, len(playfield)-1)
        y_random:int = random.randint(0, len(playfield)-1)
        if is_empty(playfield[y_random][x_random]) == True:
            playfield[y_random][x_random] = nombre
            check = False
    return True

def is_empty(slot):
    if slot==".":
        return True
    else:
        return False

def Check_Lost_Win(playfield:list[list]):
    for y in range(len(playfield)):
        for x in range(len(playfield)):
            if playfield[x][y] == 2048:
                print("gg")
                return True
            if playfield[y][x] == ".":
                    return False
            if y < len(playfield)-1: 
                if playfield[y][x] == playfield[y+1][x]:
                    return False
            if x < len(playfield)-1:
                if playfield[y][x] == playfield[y][x+1]:
                    return False
    print("rip")
    if ask_replay() == True :
        init()
    else:
        return True
    

def right(playfield:list[list]):
    for y in range(len(playfield)): # abscisse Y
        
        double_coup_checker:int = 0

        for x in range(1, len(playfield)): # abscisse X

            for i in range(1, len(playfield)): # Décalage a droite
                if playfield[y][len(playfield) - i] == ".":
                    playfield[y][len(playfield)-i] = playfield[y][len(playfield)-1-i] 
                    playfield[y][len(playfield)-1-i] = "."

            if double_coup_checker == 0:
                for i in range(1, len(playfield)):
                    w, ind = distance(playfield, "right", x, y)
                    if w == True:
                        playfield[y][x+ind] == playfield[y][x]
                        double_coup_checker = 1
                    
                    elif playfield[y][len(playfield)-i] == playfield[y][len(playfield)-i-1] != ".":
                        playfield[y][len(playfield)-i] = playfield[y][len(playfield)-i-1]*2
                        playfield[y][len(playfield)-i-1] = "."
                        double_coup_checker = 1
        
def left(playfield:list[list]):
    for y in range(len(playfield)): # abscisse Y
                
        double_coup_checker:int = 0

        for x in range(1, len(playfield)): # abscisse X

            for i in range(1, len(playfield)): # Décalage a gauche
                if playfield[y][i-1] == ".":
                    playfield[y][i-1] = playfield[y][i]
                    playfield[y][i] = "."

            if double_coup_checker == 0:

                w, ind = distance(playfield, "left", x, y)
                if w == True:
                    playfield[y][x-ind] == playfield[y][x]
                    double_coup_checker = 1
                            
                elif playfield[y][x-1] == playfield[y][x] != ".":
                        playfield[y][x-1] = playfield[y][x]*2
                        playfield[y][x] = "."
                        double_coup_checker = 1
                   
def down(playfield:list[list]):
    for y in range(1, len(playfield)): # abscisse Y
        double_coup_checker:int = 0
        for x in range(len(playfield)): # abscisse X
            for i in range(1, len(playfield)): # Décalage en bas
                    if playfield[len(playfield) - i][x] == ".":
                        playfield[len(playfield) - i][x] = playfield[len(playfield) - i - 1][x]
                        playfield[len(playfield) - i - 1][x] = "."
            
            if double_coup_checker == 0:
                    w, ind = distance(playfield, "left", x, y)
                    if w == True:
                        playfield[y+ind][x] == playfield[y][x]
                        double_coup_checker = 1
                                
                    elif playfield[len(playfield) - y][x] == playfield[len(playfield) - y - 1][x] != ".":
                        playfield[len(playfield) - y][x] = playfield[len(playfield) - y - 1][x]*2
                        playfield[len(playfield) - y - 1][x] = "."
                        double_coup_checker = 1
                        
def up(playfield:list[list]):
    for y in range(1, len(playfield)): # abscisse Y
        double_coup_checker:int = 0
        for x in range(len(playfield)): # abscisse X
            for i in range(1, len(playfield)): # Décalage en haut
                    if playfield[i-1][x] == ".":
                        playfield[i-1][x] = playfield[i][x]
                        playfield[i][x] = "."

            if double_coup_checker == 0:
                    w, ind = distance(playfield, "left", x, y)
                    if w == True:
                        playfield[y-ind][x] == playfield[y][x]
                        double_coup_checker = 1
                                
                    elif playfield[y-1][x] == playfield[y][x] != ".":
                        playfield[y-1][x] = playfield[y][x]*2
                        playfield[y][x] = "."
                        double_coup_checker = 1
                
def console(playfield:list, sens:str):
        if sens == "right":
            right(playfield)
        if sens == "left":
            left(playfield)
        if sens == "down":
            down(playfield)
        if sens == "up":
            up(playfield)
        check_if_lost = Check_Lost_Win(playfield)
        if check_if_lost == True:
            return False
        for i in range(2):
            res = aleatoire_placement(playfield, generer_nombre())
        #os.system('cls')
        afficher_grille(playfield)
        
        return res

def verif_str(content):
        
        if type(content) == str :
            return True
        else :
            return False

def distance(playfield:list, sens:str, x:int, y:int) -> tuple[bool, int]:
    if sens == "right" :        
        for i in range(len(playfield)):
            if verif_str(playfield[y][i]) == True:
                if playfield[y][i].find(".") == ".":
                    for ind in range(len(playfield)):
                        if playfield[y][x] == playfield[y][x+ind] :
                            return True , ind
                        else :
                            return False, -1
                else :
                    return False, -1
            else :
                    return False , -1
    
    if sens == "left" :        
        for i in range(len(playfield)):
            if verif_str(playfield[y][i]) == True:
                if playfield[y][i].find(".") == ".":
                    for ind in range(len(playfield)):
                        if playfield[y][x] == playfield[y][x-ind] :
                            return True , ind
                        else :
                            return False , -1
                else :
                    return False , -1
            else :
                    return False , -1

    if sens == "down" :        
        for i in range(len(playfield)):
            if verif_str(playfield[y][i]) == True:
                if playfield[y][i].find(".") == ".":
                    for ind in range(len(playfield)):
                        if playfield[y][x] == playfield[y+ind][x] :
                            return True , ind
                        else :
                            return False , -1
            
                else :
                    return False, -1
            else :
                return False, -1
                
    if sens == "up" :        
        for i in range(len(playfield)):
            if verif_str(playfield[y][i]) == True:
                if playfield[y][i].find(".") == ".":
                    for ind in range(len(playfield)):
                        if playfield[y][x] == playfield[y-ind][x] :
                            return True , ind
                        else :
                            return False , -1
                else :
                    return False , -1
            else :
                    return False , -1

def init():
    playfield:list = generer_grille(int(input("send the grid size : ")))
    x_random:int = random.randint(0, len(playfield)-1)
    y_random:int = random.randint(0, len(playfield)-1) 
    playfield[y_random][x_random] = generer_nombre()
    play:bool = True
    while play == True:
        if keyboard.is_pressed("right arrow"):
            play = console(playfield, "right")
            time.sleep(0.1)
        elif keyboard.is_pressed("left arrow"):
            play = console(playfield, "left")
            time.sleep(0.1)
        elif keyboard.is_pressed("down arrow"):
            play = console(playfield, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("up arrow"):
            play = console(playfield, "up")
            time.sleep(0.1)

init()