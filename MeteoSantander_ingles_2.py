
# coding: utf-8
import os
import re
import requests
from bs4 import BeautifulSoup
import time
import urllib
import urllib.request
import xml.etree.ElementTree as ET
import datetime

'''
respuesta = requests.get("http://weather.gmdss.org/Coruna.html")
soup_coruna = BeautifulSoup(respuesta.content, features="lxml")
href_tags = soup_coruna.find_all(href=True)

link_navtex_coruna = "http://weather.gmdss.org/{}".format(re.findall("bulletins/METAREA2.NAVTEX.CORUNA.FORECAST.*html",str(href_tags))[0])

meteo_alta_ingles = requests.get(link_navtex_coruna)

texto_limpio = meteo_alta_ingles.text.replace("\\n"," ").replace("\n"," ")

regex = r"CANTABRICO:(.*)PORTO"

alta_mar_cantabrico_ingles =re.findall(regex, texto_limpio)[0]


feed_altamar = urllib.request.urlopen("http://www.aemet.es/xml/maritima/FQNT42MM.xml")   #alta mar atlantico
tree_altamar = ET.parse(feed_altamar)
root_altamar = tree_altamar.getroot()

alta_mar_valido_hasta = root_altamar.findall("prediccion/fin")[0].text
alta_mar_cantabrico = list(root_altamar.find("*/zona[@id='9109']")[0].text)
print(alta_mar_cantabrico)
'''

# ALTA MAR CANTABRICO
#http://www.aemet.es/es/eltiempo/prediccion/maritima?opc1=1&opc2=martot&opc3=1&area=atl1&zona=9109_Cantabrico

#Extraccion de datos altamar Cantabrico
request_altmar_cantabrico = requests.get('http://www.aemet.es/es/eltiempo/prediccion/maritima?opc1=1&opc2=martot&opc3=1&area=atl1&zona=9109_Cantabrico')
soup_altamar_cantabrico = BeautifulSoup(request_altmar_cantabrico.content, features="lxml")
busca_cantabrico_fecha= soup_altamar_cantabrico.find_all('h3',{'class':"texto_entradilla"})

#Fecha elaboración aviso altamar
#texto_cantabrico_fecha = busca_cantabrico_fecha[0].text
busca_fecha_inicio_altaMar = soup_altamar_cantabrico.find_all('div',{'class':'contenedor_central marginbottom35px'})
texto_cantabrico_fecha = re.search(r'Fecha de inicio:(.*)\nFec',(busca_fecha_inicio_altaMar[1].text),re.DOTALL)

#Texto aviso altamar
busca_cantabrico= soup_altamar_cantabrico.find_all('div',{'class':"texto_normal"})
texto_aviso_cantabrico = re.search(r'Fecha de fin:(.*)',(busca_cantabrico[1].text),re.DOTALL)
aviso_cantabrico = busca_cantabrico[0].text  # texto

#Fecha de prediccion altamar
busca_fecha_fin_altaMar = soup_altamar_cantabrico.find_all('div',{'class':'contenedor_central marginbottom35px'})
texto_fecha_fin_altaMar = re.search(r'Fecha de fin:(.*)',busca_fecha_fin_altaMar[1].text)

#Texto prediccion altamar
altaMarCantabrico = busca_cantabrico[1].text # texto


# AGUAS COSTERAS CANTABRICO
# http://www.aemet.es/es/eltiempo/prediccion/maritima?opc1=0&opc2=martot&opc3=1&area=can1
rCostCantabrico = requests.get('http://www.aemet.es/es/eltiempo/prediccion/maritima?opc1=0&opc2=martot&opc3=1&area=can1')
soup_costeras_cantabrico = BeautifulSoup(rCostCantabrico.content, features="lxml")
busca_cantabria_fecha= soup_costeras_cantabrico.find_all('div',{'class':"notas_tabla"})

#Fecha elaboración aviso costero
texto_cantabria_fecha = re.search(r'Fecha de inicio:(.*)\nFec',(busca_cantabria_fecha[1].text),re.DOTALL)

#Texto aviso costero
busca_cantabria= soup_costeras_cantabrico.find_all('div',{'class':"texto_normal"})
texto_aviso_cantabria = re.search(r'Fecha de fin:(.*)',(busca_cantabria[1].text),re.DOTALL)
aviso_cantabria = busca_cantabria[0].text  # texto

#Prediccion costera valida hasta
busca_fecha_fin_costeras =soup_costeras_cantabrico.find_all('div',{'class':'notas_tabla'})
texto_fecha_fin_costeras = re.search(r'Fecha de fin:(.*)',busca_fecha_fin_costeras[1].text)
# fomateado  ::    texto_fecha_fin_costeras.group(1).replace('\xa0',' ')

#TEXTO AGUAS COSTERAS CANTABRIA
busca_costeras_cantabrico = soup_costeras_cantabrico.find_all('div',{'class':"contenedor_central"})
texto_costera_cantabria = re.search(r'Aguas costeras de Cantabria(.*)Aguas costeras de B',(busca_costeras_cantabrico[1].text),re.DOTALL)

with open ('meteo.txt','w') as archivo_texto:
    print('INFORMACION METEOROLOGICA PARA CANTABRICO Y C.A. DE CANTABRIA. CCS SANTANDER',file=archivo_texto)
    print('\nALTA MAR: CANTABRICO'.upper(),file=archivo_texto)
    #print('\nAVISO ELABORADO EL:', texto_cantabrico_fecha.strip().replace('\xa0','').upper(),file=archivo_texto)
    print('\nAVISO ELABORADO EL:',texto_cantabrico_fecha.group(1).replace('\xa0',' ').upper(),file=archivo_texto)
    print(aviso_cantabrico.strip().upper(),file=archivo_texto)
    print('\nPREDICCIÓN VÁLIDA HASTA:',texto_fecha_fin_altaMar.group(1).replace('\xa0',' ').upper(),file=archivo_texto)
    print(altaMarCantabrico.strip(),file=archivo_texto)
    #print("\nOPEN SEA AREAS SHIPPING FORECAST VALID UNTIL : {}".format((alta_mar_valido_hasta.replace("T", "  ")).replace("00:00", "00  UTC")), file=archivo_texto)
    #print("{}".format(alta_mar_cantabrico_ingles), file=archivo_texto)
    print('\n')
    print('\n\n\nAGUAS COSTERAS: CANTABRIA'.upper(),file=archivo_texto)
    print('\nAVISO ELABORADO EL:',texto_cantabria_fecha.group(1).replace('\xa0','').upper(),file=archivo_texto)
    print(aviso_cantabria.strip().upper(),file=archivo_texto)
    print('\nPREDICIÓN VÁLIDA HASTA:',texto_fecha_fin_costeras.group(1).replace('\xa0',' ').upper(),file=archivo_texto )
    print(texto_costera_cantabria.group(1).strip(),file = archivo_texto)

os.startfile('meteo.txt')
