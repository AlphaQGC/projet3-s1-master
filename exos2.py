#DEBUT
def add(x,y):
    return x + y

def sub(x,y): 
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulo(x,y):
    return x % y
def SalaireParSeconde(Salairehorraire,heureparjourouvré,Nbjoursouvréparan):
     return (salairehorraire * heureparjourouvré * Nbjoursouvréparan) / (365*24*60*60)

def SalaireNet(Brut,coefficient):
    return brut - brut *coeff

#Definir une fonction divide avec comme parametre x et y
def divide2(x,y):
    #si y est egale a 0 
    if y == 0 :
        #alors renvoyer error
        print("error")
        #retourner vide
        return
    #sinon : il n'y a pas d'erreur
    else :
        #alors diviser x par y
        return x / y

def input():
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
