p=int(input()) 
t=int(input())
n=int(input())
m=int(input())

def moguci(p,t,n):
    l=[]
    for i in range(p):
          for j in range(i,p):
            for k in range(i+j,p):
                   l.append(t*j-k*n)
    return l

zamisljeniPoeni=[]
tekst = input()
for i in tekst.split():
    zamisljeniPoeni.append(int(i))

print(zamisljeniPoeni)
print("----")

listaMogucih=moguci(p,t,n)
print(listaMogucih)
# for pi in zamisljeniPoeni:
#     if pi
# _pojedinacni=[[t,0,-n]*p] 
# # for i in range(p):
# #     moguci[i][0] = t
# #     moguci[i][1] = 0
# #     moguci[i][2] = -n
# print(_pojedinacni)

# def moguci_rezultati(p,t,n):
#    for i in range(p):
#        _pojedinacni.append(i*t)
    
    