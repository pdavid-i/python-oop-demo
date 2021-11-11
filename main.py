def printMenu():
    print("********************")
    print("0. Iesi")
    print("1. Adauga o masina")
    print("2. Afiseaza masinile ")
    print("3. Sterge o masina ")
    print("********************")


def getOption():
    pass

def adaugaMasina(masini):
    nume = input("Nume:")
    model=input("Model:")
    motor=input("Motor:")
    masina = {
        "nume":nume,
        "model":model,
        "motor":motor
    }
    masini.append(masina)
    pass

def getNume(masina):
    return masina["nume"]


def afiseazaMasini(masini):
    print("++++++++++++++++")
    for masina in masini:
        print("Nume: " + masina["nume"] + ", Model:" + masina["model"] + ", Motor:" + masina["motor"])
    print("++++++++++++++++")

def stergeMasina(masini):
    de_sters = input("Introduceti masina de sters:")
    return [ masina for masina in masini if getNume(masina) != de_sters ]
    

def runMenu():
    masina1 = {
        "nume": "Dacia",
        "model": "Sandero",
        "motor": "1.6"
    }

    masina2 = {
        "nume": "Porsche",
        "model": "cayenne",
        "motor": "2.6"
    }

    masina3 = {
        "nume": "Renault",
        "model": "Laguna",
        "motor": "1.6"
    }

    masini = [masina1, masina2, masina3]
    while True:
        printMenu()
        optiune = int(input("Introduceti otpiunea dorita:"))
        print(optiune)
        if optiune == 0:
            break
        elif optiune == 1:
            adaugaMasina(masini)
        elif optiune == 2:
            afiseazaMasini(masini)
        elif optiune == 3:
            masini = stergeMasina(masini)
        else:
            print("Optiune gresita")

runMenu()