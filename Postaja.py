z=int(input()) #("Unesite trenutni broj znanstvenika: "))
k=int(input()) #("Njihova tezina je: "))
x=int(input())#("Data je tezak: "))
y=int(input)#("Kirk je tezak: "))

def racunanje(broj_znanstvenika_u_dizalu, ukupna_tezina_znanstvenika_u_dizalu):
    if ukupna_tezina_znanstvenika_u_dizalu>=1000:
        return [broj_znanstvenika_u_dizalu, ukupna_tezina_znanstvenika_u_dizalu]
    if ukupna_tezina_znanstvenika_u_dizalu+x+y <= 1000:
        broj_znanstvenika_u_dizalu=broj_znanstvenika_u_dizalu+2
        ukupna_tezina_znanstvenika_u_dizalu=ukupna_tezina_znanstvenika_u_dizalu+x+y
    else:        
        if x<y and ukupna_tezina_znanstvenika_u_dizalu+x<=1000:
            ukupna_tezina_znanstvenika_u_dizalu=ukupna_tezina_znanstvenika_u_dizalu+x
            broj_znanstvenika_u_dizalu=broj_znanstvenika_u_dizalu+1
        else:
            if ukupna_tezina_znanstvenika_u_dizalu+y<=1000:
                ukupna_tezina_znanstvenika_u_dizalu=ukupna_tezina_znanstvenika_u_dizalu+y
                broj_znanstvenika_u_dizalu=broj_znanstvenika_u_dizalu+1
    return [broj_znanstvenika_u_dizalu, ukupna_tezina_znanstvenika_u_dizalu]         
racunanje(z, k)
print(racunanje(z, k)[0])
print(racunanje(z, k)[1])


