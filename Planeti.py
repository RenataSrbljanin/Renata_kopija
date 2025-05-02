lista=["MERKUR", "VENERA", "ZEMLJA", "MARS",
       "JUPITER", "SATURN", "URAN", "NEPTUN"]

planeta=input();
poseta=0
for i in range(len(lista)):
    if lista[i]==planeta:
        print(i)
        break
