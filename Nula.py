n = int(input())
lista=[]
for i in range(n):
    x=int(input())
   
    lista.append(x)

#brojNula=lista.count(0)
pozitivna=0
#neutral=0
negativna=0

for i in range(1, len(lista)):
    if lista[i]==0:
        if lista[i-1]<0 and lista[i+1]>0 and i<len(lista):
            pozitivna=pozitivna+1
        elif lista[i-1]>0 and lista[i+1]<0 and i<len(lista):
            negativna=negativna+1
print(pozitivna,negativna)



# n, x=map(int, input().split())
