import random 

def juste_prix(price, win, count, tentatives, essais):

    count = 1
    user_try = 0.1
    while price != user_try :
        user_try = int(input("Selon vous, quel est le prix de cet ojet ? "))
        if price < user_try :
            print("C'est moins !")

        elif price != user_try:
            print("C'est plus !")
        tentatives = tentatives + 1
    print(f"Bravo ! Vous avez trouvez le bon résultat en {tentatives} tentatives")
    win = win+1
    counter(tentatives, count, win, price, essais)
    

def counter(tentatives, count, win, price, essais): 

    essais = essais + tentatives 
    play = input("Souhaitez-vous continuer de jouer ? (Oui/Non)")
    if play == "Oui":
        price = random.randint(0, 5)
        count = count+1
        tentatives = 0
        juste_prix(price, win, count, tentatives, essais)
    elif play == 'Non' : 
        print(f"Voici vos résultats : vous avez trouvé le juste prix {win} fois avec un total de {essais} tentatives")



if __name__ =='__main__':
    win = 0
    count = 1
    tentatives = 0
    essais = 0
    price = random.randint(0, 5) 
    juste_prix(price, win, count, tentatives, essais)

# win = 0, count = 1, price = 0,1,2,3,4,5 
#user_try = le nombre choisit par le joueur
#tentatives = le nombre de tentatives réalisées
#win = 1 
#