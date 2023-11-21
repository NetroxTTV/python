import random

def jeu(tentative):
    tab = ["a", "meow", "grrrr", "imagine", "osu"]
    pew = random.randint(1, len(tab))
    mot_cache = tab[pew]
    print(mot_cache)
    lg_mot = len(mot_cache)
    while tentative > 0:
        mot_joueur = input("Donne un mot de longueur " + str(lg_mot) + " : ")
        while len(mot_joueur) > len(mot_cache) or len(mot_joueur) < len(mot_cache):
            print("mot n'a pas ", lg_mot, "caracteres")
            mot_joueur = input("Donne un mot de longueur " + str(lg_mot) + " : ")
    
        a = 0
        b = 0
        temp_base = []
        for i in range(lg_mot):    
            if mot_cache[i] == mot_joueur[i]:
                a = a+1
            elif mot_cache[i] in mot_joueur:
                b = b + 1
                
                    
        if a == lg_mot:
                print("tu as trouvé le mot")
                return
        else:
                print("tu as", a, "lettre de a la bonne place")
                print("tu as", b, "lettre de a la mauvaise place")
                print("tu as", tentative-1 , "tentative restantes")
                tentative = tentative - 1
    print("perdu")
    return

tentative = 10
jeu(tentative)
