try:
    f=open("vezbanje.txt", "r")
   
except FileNotFoundError:
    f=open("vezbanje.txt", "w+")
    print("datoteka nije postojala ali smo je napravili!")

# print(f.read())
f.close()

with open("vezbanje.txt", "r+") as f:
    f.write
    # sadrzaj = f.read()
    # f.seek(7)
  #  f.write(sadrzaj)
    # f.write("Novi uvod\n"+sadrzaj)