#DEBUT

#On admet que la fonction random renvoie une donnée au hasard
#On admet que la fonction input qui nous permet de demander à l'utilisateur une réponse
#Definir game une fonction qui est un pierre papier ciseau 
    #on creer un tableau choixJeu qui contient les 3 choix du jeu donc : "pierre", "papier", "ciseau"
    #on creer une variable pointJoueur qui est egale a 0 
    #on creer une variable pointOrdinateur qui est egale a 0
    #Tant que pointJoueur ou pointOrdianteur est different de 3 
        #alors on creer une variable iaChoix qui est egale a un random de 1 à 3 de l'index du tableau choixJeu 
        #on creer une variable monChoix en utilisant la fonction input avec en description les differentes réponse possible pour le joueur qui sont : "pierre", "papier", "ciseau" et assigne a notre variable monChoix le retour de l'execution de la fonction input
        #on affiche le contenu de la variable iaChoix pour connaitre le choix de l'ordinateur
        #Si mon choix est different de iaChoix
            #alors
            #Si monChoix est identique à "papier" et que iaChoix est different de "ciseau"
                #alors on ajoute un point au joueur
                #Sinon on ajoute un point à l'ordinateur
            #Sinon si monChoix est identique à "pierre" et iaChoix est different de "papier"
                #alors on ajoute un point au joueur
                #Sinon on ajoute un point à l'ordinateur
            #Sinon si monChoix est identique à "ciseau" et iaChoix different de "pierre"
                #alors on ajoute un point au joueur
                #Sinon on ajoute un point à l'ordinateur
        #Sinon renvoyer "égalité pour ce tour, recommencez !" à l'utilisateur 
    #Si pointJoueur egale à 3
        #alors on renvoie "Vous avez gagné ! :)"
    #Sinon on renvoie "Vous avez perdu ! :("

#Executer la fonction game pour lancer le pierre, papier, ciseau
#FIN