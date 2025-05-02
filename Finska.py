
n=int(input())


#recenica=map(str,input().split())

recenica=input()
novarecenica=""

for i in range(len(recenica)):
    if i==0 or recenica[i]!=recenica[i-1]:
        novarecenica=novarecenica+recenica[i]
       # recenica.pop(i+1)
print(novarecenica)
    #print(rec[i], end=" ")
