


##x=str(input())
##while x!="STOP":
##    print(x)
##    x=str(input())
    
    # break u WHILW petlji

##while True:
##    unos= input()
##    if unos=="STOP":
##        break
##    print("Uneseno je: ", unos)


##while True:
##    unos= input()
##    if unos=="STOP":
##        print("Uneseno je: ", unos)
##        break
##    

# prost broj

##n=int(input("Unesi neki broj: "))
##broj_djelitelja= 0
##for i in range(1,n+1,1):
##    if n%i==0:
##       broj_djelitelja=broj_djelitelja+1
##       print(i)
##    
##if broj_djelitelja<=2:
##    print("broj je prost")
##else: print("broj nije prost")


n=int(input("Unesi neki broj: "))
broj_djelitelja= 0
for i in range(1,n+1,1):
    if n%i==0:
       broj_djelitelja=broj_djelitelja+1
       if broj_djelitelja>2:
           print("broj nije prost")
           break
else: # primena else u for petlji!!!
    print("broj nije prost")
# moze se ici do polovive n ili cak do koren iz n



# ako moze for petlja, treba koristiti nju, a ne while





























