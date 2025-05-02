n=int(input()) 
x=0
  
for i in range(n):
    rp, pp, rk, pk=map(int,input().split())
    
    if rp>pp:
        if rk<pk:
         x=x+3
        elif rk==pk:
         x=x+2
    elif rp==pp:
       if rk<pk:
        x=x+1
    
print(x)
