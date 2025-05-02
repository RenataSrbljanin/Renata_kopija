lista=[]
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))


def pomeranje_udesno(lista):
    newL=[lista[-1]]+lista[:-1]
    return newL

def pomeranje_ulijevo(lista):
    newL=lista[1:]+[lista[0]]
    return newL

def pomeranje_udesno_ili_ulijevo(lista):   
    if lista[0]%2==0:
        return pomeranje_udesno(lista)
    else:
        return pomeranje_ulijevo(lista)
    
def ispis_rezultata(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()
    
l=pomeranje_udesno_ili_ulijevo(lista)
ispis_rezultata(l)