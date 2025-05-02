lista_rezultata=[]
lista_rezultata.append(int(input()))
lista_rezultata.append(int(input()))
lista_rezultata.append(int(input()))
text="DA"
vr=max(lista_rezultata)
for i in range(3):
    if lista_rezultata[i] <10:
        text="NE"
        vr=min(lista_rezultata)
        break
print(text)
print(vr)