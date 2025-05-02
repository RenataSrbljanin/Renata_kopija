##n=int(input())
##s=input()
##k=int(input())
##
##ukupno=0
##trenutno=0


n=int(input())
s=input()
k=int(input())

secer=[]
zlice=0

for i in range(n):
    if s[i]=="0":
        secer.append(0)
        zlice=zlice+1
    else:
        secer.append(zlice+1)
        zlice=0


print(sum(secer))
print(secer[k-1])
print(max(secer))
