ocjene=list(map(int, input().split()))

def prosjek(lista):
    return sum(lista)/len(lista)

def kolikoJedinica(lista):
    if lista.count(1)>0:
        return lista.count(1)
    
def kategoriraj(prosek,x):
    if x>=0:
        print("Nedovoljan! Imate negativnih ocena:", x)
    elif prosek >= 4.5: 
        print("Odlican!")
    elif prosek >= 3.5:
        print("Vrlo dobar!")
    elif prosek >= 2.5:
        print("Dobar")
    elif prosek>=1.5:
        print("Dovoljan")
    # else:
    #     print("Nedovoljan!")

print(prosjek(ocjene))
kategoriraj(prosjek(ocjene), ocjene.count(1))
#print(round(prosjek(ocjene),2))