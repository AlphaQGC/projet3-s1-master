#DEBUT
#def SalaireNet(brut, coeff) :
    #return brut - brut *coeff

def SalaireParSeconde(salairehorraire,heureparjourouvré,Nbjoursouvréparan):
    #Calculer mon salaire annuel
    salaireAnnuel = salairehorraire * heureparjourouvré * Nbjoursouvréparan
    #Calculer le nombre de secondes dans une année
    nbSecondesParAn = 365 * 24 * 60 * 60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondesParAn
    return divide (salaireAnnuel,nbSecondesParAn)
    
    #return (salairehorraire * heureparjourouvré * Nbjoursouvréparan) / (365*24*60*60)


#Definir une fonction withdrawFees qui retire un pourcentage a un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Definir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent / 100)
    #soustraire fees a total
    result = total - fees
    #retourner la valeur obtenue
    return result



    
#Definir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteure d'activité (isPubluc > booleen)
def calculBrutenNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur public
    if isPublic :
        #Alors je soustrais 15% de mon salaire Brut à mon salaire Brut et je l'assigne a la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * (15 / 100))
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : Je suis un travailleur du secteur privé
    else :
        #Alors je soustrais 23% de mon salaire brut à mon salaire brut et je l'assigne a la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * (15 / 100))
        salaireNet = withdrawFees(salaireBrut, 23)
    
    
    #Retourner salaireNet
    return salaireNet

#exercice 1
#Faire une fonction qui concatene 2 chaines de caractere, les separer
def concaWithComa(strA, strB):
    #Je m'assure que strA soit bien de type str
    stringfieldA = str(strA)
    #Je m'assure que strB soit bien de type str
    stringfieldB = str(strB)
    #retourne stra + ',' + strb
    return strA + ", "+ strB
concaWithComa(23,"toto") #retourne "23, toto"

#exercice 2
#faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensembles des occurences d'un chiffre e.g :
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7"n'hesitez pas a implementer la premiere fonction
tableau = [0,1,1,1,0,1,1,0,1]
#Definir la fonction findIndex qui itere sur tableau cherchant l'index
def findIndex (x, tableau):
#des differentes occurences de x
    #definir i un index de depart
    i = 0
    #definir chaineRetour telle qu'une chaine de caractere vide
    chaineRetour = ""
    #Je defini un boolen tel que firstTurn est true
    firstTurn = True
    #Tant que i est different du nombre d'elt dans le tableau
    while (i != len(tableau)) :
        #alors j'attribue a une variable la valeur de tableau a l'index i
        selected = tableau[i]
        
        #Si selected est egal a x ET que firstTurn est true
        if selected == x and firstTurn == True
            #Alors on assigne a chaineRetour le retour str(i)
            
            #changer la valeur de firstTurn a false
        #Sinon si selected est egal a x
        if selected == x :
            #Alors j'appelle concaWithComma tel que : concaWithComma(chaineRetour, i)
            concaWithComa(chaineRetour, i)
        #j'incremente i de 1 
        i = i + 1
    #Retourne la chaine retour
    return chaineRetour


#definir mon index
i = 0
while (i != len(tableau)):
    selected = tableau[i]
    i = i + 1



#FIN