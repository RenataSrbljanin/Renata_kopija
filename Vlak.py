n=int(input())
a=int(input())      
b=int(input())

if n%(a+b) > 0:
    print((n//(a+b))+1)
else:
    print(n//(a+b))