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

lat0 = 43.5
lon0 = -3.5
giro = "R"
pattern_width = 5
leg_length = 10
leg_spacing = 1
rumbo0 = 45
pattern_name = 'prueba'

num_legs = int(pattern_width//leg_spacing + 1)
num_tracks = num_legs*2-1 # 11
num_wps = num_legs*2 # 12
rumboDistancia = []
wpList = [[lat0, lon0]]

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
print(len(rumboDistancia))

# LISTA DE WAYPOINTS [lat, lon]   wpList
for w in range(num_wps-1):
    wpList.append(
        Directa(wpList[w][0], wpList[w][1], rumboDistancia[w][0], rumboDistancia[w][1]))

print()   
print(wpList)
print()
print(len(wpList))

################## NMEA .CSV ##########################
with open("./SPReport/{}_SPReportNMEA.csv".format(pattern_name.upper()), "w") as text_file:
    for d in range(len(wpList)):
        print('{},{},{},Pt.{}'.format(d,
            (formalat(wpList[d][0])),
            (formalon(wpList[d][1])),
            d), file=text_file)

# Uso de Pandas. Extracción de datos
df = pd.read_excel('PRUEBA_SPReportNMEA.csv', sep = ",")
df.head()