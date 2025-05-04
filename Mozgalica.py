def a1(n):
    n=int(n)
    return n+1
def a2(n):
    n=int(n)
    if n%2==0:
        return a1(n)
    else: return n-1
def a3(n):
    n=int(n)    
    x=str(n)
   # x=list(n)
    jedinica=int(x[-1])    
    return n+jedinica    
def a4(n):       
    a=str(n)
    x=a[len(a)-1]
    y=a[len(a)-2]
    a=list(a)
    a[len(a)-2]=x
    a[len(a)-1]=y
    a=''.join(a)
    return int(a)
   
n=int(input())
k=int(input())
for i in range(k):
    ai=int(input())
    if ai==1:
        n= a1(n)
    elif ai==2:
        n= a2(n)
    elif ai==3:
        n= a3(n)
    elif ai==4:
        n= a4(n)
print(n)

