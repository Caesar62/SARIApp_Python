__author__ = 'kamome'


##### imports que hagan falta
import numpy as np
from numpy import nan
import os
import pandas as pd
import shapefile as shp
import tkinter
from tkinter import filedialog



def calcula_sru1():
    def construye_puntos(nombre_archivo, lista_puntos_limpia):
        """

        :param nombre_archivo:
        :param lista_puntos_limpia:
        """
        w = shp.Writer(shp.POINT)
        w.field('X', 'F', 10, 5)  # F float, para coordenadas
        w.field('Y', 'F', 10, 5)
        w.field('point')
        # for index,row  in data.iterrows():  #itero entre las filas por el numero de index creado por PANDAS
        for index, row in dataLimpia.iterrows():  # itero entre las filas por el numero de index creado por PANDAS
            w.point(row['lon'], row['lat'])
            w.record(row['lon'], row['lat'], str(row['point']))
        w.save(filename)


    def construye_polygon(nombre_archivo):
        """

        :param nombre_archivo:
        """
        w = shp.Writer(shp.POLYGON)
        w.poly(parts=([line]))
        w.field('point')  # es el campo creado del extractor de PANDAS
        w.record(filename)
        w.save(filename)

        pass


    def construye_polyline(nombre_archivo, archivo_linea):
        w = shp.Writer(shp.POLYLINE)
        w.field("point")  # es el campo creado del extractor de PANDAS
        w.line(parts=([line]))
        w.record("Line")
        w.save(filename)


    def construye_proyeccion(nombre_arhivo):  # USING MANUAL METHOD
        """
        funcion que construye un archivo .prj para que las SHPs puedas ser proyectadas en un GIS
        :param nombre_arhivo:
        :return: No retorna resultados. Construye un archivo.
        """
        prj = open('%s.prj' % filename, 'w')
        proyeccion = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],' \
                     'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
        prj.write(proyeccion)
        prj.close()


    # asking for the save location (path and name)
    file = tkinter.filedialog.askopenfile(initialdir = 'C:\SARIApp_Full\SARIApp_Data\SARIApp_Results',
                                          title='SARIApp Results Spreadsheet')  # asking for the Excel file

    abs_path_file = os.path.abspath(file.name)  # creating the abs path to the file

    file_output_name = os.path.abspath((tkinter.filedialog.asksaveasfile(initialdir = 'C:\SARIApp_Full\SARIApp_Data\SARIApp_GIS',title='Save SHPs files as :')).name)


    #####   EXPORT SRU# 1  PARALLEL
    filename = ('%s_SRU#1_Parallel' % file_output_name)

    data = pd.read_excel(abs_path_file, 'Export_Parallel', names=['lat', 'lon', 'point'], skiprows=4,
                         usecols='B:D')
    dataLimpia = data.dropna(how='any')  # limpio los NaN  ver dropna
    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polyline(filename, line)  # write the polyline shapefile   EXPORT SRU# 1  PARALLEL
        construye_proyeccion(filename)  # write the proj file. Function    EXPORT SRU# 1  PARALLEL
        filename = ('%s_SRU#1_Parallel_wps' % file_output_name)
        construye_puntos(filename, dataLimpia)  # write the point shapefile   EXPORT SRU# 1  PARALLEL  points  wps
        construye_proyeccion(filename)  # write the proj file. Function    EXPORT SRU# 1  PARALLEL  wps

    #####      EXPORT SRU# 1 CREEPING
    filename = ('%s_SRU#1_Creeping' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Creeping', names=['lat', 'lon', 'point'], skiprows=4,
                         usecols='B:D')
    dataLimpia = data.dropna(how='any')  # limpio los NaN  ver dropna

    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polyline(filename, line)  # write the polyline shapefile  EXPORT SRU# 1 CREEPING
        construye_proyeccion(filename)  # write the proj file. Function   EXPORT SRU# 1 CREEPING
        filename = ('%s_SRU#1_Creeping_wps' % file_output_name)
        construye_puntos(filename, dataLimpia)  # write the polyline shapefile  EXPORT SRU# 1 CREEPING wps
        construye_proyeccion(filename)  # write the proj file. Function   EXPORT SRU# 1 CREEPING wps

    #####   EXPORT SRU#1 EXPANDING
    filename = ('%s_SRU#1_Expanding' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Expand', names=['point', 'lat', 'lon'], skiprows=4,
                         usecols='B:D')
    dataLimpia = data.dropna(how='any')  # limpio los NaN  ver dropna

    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polyline(filename, line)  # write the polyline shapefile   EXPORT SRU#1 EXPANDING
        construye_proyeccion(filename)  # write the proj file. Function    EXPORT SRU#1 EXPANDING
        filename = ('%s_SRU#1_Expanding_wps' % file_output_name)
        construye_puntos(filename, dataLimpia)  # write the polyline shapefile   EXPORT SRU#1 EXPANDING wps
        construye_proyeccion(filename)  # write the polyline shapefile   EXPORT SRU#1 EXPANDING wps

    ####    EXPORT SRU#1  SECTOR

    filename = ('%s_SRU#1_Sector' % file_output_name)
    data = pd.read_excel(abs_path_file, 'Export_Sector', names=['point', 'lat', 'lon'], skiprows=4,
                         usecols='B:D')
    dataLimpia = data.dropna(how='any')  # limpio los NaN  ver dropna

    if dataLimpia.empty:
        pass
    else:
        line = [[row['lon'], row['lat']] for index, row in dataLimpia.iterrows()]
        construye_polyline(filename, line)  # write the polyline shapefile    EXPORT SRU#1  SECTOR
        construye_proyeccion(filename)  # write the proj file. Function     EXPORT SRU#1  SECTOR
        filename = ('%s_SRU#1_Sector_wps' % file_output_name)
        construye_puntos(filename, dataLimpia)
        construye_proyeccion(filename)


if __name__=="__main__":
    calcula_sru1()



