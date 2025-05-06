try:
    f=open("ne_postoji.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("datoteka ne postoji!")