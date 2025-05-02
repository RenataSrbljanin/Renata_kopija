n=int(input())
k=int(input())
x=int(input())

tekst="NE"
for i in range(n+1):
    if i*k== x:
        tekst="DA"
        break
print(tekst)