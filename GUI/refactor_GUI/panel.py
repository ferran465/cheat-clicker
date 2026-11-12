from tkinter import *
import tkinter as ttk


def panel():
    pnl = Tk() # inicializar el modulo tkinter


    frme = ttk.Frame(pnl) # crea un widget Frame invisible como un esqueleto/framework que permite unir piezas es decir te permite unir diferentes widgets entre si o diferentes cosas como tamaños etc... (un widget es un objeto GUI que ya puede ser como un button una interfaz gráfica o algo visual.) 

    label = ttk.Label(pnl) # crea un widget Label que permite hacer ver algo visual ya puede ser una foto una interfaz o algo que tu veas por pantalla en tu sistema OP des de la classe ttk

    pnl.state("iconic") # estado de la ventana (al darme error ya sea de fallo de sintaxis o de que no exisitia hay tres tipos de ventaneo: _tkinter.TclError: ambiguous argument "": '''must be normal, iconic, withdrawn, or zoomed''' o si daba fallo de sintaxys: _tkinter.TclError: bad argument "inconic": must be normal, iconic, withdrawn, or zoomed)

    pnl.mainloop()

panel()