import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import datetime
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
route='D:/GitHub Project/SARIApp_Python/Imagenes/'
#Imagen 1
imagen1=PhotoImage(file=route +'HELO1_tranp.png')
imagen1 = imagen1.subsample(2, 2) 
label_imagen1=Label(root, image=imagen1).grid(column=0, row=1)
'''
#Imagen 2
imagen2=PhotoImage(file='Imagenes/HELO.png')
imagen2 = imagen2.subsample(3, 4) 
label_imagenL=Label(root, image=imagen2).grid(column=2, row=1, padx= 0, pady=20)
'''

def datum(): 
    
    datum = Toplevel() 
    datum.title("SARIApp_Data") 
    datum.geometry("600x400")
    Label(datum, text ="Introducir Datos del IAMSAR", font=('Raleway 14 underline' )).pack()

    # INCLUIMOS PANEL PARA LAS PESTAÑAS
    nb=ttk.Notebook(datum)
    nb.pack(fill='both', expand='yes')

    # CREAMOS PESTAÑAS
    p1=ttk.Frame(nb)
    p2=ttk.Frame(nb)
    
    # AGREGAMOS PESTAÑAS
    nb.add(p1, text='Pestaña1')
    nb.add(p2, text='Pestaña2')
    

    # Fecha Hora LKP
    fecha_LKP=Label(p1, text='Fecha LKP: ', font=('Raleway', 11))
    fecha_LKP.place(x=150, y=50)
    time0=tk.StringVar()
    entrada1=Entry(p1, textvariable=time0)
    entrada1.place(x=250, y=50)
    
    # Fecha Hora Datum
    fecha_datum=Label(p1, text='Fecha Datum: ', font=('Raleway', 11))
    fecha_datum.place(x=150, y=200)
    time1=tk.StringVar()
    entrada2=Entry(p1, textvariable=time1)
    entrada2.place(x=250, y=200)
    
    # POSICION EN LATITUD Y LONGITUD
    
    Label(datum, text ="Posición LKP", font=('Raleway', 12)).place(x=240, y=100)
    
    # Latitud LKP
    latitud_LKP=Label(p1, text='Latitud: ', font=('Raleway', 11))
    latitud_LKP.place(x=50, y=150)
    plat0=tk.StringVar()
    entrada3=Entry(p1, textvariable=plat0)
    entrada3.place(x=150, y=150)

    # Longitud LKP
    longitud_LKP=Label(p1, text='Longitud: ', font=('Raleway', 11))
    longitud_LKP.place(x=300, y=150)
    plon0=tk.StringVar()
    entrada4=Entry(p1, textvariable=plon0)
    entrada4.place(x=400, y=150)
    
    # Diferencia en horas
    labeldif=Label(p1, text='Diferencia: ', font=('Raleway', 11))
    labeldif.place(x=250, y=250)
    dif=tk.StringVar()
    entrada5=Label(p1, textvariable=dif)
    entrada5.place(x=500, y=150)
    
    def cambio_posicion():
        # Pasar la latitud de ggmm.mN/S a gg.ggg
        lat0=plat0.get()
        latg=lat0[0:2]
        latm=lat0[2:6]
        latf=lat0[6:7]
        lat0=(float(latg)+float(latm)/60)
        if latf != "N":
            lat0 = 0 - lat0
            
        # Pasar la Longitud de gggmm.mE/W a gg.ggg
        lon0=plon0.get()
        long=lon0[0:3]
        lonm=lon0[3:7]
        lonf=lon0[7:8]
        lon0=(float(long)+float(lonm)/60)
        if lonf != "E":
            lon0 = 0 - lon0
        
        # Transformacion del intervalo en horas 
        string_date = time0.get()
        format = "%d/%m/%Y %H:%M"
        datetime_object = datetime.strptime(string_date, format)
        
        string_date_2 = time1.get()
        format = "%d/%m/%Y %H:%M"
        datetime_object_2 = datetime.strptime(string_date_2, format)
        
        diferencia_days= (datetime_object_2 - datetime_object)/ timedelta(days=1)
        diferencia_horas=diferencia_days*24
        diferencia_horas=('{0:.2f}'.format(diferencia_horas))
                
        #labeltime=Label(datum, text=datetime_object).place(x=400, y=50)
        #labellat=Label(datum, text =lat0).place(x=250, y=100)
        #labellon=Label(datum, text =lon0).place(x=500, y=100)
        #labeltime2=Label(datum, text=datetime_object_2).place(x=400, y=200)
        labeldif_time=Label(datum, text=diferencia_horas).place(x=400, y=250)
        
    # Botón ENTER2
    boton=tk.Button(datum, text='ENTER', bg = "gray", fg="white", command = cambio_posicion)
    boton.place(x=175, y=350, width=100, height=30)
    
    # Botón SALIR
    boton1=tk.Button(datum, text='SALIR', bg = "gray", fg="white", command=quit)
    boton1.place(x=280, y=350, width=100, height=30)
    
    

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