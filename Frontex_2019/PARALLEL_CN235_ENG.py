import pandas as pd
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
try:
    os.stat("./SPReport")
except:
    os.mkdir("./SPReport")

# MENU OPCIONES


print(
"""
ENTER DATA FOR "SEARCH ACTION MESSAGE":
"""
)

print ("""
SITUACION
""")

resumen = input("\nRESUMEN\t\t\t\t\t:  ").upper()
descripcion = input("\nDESCRIPCIÓN\t\t\t\t:  ").upper()
personas = input("\nNUMERO DE PERSONAS\t\t\t:  ").upper()
objeto_primario_busqueda = input("\nOBJETO PRIMARIO DE LA BÚSQUEDA\t\t:  ").upper()
objeto_secundario_busqueda = input("\nOBJETO SECUNDARIO DE LA BÚSQUEDA\t:  ").upper()
meteo_onscene = input("\nMETEO EN ZONA\t\t:  ").upper()
area_busqueda = input("\nAREA DE BÚSQUEDA\t\t\t:  ").upper()
mrcc_coordinador = input("\nMRCC\t\t\t:  ").upper()


nombre_unidad = input("\nUNIDAD DE BÚSQUEDA\t:  ").upper()
call_sign = input("\nCALL SIGN\t:  ").upper()
vhf_primario = input("\nVHF PRIMARIO\t:  ").upper()
vhf_secundario = input("\nVHF SECUNDARIO\t:  ").upper()
other_comms = input("\nOTRAS COMUNICACIONES\t:  ").upper()

input("\nPRESS ENTER TO PROCEED PATTERN OPTIONS")



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

        ################## NMEA .CSV ##########################
        with open("./SPReport/{}_SPReportNMEA.csv".format(pattern_name.upper()), "w") as text_file:
            for d in range(len(wpList)):
                print('$IIWPL,{},{},{},{},Pt.{}'.format(
                    (formalat(wpList[d][0]).replace(" ", "")[:-1]),
                    (formalat(wpList[d][0])[-1]),
                    (formalon(wpList[d][1]).replace(" ", "")[:-1]),
                    (formalon(wpList[d][1])[-1]),
                    d
                ), file=text_file)

        ################## SALIDA .TXT ##########################
        with open("./SPReport/{}_SPReport.txt".format(pattern_name.upper()), "w",encoding= "UTF-8") as text_file:
            
            #######################  MENSAJE DE ACCIÓN DE BÚSQUEDA
            
            print("""

IAMSAR SEARCH ACTION MESSAGE


SITUATION:
    SUMMARY:                    {}
    DESCRIPTION:                {}
    PERSONS IN DISTRESS:        {}
    PRIMARY SEARCH OBJECT:      {}
    SECONDARY SEARCH OBJECT:    {}
WEATHER:
     ON SCENE WEATHER:          {}

    SEARCH AREA:                {}
    A {} - {}
    B {} - {}
    C {} - {}
    D {} - {}
PATTERN EXECUTION:    
    PATTERN TYPE: PARALLEL PATTERN
    CSP (COMMENCE SEARCH POINT):        {} - {}
    TRACK LENGHT (LEG)                  {} NM
    SEPARATION (TRACK SPACING)          {} NM
    FIRST TURN (SENSE)                        {}
ASSET:
    {}   CALL SIGN: {}

COORDINATION INSTRUCITIONS:
    M.R.C.C. {}

COMUNICACIONES:
    PRIMARY VHF     {}
    SECONDARY VHF   {}
    OTHER COMMS     {}
    """.format(
                resumen,
                descripcion,
                personas,
                objeto_primario_busqueda,
                objeto_secundario_busqueda,
                meteo_onscene,
                pattern_name,
                formalat(wpList[0][0]),formalon (wpList[0][1]),
                formalat(wpList[1][0]),formalon (wpList[1][1]),
                formalat(wpList[-2][0]),formalon (wpList[-2][1]),
                formalat(wpList[-1][0]),formalon (wpList[-1][1]),

                formalat(wpList[0][0]),formalon (wpList[0][1]),
                leg_length,
                leg_spacing,
                "RIGHT" if giro.upper() == "R" else "LEFT",

                
                nombre_unidad,
                call_sign,
                mrcc_coordinador,

                vhf_primario,
                vhf_secundario,
                other_comms

                ), file=text_file)
                       
 
                        
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
PATT. TOTAL LENGTH\t:  {7} NM
ESP\t\t\t:  {8}  {9}""".format(
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                rumboDistancia[0][0],
                leg_length,
                leg_spacing,
                giro_fms(giro),
                num_legs,
                longitudTotalPattern,
                formalat(wpList[-1][0]),
                formalon(wpList[-1][1])
            ), file=text_file)

            

        ############  CN 235   ############################


            print("""
