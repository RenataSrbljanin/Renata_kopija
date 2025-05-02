

brojevi=[]
for i in range(7):
    m=int(input())
    brojevi.append(m)

##x=1
##for i in range(1,14):
##    for j in range(1,4):
##        print(x,end="")
##        x=x+1
##    print()
    
x=1
for i in range(1,14):
    for j in range(1,4):
        if x in brojevi:
            print("X",end="")
        else:print("*",end="")
        x=x+1
    print()
