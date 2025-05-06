import os
if os.path.exists("biljeske.txt"):
    os.remove("biljeske.txt")
else:
    print("datoteka ne postoji")