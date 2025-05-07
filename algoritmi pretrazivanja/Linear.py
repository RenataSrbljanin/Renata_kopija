


def postoji(lista, broj):
    lista=[]
    lista = map(int,input().split(","))
    lista=list(lista)
    bulijan=True
    while bulijan:
        broj = int(input())
        print(lista, broj)
        n=1
        for br in lista:
            if br==broj:
                print(f"Pogodili ste, trazeni broj je: {br}, {n}-i u listi {lista}")
                bulijan=False
                break
            else:
                n=n+1
        else:    
            print("broj nije pronadjen.")

def trazenjeReciUimenima(lista, cilj):
    for i in range(len(lista)):
        if lista[i]==cilj:
            return i
    return -1
    