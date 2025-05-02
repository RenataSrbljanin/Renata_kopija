##a=int(input("Unesite bodove"))
##b=int(input("Unesite prisutnost"))
##
##if
##a>=90 and b==100
##    print("Izvanredan rezultat")
##elif
##    a>=60
##    if b<80:
##    print("Uvjetna ocena")
##    else:
##    print("polozio")
##else:
##    print("nije polozio")

t=int(input()
k="B"
o="XS"

if t>=43:
    if t>=73:
        k="XL"
    elif  b==2:
         k="L"
    elif b==3:
         k="M"
    elif b==4:
         k="S"
    
print(k,o, sep)


#Sat

##s=int(input())
##m=int(input())
##if s>=12:
##    h=s-12
##else:
##    h=s+12
##print(h)
##print(m)


#Pascal
##n=int(input())
##g=int(input())
##if n>=2*g:
##    print("DA")
##else:
##    print("NE")

##
### UV Ikz
##
##n=int(input())
##tekst ="Niska opasnost"
##if n<=50:
##    tekst ="dobra kvaliteta zraka"
##    
##else:
##        if  n>300:
##            tekst ="opasan zrak"
##       
##        elif n>200:
##             tekst ="vrlo nezdrav zrak"
##        elif n>150:
##             tekst ="nezdrav zrak"
##        elif n>100:
##             tekst ="zrak nezdrav za osjetljive grupe"
##        else:
##             tekst ="umjerena kvaliteta zraka"
##
##print(tekst)


###Centum
##g=int(input())
##if g%100>0:
##    s=(g//100)+1
##else:
##    s=g//100
##print(s)

# Torta

##n=int(input())
##j=int(input())
##z=int(input())
##b=int(input())
##
##if z>=b:
##    bj=n*(j+z)
##else:
##    bj=n*(j+b)
##
##print(bj)

##a=int(input())
##b=int(input())
##c=int(input())
##d=int(input())
##
##print(a)
##print(a+b)
##print(a+b+c)
##print(a+b+c+d)
##
##if a+b+c+d>=100:
##    print("DA")
##else:
##    print("NE")

# Pat
##p1=int(input())
##p2=int(input())
##p3=int(input())
##p4=int(input())
##m1=int(input())
##m2=int(input())
##m3=int(input())
##m4=int(input())
##text="PAT"
##if p1<m1:
##    text="MAT"   
##print(text)
##text="PAT"
##if p1+p2<m1+m2:
##    text="MAT"   
##print(text)
##text="PAT"
##if p1+p2+p3<m1+m2+m3:
##    text="MAT"   
##print(text)
##text="PAT"
##if p1+p2+p3+p4<m1+m2+m3+m4:
##    text="MAT"   
##print(text)

# Mlijeko

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

n=int(input())


if(n<=a):
    print(n)
    print(0)
    print(0)
    print(0)
    print(0)
elif n<=a+b:
    print(a)
    print(n-a)
    print(0)
    print(0)
    print(0)
elif n<=a+b+c:
    print(a)
    print(b)
    print(n-a-b)
    print(0)
    print(0)
elif n<=a+b+c+d:
    print(a)
    print(b)
    print(c)
    print(n-(a+b+c))
    print(0)
else: 
    print(a)
    print(b)
    print(c)
    print(d)
    if (n-(a+b+c+d)<e):
        print(n-(a+b+c+d))
    else: print(e)
   




