+-----------------------+
| CN 235 CAM PARAMETERS |
+-----------------------+
SEARCH PATTERN TYPE\t:  PARALLELOGRAM (PS)
CSP \t\t\t:  {0} {1}
ORIENTATION\t\t:  {2}
TRACK LENGHT\t\t:  {3}
NUMBER OF TRACKS\t:  {4}
SENSE\t\t\t:  {5}
TRACK SPACE METHOD\t: {6}
TRACK SPACE\t\t:  {7}
        """.format(
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                rumbo0,
                leg_length,
                num_legs,
                giro_fms(giro),
                " MANUALLY",
                leg_spacing
            ), file=text_file)

        # 235 FMS
            print("""
+-----------------------+
|CN 235 FMS PARAMETERS  |
+-----------------------+
PATTERN TYPE\t\t:  PARALLEL RISING LADDER
IWPT INITIAL WAYPOINT\t:  {0} {1}
ITRK INITIAL TRACK\t:  {2}
IRTN INITIAL TURN DIR\t:  {3}
LNTH LEG LEGHT\t\t:  {4}
LSPC LEG SEPARATION\t:  {5}
SEARCH SPEED\t\t:  {6}

CSP COMMENCE SEARCH P\t:  {7} {8}
ESP END SEARCH P\t:  {9} {10}""".format(
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                rumbo0,
                giro_fms(giro),
                leg_length,
                leg_spacing,
                "DEFAULT 148 KIAS",
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                formalat(wpList[-1][0]),
                formalon(wpList[-1][1])
            ), file=text_file)

        # 235 FITS
            print("""
+-----------------------+
|CN 235 FITS PARAMETERS |
+-----------------------+
PATTERN TYPE\t\t:  PARALLEL SEARCH
CSP COMMENCE SEARCH P\t:  {0} {1}
ORIENTATION\t\t:  {2}
SENSE\t\t\t:  {3}
NUMBER OF TRACKS\t:  {4}
TRACK SPACE\t\t:  {5}
SEARCH SPEED\t\t:  {6}
ESP END SEARCH P\t:  {7} {8}""".format(
                formalat(wpList[0][0]),
                formalon(wpList[0][1]),
                rumbo0,
                giro_fms(giro),
                num_legs,
                leg_spacing,
                "DEFAULT ",
                formalat(wpList[-1][0]),
                formalon(wpList[-1][1])
            ), file=text_file)




# PATTERN
            print("""
+---------------------+
|PATTERN WAYPOINTS    |
+---------------------+""", file=text_file)
            for d in range(len(wpList)):
                print('WP{:02}\t\t:  {}  {}'.format(d, formalat(
                    wpList[d][0]), formalon(wpList[d][1])), file=text_file)

            print("""
