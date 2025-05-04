
def prost(n):
    n=int(n)
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def dajProste(n):
    n=int(n)
    s=str(n)
    s=list(s)
    lista=[]
    for i in s:
        i=int(i)
        if prost(i)==True:
            lista.append(i)
    return lista
def baremDve_DajuZbroj_11(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if int(lista[i])+int(lista[j])==11:
                return True
    return False

def o1(n):
    m=str(n)
    m=list(m)
    if m.count("8")==3:
        x= n//2    
        return (True, x)
    else:
        return (False, n)
def o2(n):
    if n>=1000:
        x=n-500
        return (True, x)
    else:
        return (False, n)        
def o3(n):
    lista=dajProste(n)
   # print(lista, sum(lista))
    
    if len(lista)>=2:
        x=n+sum(lista)
        if x<10000:
            return (True, x)
        else:
            return (False, n)
    else:
        return (False, n)
def o4(n):
    s=str(n)
    s=list(s) 
    if baremDve_DajuZbroj_11(s):
        suma=0
        for i in s:
            suma+=int(i) 
        r=n*suma
        if r<10000:
            return (True, r)
        else:
            return (False, n)         
    else:
        return (False, n)   
def o5(n):
    z=n+1
    if z<10000:
        return (True, z)
    else:   
        return (False, n)    

def jedanKrug(n):
    (bulijan,x1)=o1(n)
    if bulijan==True:
       # print("o1: ",x1)
        return x1
    else:
        (bulijan,x2)=o2(n)
        if bulijan==True:
           # print("o2: ",x2)
            return x2
        else:
            (bulijan,x3)=o3(n)
            if bulijan==True:
              #  print("o3: ",x3)
                return x3
            else:
                (bulijan,x4)=o4(n)
                if bulijan==True:
                  #  print("o4: ",x4)
                    return x4
                else:
                    (bulijan,x5)=o5(n)
                   # if bulijan==True: 
                     #   print("o5:", x5)                      
                    return (x5)
                   
z1000=int(input())
z100=int(input())
z10=int(input())
z1=int(input())
n=z1000*1000+z100*100+z10*10+z1
k=int(input())
# print(n)

for i in range(k):
    n=jedanKrug(n)
print(n)
