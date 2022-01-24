import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

root = tk.Tk()
#root.geometry('+%d+%d'%(400,300)) #Place GUI at x=350, y=10
#root.config(bg='blue')
root.title('Ejemplo de Imagenes')
canvas=tk.Canvas(root, width=700, height=600)
canvas.grid(columnspan=5, rowspan=5)

'''
root = Tk()     #you must create an instance of Tk() first
root.geometry('700x600+0+0')
root.config(bg='blue')
root.title('Ejemplo de Imagenes')
'''
#Creación de imagenes
#Imagen 1
imagen1=PhotoImage(file='Imagenes/HELO1_tranp.png')
imagen1 = imagen1.subsample(2, 2) 
label_imagen1=Label(root, image=imagen1).grid(column=1, row=1)
'''
#Imagen 2
imagen2=PhotoImage(file='Imagenes/HELO.png')
imagen2 = imagen2.subsample(2, 2) 
label_imagenL=Label(root, image=imagen2).grid(column=2, row=1, padx= 0, pady=20)
'''

# Botón
boton=tk.Button(text='Hola mundo', bg = "blue", fg="white")
boton.place(x=250, y=370, width=100, height=30)

root.mainloop()