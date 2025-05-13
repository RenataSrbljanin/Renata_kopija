import tkinter as tk
from tkinter import messagebox
from typing import Self
import os

if not os.path.exists("biljeske"):
        os.makedirs("biljeske")
root = tk.Tk()
root.title('Dnevnik prehrane')

root.geometry('400x700')


def spremi_biljesku():
    naslov = txt_naslov.get().strip()
    sadrzaj=txt_sadrzaj.get('1.0', tk.END)
    if naslov and sadrzaj:
        putanja=os.path.join("biljeske", f"{naslov}.txt")
        lbl.configure(text=putanja)
        with open(putanja, "w", encoding="utf-8") as f:
                f.write(sadrzaj)
        messagebox.showinfo("Uspjeh", "Biljeska spremljena")
        txt_naslov.delete(0, tk.END)
        txt_sadrzaj.delete("1.0", tk.END)
    else:
        messagebox.showerror("Greska", "Naslov i sadrzaj ne smiju biti prazni")
def osvjezi_listu():
      listbox.delete(0, tk.END)
      for datoteka in os.listdir("biljeske"):
            if datoteka.endswith(".txt"):
                  listbox.insert(tk.END, datoteka)

def prikazi_biljesku():
      odabrano=listbox.curselection()
      if odabrano:
            naziv=listbox.get(odabrano[0])
            putanja=os.path.join("biljeske", naziv)
            with open(putanja, "r", encoding="utf-8") as f:
                  sadrzaj = f.read()
            txt_sadrzaj.delete("1.0", tk.END)
            txt_sadrzaj.insert(tk.END, sadrzaj)
            txt_naslov.delete(0, tk.END)

lbl_1 = tk.Label(root, text="Naslov biljeske")
lbl_1.pack()
# TextBox for input
txt_naslov = tk.Entry(root, width=40)
txt_naslov.pack(pady=5)
#naslov=txt_naslov.get("1.0",tk.END)  # self.myText_Box.get("1.0",END)

lbl_2 = tk.Label(root, text="Sadrzaj:")
lbl_2.pack()

txt_sadrzaj = tk.Text(root,  bd=5, width=50)
txt_sadrzaj.pack()

btn_spremi = tk.Button(root, text="Spremi biljesku", command=spremi_biljesku, pady=5)
btn_spremi.pack(pady=5)

lbl_spremljene = tk.Label(root, text="Spremljene biljeske", pady=5)
lbl_spremljene.pack()
# TextBox for input
listbox = tk.Listbox(root, bd=5, height=5, width=50)
listbox.pack(pady=5)
# Button to print input
btn_prikazi = tk.Button(root, text="Prikazi biljesku", command=prikazi_biljesku, padx=15, pady=15)
btn_prikazi.pack()

# Label to display input
lbl = tk.Label(root, text="")
lbl.pack()

osvjezi_listu()
root.mainloop()