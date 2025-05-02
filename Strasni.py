a1000=input()
a100=input()
a10=input()
a1=input()

z1000=int(a1000)
z100=int(a100)
z10=int(a10)
z1=int(a1)
n=z1000*1000+z100*100+z10*10+z1
k=int(input())


def o1(n):
    m=str(n)
    m=list(m)
    if m.count("8")==3:
        n= n//2    
        return (True, n)
    else:
        return (False, n)

def o2(n):
    if n>=1000:
        n=n-500
        return (True, n)
    else:
        return (False, n)
        
def o3(n):
    
    
if o1(n)[0]==False :
    if o2(n)[0]== False:
        pass
    else:
        print("Ispunjen je o2 ",o2(n)[1])
else:print("Ispunjen je o1 ",o1(n)[1])
    
    
#print(o1(n))
  
