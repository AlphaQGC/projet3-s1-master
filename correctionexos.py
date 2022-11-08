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







#FIN