
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

# Crear la ventana desde la que ejecutar SARIApp

root = tk.Tk()
root.geometry('+%d+%d'%(350,10)) #Place GUI at x=350, y=10
canvas=tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=5, rowspan=5)

# Logo
ruta= 'Imagenes/'

logo=Image.open(ruta +'HELO1_tranp.png')
logo=ImageTk.PhotoImage(logo)
logo = logo.subsample(4, 4)   #create a new image half as large as the original
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=2, row=1)

'''
logo = PhotoImage(ruta +'HELO1_tranp.png')
#image = image.zoom(2, 2)         #create a new image twice as large as the original
image = logo.subsample(4, 4)   #create a new image half as large as the original
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=2, row=1)
'''
# Botón

boton=ttk.Button(text='Hola mundo')
boton.grid(column=2, row=2)

root.mainloop()
