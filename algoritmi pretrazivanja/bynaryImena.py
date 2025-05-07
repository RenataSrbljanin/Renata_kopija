# "Agata", "Jovica", "Perica", "Marica", "violeta"
# Agata Jovica Perica Marica Violeta
lista=[]
lista = map(str, input().split())
lista=list(lista) # !!!
lista.sort()
cilj=input()

def binarno(lista, cilj):
    levo=0  # lijevaGranicaIndex
    desno=len(lista)-1  # desnaGranicaIndex
    korak =0
    while levo <= desno:
        korak +=1
        sredina= (levo+desno)//2
        if lista[sredina]==cilj:
            return sredina,korak,True
        elif lista[sredina]<cilj:
            levo=sredina+1
        else:
            desno=sredina-1
    return -1, -1, False

print(lista)
pozicija, korak, imaLi=binarno(lista, cilj)
print(pozicija, korak, imaLi)