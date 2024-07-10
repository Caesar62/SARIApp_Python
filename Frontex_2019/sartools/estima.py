"""
librería de funciones.


quita360        FUNCION PARA QUITARLE 360 GRADOS A UN VALOR ANGULAR
deg_to_rad      GRADOS SEXAGESIMALES A RADIANES
rad_to_deg      RADIANES A SEXAGESIMALES
formalat        FORMATEA LATITUD
formalon        FORMATEA LONGITUD
Directa         ESTIMA DIRECTA
DirectaReverse  ESITMA DIRECTA REVERSE
Inversa         ESTIMA INVERSA
"""



import math

def quita360(x): return x if x <= 360 else x-360

def deg_to_rad(degree): return degree*math.pi/180

def rad_to_deg(radian): return radian*180/math.pi

def formalat(lat):
    if lat >= 0:
        signolat = 'N'
    else:
        signolat = 'S'
    return "{:02} {:06.3f} {}".format(int(abs(lat)), (abs(lat) - abs(int(lat)))*60, signolat)


def formalon(lon):
    if lon >= 0:
        signolon = 'E'
    else:
        signolon = 'W'
    return "{:03} {:06.3f} {}".format(int(abs(lon)), (abs(lon) - abs(int(lon)))*60, signolon)

# ESTIMA DIRECTA CON RETURN EN [lat,lon]

def Directa(lat0, lon0, rumbo, distancia):
    diferencia_latitud = distancia * math.cos(deg_to_rad(rumbo))
    lat1 = lat0 + (diferencia_latitud/60)
    apartamiento = distancia * math.sin(deg_to_rad(rumbo))
    latitud_media = (lat0+lat1)/2
    diferencia_longitud = apartamiento / \
        (math.cos(deg_to_rad(latitud_media)))
    lon1 = lon0 + (diferencia_longitud / 60)
    return [lat1, lon1]


# ESTIMA DIRECTA CON RETURN EN [lon,lat]
def DirectaReverse(lat0, lon0, rumbo, distancia):
    diferencia_latitud = distancia * math.cos(deg_to_rad(rumbo))
    lat1 = lat0 + (diferencia_latitud/60)
    apartamiento = distancia * math.sin(deg_to_rad(rumbo))
    latitud_media = (lat0+lat1)/2
    diferencia_longitud = apartamiento / \
        (math.cos(deg_to_rad(latitud_media)))
    lon1 = lon0 + (diferencia_longitud / 60)
    return [lon1, lat1]

def Inversa(lat0, lon0, lat1, lon1):
    diferencia_latitud = (lat1-lat0)
    diferencia_longitud = (lon1-lon0)
    latitud_media = (lat0+lat1)/2
    apartamiento = diferencia_longitud * math.cos(deg_to_rad(latitud_media))
    rumbo = math.atan(deg_to_rad(apartamiento/diferencia_latitud))
    distancia = diferencia_latitud/math.cos(deg_to_rad(rumbo))
    return [rumbo, distancia]


if __name__=="main":
    pass