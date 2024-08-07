import folium
from folium import plugins
from folium.plugins import Draw
from folium.plugins import MeasureControl
from folium import features
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
    DirectaReverse)

pattern_name = "PRUEBA_1"
pattern_width = 10
leg_spacing = 0.5
lat0 = 43.5
lon0 = -3.5

num_legs = int(pattern_width//leg_spacing+1)
print("Numero de patas: ",num_legs)

num_wps = num_legs*2
num_tracks = num_legs*2-1
rumboDistancia = []
wpList = ([lat0, lon0])
wpListReverse = ([lon0, lat0])
print(num_wps)
print(num_tracks)
print(wpList)

################## SALIDA .TXT ##########################
with open("./SPReport/{}_SPReport.txt".format(pattern_name.upper()), "w",encoding= "UTF-8") as text_file:

    print(formalat(wpList[0])," ",formalon(wpList[1]))
    print("""
    +-----------------------+
    |    SEARCH PATTERN     |
    +-----------------------+
    CSP\t\t\t:  {0}  {1}""".format(
                    formalat(wpList[0]),
                    formalon(wpList[1])
                ), file=text_file)

    print("""
\t+-----------------------------------------------------------------+
\t|           PATRON DE BUSQUEDA.PARALLEL LADDER SEARCH             |
\t|           CSP IN A CORNER OF THE SEARCH AREA                    |
\t+-----------------------------------------------------------------+
        """)
    lat0 = float(input("\n\tLATITUD GG.ggg\t\t\t:  "))
    lon0 = float(input("\n\tLONGITUD GGG.ggg\t\t:  "))
    rumbo0 = float(input("\n\tRUMBO INICIAL\t\t\t:  "))
    leg_length = float(input("\n\tLARGO DEL PATRON DE BUSQUEDA\t:  "))
    pattern_width = float(input("\n\tANCHO DEL PATRON DE BUSQUEDA\t:  "))
    leg_spacing = float(input("\n\tLEG SPACING\t\t\t:  "))
    giro = input("\n\tSENSE (GIRO) L OR R\t\t:  ")
    pattern_name = input("\n\tPATTERN NAME\t\t\t:  ")

    num_legs = int(pattern_width//leg_spacing+1)

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

    # LISTA DE WAYPOINTS [lat, lon]   wpList
    for w in range(num_wps-1):
        wpList.append(
            Directa(wpList[w][0], wpList[w][1], rumboDistancia[w][0], rumboDistancia[w][1]))
    # LISTA DE WAYPOINTS [lon,lat] wpListReverse
    for z in range(num_wps-1):
        wpListReverse.append(DirectaReverse(
            wpList[z][0], wpList[z][1], rumboDistancia[z][0], rumboDistancia[z][1]))
    
    ################## SALIDA CONSOLA ##########################

    def giro_fms(giro): return 'RIGHT'if giro.upper() == 'R' else 'LEFT'
    patternTrack = rumbo0+90 if giro.upper() == "R" else rumbo0-90
    patternTrack = patternTrack if patternTrack <= 360 else patternTrack-360
    patternTrack = patternTrack if patternTrack > 0 else patternTrack+360

    longitudTotalPattern = 0
    for elemento in rumboDistancia:
        longitudTotalPattern = longitudTotalPattern+elemento[1]