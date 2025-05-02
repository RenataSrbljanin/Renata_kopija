
n = input()
m=len(n)//2

a=n[:m]
b=n[m:]
a=int(a)
b=int(b)
print(abs(a-b))

# matematicki

a=int(input())
if a>99999 and a<1000000:
    pass
elif  a>9999 and a<100000 :
    pass
elif  a>999 and a<10000 :
    pass
else:
