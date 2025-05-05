def C_to_F(x):
    return ((x*9/5)+32)

def F_to_C(x):
    return((x-32)*5/9)

x=int(input("Unesi koliko: ").upper())
jadinicaMere=input("Unesite jedinicu mere:")

if jadinicaMere == "C":
    print(round(C_to_F(x),2))
else:
    print(round(F_to_C(x),2))