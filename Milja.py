
lista=[1, 39370.1, 3280.84, 1093.61, 0.621371]

def konvertor(d,n,m):
    if n==1:
        if m==1:
            return d
        elif m==2:
            return d*lista[1]
        elif m==3:
            return d*lista[2]
        elif m==4:
            return d*lista[3]
        elif m==5:
            return d*lista[4]
    elif n==2:  
        if m==1:
            return d/lista[1]
        elif m==2:
            return d
        elif m==3:
            return d*lista[2]/lista[1]
        elif m==4:
            return d*lista[3]/lista[1]
        elif m==5:
            return d*lista[4]/lista[1]
    elif n==3:  
        if m==1:
            return d/lista[2]
        elif m==2:
            return d*lista[1]/lista[2]
        elif m==3:
            return d
        elif m==4:
            return d*lista[3]/lista[2]
        elif m==5:
            return d*lista[4]/lista[2]
    elif n==4:
        if m==1:
            return d/lista[3]
        elif m==2:
            return d*lista[1]/lista[3]
        elif m==3:
            return d*lista[2]/lista[3]
        elif m==4:
            return d
        elif m==5:
            return d*lista[4]/lista[3]
    elif n==5:
        if m==1:
            return d/lista[4]
        elif m==2:
            return d*lista[1]/lista[4]
        elif m==3:
            return d*lista[2]/lista[4]
        elif m==4:
            return d*lista[3]/lista[4]
        elif m==5:
            return d
        
d=int(input())
n=int(input())
m=int(input()) 
print(konvertor(d,n,m))