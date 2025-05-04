p=int(input()) 
t=int(input())
n=int(input())
m=int(input())

poeni=[]
tekst = input()
for i in tekst.split():
    poeni.append(int(i))

print(poeni)
print("----")
_pojedinacni=[[t,0,-n]*p] 
# for i in range(p):
#     moguci[i][0] = t
#     moguci[i][1] = 0
#     moguci[i][2] = -n
print(_pojedinacni)

def moguci_rezultati(p,t,n):
   for i in range(p):
       _pojedinacni.append(i*t)
    
    