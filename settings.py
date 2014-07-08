# -*- coding: utf-8 -*-
"""
***************************************************************************
Name			 	 :
Description          :
Date                 :
copyright            :
email                :
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


CONFIG = {
    u'001_PTE': {
        u'description': u'Pendiente',
        u'layername': u'Pendiente',
        u'req': 1,
        u'pos': 0,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [1, 0.0, 20.0, u'Pte. Suave (menos del 20%) y/o terreno aledaño poco accidentado.'],
            [3, 21.0, 30.0, u'Pte. Media (20-30 %) y/o terreno aledaño ondulado-accidentado.'],
            [5, 31.0, 9999.0, u'Pte. Fuerte (superior al 30%) y/o terreno escarpado.']
        ]
    },
    u'002_ACC': {
        u'description': u'Accesibilidad',
        u'layername': u'Accesibilidad',
        u'req': 1,
        u'pos': 1,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [1, 1.0, None, u'Accesibilidad Alta por viales y/o buen tránsito de vehículos fuera de ellos.'],
            [3, 3.0, None, u'Accesibilidad Media por viales y/o regular tránsito de vehículos fuera de ellos.'],
            [5, 5.0, None, u"Accesibilidad Baja por viales y/o nulo tránsito de vehículos fuera de ellos."]
        ]
    },
    u'003_COM': {
        u'description': u'Combustibilidad',
        u'layername': u'Combustibilidad',
        u'req': 1,
        u'pos': 2,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [5, 1.0, 1.0, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)'],
            [3, 2.0, 2.0, u'Combustibilidad Media (Mod. 5,7 y 2)'],
            [5, 3.0, 4.0, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)'],
            [3, 5.0, 5.0, u'Combustibilidad Media (Mod. 5,7 y 2)'],
            [5, 6.0, 6.0, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)'],
            [3, 7.0, 7.0, u'Combustibilidad Media (Mod. 5,7 y 2)'],
            [1, 8.0, 11.0, u'Combustibilidad Baja (Mod. 8,9,10,11)'],
            [5, 12.0, 13.0, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)'],
        ]
    },
    u'004_CON': {
        u'description': u'Continuidad',
        u'layername': u'Continuidad',
        u'req': 1,
        u'pos': 3,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [1, 1.0, 33.0, u'Continuidad Nivel 1. (Fcc menor del 33%, y/o 10 metros de distancia de F.S del frente de llama)'],
            [3, 34.0, 66.0, u'Continuidad Nivel 2. (Fcc 33-66% y/o 10-100 metros de distancia del F.S del Frente de llama)'],
            [5, 67.0, 100.0, u'Continuidad Nivel 3. (Fcc mayor del 66% y/o más de 100 metros de distancia del F.S del frente de llama)']
        ]
    },
    u'005_VIE': {
        u'description': u'Viento',
        u'layername': u'',
        u'req': 0,
        u'pos': 4,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'Km/h',
        u'values': [
            [1, 0.0, 10.0, u'Velocidad de Viento Baja (menor o igual a 10 km/h)'],
            [3, 11.0, 30.0, u'Velocidad viento Media  (10-30 km/h)'],
            [5, 31.0, 100.0, u'Velocidad de Viento Alta (más de 30 km/h)']
        ]
    },
    u'006_TEM': {
        u'description': u'Temperatura',
        u'layername': u'',
        u'req': 0,
        u'pos': 5,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'ºC',
        u'values': [
            [1, 0.0, 25.0, u'Temperatura Baja (menor igual a 25 ºC)'],
            [3, 26.0, 39.0, u'Temperatura Media  (26-39 ºC)'],
            [5, 40.0, 9999.0, u'Temperatura Alta (más de 40ºC)']
        ]
    },
    u'007_EDE': {
        u'description': u'E.D.E.',
        u'layername': u'EDE',
        u'req': 1,
        u'pos': 6,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [5, 5.0, None, u'Presencia de E.D.E. en el área de afección del incendio y/o futura progresión del mismo (Área recreativa, Campings, Hospitales, colegios etc.).']
        ]
    },
    u'008_IIE': {
        u'description': u'I.I.E.R.',
        u'layername': u'IIER',
        u'req': 1,
        u'pos': 7,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [5, 5.0, None, u'Presencia de I.I.E.R. en el área de afección del incendio y/o futura progresión del mismo (Bases aéreas, gasolineras, Centrales de producción de electricidad, vías de comunicación de primer orden etc.).']
        ]
    },
    u'009_EVA': {
        u'description': u'Evacuación',
        u'layername': u'Evacuación',
        u'req': 1,
        u'pos': 8,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [5, 5.0, None, u'Evacuación de la población de sus viviendas o municipios en el área de afección del incendio y/o futura progresión del mismo.']
        ]
    },
    u'010_PAT': {
        u'description': u'Patrimonio',
        u'layername': u'Patrimonio',
        u'req': 1,
        u'pos': 9,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [5, 5.0, None, u'Afección de elementos y/o lugares de especial relevancia catalogados y protegidos de carácter histórico artístico.']
        ]
    },
    u'011_ECO': {
        u'description': u'Ecológico',
        u'layername': u'Ecológico',
        u'req': 1,
        u'pos': 10,
        u'not_found': u'Sin presencia o valor desconocido',
        u'units': u'',
        u'values': [
            [5, 5.0, None, u'Afección de espacios de especial relevancia ecológica catalogados y protegidos, así como elementos que por su singularidad rareza o difícil perpetuidad también gocen de especial protección']
        ]
    }
}

VALUES_SYM = {
    u'Baja': ('#55FF7F', 'Riesgo Bajo'),
    u'Moderada': ('#FFAA7F', 'Riesgo Moderado'),
    u'Alta': ('#FF557F', 'Riesgo Alto'),
    u'Severa': ('#FF0000', 'Riesgo Severo'),
    '': ('#000', 'Desconocido')}

SCORE = [
    [u'Baja', 6, 12, 'background-color: rgb(85, 255, 127);'],
    [u'Moderada', 13, 26, 'background-color: rgb(255, 170, 0);'],
    [u'Alta', 27, 42, 'background-color: rgb(255, 85, 127);'],
    [u'Severa', 43, 55, 'background-color: rgb(255, 0, 0);']
]

RESULTS = {
    u'001_PTE': [1, u'', 1],
    u'002_ACC': [1, u'', 1],
    u'003_COM': [1, u'', 1],
    u'004_CON': [1, u'', 1],
    u'005_VIE': [1, u'', 1],
    u'006_TEM': [1, u'', 1],
    u'007_EDE': [1, u'', 1],
    u'008_IIE': [1, u'', 1],
    u'009_EVA': [1, u'', 1],
    u'010_PAT': [1, u'', 1],
    u'011_ECO': [1, u'', 1],
    u'012_X':   [1, u'', 1],
    u'013_Y':   [1, u'', 1],
    u'014_IGP': [1, u'', 1],
    u'015_IGP_DES': [1, u'', 1],
    u'016_ISLA': [1, u'', 1],
    u'017_MUNICIPIO': [1, u'', 1],
    u'018_FECHA': [1, u'', 1],
}

LAYER_MUNICIPIOS = u'Municip_5isl'


for layerid in sorted(RESULTS.iterkeys()):
    print layerid
