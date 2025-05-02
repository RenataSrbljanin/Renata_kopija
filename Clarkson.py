x=int(input())
y=int(input())
z=int(input())

pomereno=0
skladista={'A':x, 'B':y, 'C':z}
rezultati=[]
for j in range(2):
    max=0
    min=100
    for i in skladista:
        if skladista[i]>max:
            max=skladista[i]
            max_skladiste=i
        if skladista[i]<min:
            min=skladista[i]
            min_skladiste=i
    #skladista   
    pomereno=pomereno+min
   # print(min_skladiste,max_skladiste)
    rezultati.append(min_skladiste)
    rezultati.append(max_skladiste)
    skladista[max_skladiste] = skladista[max_skladiste] + skladista[min_skladiste]
    skladista.pop(min_skladiste)      
#
print(pomereno)

print(rezultati[0], rezultati[1])
print(rezultati[2], rezultati[3])
#print(rezultati)