+---------------------+
|PATTERN TRACKS       |
+---------------------+""", file=text_file)
            for e in range(len(rumboDistancia)):
                print('TRK{:02}\t\t:  {:06.2f}  {:05.2f} NM'.format(
                    e+1, rumboDistancia[e][0], rumboDistancia[e][1]), file=text_file)

        ################## SALIDA GEOJSON ##########################

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




        #################  CSV ##########################

        df = pd.DataFrame(wpList,columns=["latitude", "longitude"])
        df.to_csv(
            "./SPReport/{}_SPReport_WPList.csv".format(pattern_name.upper())
        )
        

        # INFORMACION FINAL CONSOLA.

        print("""
\t+---------------------+
\t|    SEARCH PATTERN   |
\t+---------------------+
\t
\tCSP COMENCE SEARCH POINT\t:  {0}  {1}
\tCSC COMENCE SEARCH COURSE\t:  {2}
\tTRACK LENGHT\t\t\t:  {3}
\tTRACK SPACING\t\t\t:  {4}
\tFIRST TURN\t\t\t:  {5}
\tPATTERN WIDTH\t\t\t:  {6}
\tNUMBER OF LEGS\t\t\t:  {7}
\tPATTERN TOTAL LENGTH\t\t:  {8} NM
\tESP END SEARCH POINT\t\t:  {9}  {10}""".format(
            formalat(wpList[0][0]),
            formalon(wpList[0][1]),
            rumbo0,
            leg_length,
            leg_spacing,
            giro_fms(giro),
            pattern_width,
            num_legs,
            longitudTotalPattern,
            formalat(wpList[-1][0]),
            formalon(wpList[-1][1])
        ))

        print('\n')

        print("""
+---------------------+
|PATTERN WAYPOINTS    |
+---------------------+""")
        for d in range(len(wpList)):
            print('WP{:02}\t\t:  {}  {}'.format(
                d, formalat(wpList[d][0]), formalon(wpList[d][1])))

        print("""
+---------------------+
|PATTERN TRACKS       |
+---------------------+""")
        for e in range(len(rumboDistancia)):
            print('TRK{:02}\t\t:  {:06.2f}  {:05.2f} NM'.format(
                e+1, rumboDistancia[e][0], rumboDistancia[e][1]))


    elif opcion == "2":
        print("""
\t+-----------------------------------------------------------------+
\t|           PATRON DE BUSQUEDA.PARALLEL                           |
\t|           CSP AT THE CENTER POINN OF THE SEARCH AREA SIDE       |
\t+-----------------------------------------------------------------+
        """)
        lat0 = float(input("\n\tLATITUD GG.ggg\t\t\t:  "))
        lon0 = float(input("\n\tLONGITUD GGG.ggg\t\t:  "))
        rumbo0 = float(input("\n\tRUMBO INICIAL\t\t\t:  "))
        leg_length = float(input("\n\tLARGO DEL PATRON DE BUSQUEDA\t:  "))
        pattern_width = float(input("\n\tANCHO DEL PATRON DE BUSQUEDA\t:  "))
        leg_spacing = float(input("\n\tLEG SPACING\t\t\t:  "))
        pattern_name = input("\n\tPATTERN NAME\t\t\t:  ")

        num_legs = int(pattern_width//leg_spacing)
        wpList = [[lat0, lon0]]
        wpListReverse = [[lon0, lat0]]

        # FUNCIONES
        lista_distancias = []
        for i in range(1, int(num_legs)+1):
            lista_distancias.append(leg_length)
            lista_distancias.append(i*leg_spacing)
            lista_distancias = lista_distancias[0:(num_legs*2)]

        lista_rumbos = []
        for j in range(int(num_legs)):
            lista_rumbos.append(quita360(rumbo0))
            lista_rumbos.append(quita360(rumbo0+90))
            lista_rumbos.append(quita360(rumbo0+180))
            lista_rumbos.append(quita360(rumbo0+270))
            lista_rumbos = lista_rumbos[0:((num_legs*2))]

        rumboDistancia = []
        for k in range(len(lista_rumbos)):
            rumboDistancia.append([lista_rumbos[k], lista_distancias[k]])

        # LISTA DE WAYPOINTS [lat, lon]   wpList

        for w in range((len(rumboDistancia)-1)):
            # for w in range(num_wps-1):
            wpList.append(
                Directa(wpList[w][0], wpList[w][1], rumboDistancia[w][0], rumboDistancia[w][1]))
        # LISTA DE WAYPOINTS [lon,lat] wpListReverse
        for z in range(len(rumboDistancia)-1):
            # for z in range(num_wps-1):
            wpListReverse.append(DirectaReverse(
                wpList[z][0], wpList[z][1], rumboDistancia[z][0], rumboDistancia[z][1]))

        longitudTotalPattern = 0
        for elemento in rumboDistancia:
            longitudTotalPattern = longitudTotalPattern+elemento[1]

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

#########################  CSV  ##############################33


        df = pd.DataFrame(wpList,columns=["latitude", "longitude"])
        df.to_csv("./SPReport/{}_SPReport_WPList.csv".format(pattern_name.upper()),index=False)
        



        # CONSOLA

        print("""
