n=int(input())
lista=[]
ime_prezime_polje=0
for i in range(n):
    ime, prezime, bodovi = map(str, input().split())
   
    ime_prezime = 2+len(ime)+len(prezime)+2
    if ime_prezime_polje<ime_prezime:
        ime_prezime_polje=ime_prezime
        
    lista.append([bodovi, ime, prezime])
    lista.sort()
lista_sa_razlikama=[]
for item in lista:
    lista_sa_razlikama.append([item[0], item[1], item[2], ime_prezime_polje-(len(lista[i][1])+len(lista[i][2]))])
    
print(lista)

redni_broj=0
for item in lista_sa_razlikama:
    redni_broj=redni_broj+1
    print(f"|  {str(redni_broj)} | {item[1]} {item[2]}"+item[3]*" ", end="")
    print(f"| {lista[i][0]} / 400 |")
   # print(f"| {str(i)} | {lista[i][0]} {lista[i][1]} | {lista[i][2]} / 400 |")