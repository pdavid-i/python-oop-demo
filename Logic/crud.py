from Domain.Vanzare import Vanzare

def addVanzare(lista, id, titlu, gen, pret, tip_reducere):
    vanzare_noua = Vanzare(id, titlu, gen, pret, tip_reducere)
    lista.append(vanzare_noua)

def modificaVanzare(lista, id, titlu_nou, gen_nou, pret_nou, tip_reducere_nou):
    for vanzare in lista:
        if vanzare.getId() == id:
            vanzare.setTitlu(titlu_nou)
            vanzare.setGen(gen_nou)
            vanzare.setPret(pret_nou)
            vanzare.setTipReducere(tip_reducere_nou)

def stergeVanzare(lista, id):
    return [ vanzare for vanzare in lista if vanzare.getId() != id]
    