n=int(input())
x=int(input())

lista = []

for i in range(n):
    p=int(input())-1
    lista.insert(p,(i+1))  
    
#print(lista)   
for i in range(len(lista)-1):
    if lista[i] == x:
        print(i+1)
        break