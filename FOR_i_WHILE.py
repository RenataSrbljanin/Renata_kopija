##for i  in range(30,2,-5):
##    print("Iteracija:",i)


##n=int(input("Unesi broj do kojeg zelis iteraciju: "))
##for i  in range(1,n+1):
##    print("Iteracija:",i)

##n=int(input("Unesi broj do kojeg zelis iteraciju parnih brojeva: "))
##for i  in range(0,n+1,2):
##    print("Iteracija:",i)

#od 10 do 1
##n=int(input("Unesi broj do kojeg zelis iteraciju unatrag: "))
##for i  in range(10,0,-1):
##    print("Iteracija:",i)

##for i  in range(1,31):
##    if i%3==0:
##        print("Iteracija:",i)

# BREAK
##for i in range(10):
##    if i==5:
##        print(i)    
##        break
##    print(i)


###continue
##
##for i in range(10):
##    if i==5:
##        continue
##    print(i)

# else
##
##for i in range(3):
##    print(i)
##else:
##    print("Petlja je gotova")


# parne preskacemo
##for i in range(1,10):
##   if i%2==0:
##    continue
##   print(i)


##n=int(input("Unesi broj do kojeg zelis iteraciju: "))
##k=int(input("Unesi broj koliko da preskace: "))
##
##for i in range(1,n+1):
##   if i%k==0:
##    continue
##   print(i)


### sa kaunterom
##n=int(input("Unesi broj do kojeg zelis iteraciju: "))
##k=int(input("Unesi broj koliko da preskace: "))
##kaunter=0
##for i in range(1,n+1):
##   if i%k==0:
##    continue
##    kaunter=+1
##    print(i)
##else: print("broj ispisa je: ", kaunter) # nije uradjeno


##n=int(input("Upisi koliko hoces unosa: "))
###k=int(input("Unesi broj koliko da preskace: "))
##zbroj=0
##for i in range(n):
##    k=int(input())
##    zbroj=zbroj+k
##print(zbroj)

##n=int(input("Upisi broj izmedju 1 i 5: "))
##
##for i in range(3):
##    k=int(input(f"pogadjaj {i+1}. put: "))
##    if k==n: 
##     print("Cestitam")
##     break
##else:
## print(" zao nam je")

# BREAK
##for i in range(10):
##    if i==5:
##        print(i)    
##        break
##    print(i)

##for i in range(100, 201):
##   # k=int(input(f"pogadjaj {i+1}. put: "))
##    if i%5==0 and i%7==0: 
##     print(i)
##     break
##else:
## print(" zao nam je")

for i in range(10, 31):
  
    if i%5==0 and i%7==0: 
     print(i)
     break
else:
 print(" zao nam je") 

