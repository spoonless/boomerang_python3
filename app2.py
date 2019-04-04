'''
Application simple

@author: david
'''
import tkinter as tk
from collections import OrderedDict

window = tk.Tk()
window.title("Info contact")

champs = OrderedDict({
    "nom": tk.StringVar(),
    "prenom": tk.StringVar(),
    "adresse": tk.StringVar(),
    "code postal": tk.StringVar(),
    "ville": tk.StringVar(),
})

for ligne, (libelle, var) in enumerate(champs.items()):
    label = tk.Label(window, text=libelle)
    label.grid(sticky=tk.E, row=ligne, column=0)
    entry = tk.Entry(window, textvariable=var)
    entry.grid(sticky=tk.W, row=ligne, column=1, columnspan=2)

def printConsole():
    for k, v in champs.items():
        print(f"{k} = {v.get()}")

btn = tk.Button(window, text="ok", command=printConsole)
btn.grid(sticky=tk.E, row=len(champs), column=2)

window.mainloop()