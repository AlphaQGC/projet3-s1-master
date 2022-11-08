#DEBUT
#def input():
    #renvoie un caractere de type string au hasard

#Exercice :
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere
    # le caractere doit etre parametrable

#Definir jeu avec comme parametre x
def jeu(x):
    #appeler input et l'assigné dans une variable
    lettre = input("devine la lettre :")
    #variable compteur = 0
    compteur = 0
    #Tant que :  x n'est pas egale au string que a renvoyé input
    while x != lettre :
        #rappeler input
        lettre = input()
        # on ajoute 1 à compteur a chaque fois que input est rappeler 
        compteur = compteur + 1
        #retourner compteur
        print(compteur)
    
    #alors renvoyer un message victoire
    print("victoire")
    return 

#CORRECTION

#je definis un mini jeu
def miniJeux(x):
    compteur = 0
    #je definis une variable y qui sera le input
    lettre = input ("Devine la lettre")
    #tant que y est different de x
    while y!= x :
        #ajouter 1 au compteur
        compteur = compteur + 1
        #afficher le compteur
        print(compteur)
        #Alors j'appelle un nouveau y 
        lettre = input("Devine la lettre")
    #lorsque la variable y est egale a la variable x alors
    print("reussi")


#FIN

