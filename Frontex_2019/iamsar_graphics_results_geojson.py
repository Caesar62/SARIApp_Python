__author__ = 'jose m allegue (kamome)'

import numpy as np
from numpy import nan
import os
import pandas as pd
import shapefile as shp
import tkinter
from tkinter import filedialog


def procesa():
    def construye_puntos(nombre_archivo, lista_puntos_limpia):  
        w = shp.Writer(shp.POINT)
        w.field('X', 'F', 10, 5)  # F float, para coordenadas
        w.field('Y', 'F', 10, 5)
        w.field('point')
        for index, row in dataLimpia.iterrows(): 
            w.point(row['lon'], row['lat'])
            w.record(row['lon'], row['lat'], str(row['point']))
        w.save(filename)

    def construye_polygon(nombre_archivo):  
        w = shp.Writer(shp.POLYGON)
        w.poly(parts=([line]))
        w.field('point') 
        w.record(filename)
        w.save(filename)

    def construye_polyline(nombre_archivo, archivo_linea):
        w = shp.Writer(shp.POLYLINE)
        w.field("point")  
        w.line(parts=([line]))
        w.record("Line")
        w.save(filename)

    def construye_proyeccion(nombre_arhivo):  
        prj = open('%s.prj' % filename, 'w')
        proyeccion = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],' \
                     'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
        prj.write(proyeccion)
        prj.close()

    file = tkinter.filedialog.askopenfile(initialdir = 'C:\SARIApp_Full\SARIApp_Data\SARIApp_Results',
                                          title='SARIApp Results Spreadsheet')  # asking for the Excel file

    abs_path_file = os.path.abspath(file.name)  # creating the abs path to the file

    file_output_name = os.path.abspath((tkinter.filedialog.asksaveasfile(initialdir = 'C:\SARIApp_Full\SARIApp_Data\SARIApp_GIS',title='Save SHPs files as :')).name)

    filename = ('%s_IAMSAR_AREA' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Area IAMSAR', names=['lat', 'lon', 'point'], skiprows=3,
                         usecols='B:D', lineterminator=5)
    dataLimpia = data.dropna(how='any')  
    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polygon(filename)  
        construye_proyeccion(filename)  


    filename = ('%s_SAR_AREA' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Area', names=['lat', 'lon', 'point'], skiprows=3,
                         usecols='B:D', lineterminator=5)
    dataLimpia = data.dropna(how='any')  
    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polygon(filename) 
        construye_proyeccion(filename)


    filename = ('%s_PROBABILIIY_AREA' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_PM', names=['lat', 'lon', 'point'], skiprows=3,
                         usecols='B:D', lineterminator=5)
    dataLimpia = data.dropna(how='any')  
    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polygon(filename)  
        construye_proyeccion(filename)

    #####  EXPORT DATUMS
    filenameDatums = ('%s_DATUMS' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Datums', names=['lat', 'lon', 'point'], skiprows=4,
                         usecols='B:D')
    dataLimpia = data.dropna(how='all')

    filename = ("%s_DATUMS" % file_output_name)
    construye_puntos(filename, dataLimpia)
    construye_proyeccion(filename)

    filename = ('%s_TRACKING_LINE' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export Tracking', names=['lat', 'lon', 'point'], skiprows=3,
                         usecols='B:D')
    dataLimpia = data.dropna(how='all')  # limpio los NaN  ver dropna
    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polyline(filename, line)
        construye_proyeccion(filename)
        filename = ('%s_5_TRACKING_POINTS' % file_output_name)
        construye_puntos(filename, dataLimpia)
        construye_proyeccion(filename)

    filename = ('%s_EA_AREA' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Area_Za', names=['lat', 'lon', 'point'], skiprows=3,
                         usecols='B:D', lineterminator=5)
    dataLimpia = data.dropna(how='any')
    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        # polygon build
        construye_polygon(filename)
        construye_proyeccion(filename)


if __name__ == "__main__":
    procesa()
