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
    #variable compteur 
    compteur = 0
    #Tant que :  x n'est pas egale au string que a renvoyé input
    while x != lettre :
        #rappeler input
        lettre = input()
        # on ajoute 1 à compteur a chaque fois que input est rappeler 
        compteur = compteur + 1
    #input est egale à x
    if lettre == x :
        #alors renvoyer un message victoire
        print("victoire")
        #retourner vide
        return compteur 

jeu(a)
#FIN