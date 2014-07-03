# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IGPDialog
                                 A QGIS plugin
 
                             -------------------
        begin                : 2014-05-14
        copyright            : (C) 2014 by Felix Jose Hernandez
        email                : fhernandeze@grafcan.es
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

import os

from datetime import datetime

from PyQt4 import QtXml
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

from qgis.core import *

from ui_igpdialog import Ui_IGPDialog

from settings import CONFIG
from settings import SCORE
from settings import LAYER_MUNICIPIOS
from settings import RESULTS
from settings import VALUES_SYM

class IGPDialog(QtGui.QDialog, Ui_IGPDialog):

    def __init__(self, iface):
        """
        """
        QtGui.QDialog.__init__(self)

        self.iface = iface
        if self.iface:
            self.canvas = self.iface.mapCanvas()

        # Set up the user interface from Designer. 
        self.ui = Ui_IGPDialog()
        self.ui.setupUi(self)

        # TODO: 140614
        self.connect(self.ui.btnReport, SIGNAL("clicked()"), self.onclickbtnreport)
        self.connect(self.ui.btnIGP, SIGNAL("clicked()"), self.onclickbtnigp)
        self.connect(self.ui.btnPasteCoord, SIGNAL("clicked()"), self.onclick_btnpastecoord)

        basedirectory = os.path.dirname(__file__)
        fillpath = lambda x: os.path.join(basedirectory, x)
        setting, filenamelog = map(fillpath, ['setting.txt', 'igp.log'])

        # Log file
        self.DEBUG = True
        self.filenamelog = filenamelog
        self.log("init app")

        # TODO: 140624, layer IGP
        self.layerigp = None
        self.layeridigp = None
        self.providerigp = None

        self.igp = None
        self.igp_des = None

        #self.pto = u"458233.02, 3110465.86"
        self.pto = None

    def createIGPLayer(self):
        """
        """
        self.layerigp = QgsVectorLayer("Point", u'Resultados IGP', "memory")
        self.providerigp = self.layerigp.dataProvider()
        crs = QgsCoordinateReferenceSystem()
        crs.createFromSrid(32628)
        self.layerigp.setCrs(crs)

        #
        attrs = []
        for layerid in RESULTS:
            attrs.append(QgsField(layerid, QtCore.QVariant.String))
        self.providerigp.addAttributes(attrs)

        #
        self.layerigp.updateFields()

        # label
        label = self.layerigp.label()
        label.setLabelField(QgsLabel.Text, self.layerigp.fieldNameIndex(u'IGP_DES'))
        self.layerigp.enableLabels(True)

        # symbol
        # create a category for each item
        categories = []
        for value, (color, label) in VALUES_SYM.items():
            symbol = QgsSymbolV2.defaultSymbol(self.layerigp.geometryType())
            symbol.setColor(QtGui.QColor(color))
            category = QgsRendererCategoryV2(value, symbol, label)
            categories.append(category)

        expression = u'IGP_DES'
        renderer = QgsCategorizedSymbolRendererV2(expression, categories)
        self.layerigp.setRendererV2(renderer)

        #
        QgsMapLayerRegistry.instance().addMapLayer(self.layerigp)

        #
        self.layeridigp = QgsMapLayerRegistry.instance().mapLayers().keys()[-1]
        self.canvas.refresh()


    def addIGPLayerValue(self, pto):
        """
        """
        # TODO: add point to layer
        if not self.layerigp:
            self.createIGPLayer()

        fields = self.layerigp.pendingFields()
        fet = QgsFeature(fields)
        fet.setGeometry(QgsGeometry.fromPoint(pto))
        
        # fill record
        i = 0
        for layerid in RESULTS:
            fet[i] = RESULTS[layerid][0]
            i += 1
        self.providerigp.addFeatures([fet])

        #
        self.layerigp.updateExtents()

        #
        scale = 1
        extent = self.canvas.extent()
        width = extent.width() * scale
        height = extent.height() * scale

        # Recenter
        rect = QgsRectangle(pto[0] - width/2.0,
                            pto[1] - height/2.0,
                            pto[0] + width/2.0,
                            pto[1] + height/2.0)

        # Set the extent to our new rectangle
        self.canvas.setExtent(rect)
        self.canvas.refresh()

    def onclickbtnigp(self):
        """
        :return:
        """

        def alert(msg):
            style = "background-color: rgb(0, 0, 0);\ncolor: rgb(255, 255, 255);"
            text = msg
            self.ui.txtResult.setStyleSheet(style)
            self.ui.txtResult.setText(text)
            
        
        if self.ui.txtCoord.text() == "":
            alert(u"Faltan las coordenadas")
            self.ui.txtCoord.setFocus()
            return False

        try:
            pto = QgsPoint(float(self.ui.txtCoord.text().split(',')[0].strip()),
                       float(self.ui.txtCoord.text().split(',')[1].strip()))
        except:
            alert(u"Coordenadas no válidas")
            self.ui.txtCoord.setFocus()
            return False

        # TODO: check if pto is UTM
        #pntGeom = QgsGeometry.fromPoint(pto)
        #self.log("%s" % QgsGeometry.fromPoint(pto).isGeosValid())

        if not pto:
            alert(u"Coordenadas no válidas")
            self.ui.txtCoord.setFocus()
            return False

        igp = 0
        for layerid, data in CONFIG.items():
            #print layerid
            #print data[u'description'].encode('utf-8')
            if data[u'req'] == 1:
                if self.isloadlayer(data[u'layername']):
                    value = self.getinfovalue(pto, data[u'layername'])
                    score, description = self.checkvalue(layerid, value)

                    # format value
                    self.log("%s %s" % (layerid, type(value)))
                    if isinstance(value, float):
                        RESULTS[layerid] = ['%.2f' % value, description, score]
                    else:
                        RESULTS[layerid] = [value, description, score]
                    
                    # Show table
                    self.ui.tableWidget.item(data[u'pos'], 0).setText(unicode(RESULTS[layerid][0]))
                    self.ui.tableWidget.item(data[u'pos'], 1).setText(unicode(RESULTS[layerid][1]))
                    self.ui.tableWidget.item(data[u'pos'], 2).setText(unicode(RESULTS[layerid][2]))

                    igp += score
                else:
                    text = "Falta capa: %s" % data[u'layername']
                    alert(text)
                    return False

        # TODO: viento
        layerid = u'VIE'
        value = int(self.ui.tableWidget.item(4, 0).text())
        if value == "":
            alert(u"Falta viento")
            self.ui.tableWidget.item(4, 0).setFocus()
            return False
        score, description = self.checkvalue(layerid, value)
        igp += score
        RESULTS[layerid] = [value, description, score]

        # TODO: temperatura
        layerid = u'TEM'
        value = int(self.ui.tableWidget.item(5, 0).text())
        if value == "":
            alert(u"Falta temperatura")
            self.ui.tableWidget.item(5, 0).setFocus()
            return False
        score, description = self.checkvalue(layerid, value)
        igp += score
        RESULTS[layerid] = [value, description, score]

        # TODO: Final score
        for sc in SCORE:
            if sc[1] <= igp <= sc[2]:
                style = sc[3]
                text = "%d - %s" % (igp, sc[0])
                self.ui.txtResult.setStyleSheet(style)
                self.ui.txtResult.setText(text)

                # 
                RESULTS[u'X'] = [self.ui.txtCoord.text().split(',')[0].strip(), u'', 1]
                RESULTS[u'Y'] = [self.ui.txtCoord.text().split(',')[1].strip(), u'', 1]
                RESULTS[u'IGP'] = [igp, u'', 1]
                RESULTS[u'IGP_DES'] = [sc[0], u'', 1]
                i, m = self.getinfoislavalue(pto)
                RESULTS[u'ISLA'] = [i, u'', 1]
                RESULTS[u'MUNICIPIO'] = [m, u'', 1]
                RESULTS[u'FECHA'] = [str(datetime.now()), u'', 1]

                self.igp = igp
                self.igp_des = sc[0]
                self.pto = pto

                # 
                self.log('%s' % RESULTS)
                self.addIGPLayerValue(pto)

        return True

    def isloadlayer(self, layername):
        """
        :param layerid:
        :return:
        """
        aux = QgsMapLayerRegistry().instance().mapLayersByName(layername)
        self.log("%s %s" % (aux, layername))
        return True if len(aux) > 0 else False

    def getinfovalue(self, pto, layername):
        """
        :param x:
        :param y:
        :param layerid:
        :return:
        """
        aux = QgsMapLayerRegistry().instance().mapLayersByName(layername)
        rlayer = aux[0]
        results = rlayer.dataProvider().identify(pto, QgsRaster.IdentifyFormatValue).results()
        self.log("%s" % results)
        return results[1]

    def getinfoislavalue(self, pto):
        """
        :param pto:
        :return:
        """
        try:
            aux = QgsMapLayerRegistry().instance().mapLayersByName(LAYER_MUNICIPIOS)
            vlayer = aux[0]

            # 5 meters
            searchRadius = 5
            rect = QgsRectangle()
            rect.setXMinimum(pto.x() - searchRadius)
            rect.setXMaximum(pto.x() + searchRadius)
            rect.setYMinimum(pto.y() - searchRadius)
            rect.setYMaximum(pto.y() + searchRadius)
            rq = QgsFeatureRequest().setFilterRect(rect)

            feature = vlayer.getFeatures(rq).next()
            self.log("%s" % feature)
            return feature[6], feature[1]
        except:
            return None, None

    def checkvalue(self, layerid, value):
        """
        :param id:
        :param value:
        :return:
        """
        for e in CONFIG[layerid][u'values']:
            if e[2]:
                if e[1] <= value <= e[2]:
                    return e[0], e[3]
            else:
                if e[1] == value:
                    return e[0], e[3]
        return 0, CONFIG[layerid][u'not_found']

    def onclick_btnpastecoord(self):
        """
        """
        clipboard = QtGui.QApplication.clipboard()
        self.ui.txtCoord.setText(clipboard.text())

    def log(self, msg):
        """
        """
        if self.DEBUG:
            f = open(self.filenamelog, "a")
            f.write("%s: %s\n" % (datetime.now(), msg.encode('utf-8')))
            f.close()

    def onclickbtnreport(self):
        """

        :return:
        """
        def alert(msg):
            style = "background-color: rgb(0, 0, 0);\ncolor: rgb(255, 255, 255);"
            text = msg
            self.ui.txtResult.setStyleSheet(style)
            self.ui.txtResult.setText(text)

        if not self.pto:
            alert(u"Sin datos para generar informe")
            return False

        # center
        pto = self.pto
        scale = 1
        extent = self.canvas.extent()
        width = extent.width() * scale
        height = extent.height() * scale

        # Recenter
        rect = QgsRectangle(pto[0] - width/2.0,
                            pto[1] - height/2.0,
                            pto[0] + width/2.0,
                            pto[1] + height/2.0)

        # Set the extent to our new rectangle
        self.canvas.setExtent(rect)

        # TODO: add Marker !!!! to layer!!! -- better create symbology in create layer

        # Add all layers in map canvas to render
        myMapRenderer = self.canvas.mapRenderer()

        savePDFFileName = QtGui.QFileDialog.getSaveFileName(None, 
            u'Guardar como PDF', 
            os.path.join(QtCore.QDir.homePath(), 'report_IGP_00x.xml'), 
            u'PDF files (*.pdf)')

        if not savePDFFileName:
            alert(u"Informe cancelado")
            return False

        #savePDFFileName = '/tmp/out.pdf'

        # Load template from file
        myComposition = QgsComposition(myMapRenderer)
        myFile = os.path.join(os.path.dirname(__file__), 'template006.qpt')
        myTemplateFile = file(myFile, 'rt')
        myTemplateContent = myTemplateFile.read()
        myTemplateFile.close()
        myDocument = QtXml.QDomDocument()
        myDocument.setContent(myTemplateContent)
        myComposition.loadFromTemplate(myDocument)

        myMap = myComposition.getComposerItemById('mapa')
        myMap.setNewExtent(rect)

        mIsla, mMunicipio = self.getinfoislavalue(pto)
        mX = pto.x()
        mY = pto.y()
        myHeader = myComposition.getComposerItemById('header')
        htmlHeader= u"""
        <style type="text/css">
            table.myTable { border-collapse:collapse; }
            table.myTable td,
            table.myTable th { border:1px solid black;padding:5px; }
        </style>
        <table class="myTable">
        <tr>
            <td>ISLA</td>
            <td>MUNICIPIO</td>
            <td>X</td>
            <td>Y</td>
            <td>FECHA</td>
        </tr>
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
        </table>""" % (RESULTS[u'ISLA'][0], RESULTS[u'MUNICIPIO'][0], RESULTS[u'X'][0], RESULTS[u'Y'][0], RESULTS[u'FECHA'][0])
        myHeader.setText(htmlHeader)

        myTable = myComposition.getComposerItemById('table')
        i = 0
        rows = ""
        for layerid in RESULTS:
            if layerid in CONFIG:
                rows += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (CONFIG[layerid][u'description'], 
                    RESULTS[layerid][0], 
                    RESULTS[layerid][1], 
                    RESULTS[layerid][2])
            i += 1
        htmlTable = u"""
        <style type="text/css">
            table.myTable { border-collapse:collapse; }
            table.myTable td,
            table.myTable th { border:1px solid black;padding:5px; }
        </style>
        <table class="myTable">
        <tr>
            <td>FACTORES</td>
            <td>VALOR</td>
            <td>SIGNIFICADO</td>
            <td>PUNTUACIÓN</td>
        </tr>%s
        </table>""" % rows
        myTable.setText(htmlTable)

        myFooter = myComposition.getComposerItemById('footer')
        htmlFooter = u"<center><h1>IGP = %s INCENDIO DE GRAVEDAD %s</h1></center>" % (RESULTS['IGP'][0], RESULTS['IGP_DES'][0].upper())
        myFooter.setText(htmlFooter)

        # logos
        mlogo_gobcan = myComposition.getComposerItemById('logo_gobcan')
        mlogo_gobcan.setPictureFile(os.path.join(os.path.dirname(__file__), 'gobcanarias.jpg'))
        mlogo_112 = myComposition.getComposerItemById('logo_112')
        mlogo_112.setPictureFile(os.path.join(os.path.dirname(__file__), '112.jpg'))

        # print PDF
        printer = QtGui.QPrinter()
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName(savePDFFileName)
        printer.setPaperSize(QtCore.QSizeF(myComposition.paperWidth(),
                                           myComposition.paperHeight()),
                             QtGui.QPrinter.Millimeter)
        printer.setFullPage(True)
        printer.setColorMode(QtGui.QPrinter.Color)
        printer.setResolution(myComposition.printResolution())

        pdfPainter = QtGui.QPainter(printer)
        paperRectMM = printer.pageRect(QtGui.QPrinter.Millimeter)
        paperRectPixel = printer.pageRect(QtGui.QPrinter.DevicePixel)
        myComposition.render(pdfPainter, paperRectPixel, paperRectMM)
        pdfPainter.end()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = IGPDialog(None)
    dlg.show()
    sys.exit(app.exec_())