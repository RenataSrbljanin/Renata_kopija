imefajla="evidencija.txt"
lista=[[0, "Izlaz"], 
       [1, "Dodavanje novih zapisa"],
       [2, "Prikaz svih zapisa"],
       [3, "Pretrazivanje po prezimenu"],
       [4, "Brisanje cijele datoteke"]]


def dodavanjeNovihZapisa():
    print("Dodavanje novih zapisa")
    unos= input("Unesite Ime, Prezime, Ocenu:")
    if unos.count(",")==2:
            ime, prezime, ocjena = map(str,unos.split(",")) # !!!!
            if ocjena.strip().isdigit():   # !!!
                if int(ocjena)>0 and int(ocjena)<6:
                    print(ocjena)
                    f.write(unos+"\n")
                    return unos
                else:
                    print("ocjena mora biti od 1 do 5")
            else:
                print("za ocjenu mora biti upisan broj izmedju 1 i 5")
    else:
        print("Pogresan unos")

def prikaz():
    print("Prikaz svih zapisa")
    f.seek(0)
    print(f.read())

def pretraga():
    print("Pretrazivanje po prezimenu")
    f.seek(0)
    listaLinija=f.readlines()[1:] # !!!
    novaListaLinija=[]
    for s in listaLinija:
        sl=s.strip()  # !!!
       # sl=s.replace("\n","")
        novaListaLinija.append(sl)
   # ''.join(file.readlines()).split('\n'))[5:10]
    print(listaLinija, novaListaLinija)

def brisanje():
    print("Brisanje datoteke")
    with open(imefajla, "w+", encoding="utf-8") as f:
        f.write("obrisali smo evidenciju i napravili smo novi fajl")

listaUcenika=[]
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
        noviunos = input("Odaberite opciju:")
        if noviunos.strip().isdigit() and int(noviunos)<5 and int(noviunos)>=0:
            if int(noviunos)==0:
                print("Izasli smo iz evidencije")
                break
            elif int(noviunos)==1:
                dodavanjeNovihZapisa()
            elif int(noviunos)==2:
                prikaz()
            elif int(noviunos)==3:
                pretraga()
            else:
                brisanje()
        else:
            print("Molimo Vas unesite broj ozmedju 0 i 4: ")

        if noviunos.strip().lower() == "kraj":  # !!!
            break
        
       
        
   