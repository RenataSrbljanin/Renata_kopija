def faktorijel(n):
    if n==1 or n==0:
        return 1
    else:
        return n*faktorijel(n-1)

def sabiranje_do_broja(n):
    lista=[1,1]
    for i in range(2,n+1):
        print(lista[i-1]+lista[i-2])
        lista.add(lista[i-1]+lista[i-2])
    return lista   

def fibonaci(n):
    prvi,drugi=1,1  
    if n==1 or n==2:
        return(1)
    else:
        for i in range(2,n):
            # temp=prvi
            # prvi=drugi
            # drugi=temp+drugi
            prvi, drugi = drugi, prvi+drugi
    return drugi
def fibonaci_1(n):
    prvi,drugi=1,1  
    if n==1 or n==2:
        return(1)
    else:         
         return fibonaci_1(n-1)+fibonaci_1(n-2)
def koliko_znamenki(m):
    m=str(m)
    a=m.split()
    return a

def broj_znamenki(n):
    if n<10:
        return 1
    return 1+broj_znamenki(n//10)
   

def obrce_string(s):
    return s[::-1]

def obrce_string_1(s):
    if len(s)==0:
        return ""
    else:
        return obrce_string_1(s[1:])+s[0]
    
def daLiJePalindrom(string):  # Ne radi kako treba!!!
    if len(string)%2==0:
        for i in range(len(string)//2+1):
            if string[i]!=string[-i]:
                return "NE"
    else:
        for i in range(len(string)//2+2):
            if string[i]!=string[-i]:
                return "NE"
    return "DA"



# n=int(input("Unesite broj: "))
# print(f"Faktorijel od broja {n} je {faktorijel(n)}")
# #print(f"Zbroj brojeva od 1 do {n} je {sabiranje_do_broja(n)}")
# print(f"fibonaci od broja {n} je {fibonaci(n)}")
# print(f"fibonaci od broja {n} je {fibonaci_1(n)}")

s= input("Unesi string za obrtanje: ")
print(obrce_string(s))
print(obrce_string_1(s))
#print(obrce_string_2(s))
print(daLiJePalindrom(s))

# ana