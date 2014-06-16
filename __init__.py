# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IGP
                                 A QGIS plugin
                             -------------------
        begin                : 2014-06-14
        copyright            : (C) 2014 by Felix Jose Hernandez
        email                : contacto@felixjosehernandez.es
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    #
    from igp import IGP
    return IGP(iface)
