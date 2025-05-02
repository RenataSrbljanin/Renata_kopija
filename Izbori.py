
a, b, c, d=map(int,input().split())
p, q=map(int,input().split())



n=int(input())


najveci=0
druginajveci=0
if a>b and a>c and a>d:
    najveci=a
    if b>c and b>d:
    drugi_najveci=b

elif b>a and b>c and b>d:
    najveci=b
    if c>d:
    drugi_najveci=c
elif c>d :
    najveci=c
    
    
elif b>c:
    najveci=b
elif c>d:
    najveci=c
else:  najveci=d


    
    




