import operator

n=int(input())
lista=[]
ime_prezime_polje=0
max_cifara_bodova=0
koliko_crtica=13
for i in range(n):
    ime, prezime, bodovi = map(str, input().split())
   
    ime_prezime = 1+len(ime)+len(prezime)
    if ime_prezime_polje<ime_prezime:
        ime_prezime_polje=ime_prezime
        
    lista.append([int(bodovi), ime, prezime])

lista.sort(key = operator.itemgetter(1,2)) # !!!

lista.sort(key = operator.itemgetter(0), reverse=True) # !!!

lista_sa_razlikama=[]
for item in lista:
    lista_sa_razlikama.append([item[0], item[1], item[2], ime_prezime_polje-(len(item[1])+len(item[2]))])
    broj_cifara_bodova=len(str(item[0]))
    if broj_cifara_bodova>max_cifara_bodova:
        max_cifara_bodova=broj_cifara_bodova

koliko_cifara_max=len(str(len(lista_sa_razlikama)))
print(lista_sa_razlikama)
print()
koliko_crtica=koliko_crtica+max_cifara_bodova+ime_prezime_polje+koliko_cifara_max+3
i=0
redni_broj=0
print(koliko_crtica*"-")
for item in lista_sa_razlikama:
    i=i+1
    if lista_sa_razlikama[i][0]<lista_sa_razlikama[i-1][0]:
        redni_broj=i
    cifara_rednog_broja=len(str(redni_broj))
    razlika_broja_cifara=koliko_cifara_max-cifara_rednog_broja
    
    broj_cifara_bodova=len(str(item[0]))
    razlika=max_cifara_bodova-broj_cifara_bodova
    print(f"| "+razlika_broja_cifara*" "+f"{str(redni_broj)} | {item[1]} {item[2]}"+item[3]*" ", end="")
    print(f"| "+razlika*" "+f"{item[0]} / 400 |")
  
print(koliko_crtica*"-")