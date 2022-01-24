import qgis
from qgis.analysis import *
QgsGeometryAnalyzer().buffer(layer,r'C:\SARIApp_Full\SARIApp_Data\SARIApp_GIS\A1_4_TRACKING_LINE.shp',0.1)
