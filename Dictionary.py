ucenik={
"ime":"Anna",
"razred":6,
"ocjena": 5
    }
print(ucenik["ime"])
print(ucenik["razred"])
print(ucenik["ocjena"])


# DODAVANJE
ucenik["prezime"]="Maric"
print(ucenik["prezime"])

# IZMJENA
ucenik["razred"]=7
print(ucenik)

for kljuc in ucenik:
    print(kljuc, ucenik[kljuc])


ocjene=[5,5,2,5]
ucenik={"ime":"Luka", "ocjene":ocjene}
print(ucenik["ocjene"])
