
    # Tablica mnozenja
    
##for i in range(1,6):
##    for j in range(1,6):
##        print(i*j,end=" ")
##    print()

##    for i in range(1,6):
##     for j in range(1,6):
##        print(i*j,end="\t") # \t je tab
##     print()
    


##for i in range(1,4):
##    for j in range(1,7):
##        print(i*j,end="\t") # \t je tab
##    print()


##for i in range(1,4):
##    for j in range(1,7):
##        print("*",end="\t") # \t je tab
##    print()

# sa kaunterom

##for i in range(1,4):
##    for j in range(1,4):
##        print(x,end="")
##        x=x+1
##    print()

# matematicki
   
##for i in range(3):
##    for j in range(1,4):
##        print(j+i*3,end="")
##        
##    print()


# trokut od zvezdica

# ovaj ne valja!
##for i in range(1,6):
##    for j in range(1,6):
##        print("*",end="") # \t je tab
##    print()  
    

##
##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end="") # \t je tab
##    print()


##for i in range(1,6):
##    for j in range(i):
##        print("*",end="")
##
##    print()


# obrnuti trougao

##for i in range(5,0, -1):
##    for j in range(i):
##        print("*",end="")
##    print()

# prazan kvadrat

##n = int(input("Unesi koliko zelis dugacke stranice kvadrata: "))
##for i in range(n):
##   
##    for j in range(n):
##        if i==0 or i==n-1 or  j==0 or j==n-1:           
##         print("*",end=" ")
##        else:
##            print(" ", end=" ")
##    print( )

# ispisi dijagonalu kvadrata

##n = int(input("Unesi koliko zelis dugacke stranice kvadrata: "))
##for i in range(n):
##    for j in range(n):
##        if i==j:
##          print(i+1,end="")
##        else: print(" ", end=" ")
##    print()

# ispisi dijagonalu kvadrata sa zvezdicama,a prazne sa tarabama

n = int(input("Unesi koliko zelis dugacke stranice kvadrata: "))
for i in range(n):
    for j in range(n):
        if i==j:
          print("*  ",end="")
        else: print("#", end=" ")
    print()



























