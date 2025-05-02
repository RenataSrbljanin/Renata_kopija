
j1, s1=map(int, input().split())
s2, j2=map(int, input().split())

uj=j1+j2
us=s1+s2

print(uj,us)
if uj>us:
    print("Junak")
elif us>uj:
    print("Segesta")
else:
    if j2>s1:
        print("Junak")
    elif s1>j2:
        print("Segesta")
    else: print("Jedanaesterci")
