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

feed_altamar = urllib.request.urlopen("http://www.aemet.es/xml/maritima/FQNT42MM.xml")   #alta mar atlantico
tree_altamar = ET.parse(feed_altamar)
root_altamar = tree_altamar.getroot()

alta_mar_valido_hasta = root_altamar.findall("prediccion/fin")[0].text
alta_mar_cantabrico = root_altamar.find("*/zona[@id='9109']")[0].text
#print(alta_mar_valido_hasta)
#print(alta_mar_cantabrico)

#Texto aviso altamar
feed_altamar = urllib.request.urlopen("https://www.aemet.es/xml/maritima/WONT40MM.xml")   #aviso alta mar atlantico
tree_aviso_altamar = ET.parse(feed_altamar)
root_aviso_altamar = tree_aviso_altamar.getroot()

aviso_altamar_valido_hasta = root_aviso_altamar.findall("origen/fin")[0].text
aviso_alta_mar_cantabrico = root_aviso_altamar.find("*/zona[@id='9106']")[0].text

print(aviso_altamar_valido_hasta)
print(aviso_alta_mar_cantabrico)


with open ('meteo.txt','w') as archivo_texto:
    print('INFORMACION METEOROLOGICA PARA CANTABRICO Y C.A. DE CANTABRIA. CCS SANTANDER',file=archivo_texto)
    print('\nALTA MAR: CANTABRICO'.upper(),file=archivo_texto)
    #print('\nAVISO ELABORADO EL:', texto_cantabrico_fecha.strip().replace('\xa0','').upper(),file=archivo_texto)
    #print('\nAVISO ELABORADO EL:',texto_cantabrico_fecha.group(1).replace('\xa0',' ').upper(),file=archivo_texto)
    print('\nPREDICCION VALIDA HASTA EL:', alta_mar_valido_hasta.strip().replace('T',' ').upper(),'UTC',file=archivo_texto)
    #print('\n',aviso_alta_mar_cantabrico.strip().upper(),file=archivo_texto)
    
    print('\n', file=archivo_texto)
    
os.startfile('meteo.txt')
