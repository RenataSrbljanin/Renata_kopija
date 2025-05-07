
# Linearno resenje:
n,m=map(int,input().split())
stabla = list(map(int, input().split()))
#lista=list(lista) # !!!
visina =max(stabla)
odrezano=0
while odrezano<m:
    visina =visina-1
    odrezano=0
    for i in range(n):
        if stabla[i]>visina:
            odrezano=odrezano+stabla[i]-visina
print(visina)


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