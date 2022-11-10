#DEBUT

#Definir game une fonction qui est un pierre feuille papier ciseau 
    #on creer une liste choixJeu qui contient les 4 choix du jeu donc : pierre, papier, ciseau
    #on creer une variable pointJoueur qui est egale a 0 
    #on creer une variable pointOrdinateur qui est egale a 0
    #Tant que pointJoueur ou pointOrdianteur est != 3 
        #alors
        #on creer une autre variable iaChoix qui est egale a un random de la liste choixJeu
        #on creer une variable monChoix en input
        #on renvoie le contenu de la variable iaChoix pour connaitre le choix de l'ordinateur
        #Si mon choix != iaChoix
            #alors verifier les reponses 
            #Si monChoix == "papier" et que iaChoix != "ciseau"
                #alors on ajoute un point au joueur
                #Sinon on ajoute un point à l'ordinateur
            #Si monChoix == "pierre" et iaChoix != "papier"
                #alors on ajoute un point au joueur
                #Sinon on ajoute un point à l'ordinateur
            #Si monChoix == "ciseau" et iaChoix != "pierre"
                #alors on ajoute un point au joueur
                #Sinon on ajoute un point à l'ordinateur
        #Sinon renvoyer "égalité pour ce tour, recommencer !"


#FIN