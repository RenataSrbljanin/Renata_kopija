

##
##def pozdrav(ime):
##    print(f"Pozdrav {ime}!")
##    
##pozdrav(input("unesi prvo ime: "))
##pozdrav(input("unesi drugo ime: "))
##
##def zbroj(a,b):
##    print("Zbroj je: ", a+b)
##zbroj(2,5)
##
##def kvadrat(x):
##    return x*x
##print(kvadrat(7))


##def pozdrav(ime, pol):
##    if pol=="f":
##        print(f"Dobrodosla {ime}!")
##    else:
##        print(f"Dobrodosao {ime}!")
##        
##pozdrav(input("unesi prvo ime: "), input("unesi pol: "))


##def maksimum(a,b):
##    if a>b:
##        return a
##    else:
##        return b
##print("veci je ", maksimum(int (input("unesi broj a: ")),int(input("unesi broj b: "))))


##def paran(n):
##    return n%2==0
##
##def paran_tekst(n):
##    if paran(n):
##        print("Broj je paran")
##    else:
##        print("Broj je neparan")
##
##paran_tekst(int (input("unesi broj: ")))
   


##def unos():
##    return int(input("Unesi broj: "))
##
##def kvadrat(x):
##        return x*x
##
##def ispis(rezultat):
##        print("Kvadrat je: ", rezultat)
##
##broj=unos()
##r= kvadrat(broj)
##ispis(r)
##
##def unos():
##    return int(input("Unesi broj: "))
##
##def je_paran(n):
##    return n%2==0
##
##def ispis(paran):
##    if paran:
##        print("broj je paran ")
##    else:
##        print("broj je neparan ")
##
##ispis(je_paran(unos()))



def unos_brojeva():
    a=int(input("Unesi broj a: "))
    b=int(input("Unesi broj b: "))
    return a,b

def zbroji(a,b):
    return a+b

def ispisi(rezultat):
    print("Zbroj je: ", rezultat)

x,y= unos_brojeva()
z=zbroji(x,y)
ispisi(z)
