
n=int(input())
bol=0

zg=list(map(int, input().split()))
vr=list(map(int, input().split()))

prethodni=[""]

for i in range(n):
    if zg[i]!=vr[i]:
        if zg[i]>vr[i]:
            if prethodni[-1]=="v":
                bol=bol+1
            prethodni.append("z")
            
        else:
            if prethodni[-1]=="z":
                 bol=bol+1
            prethodni.append("v")            
               
                
print(bol)       
    



    
