#DEBUT

#On admet que la fonction random renvoie une donnée au hasard
from random import *
#On admet que la fonction input qui nous permet de demander à l'utilisateur une réponse

#Definir game une fonction qui est un pierre papier ciseau
def game (): 
    #on creer un tableau choixJeu qui contient les 3 choix du jeu donc : "pierre", "papier", "ciseau"
    choixJeu = ["pierre","papier","ciseau" ]
    #on creer une variable pointJoueur qui est egale a 0
    pointJoueur = 0 
    #on creer une variable pointOrdinateur qui est egale a 0
    pointOrdinateur = 0
    #Tant que pointJoueur ou pointOrdianteur est different de 3 
    while (pointJoueur != 3) or (pointOrdinateur != 3) :
        #alors on creer une variable iaChoix qui est egale a un random de 1 à 3 de l'index du tableau choixJeu
        iaChoix = choice(choixJeu) 
        #on creer une variable monChoix en utilisant la fonction input avec en description les differentes réponse possible pour le joueur qui sont : "pierre", "papier", "ciseau" et assigne a notre variable monChoix le retour de l'execution de la fonction input
        monChoix = input("Choisir une des réponses suivantes :pierre, papier, ciseau : " )
        #on affiche le contenu de la variable iaChoix pour connaitre le choix de l'ordinateur
        print(iaChoix)
        #Si mon choix est different de iaChoix
        if monChoix != iaChoix :
            #alors
            #Si monChoix est identique à "papier" et que iaChoix est different de "ciseau"
            if (monChoix == "papier") and (iaChoix != "ciseau"):
                #alors on ajoute un point au joueur
                pointJoueur = pointJoueur + 1
                print("vous avez gagné ce tour, bien joué !")
                #Sinon on ajoute un point à l'ordinateur
            
            #Sinon si monChoix est identique à "pierre" et iaChoix est different de "papier"
            elif (monChoix == "pierre") and (iaChoix != "papier") :
                #alors on ajoute un point au joueur
                pointJoueur = pointJoueur + 1
                print("vous avez gagné ce tour, bien joué !")
                #Sinon on ajoute un point à l'ordinateur
                
            #Sinon si monChoix est identique à "ciseau" et iaChoix different de "pierre"
            elif (monChoix == "ciseau") and (iaChoix != "papier") :
                #alors on ajoute un point au joueur
                pointJoueur = pointJoueur + 1
                #Sinon on ajoute un point à l'ordinateur
            else :
                pointOrdinateur = pointOrdinateur + 1
                print("vous avez perdu ce tour, pas de chance !")
            #Si pointJoueur egale à 3
            if pointJoueur == 3 :
                #alors on renvoie "Vous avez gagné ! :)"
                return "Vous avez gagné ! :)"
            #Sinon on renvoie "Vous avez perdu ! :("
            elif pointOrdinateur == 3 :
                return "Vous avez perdu ! :("
        #Sinon renvoyer "égalité pour ce tour, recommencez !" à l'utilisateur 
        else :
            print("égalité pour ce tour, recommencez !")
   

#Executer la fonction game pour lancer le pierre, papier, ciseau
print(game())
#FIN