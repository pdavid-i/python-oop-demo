from Logic.crud import *
from Logic.functionalities import *
import copy

def printMenuUI():
    print("*****************************************************************************************************")
    print("0. Exit")
    print("1. Adauga o vanzare")
    print("2. Modifica o vanzare")
    print("3. Sterge o vanzare")
    print("4. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.")
    print("5. Modificarea genului pentru un titlu dat.")
    print("6. Determinarea prețului minim pentru fiecare gen.")
    print("7. Ordonarea vânzărilor crescător după preț.")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen.")
    print("9. Afisati toate vanzarile")
    print("10. Undo")
    print("*****************************************************************************************************")


def addVanzareUI(lista):
    id = input("Introduceti ID:")
    titlu = input("Introduceti Titlu:")
    gen = input("Introduceti Gen:")
    pret = input("Introduceti Pret:")
    tip_reducere = input("Introduceti Tip Reducere:")
    addVanzare(lista, id, titlu, gen, pret, tip_reducere)


def modificaVanzareUI(lista):
    id = input("Introduceti ID-ul cartii de modificat:")
    titlu = input("Introduceti Titlu nou:")
    gen = input("Introduceti Gen nou:")
    pret = input("Introduceti Pret nou:")
    tip_reducere = input("Introduceti Tip Reducere nou:")
    modificaVanzare(lista, id, titlu, gen, pret, tip_reducere)


def stergeVanzareUI(lista):
    id = input("Introduceti ID-ul cartii de sters:")
    return stergeVanzare(lista, id)

def discountReduceriUI(lista):
    discountReduceri(lista)
    showAllUI(lista)

def modificareGenUI(lista):
    titlu = input("Introduceti titlul de modificat:")
    gen = input("Introduceti noul gen:")
    modificareGen(lista, titlu, gen)

def pretMinimUI(lista):
    rezultat = pretMinim(lista)
    for gen in rezultat.keys():
        print("Gen {0}, Pret minim: {1}".format(gen, rezultat[gen]))

def ordonareCrescatorUI(lista):
    ordonareCrescator(lista)

def nrTitluriDistincteUI(lista):
    rezultat = nrTitluriDistincte(lista)
    for gen in rezultat.keys():
        print("Gen {0}, Numar Titluri: {1}".format(gen, rezultat[gen]))

def showAllUI(lista):
    if len(lista) == 0:
        print("Lista de vanzari este goala!")
    for vanzare in lista:
        print(vanzare)

def undo():
    pass

def runConsoleUI():
    vanzari = []
    vanzari_undo = []
    addVanzare(vanzari, "1", "200 de leghe sub mari", "Fantasy", 100, "gold")
    addVanzare(vanzari, "3", "In jurul pamantului in 80 de zile", "Fantasy", 90, "silver")
    addVanzare(vanzari, "2", "Calatorie in centrul pamantului", "Mister", 95, "none")

    while True:
        printMenuUI()
        optiune = int(input("Introduceti otpiunea dorita:"))
        if optiune == 0:
            break
        elif optiune == 1:
            vanzari_undo = copy.deepcopy(vanzari)
            addVanzareUI(vanzari)
        elif optiune == 2:
            vanzari_undo = copy.deepcopy(vanzari)
            modificaVanzareUI(vanzari)
        elif optiune == 3:
            vanzari_undo = copy.deepcopy(vanzari)
            vanzari = stergeVanzareUI(vanzari)
        elif optiune == 4:
            vanzari_undo = copy.deepcopy(vanzari)
            discountReduceriUI(vanzari)
        elif optiune == 5:
            vanzari_undo = copy.deepcopy(vanzari)
            modificareGenUI(vanzari)
        elif optiune == 6:
            pretMinimUI(vanzari)
        elif optiune == 7:
            vanzari_undo = copy.deepcopy(vanzari)
            ordonareCrescatorUI(vanzari)
        elif optiune == 8:
            nrTitluriDistincteUI(vanzari)
        elif optiune == 9:
            showAllUI(vanzari)
        elif optiune == 10:
            vanzari = copy.deepcopy(vanzari_undo)
        else:
            print("Optiune gresita")
