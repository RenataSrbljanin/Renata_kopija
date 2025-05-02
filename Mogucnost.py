
r=int(input())
o=r%5
os=o/5


if r%5==0:
    print(r)
else:
    if r//5<0:
        print(r/5*(1-(r%5)/5))
    else:
        print(r/5*(1+os))
        
