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

LAYERSID = [u'pendiente',
            u'accesibilidad',
            u'combustibilidad',
            u'FCC_5ISMASK',
            u'ede',
            u'iier',
            u'evacuacion',
            u'patrimonio',
            u'ecologico']

FULL_LAYERSID = [u'pendiente',
             u'accesibilidad',
             u'combustibilidad',
             u'FCC_5ISMASK',
             u'viento',
             u'temperatura',
             u'ede',
             u'iier',
             u'evacuacion',
             u'patrimonio',
             u'ecologico']

MATRIX = {
    u'pendiente': [
        [1, 0, 20, u'Pte. Suave (menos del 20%) y/o terreno aledaño poco accidentado.'],
        [3, 20, 30, u'Pte. Media (20-30 %) y/o terreno aledaño ondulado-accidentado.'],
        [5, 30, 9999, u'Pte. Fuerte (superior al 30%) y/o terreno escarpado.']
    ],
    u'accesibilidad': [
        [1, 1, None, u'Accesibilidad Alta por viales y/o buen tránsito de vehículos fuera de ellos.'],
        [3, 2, None, u'Accesibilidad Media por viales y/o regular tránsito de vehículos fuera de ellos.'],
        [5, 3, None, u"Accesibilidad Baja por viales y/o nulo tránsito de vehículos fuera de ellos."]
    ],
    u'combustibilidad': [
        [1, 1, None, u'Combustibilidad Baja (Mod. 8,9,10,11)'],
        [3, 2, None, u'Combustibilidad Media (Mod. 5,7 y 2)'],
        [5, 3, None, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)']
    ],
    u'FCC_5ISMASK': [
        [1, 1, 33, u'Continuidad Nivel 1. (Fcc menor del 33%, y/o 10 metros de distancia de F.S del frente de llama)'],
        [3, 34, 66, u'Continuidad Nivel 2. (Fcc 33-66% y/o 10-100 metros de distancia del F.S del Frente de llama)'],
        [5, 67, 100, u'Continuidad Nivel 3. (Fcc mayor del 66% y/o más de 100 metros de distancia del F.S del frente de llama)']
    ],
    u'viento': [
        [1, 0, 10, u'Velocidad de Viento Baja (menor o igual a 10 km/h)'],
        [3, 10, 30, u'Velocidad viento Media  (10-30 km/h)'],
        [5, 30, 100, u'Velocidad de Viento Alta (más de 30 km/h)']
    ],
    u'temperatura': [
        [1, 0, 25, u'Temperatura Baja (menor igual a 25 ºC)'],
        [3, 25, 39, u'Temperatura Media  (26-39 ºC)'],
        [5, 39, 9999, u'Temperatura Alta (más de 40ºC)']
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

SCORE = [
    [u'Baja', 6, 12, 'background-color: rgb(85, 255, 127);'],
    [u'Moderada', 13, 26, 'background-color: rgb(255, 170, 0);'],
    [u'Alta', 27, 42, 'background-color: rgb(255, 85, 127);'],
    [u'Severa', 43, 55, 'background-color: rgb(255, 0, 0);']
]

TEST_MATRIX = {
    u'pendiente': 15,
    u'accesibilidad': u'media',
    u'combustibilidad': u'media',
    u'FCC_5ISMASK': 2,
    u'viento': 15,
    u'temperatura': 24,
    u'ede': 1,
    u'iier': 1,
    u'evacuacion': 1,
    u'patrimonio': 1,
    u'ecologico': 1
}

LAYER_MUNICIPIOS = u'icd_muns'