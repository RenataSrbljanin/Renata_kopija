def povecaj_za_jedan(n):
    return n+1
def aktivnost_2(n):
    if n%2==0:
        return povecaj_za_jedan(n)
    else: return n-1

def aktivnost_3(n):
    n=str(n)
    n=list(n)
    jedinica=n[-1]    
    return jedinica

def aktivnost_4(n):
    if type(n)!="str":      
    
        n=str(n)
        n=list(n)
        x=n[len(n)-1]
        y=n[len(n)-2]
        n[len(n)-2]=x
        n[len(n)-1]=y
   
n=int(input())
k=int(input())
for i in range(k):
    ai=int(input())
if ai==1:
    print(povecaj_za_jedan(n))
elif ai==2:
    print(aktivnost_2(n))
elif ai==3:
    print(aktivnost_3(n))
elif ai==4:
    print(aktivnost_4(n))

# nije uradjena!!!
