import pandas as pd
import os
import tkinter
from tkinter import filedialog

file = tkinter.filedialog.askopenfile(initialdir = 'C:\SARIApp_Full\SARIApp_Data\SARIApp_Results',
                                          title='SARIApp Results Spreadsheet')  # asking for the Excel file
abs_path_file = os.path.abspath(file.name)  # creating the abs path to the file

lista_de_archivos = os.listdir("C:/SARIApp_Full/SARIApp_Data/SARIApp_Results/")
if len(lista_de_archivos) > 0:
    print("vamos a iniciar con " + str(len(lista_de_archivos)) + " Archivos")
    data = pd.read_excel(abs_path_file, 'Export_Datums', names=['lat', 'lon', 'point'], skiprows=4,
                         usecols='B:D', encoding = 'utf8')
    data.to_json(path_or_buf= file.name+'.json',orient='records')
else:
    print("terminado")