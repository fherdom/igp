# -*- coding: utf-8 -*-
"""
***************************************************************************
Name			 	 : Geocoding
Description          : Geocoding and reverse Geocoding using Google
Date                 : 28/May/09
copyright            : (C) 2009 by ItOpen
email                : info@itopen.it
 ***************************************************************************/

 /***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.core import *
from qgis.gui import *

MATRIX = {
    u'pendiente': [
        [1, 0, 20, u'Pte. Fuerte (superior al 30%) y/o terreno escarpado.'],
        [3, 20, 30, u'Pte. Media (20-30 %) y/o terreno aledaño ondulado-accidentado.'],
        [5, 30, 100, u'Pte. Fuerte (superior al 30%) y/o terreno escarpado.']
    ],
    u'accesibilidad': [
        [1, u'alta', None, u'Accesibilidad Alta por viales y/o buen tránsito de vehículos fuera de ellos.'],
        [3, u'media', None, u'Accesibilidad Media por viales y/o regular tránsito de vehículos fuera de ellos.'],
        [5, u"baja", None, u"Accesibilidad Baja por viales y/o nulo tránsito de vehículos fuera de ellos."]
    ],
    u'combustibilidad': [
        [1, u'baja', None, u'Combustibilidad Baja (Mod. 8,9,10,11)'],
        [3, u'media', None, u'Combustibilidad Media (Mod. 5,7 y 2)'],
        [5, u'alta', None, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)']
    ],
    u'continuidad': [
        [1, 1, None, u'Continuidad Nivel 1. (Fcc menor del 33%, y/o 10 metros de distancia de F.S del frente de llama)'],
        [3, 2, None, u'Continuidad Nivel 2. (Fcc 33-66% y/o 10-100 metros de distancia del F.S del Frente de llama)'],
        [5, 3, None, u'Continuidad Nivel 3. (Fcc mayor del 66% y/o más de 100 metros de distancia del F.S del frente de llama)']
    ],
    u'viento': [
        [1, 0, 10, u'Velocidad de Viento Baja (menor o igual a 10 km/h)'],
        [3, 10, 30, u'Velocidad viento Media  (10-30 km/h)'],
        [5, 30, 100, u'Velocidad de Viento Alta (más de 30 km/h)']
    ],
    u'temperatura': [
        [1, 0, 25, u'Temperatura Baja (menor igual a 25 ºC)'],
        [3, 25, 39, u'Temperatura Media  (26-39 ºC)'],
        [5, 39, 999, u'Temperatura Alta (más de 40ºC)']
    ],
    u'ede': [
        [5, 1, None, u'Presencia de E.D.E. en el área de afección del incendio y/o futura progresión del mismo (Área recreativa, Campings, Hospitales, colegios etc.).']
    ],
    u'iier': [
        [5, 1, None, u'Presencia de I.I.E.R. en el área de afección del incendio y/o futura progresión del mismo (Bases aéreas, gasolineras, Centrales de producción de electricidad, vías de comunicación de primer orden etc.).']
    ],
    u'evacuacion': [
        [5, 1, None, u'Evacuación de la población de sus viviendas o municipios en el área de afección del incendio y/o futura progresión del mismo.']
    ],
    u'patrimonio': [
        [5, 1, None, u'Afección de elementos y/o lugares de especial relevancia catalogados y protegidos de carácter histórico artístico.']
    ],
    u'ecologico': [
        [5, 1, None, u'Afección de espacios de especial relevancia ecológica catalogados y protegidos, así como elementos que por su singularidad rareza o difícil perpetuidad también gocen de especial protección']
    ]
}


class ClickTool(QgsMapTool):
    def __init__(self,iface, callback):
        QgsMapTool.__init__(self,iface.mapCanvas())
        self.iface      = iface
        self.callback   = callback
        self.canvas     = iface.mapCanvas()
        return None


    def canvasReleaseEvent(self,e):
        point = self.canvas.getCoordinateTransform().toMapPoint(e.pos().x(),e.pos().y())
        self.callback(point)
        return None

def get_dest_projection():
    """
    Returns project projection
    """
    
    """
    p = QgsProject.instance()
    (proj4string,ok) = p.readEntry("SpatialRefSys","ProjectCRSProj4String")
    if not ok :
        return None
    crs = QgsCoordinateReferenceSystem()
    crs.createFromProj4(proj4string)
    """
    
    # TODO: CHANGE
    crs = QgsCoordinateReferenceSystem()
    #crs.createFromProj4('+proj=utm +zone=28 +datum=WGS84 +units=m +no_defs')
    crs.createFromSrid(32628)
    return crs


def pointToWGS84(point):
    t=QgsCoordinateReferenceSystem()
    t.createFromSrid(4326)
    transformer = QgsCoordinateTransform(get_dest_projection(), t)
    pt = transformer.transform(point)
    return pt 

def pointFromWGS84(point):
    f=QgsCoordinateReferenceSystem()
    f.createFromSrid(4326)
    transformer = QgsCoordinateTransform(f, get_dest_projection())
    pt = transformer.transform(point)
    return pt


if __name__ == "__main__":
    pass

