import pandas as pd
import xlrd
import openpyxl
import json
import math
import os
import webbrowser
from sartools.estima import(    # paquete.modulo  en el paquete estará el __init__.py
    quita360,
    deg_to_rad,
    rad_to_deg,
    formalat,
    formalon,
    Directa,
    DirectaReverse
)

# Crea el directorio SPReport
try:
    os.stat("./SPReport")
except:
    os.mkdir("./SPReport")
    
# Entrada de datos
lat0 = float(input("\n\tLATITUD GG.ggg\t\t\t:  "))
lon0 = float(input("\n\tLONGITUD GGG.ggg\t\t:  "))
rumbo0 = float(input("\n\tRUMBO INICIAL\t\t\t:  "))
leg_length = float(input("\n\tLARGO DEL PATRON DE BUSQUEDA\t:  "))
pattern_width = float(input("\n\tANCHO DEL PATRON DE BUSQUEDA\t:  "))
leg_spacing = float(input("\n\tLEG SPACING\t\t\t:  "))
giro = input("\n\tSENSE (GIRO) L OR R\t\t:  ")
pattern_name = input("\n\tPATTERN NAME\t\t\t:  ")

# Calculo del número de patas a ejecutar
num_legs = int(pattern_width//leg_spacing+1)
print(num_legs)

# Calculo del Rumbos y distancias de cada una de las patas a ejecutar
num_wps = num_legs*2
num_tracks = num_legs*2-1
rumboDistancia = []
wpList = [[lat0, lon0]]
wpListReverse = [[lon0, lat0]]

j = 1
if giro.upper() == "R":
    while j <= num_legs*2-1:
        rumboDistancia.extend(([quita360(rumbo0), leg_length], ([quita360(rumbo0 + 90), leg_spacing]),
                                ([quita360(rumbo0+180), leg_length]),
                                ([quita360(rumbo0 + 90), leg_spacing])
                                ))
        j = j+4
        rumboDistancia = rumboDistancia[0:num_tracks]
else:
    while j <= num_legs*2-1:
        rumboDistancia.extend(([quita360(rumbo0), leg_length], ([quita360(rumbo0 + 270), leg_spacing]),
                                ([quita360(rumbo0+180), leg_length]),
                                ([quita360(rumbo0 + 270), leg_spacing])
                                ))
        j = j+4
        rumboDistancia = rumboDistancia[0:num_tracks]
        
print(rumboDistancia)

# LISTA DE WAYPOINTS [lat, lon]   wpList
for w in range(num_wps-1):
    wpList.append(
        Directa(wpList[w][0], wpList[w][1], rumboDistancia[w][0], rumboDistancia[w][1]))
'''
# LISTA DE WAYPOINTS [lon,lat] wpListReverse
for z in range(num_wps-1):
    wpListReverse.append(DirectaReverse(
        wpList[z][0], wpList[z][1], rumboDistancia[z][0], rumboDistancia[z][1]))
'''

print()   
print(wpList)
print(len(wpList))

################## NMEA .CSV ##########################
with open("./SPReport/{}_SPReportNMEA.csv".format(pattern_name.upper()), "w") as text_file:
    for d in range(len(wpList)):
        print('$IIWPL,{},{},Pt.{}'.format(
            (formalat(wpList[d][0])),
            (formalon(wpList[d][1])),
            d), file=text_file)

print(wpList[2])


# Uso de Pandas. Extracción de datos
#df = pd.read_excel('C:/Users/cesai/Desktop/SARIApp Python/SPReport/XX_SPReportNMEA.csv')
#df.head()