import random



def AskInput(message: str, allowed_inputs: list[str]) -> str:
    choice = input(message)
    for i in range(len(allowed_inputs)):
        if choice == allowed_inputs[i]:
            return choice
        else:
            print("lit stp")

def game():
    verif_return: bool = True
    moves_dict = {'r': 0, 'p': 1, 's': 2}
    moves = ['rock', 'paper', 'scissors']
    result: list[list[str]] = \
        [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2],
        ]

    end_message: list[str] = \
        [
            "Computer wins",
            "Player wins",
            "It's a draw"
        ]
    
    while verif_return == True:
        player_input: str = AskInput('Let\'s play a game.\n\nR for Rock.\nP for Paper.\nS for Scissors.\nMake a move : ', ["r", "p", "s"])
        computer_choice = random.randint(0, 2)
        player_choice = moves_dict[player_input]
        print('The player choose :', moves[player_choice])
        print('The computer choose', moves[computer_choice])
        print(end_message[result[player_choice][computer_choice]])
        verif_return = Restart()


def Restart():
    
    while len(nb_game) < 3 :
        restart:str = input("Do you want to restart ? (Yes/No)")
        if restart =='Yes' or restart == "y":
            nb_game.append("")
            
            return True
        else:
            return False
nb_game = []
game()

