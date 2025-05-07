# log(n)+1

#lista=[2,4,6,8,10]

lista=[]
lista = map(int,input().split(","))
lista=list(lista) # !!!
cilj=int(input())

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


pozicija, korak, imaLi=binarno(lista, cilj)
print(pozicija, korak, imaLi)

# novicilj=int(input())
# koraci=0
# m=binarno(lista, novicilj)
# while m!=-1:
#     novicilj=int(input())
#     m=binarno(lista, novicilj)
#     print(m)
# print("m: ",m)
# print("koraci: ",koraci)

