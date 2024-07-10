import pandas as pd
import json
import math
import os
import webbrowser
import folium
from folium import plugins
from folium.plugins import Draw
from folium.plugins import MeasureControl
from sartools.estima import(    # paquete.modulo  en el paquete estará el __init__.py
    quita360,
    deg_to_rad,
    rad_to_deg,
    formalat,
    formalon,
    Directa,
    DirectaReverse
)
try:
    os.stat("./SPReport")
except:
    os.mkdir("./SPReport")

opcion = True
while opcion:
    print("""
    1.Parallel Pattern CSP in a corner of the search area
    2.Parallel Pattern CSP at the center point on the side of the search area
    3.Exit/Quit
    """)
    opcion = input("What would you like to do? ")
    if opcion == "1":
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
        print(wpList)
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

                ################## SALIDA .TXT ##########################
        with open("./SPReport/{}_SPReport.txt".format(pattern_name.upper()), "w") as text_file:

            
            print("""
+-----------------------+
|    SEARCH PATTERN     |
+-----------------------+
CSP\t\t\t:  {0}  {1}
CSC\t\t\t:  {2}
LENGHT\t\t\t:  {3}
SPACING\t\t\t:  {4}
TURN\t\t\t:  {5}
LEGS\t\t\t:  {6}
PATTERN TOTAL LENGTH\t:  {7} NM
ESP\t\t\t:  {8}  {9}""".format(
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                rumboDistancia[0][0],
                leg_length,
                leg_spacing,
                "DEFAULT RIGHT",
                num_legs,
                longitudTotalPattern,
                formalat(wpList[-1][0]),
                formalon(wpList[-1][1])
            ), file=text_file)

            print("""
+-----------------------+
|AW 139 FMS PARAMETERS  |
+-----------------------+
SEARCH TYPE\t\t:  PARALLEL PATTERN SEARCH
1L\tSTART POSICION\t:  {0} {1}
2L\tTURN DIRECTION\t:  {2}  
2R\tINITIAL TRACK\t:  {3}
3L\tLEG SPACE\t:  {4}
3R\tPATTERN WIDTH\t:  {5}
4L\tSPEED\t\t:  {6}
4R\tPATTERN LENGTH\t:  {7}""".format(  # {7:05.2f}
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                'DEFAULT (RIGHT)',
                rumboDistancia[0][0],
                leg_spacing,
                num_legs*leg_spacing,
                "DEFAULT 90 KIAS",
                leg_length
            ), file=text_file)

#################  GEOJSON ##########################
        data = {}
        data["type"] = "FeatureCollection"
        data["features"] = [{
            "type": "Feature",
            "properties": {},
            "geometry": {
                    "type": "Point",
                    "coordinates": wpListReverse[0]
            },
            "properties": {
                "name": "CSP"
            }
        },
            {
            "type": "Feature",
            "properties": {},
            "geometry": {
                    "type": "Point",
                    "coordinates": wpListReverse[-1]
            },
            "properties": {
                "name": "ESP"
            }
        },
            {"type": "Feature",
             "properties": {},
             "geometry": {
                 "type": "LineString",
                 "coordinates": wpListReverse
             }
             }]

        # VOLCAR DATOS A ARCHIVO
        # with open("C:\\SPRreport\SPReport.geojson", "w") as outfile:
        with open("./SPReport/{}_SPReport.geojson".format(pattern_name.upper()), "w") as outfile:
            json.dump(data, outfile)

        # MAPA

        map = folium.Map(
            location=[lat0, lon0],
            tiles='cartodbpositron',
            zoom_start=10
        )

        # MAP TOOLS PLUGIN
        draw = Draw()
        draw.add_to(map)

        folium.GeoJson("SPReport/{}_SPReport.geojson".format(pattern_name.upper()),
                       name=pattern_name.upper()).add_to(map)

        plugins.Fullscreen(
            position="topright",
            force_separate_button=True).add_to(map)

        folium.LayerControl().add_to(map)

        map.add_child(MeasureControl())

        map.save("pattern.html")
        webbrowser.open("pattern.html")
        map

    elif opcion == "3":
        print("\n Goodbye")
        opcion = None
    else:
        print("\n Not Valid Choice Try again")  
