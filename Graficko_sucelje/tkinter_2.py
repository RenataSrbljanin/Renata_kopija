import tkinter as tk
from time import strftime

def update_time():

  
    str_time=strftime('%H:%M:%S %p')
    digital_clock.configure(text=str_time)
    digital_clock.after(1000, update_time)

root=tk.Tk()
root.title('Digital Clock')


digital_clock=tk.Label(root, font=('calibri', 40, 'bold'), background='darkblue', foreground='white')
digital_clock.pack(pady=20)

update_time()

root.mainloop()
