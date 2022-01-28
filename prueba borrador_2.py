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
    datum.geometry("600x400")
    Label(datum, text ="Introducir Datos del IAMSAR", font=('Raleway 14 underline' )).pack()
    
    # Botón SALIR
    boton1=tk.Button(datum, text='SALIR', bg = "gray", fg="white", command=quit)
    boton1.place(x=280, y=350, width=100, height=30)
    
    # Fecha LKP
    fecha_LKP=Label(datum, text='Fecha LKP: ', font=('Raleway', 11))
    fecha_LKP.place(x=50, y=50)
    entrada1=Entry(datum)
    entrada1.place(x=150, y=50)
    
    # Hora LKP
    hora_LKP=Label(datum, text='Hora LKP: ', font=('Raleway', 11))
    hora_LKP.place(x=300, y=50)
    entrada2=Entry(datum)
    entrada2.place(x=400, y=50)
    
    # POSICION EN LATITUD Y LONGITUD
    
    Label(datum, text ="Posición LKP", font=('Raleway', 12)).place(x=240, y=110)
    
    # Latitud LKP
    latitud_LKP=Label(datum, text='Latitud: ', font=('Raleway', 11))
    latitud_LKP.place(x=50, y=150)
    entrada3=Entry(datum)
    entrada3.place(x=150, y=150)

    # Longitud LKP
    longitud_LKP=Label(datum, text='Longitud: ', font=('Raleway', 11))
    longitud_LKP.place(x=300, y=150)
    entrada4=Entry(datum)
    entrada4.place(x=400, y=150)

# Botón ENTER
boton=tk.Button(text='ENTER', bg = "gray", fg="white", command = datum)
boton.place(x=175, y=300, width=100, height=30)

# Copyright
copyright= Label(root, text="Cesar Sainz©", font=('Raleway', 7), fg="blue")
copyright.place(x=400, y=380)

# Instrucción
instruction= Label(root, text="Para ejecutar el SARIApp, pulsa ENTER", font=('Raleway', 9))
instruction.place(x=10, y=380)

root.mainloop()