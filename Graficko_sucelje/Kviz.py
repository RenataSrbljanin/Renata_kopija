from tkinter import *

# define question dictionary
pitanja = {
    "2+3": ['2', '3', '5', '9'],
    "2-1": ['2', '1', '5'],
    "3+3": ['3', '6', '9', '7']
}
# define answer list
odgovori = ['5', '1', '6']

aktualno_pitanje = 0


def zapocni_kviz():
    start_button.forget()
    next_button.pack()
    sledece_pitanje()


def sledece_pitanje():
    global aktualno_pitanje
    if aktualno_pitanje < len(pitanja):
        # get key or question that need to be printed
        provera_odgovora()
        korisnikov_odgovor.set('None')
        c_pitanje = list(pitanja.keys())[aktualno_pitanje]
        # clear frame to update its content
        ocisti_frame()
        # printing question
        Label(f1, text=f"Pitanje : {c_pitanje}", padx=15,
              font="calibre 12 normal").pack(anchor=NW)
        # printing options
        for option in pitanja[c_pitanje]:
            Radiobutton(f1, text=option, variable=korisnikov_odgovor,
                        value=option, padx=28).pack(anchor=NW)
        aktualno_pitanje += 1
    else:
        next_button.forget()
        provera_odgovora()
        ocisti_frame()
        output = f"Vas skor je: {korisnikov_score.get()} od ukupno {len(pitanja)}"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Hvala na ucescu",
              font="calibre 18 bold").pack()


def provera_odgovora():
    trenutni_odgovor = korisnikov_odgovor.get()
    if trenutni_odgovor != 'None' and trenutni_odgovor == odgovori[aktualno_pitanje-1]:
        korisnikov_score.set(korisnikov_score.get()+1)


def ocisti_frame():
    for widget in f1.winfo_children():
        widget.destroy()


if __name__ == "__main__":
    root = Tk()
    # setup basic window
    root.title("KVIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)

    korisnikov_odgovor = StringVar()
    korisnikov_odgovor.set('None')
    korisnikov_score = IntVar()
    korisnikov_score.set(0)

    Label(root, text="Kviz aplikacija", 
          font="calibre 40 bold",
          relief=SUNKEN, background="cyan", 
          padx=10, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(root, 
                          text="Zapocni kviz",
                          command=zapocni_kviz, 
                          font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Sledece pitanje",
                         command=sledece_pitanje, 
                         font="calibre 17 bold")

    root.mainloop()