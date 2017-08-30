import sys
def oper(param1,param3):
    global montant
    global Type
    param1 = param1 / 100
    param2 = montant * param1
    montant = montant - param2
    print("le montant est: ",param3)
    print(Type,taux," = ",param1)
    print("la valeur de ",Type,"est : ",param2)
    print("Résultat = ",montant)
    return
def tva(param1):
    global montant
    param1=montant
    tva=int(input("entrer le taux de la tva : "))
    tva= tva/100
    print("le taux de la tva = ",tva)
    print("la valeur de la tva = ",param1*tva)
    param1= param1*(1+tva)
    print("le montant ttc = ",param1)
    return
while True:
    montant=int(input("entrer le montant : "))
    while True:
        answer=input("des remises ?? [oui/non]")
        if answer =="oui" or answer=="OUI":
                    Type = input("type de remise : ")    
                    taux = int(input("taux de remise: "))
                    oper(taux,montant)
        else:
            pass;
        answer=input("d'autres remises ? [oui/non] : ")
        if answer =="oui" or answer=="OUI":
            pass;
        if answer=="non" or answer=="NON":
            break;
    tva(montant)
    answer=input("d'autres facture a faire ?? [oui/non] : ")
    if answer=="oui" or answer=="OUI":
        pass;
    if answer=="non" or answer =="NON":
        sys.exit()
