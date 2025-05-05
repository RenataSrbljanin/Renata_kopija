
def mnozitelj(a,b):
    if a%2==0:
        if b%2==0:
            return 2
        else:
            return 1
    else:
        if b%2==0:
            return 4
        else:
            return 3
n=int(input())
x=int(input())
z=int(input())
lista=[]
# mnozitelji=[]
# brojPredjenihStanica=[]
racuni=[]
for i in range(z):
    stanica,kartica,senzor = map(int, input().split())
    lista.append((kartica,stanica,senzor))

lista.sort()

for i in range(0, len(lista), 2):
   # print(lista[i], lista[i+1])
    # brojPredjenihStanica.append(lista[i+1][1]-lista[i][1])
    # mnozitelji.append(mnozitelj(lista[i][2],lista[i+1][2]))
    racuni.append((lista[i+1][1]-lista[i][1])*x*mnozitelj(lista[i][2],lista[i+1][2]))
# print(brojPredjenihStanica)
# print(mnozitelji)

print(sum(racuni))