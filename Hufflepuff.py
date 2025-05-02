

n=int(input()) 
uc=0
uz=0
up=0
uy=0
  
for i in range(n):
    boja=input()
    
    if boja=="C":
        uc=uc+1
    elif boja=="Z":
         uz=uz+1
    elif boja=="P":
         up=up+1
    elif boja=="Y":
         uy=uy+1
    


if  uc>uz and uc>up and uc>uy:
    print("LANA")
elif uz>uc and uz>up and uz>uy:
    print("LARA")
elif  up>uc and up>uz and up>uy:
    print("MASA")
else:
    print("EXPELLIARMUS")
