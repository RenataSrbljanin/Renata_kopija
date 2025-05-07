# imefajla="Zadatak2.txt"

# try:
#     with open(imefajla, "x+", encoding="utf-8") as f:
#         f.write("Ime, Prezime, Ocjena\n")
#         f.write("Loris, Raspolic, 4\n")
#         f.seek(0)
#         print("Stvorena nova evidencija")
#         print(f.read())
# except FileExistsError:
#    with open(imefajla, "x+", encoding="utf-8") as f:
#     noviunos = input("Unesi novi zapis (Ime, Prezime, Ocena):")
#     f.write(noviunos+"\n")
#     f.seek(0)
#     print("Azurirana evidencija: ")
#     print(f.read())

imefajla="Zadatak3.txt"

try:
    with open(imefajla, "x+", encoding="utf-8") as f:
        f.write("Ime, Prezime, Ocjena\n")
        f.write("Loris, Raspolic, 4\n")
        f.seek(0)
        print("Stvorena nova evidencija")
        print(f.read())
except FileExistsError:
   with open(imefajla, "a+", encoding="utf-8") as f:
    while True:
        noviunos = input("Unesi novi zapis (Ime, Prezime, Ocena):")
        if noviunos.strip().lower() == "kraj":  # !!!
            break
        if noviunos.count(",")==2:
            ime, prezime, ocjena = map(str,noviunos.split(",")) # !!!!
            if ocjena.strip().isdigit():   # !!!
                if int(ocjena)>0 and int(ocjena)<6:
                    print(ocjena)
                    f.write(noviunos+"\n")
                else:
                    print("ocjena mora biti od 1 do 5")
            else:
                print("za ocjenu mora biti upisan broj izmedju 1 i 5")
        else:
           print("Pogresan unos")
       
        
    f.seek(0)
    print("Azurirana evidencija: ")
    print(f.read())


