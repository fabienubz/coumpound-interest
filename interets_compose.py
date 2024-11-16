from PyQt6 import QtCore, QtWidgets, QtGui

while True:
    BASE_INVESTISSEMENT = input("Saisissez la valeur que vous voulez investir: ")

    try:
         BASE_INVESTISSEMENT = int(BASE_INVESTISSEMENT)
         if BASE_INVESTISSEMENT < 0:
             print("La valeur doit être supérieur à 0")
             
         else:
            print(f"Vous avez investis: {BASE_INVESTISSEMENT}€")
            break
            
    except ValueError :
        print("Veuillez saisir une valeur valide.")

        

while True:
    NOMBRE_ANNEE = input("Choisissez un nombre d'années a investir: ")

    try:
        NOMBRE_ANNEE = int(NOMBRE_ANNEE)
        if NOMBRE_ANNEE < 0:
            print("Veuillez saisir une valeur correct.")
        else:
            print(f"Vous voulez investir sur {NOMBRE_ANNEE} !")
            break
    
    except ValueError:
        print("Veuillez saisir un nombre.")

while True: 
    APY_MOYEN = input("Saisissez le rendement annuel espéré: ")

    try:
        print(f"Le rendement attendu est de {APY_MOYEN}% !")
        APY_MOYEN = int(APY_MOYEN)
        APY_MOYEN = APY_MOYEN / 100
        break
    
    except ValueError:
        print("Veuillez saisir une valeur valide !")

while True:
    INVEST = input("Voulez-vous réinvestir vos gains chaque années ? (Oui/Non)")
    if INVEST == "Oui":
        INVEST = 1
        print("Vous réinvestiré chaques années vos gains.")
        break
    elif INVEST == "Non":
        INVEST = 0
        print("Vous ne réinvestiré pas chaques années vos gains")
        break
    else:
        print("Veuillez saisir répondre par Oui ou Non.")

if INVEST == 1:
    RESULT = BASE_INVESTISSEMENT * ((1 + APY_MOYEN)**NOMBRE_ANNEE)
    print(RESULT)

elif INVEST == 0:
    RESULT = BASE_INVESTISSEMENT + ((APY_MOYEN * BASE_INVESTISSEMENT) * NOMBRE_ANNEE)
    print(RESULT)


