a=int(input())
b=int(input())
c=int(input())
if a+b<=c:print("NE")
else:
    if a+c<=b:print("NE")
    else:
        if b+c<=a: print("NE")
        else: print("DA")


