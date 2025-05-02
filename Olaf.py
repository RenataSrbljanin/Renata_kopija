

##for i in range(n):
##    smer=str(input())
##    duzina=int(input())
##    if smer=="L":
##        x=x-duzina
##        if x<0:
##            x=0
##    else: x=x+duzina
##    ud=ud+x
##print(ud)

ud=0
n, x=map(int, input().split())
pocetna=x
for i in range(n):
    smer=str(input())
    duzina=int(input())
##    if smer=="L":
##        x=x-duzina
##        if x<0:
##            x=0
##    else: x=x+duzina
ud=ud+duzina
ud=ud+(x-pocetna)   
print(ud)


