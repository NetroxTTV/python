import random

def jeu(tentative):
    tab = ["trace", "creer", "jouer", "lucas", "amour", "avoir", "monde", "poule", "foule"]
    word = random.randint(1, len(tab))
    hidden_word = tab[word]
    lg_mot = len(hidden_word)
    while tentative > 0:
        mot_joueur = input("Donne un mot de longueur " + str(lg_mot) + " : ")
        while len(mot_joueur) > len(hidden_word) or len(mot_joueur) < len(hidden_word):
            print("mot n'a pas ", lg_mot, "caracteres")
            mot_joueur = input("Donne un mot de longueur " + str(lg_mot) + " : ")
    
        print_word = []
        for i in range(lg_mot):    
            if hidden_word[i] == mot_joueur[i]:
                print_word.append("\033[92m" + mot_joueur[i] + "\033[0m ")
            elif mot_joueur[i] in hidden_word:
                print_word.append("\033[91m" + mot_joueur[i] + "\033[0m ")
            else:
                print_word.append("\033[90m" + mot_joueur[i] + "\033[0m ")
        word_a = ""
        for i in range(len(print_word)):
            word_a = word_a + print_word[i]            
        
        tentative -= 1
        print(f"{word_a}\n Tu as {tentative} tentatives restantes\n")

        if hidden_word == mot_joueur:
            print("you won")
            return 
    return
tentative = 10
jeu(tentative)