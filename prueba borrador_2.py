import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

from datetime import datetime, date, time, timedelta

root = tk.Tk()
#root.geometry('+%d+%d'%(400,300)) #Place GUI at x=350, y=10
#root.config(bg='blue')
root.title('SARIApp v.22.0')
canvas=tk.Canvas(root, width=300, height=400)
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
label_imagen1=Label(root, image=imagen1).grid(column=0, row=1)
'''
#Imagen 2
imagen2=PhotoImage(file='Imagenes/HELO.png')
imagen2 = imagen2.subsample(3, 4) 
label_imagenL=Label(root, image=imagen2).grid(column=2, row=1, padx= 0, pady=20)
'''

def datum(): 
    
    datum = Toplevel(root) 
    datum.title("SARIApp_Data") 
    datum.geometry("1360x768")
    Label(datum, text ="Introducir Datos del IAMSAR", font=('Raleway', 12)).pack()
    
    # Copyright
    fecha_lkp= Label(root, text="Fecha del LKP: ", font=('Raleway', 7), fg="blue")
    copyright.place(x=400, y=380)
    
    # Botón
    boton1=tk.Button(datum, text='ENTER', bg = "gray", fg="white")
    boton1.place(x=600, y=550, width=100, height=30)
    
    
# Botón
boton=tk.Button(text='ENTER', bg = "gray", fg="white", command = datum)
boton.place(x=175, y=300, width=100, height=30)

# Copyright
copyright= Label(root, text="Cesar Sainz©", font=('Raleway', 7), fg="blue")
copyright.place(x=400, y=380)

# Instrucción
instruction= Label(root, text="Para ejecutar el SARIApp, pulsa ENTER", font=('Raleway', 9))
instruction.place(x=10, y=380)

root.mainloop()