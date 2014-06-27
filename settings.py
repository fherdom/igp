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
    u'PTE': {
        u'description': u'Pendiente',
        u'filename': u'PTE_5isl_MASK',
        u'req': 1,
        u'pos': 0,
        u'values': [
            [1, 0, 20, u'Pte. Suave (menos del 20%) y/o terreno aledaño poco accidentado.'],
            [3, 20, 30, u'Pte. Media (20-30 %) y/o terreno aledaño ondulado-accidentado.'],
            [5, 30, 9999, u'Pte. Fuerte (superior al 30%) y/o terreno escarpado.']]
    },
    u'ACC': {
        u'description': u'Accesibilidad',
        u'filename': u'accesibilidad',
        u'req': 1,
        u'pos': 1,
        u'values': [
            [1, 1, None, u'Accesibilidad Alta por viales y/o buen tránsito de vehículos fuera de ellos.'],
            [3, 2, None, u'Accesibilidad Media por viales y/o regular tránsito de vehículos fuera de ellos.'],
            [5, 3, None, u"Accesibilidad Baja por viales y/o nulo tránsito de vehículos fuera de ellos."]]
    },
    u'COM': {
        u'description': u'Combustibilidad',
        u'filename': u'combustibilidad',
        u'req': 1,
        u'pos': 2,
        u'values': [
            [1, 1, None, u'Combustibilidad Baja (Mod. 8,9,10,11)'],
            [3, 2, None, u'Combustibilidad Media (Mod. 5,7 y 2)'],
            [5, 3, None, u'Combustibilidad Alta (Mod. 1,3,4,6,12,13)']]
    },
    u'CON': {
        u'description': u'Continuidad',
        u'filename': u'FCC_5ISMASK',
        u'req': 1,
        u'pos': 3,
        u'values': [
            [1, 1, 33, u'Continuidad Nivel 1. (Fcc menor del 33%, y/o 10 metros de distancia de F.S del frente de llama)'],
            [3, 34, 66, u'Continuidad Nivel 2. (Fcc 33-66% y/o 10-100 metros de distancia del F.S del Frente de llama)'],
            [5, 67, 100, u'Continuidad Nivel 3. (Fcc mayor del 66% y/o más de 100 metros de distancia del F.S del frente de llama)']]
    },
    u'VIE': {
        u'description': u'Viento',
        u'filename': u'',
        u'req': 0,
        u'pos': 4,
        u'values': [
            [1, 0, 10, u'Velocidad de Viento Baja (menor o igual a 10 km/h)'],
            [3, 10, 30, u'Velocidad viento Media  (10-30 km/h)'],
            [5, 30, 100, u'Velocidad de Viento Alta (más de 30 km/h)']]
    },
    u'TEM': {
        u'description': u'Temperatura',
        u'filename': u'',
        u'req': 0,
        u'pos': 5,
        u'values': [
            [1, 0, 25, u'Temperatura Baja (menor igual a 25 ºC)'],
            [3, 25, 39, u'Temperatura Media  (26-39 ºC)'],
            [5, 39, 9999, u'Temperatura Alta (más de 40ºC)']]
    },
    u'EDE': {
        u'description': u'E.D.E.',
        u'filename': u'EDE_5isl_MASK',
        u'req': 1,
        u'pos': 6,
        u'values': [
            [5, 1, None, u'Presencia de E.D.E. en el área de afección del incendio y/o futura progresión del mismo (Área recreativa, Campings, Hospitales, colegios etc.).']]
    },
    u'IIE': {
        u'description': u'I.I.E.R.',
        u'filename': u'IIER_5isl_MSK',
        u'req': 1,
        u'pos': 7,
        u'values': [
            [5, 5, None, u'Presencia de I.I.E.R. en el área de afección del incendio y/o futura progresión del mismo (Bases aéreas, gasolineras, Centrales de producción de electricidad, vías de comunicación de primer orden etc.).']]
    },
    u'EVA': {
        u'description': u'Evacuación',
        u'filename': u'evacuacion',
        u'req': 1,
        u'pos': 8,
        u'values': [
            [5, 1, None, u'Evacuación de la población de sus viviendas o municipios en el área de afección del incendio y/o futura progresión del mismo.']]
    },
    u'PAT': {
        u'description': u'Patrimonio',
        u'filename': u'Patri_5isl_MK',
        u'req': 1,
        u'pos': 9,
        u'values': [
            [5, 1, None, u'Afección de elementos y/o lugares de especial relevancia catalogados y protegidos de carácter histórico artístico.']]
    },
    u'ECO': {
        u'description': u'Ecológico',
        u'filename': u'Ecolo_5isl_MK',
        u'req': 1,
        u'pos': 10,
        u'values': [
            [5, 1, None, u'Afección de espacios de especial relevancia ecológica catalogados y protegidos, así como elementos que por su singularidad rareza o difícil perpetuidad también gocen de especial protección']]
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
    u'PTE': [1, u'', 1],
    u'ACC': [1, u'', 1],
    u'COM': [1, u'', 1],
    u'CON': [1, u'', 1],
    u'VIE': [1, u'', 1],
    u'TEM': [1, u'', 1],
    u'EDE': [1, u'', 1],
    u'IIE': [1, u'', 1],
    u'EVA': [1, u'', 1],
    u'PAT': [1, u'', 1],
    u'ECO': [1, u'', 1],
    u'X':   [1, u'', 1],
    u'Y':   [1, u'', 1],
    u'IGP': [1, u'', 1],
    u'IGP_DES': [1, u'', 1],
    u'ISLA': [1, u'', 1],
    u'MUNICIPIO': [1, u'', 1],
    u'FECHA': [1, u'', 1],
}

LAYER_MUNICIPIOS = u'Municip_5isl'
