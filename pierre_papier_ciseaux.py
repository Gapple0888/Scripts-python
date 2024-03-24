import random

win = 0
loose = 0
draw = 0
game = 1

def choice():
        
    user_play = input("Choisissez-vous Pierre, Papier ou Ciseaux ? ")
    npc_play = random.choice(["Papier", "Pierre", "Ciseaux"])
    play(npc_play, user_play)
    

def play(npc_play, user_play):
    global win, loose, draw, game

    if user_play == "Papier":
        cissors(npc_play)
    elif user_play == "Pierre":
        rock(npc_play)
    else :
        paper(npc_play,)
    play_or_no = input("Souhaitez-vous continuer à jouer ? (Oui/Non) ")
    if play_or_no == "Oui":
        game = game + 1
        choice()
    else :
        print(f"Vous avez jouer un total de {game} parties pour {win} victoire(s), {loose} défaite(s) et {draw} match nul(s).")
        

def cissors(npc_play):
    global loose, win, draw

    if npc_play == "Pierre" :
        loose = loose + 1
        print("Vous avez perdu !")
    elif npc_play == "Papier":
        win = win + 1
        print ("Vous avez gagné !")
    else : 
        draw = draw + 1 
        print("Egalité !")


def paper(npc_play):
    global loose, win, draw

    if npc_play == "Ciseaux" :
        loose = loose + 1
        print("Vous avez perdu !")
    elif npc_play == "Pierre":
        win = win + 1
        print ("Vous avez gagné !")
    else : 
        draw = draw + 1 
        print("Egalité !")


def rock(npc_play):
    global loose, win, draw

    if npc_play == "Papier" :
        loose = loose + 1
        print("Vous avez perdu !")
    elif npc_play == "Ciseaux":
        win = win + 1
        print ("Vous avez gagné !")
    else : 
        draw = draw + 1 
        print("Egalité !")


if __name__ == "__main__":
    choice()