\t+---------------------+
\t|    SEARCH PATTERN   |
\t+---------------------+
\t PATTERN TYPE:   AW139 PARALLEL PATTERN SEARCH 
\tCSP COMENCE SEARCH POINT\t:  {0}  {1}
\tCSC COMENCE SEARCH COURSE\t:  {2}
\tTRACK LENGHT\t\t\t:  {3}
\tTRACK SPACING\t\t\t:  {4}
\tFIRST TURN\t\t\t:  {5}
\tPATTERN WIDTH\t\t\t:  {6}
\tNUMBER OF LEGS\t\t\t:  {7}
\tPATTERN TOTAL LENGTH\t\t:  {8} NM
\tESP END SEARCH POINT\t\t:  {9}  {10}""".format(
            formalat(wpList[0][0]),
            formalon(wpList[0][1]),
            rumbo0,
            leg_length,
            leg_spacing,
            "DEFAULT RIGHT",
            pattern_width,
            num_legs,
            longitudTotalPattern,
            formalat(wpList[-1][0]),
            formalon(wpList[-1][1])
        ))

        print("""
+---------------------+
|PATTERN WAYPOINTS    |
+---------------------+""")
        for d in range(len(wpList)):
            print('WP{:02}\t\t:  {}  {}'.format(
                d, formalat(wpList[d][0]), formalon(wpList[d][1])))

        print("""
+---------------------+
PATTERN TRACKS        |
+---------------------+""")
        for e in range(len(rumboDistancia)):
            print('TRK{:02}\t\t:  {:06.2f}  {:05.2f} NM'.format(
                e+1, rumboDistancia[e][0], rumboDistancia[e][1]))

        ################## NMEA .CSV ##########################
        with open("./SPReport/{}_SPReportNMEA.csv".format(pattern_name.upper()), "w") as text_file:
            for d in range(len(wpList)):
                print('$IIWPL,{},{},{},{},Pt.{}'.format(
                    (formalat(wpList[d][0]).replace(" ", "")[:-1]),
                    (formalat(wpList[d][0])[-1]),
                    (formalon(wpList[d][1]).replace(" ", "")[:-1]),
                    (formalon(wpList[d][1])[-1]),
                    d
                ), file=text_file)

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
+---------------------+
|PATTERN WAYPOINTS    |
+---------------------+""", file=text_file)
            for d in range(len(wpList)):
                print('WP{:02}\t\t:  {}  {}'.format(d, formalat(
                    wpList[d][0]), formalon(wpList[d][1])), file=text_file)

            print("""
+---------------------+
PATTERN TRACKS        |
+---------------------+""", file=text_file)
            for e in range(len(rumboDistancia)):
                print('TRK{:02}\t\t:  {:06.2f}  {:05.2f} NM'.format(
                    e+1, rumboDistancia[e][0], rumboDistancia[e][1]), file=text_file)

    elif opcion == "3":
        print("\n Goodbye")
        opcion = None
    else:
        print("\n Not Valid Choice Try again")
