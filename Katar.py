n=int(input())
x=int(input())

klime=[0]*n

for i in range(x):
    k=int(input())
    if i%2==0:
        klime[k-1]=1
    else:
        klime[k-1]=0
suma=sum(klime)
print(suma)
preostalo = n-suma
if x%2 ==0:
    print(preostalo*2-1)
else:
    print(preostalo*2)

