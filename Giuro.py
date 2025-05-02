
r=int(input())
o=r%5
os=o/5


if r%5==0:
    print(r)
else:
    if r//5<0:
        print(r*(1-os*5))
    else:
        print(o, os)
        
