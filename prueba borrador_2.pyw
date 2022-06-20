import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import datetime
from datetime import datetime, date, time, timedelta
from sartools.estima import(    # paquete.modulo  en el paquete estará el __init__.py
    quita360,
    deg_to_rad,
    rad_to_deg,
    formalat,
    formalon,
    Directa,
    DirectaReverse
)

# Creacion de Ventana Principal donde incluir las pestañas
datum=tk.Tk()
datum.title('SARIApp v.22.0') 
datum.geometry("800x500+250+80")

# INCLUIMOS PANEL PARA LAS PESTAÑAS
nb=ttk.Notebook(datum)
nb.pack(fill='both', expand='yes')

# CREAMOS PESTAÑAS
p0=ttk.Frame(nb)
p1=ttk.Frame(nb)
p2=ttk.Frame(nb)

# AGREGAMOS PESTAÑAS
nb.add(p0, text='Present')
nb.add(p1, text='Index')
nb.add(p2, text='ASW')

#####################   PESTAÑA 0    #######################
#Creación de imagenes
route='D:/GitHub Project/SARIApp_Python/Imagenes/'
#Imagen 1
imagen1=PhotoImage(file=route +'HELO1_tranp.png')
imagen1 = imagen1.subsample(1, 1) 
label_imagen1=Label(p0, image=imagen1).pack()

# Botón SALIR
boton1=tk.Button(p0, text='SALIR', bg = "gray", fg="white", command=quit)
boton1.place(x=360, y=400, width=100, height=30)

# Copyright
copyright= Label(p0, text="Cesar Sainz©", font=('Raleway', 7), fg="blue")
copyright.place(x=720, y=455)

# Instrucción
instruction= Label(p0, text="Para ejecutar el SARIApp, entra en las pestañas", font=('Raleway', 9))
instruction.place(x=10, y=455)

#####################   PESTAÑA 1    #######################

labelitle1=Label(p1, text ="Introducir Datos del IAMSAR", font=('Raleway 14 underline' ))
labelitle1.pack()

# Fecha Hora LKP
fecha_LKP=Label(p1, text='Fecha LKP: ', font=('Raleway', 11))
fecha_LKP.place(x=290, y=70)  
time0=tk.StringVar()
entrada1=Entry(p1, textvariable=time0)
entrada1.place(x=400, y=70)

# Fecha Hora Datum
fecha_datum=Label(p1, text='Fecha Datum: ', font=('Raleway', 11))
fecha_datum.place(x=290, y=260)
time1=tk.StringVar()
entrada2=Entry(p1, textvariable=time1)
entrada2.place(x=400, y=260)

# POSICION EN LATITUD Y LONGITUD

Label(p1, text ="Posición LKP", font=('Raleway', 12)).place(x=350, y=130)

# Latitud LKP
latitud_LKP=Label(p1, text='Latitud: ', font=('Raleway', 11))
latitud_LKP.place(x=170, y=190)
plat0=tk.StringVar()
entrada3=Entry(p1, textvariable=plat0)
entrada3.place(x=240, y=190)

# Longitud LKP
longitud_LKP=Label(p1, text='Longitud: ', font=('Raleway', 11))
longitud_LKP.place(x=420, y=190)
plon0=tk.StringVar()
entrada4=Entry(p1, textvariable=plon0)
entrada4.place(x=490, y=190)

# Diferencia en horas
labeldif=Label(p1, text='Diferencia: ', font=('Raleway', 11))
labeldif.place(x=330, y=320)

def cambio_posicion():
    # Pasar la latitud de ggmm.mN/S a gg.ggg
    lat0=plat0.get()
    latg=lat0[0:2]
    latm=lat0[3:7]
    latf=lat0[7:8]
    lat0=(float(latg)+float(latm)/60)
    if latf != "N":
        lat0 = 0 - lat0
        
    # Pasar la Longitud de gggmm.mE/W a gg.ggg
    lon0=plon0.get()
    long=lon0[0:4]
    lonm=lon0[5:8]
    lonf=lon0[8:9]
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
    
    #######   DATOS FINALES   ######
            
    #labeltime=Label(datum, text=datetime_object).place(x=400, y=50)                            # Fecha_Hora LKP
    #labellat=Label(p1, text =lat0).place(x=170, y=160)                                         # Latitud LKP (GG.ggg N/S)
    #labellon=Label(p1, text =lon0).place(x=390, y=160)                                         # Longitud LKP (GGG.ggg E/W)
    #labeltime2=Label(datum, text=datetime_object_2).place(x=400, y=200)                        # Fecha_Hora Datum
    labeldif_time=Label(p1, text=diferencia_horas, font=('Arial 12' )).place(x=430, y=320)      # Intervalo de tiempo (HH.hh)
    
    
# Botón ENTER2
boton=tk.Button(p1, text='ENTER', bg = "gray", fg="white", command = cambio_posicion)
boton.place(x=250, y=400, width=100, height=30)

# Botón SALIR
boton1=tk.Button(p1, text='SALIR', bg = "gray", fg="white", command=quit)
boton1.place(x=450, y=400, width=100, height=30)    

#####################   PESTAÑA 2    #######################

labelitle2=Label(p2, text ="Introducir Viento en Superficie (ASW)", font=('Raleway 14 underline' )).pack()

# Intervalo en tiempo
intervalo=Label(p2, text='Intervalo: ', font=('Raleway', 11))
intervalo.place(x=100, y=140)
intv0=tk.StringVar()
entrada5=Entry(p2, textvariable=intv0)
entrada5.place(x=170, y=140)

def enter2():
       
    # Transformacion del intervalo en horas 
    string_date = time0.get()
    format = "%d/%m/%Y %H:%M"
    datetime_object = datetime.strptime(string_date, format)
    
    string_date_2 = time1.get()
    format = "%d/%m/%Y %H:%M"
    datetime_object_2 = datetime.strptime(string_date_2, format)
    
    diferencia_days= (datetime_object_2 - datetime_object)/ timedelta(days=1)
    diferencia_minutos=diferencia_days*24*60
    diferencia_minutos=('{0:.2f}'.format(diferencia_minutos))
    diferencia_minutos=int(float(diferencia_minutos))
    
    labeldif_time_1=Label(p2, text=diferencia_minutos, font=('Arial 12' )).place(x=430, y=320)
    
    print(type(diferencia_minutos))
    print(diferencia_minutos)
    print()
    print(type(entrada5))
    print(entrada5)
    
    # Numero de Intervalos
    N_intervalos= int(diferencia_minutos/(entrada5))
    labelN_intervalos=Label(p2, text=N_intervalos, font=('Arial 12' )).place(x=430, y=320) 
    

# Botón ENTER2
boton=tk.Button(p2, text='ENTER', bg = "gray", fg="white", command = enter2)
boton.place(x=170, y=300, width=100, height=30)

# Botón SALIR
boton1=tk.Button(p2, text='SALIR', bg = "gray", fg="white", command=quit)
boton1.place(x=300, y=300, width=100, height=30)    
  

datum.mainloop()