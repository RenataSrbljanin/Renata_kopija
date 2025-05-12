fajl="ucenici.txt"
drugiFajl= "za_pretragu"

def procitajFajl(fajl):
       with open(fajl, "a+", encoding="utf-8") as f:
            f.seek(0)
            linije=f.readlines()
            print(linije)
            novaListaLinija=[]
            for s in linije:
                sl=s.strip()  # !!!
            # sl=s.replace("\n","")
                novaListaLinija.append(sl)
        # ''.join(file.readlines()).split('\n'))[5:10]
            novaListaLinija=novaListaLinija[1:]
            return novaListaLinija
       
def pretraga(imefajla):
    with open(imefajla, "w+", encoding="utf-8") as f:
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

def napuniVelikiFajl(fajl):
         with open(fajl, "x+", encoding="utf-8") as f:
            f.write("Ime, Prezime, Ocjena\n")
            f.write("Loris, Raspolic, 4\n")
            f.write("Renata, Srbljanin, 4\n")
            f.write("Dragan, Srbljanin, 4\n")
            f.write("Vjeran, Maric, 4\n")
            f.write("Anastasia, Srbljanin, 4\n")
            f.seek(0)
            print("Stvorena nova evidencija")
           # print(f.read())
            n=f.read()
            return n

def napuniMaliFajl(fajl):
         with open(fajl, "x+", encoding="utf-8") as f:
            f.write("Ime, Prezime, Ocjena\n")           
            f.write("Renata, Srbljanin, 4\n") 
            f.write("Video, Gamer, 4\n")
            f.write("Anastasia, Srbljanin, 4\n")          
            f.seek(0)
            print("Stvorena nova evidencija")
          #  print(f.read())
            n=f.read()
            return n
         
def otvoriFajl_i_procitaj_ga(fajl):
    try:
        return napuniVelikiFajl(fajl)
    except FileExistsError:
        return procitajFajl(fajl)

def otvoriMaliFajl_i_procitaj_ga(fajl):
    try:
        return napuniMaliFajl(fajl)
    except FileExistsError:
       return  procitajFajl(fajl)
def prelistaj_i_proveri(malaLista, velikaLista):
     for item in malaLista:
          if item in velikaLista:
               print(item+" - DA")
          else:
               print(item+" - NE")
          

velikaLista =otvoriFajl_i_procitaj_ga("ucenici.txt")
malaLista=otvoriMaliFajl_i_procitaj_ga("za_pretragu.txt")
print(velikaLista)
print(malaLista)
print()
prelistaj_i_proveri(malaLista, velikaLista)