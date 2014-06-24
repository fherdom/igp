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

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

from qgis.core import *

from ui_igpdialog import Ui_IGPDialog

from settings import MATRIX
from settings import LAYERSID
from settings import FULL_LAYERSID
from settings import SCORE
from settings import TEST_MATRIX


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

        # TODO: 140618, load matrix
        self.matrix = MATRIX

        # TODO: 140624, layer IGP
        self.layerigp = None
        self.layeridigp = None
        self.providerigp = None

    def onclickbtnigp(self):
        """
        :return:
        """
        pto = QgsPoint(float(self.ui.txtCoord.text().split(',')[0].strip()),
                       float(self.ui.txtCoord.text().split(',')[1].strip()))
        igp = 0
        for layerid in LAYERSID:
            if self.isloadlayer(layerid):
                value = self.getinfovalue(pto, layerid)
                score, description = self.checkvalue(layerid, value)
                TEST_MATRIX[layerid] = [value, description, score]
                igp += score
            else:
                style = "background-color: rgb(0, 0, 0);\ncolor: rgb(255, 255, 255);"
                text = "Falta layerid"
                self.ui.txtResult.setStyleSheet(style)
                self.ui.txtResult.setText(text)
                return None, None

        # TODO: viento
        layerid = u'viento'
        value = int(self.ui.tableWidget.item(4, 0).text())
        score, description = self.checkvalue(layerid, value)
        igp += score
        TEST_MATRIX[layerid] = [value, description, score]

        # TODO: temperatura
        layerid = u'temperatura'
        value = int(self.ui.tableWidget.item(5, 0).text())
        score, description = self.checkvalue(layerid, value)
        igp += score
        TEST_MATRIX[layerid] = [value, description, score]

        for sc in SCORE:
            if sc[1] <= igp <= sc[2]:
                style = sc[3]
                text = "%d - %s" % (igp, sc[0])
                self.ui.txtResult.setStyleSheet(style)
                self.ui.txtResult.setText(text)

                # TODO: show TEST_MATRIX on table
                i = 0
                for layerid in FULL_LAYERSID:
                    self.ui.tableWidget.item(i, 0).setText(unicode(TEST_MATRIX[layerid][0]))
                    self.ui.tableWidget.item(i, 1).setText(unicode(TEST_MATRIX[layerid][1]))
                    self.ui.tableWidget.item(i, 2).setText(unicode(TEST_MATRIX[layerid][2]))
                    i += 1

                # TODO: add point to layer
                if not QgsMapLayerRegistry.instance().mapLayer(self.layeridigp):

                    self.layerigp = QgsVectorLayer("Point", u'Resultados IGP', "memory")
                    self.providerigp = self.layerigp.dataProvider()
                    crs = QgsCoordinateReferenceSystem()
                    crs.createFromSrid(32628)
                    self.layerigp.setCrs(crs)

                    #
                    self.providerigp.addAttributes([
                        QgsField(u'pendiente', QtCore.QVariant.Int),
                        QgsField(u'accesibilidad', QtCore.QVariant.Int),
                        QgsField(u'combustibilidad', QtCore.QVariant.Int),
                        QgsField(u'continuidad', QtCore.QVariant.Int),
                        QgsField(u'viento', QtCore.QVariant.Int),
                        QgsField(u'temperatura', QtCore.QVariant.Int),
                        QgsField(u'ede', QtCore.QVariant.Int),
                        QgsField(u'iier', QtCore.QVariant.Int),
                        QgsField(u'evacuacion', QtCore.QVariant.Int),
                        QgsField(u'patrimonio', QtCore.QVariant.Int),
                        QgsField(u'ecologico', QtCore.QVariant.Int),
                        QgsField(u'igp', QtCore.QVariant.Int),
                        QgsField(u'igp_des', QtCore.QVariant.String),
                        QgsField(u'x', QtCore.QVariant.Double),
                        QgsField(u'y', QtCore.QVariant.Double),
                        QgsField(u'fecha', QtCore.QVariant.String),

                    ])

                    #
                    self.layerigp.updateFields()

                    #
                    label = self.layerigp.label()
                    label.setLabelField(QgsLabel.Text, 0)
                    self.layerigp.enableLabels(True)

                    #
                    QgsMapLayerRegistry.instance().addMapLayer(self.layerigp)

                    #
                    self.layeridigp = QgsMapLayerRegistry.instance().mapLayers().keys()[-1]
                    self.canvas.refresh()

                fields = self.layerigp.pendingFields()
                fet = QgsFeature(fields)
                fet.setGeometry(QgsGeometry.fromPoint(pto))
                i = 0
                for layerid in FULL_LAYERSID:
                    fet[i] = TEST_MATRIX[layerid][0]
                    i += 1
                fet[i] = igp
                fet[i+1] = sc[0]
                fet[i+2] = pto[0]
                fet[i+3] = pto[1]
                now = QtCore.QDateTime.currentDateTime()
                fet[i+4] = str(datetime.now())
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

                return igp, sc[0]

    def isloadlayer(self, layerid):
        """
        :param layerid:
        :return:
        """
        aux = QgsMapLayerRegistry().instance().mapLayersByName(layerid)
        self.log("%s %s" % (aux, layerid))
        return True if len(aux) > 0 else False

    def getinfovalue(self, pto, layerid):
        """
        :param x:
        :param y:
        :param layerid:
        :return:
        """
        aux = QgsMapLayerRegistry().instance().mapLayersByName(layerid)
        rlayer = aux[0]
        results = rlayer.dataProvider().identify(pto, QgsRaster.IdentifyFormatValue).results()
        self.log("%s" % results)
        return results[1]
        #return TEST_MATRIX[layerid]

    def checkvalue(self, layerid, value):
        """
        :param id:
        :param value:
        :return:
        """
        for e in MATRIX[layerid]:
            if e[2]:
                if e[1] < value <= e[2]:
                    return e[0], e[3]
            else:
                if e[1] == value:
                    return e[0], e[3]
        return 0, "No encontrado"

    def onclick_btnpastecoord(self):
        """
        """
        clipboard = QtGui.QApplication.clipboard()
        self.ui.txtCoord.setText(clipboard.text())
        #clipboard.setText(self.ui.txtCoordinates.text()) 

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
        from PyQt4 import QtXml

        # center
        pto = QgsPoint(float(self.ui.txtCoord.text().split(',')[0].strip()),
                       float(self.ui.txtCoord.text().split(',')[1].strip()))

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

        # Add all layers in map canvas to render
        myMapRenderer = self.canvas.mapRenderer()

        savePDFFileName = QtGui.QFileDialog.getSaveFileName(None, u'save as PDF', '.', 'PDF files (*.pdf)')

        # Load template from file
        myComposition = QgsComposition(myMapRenderer)
        myFile = os.path.join(os.path.dirname(__file__), 'template004.qpt')
        myTemplateFile = file(myFile, 'rt')
        myTemplateContent = myTemplateFile.read()
        myTemplateFile.close()
        myDocument = QtXml.QDomDocument()
        myDocument.setContent(myTemplateContent)
        myComposition.loadFromTemplate(myDocument)


        myMap = myComposition.getComposerItemById('mapa')
        myMap.setNewExtent(rect)

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



    def onclickbtnreport001(self):
        """
        :return: pdf
        """

        """
        text_file_path = open('/tmp/hX6582.gml').read()
        doc = QtGui.QTextDocument(text_file_path)
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName('/tmp/sample.pdf')
        doc.print_(printer)
        """

        # Option web
        """
        from PyQt4.QtWebKit import QWebView
        web = QWebView()
        #web.load(QUrl("http://www.google.com"))
        web.load(QUrl("file:////tmp/report001.html"))
        printer = QtGui.QPrinter()i.QTableWidgetItem(nombre)
            item002 = QtGui.QTableWidgetItem(clasificacion)
            item003 = QtGui.QTableWidgetItem(localizacion)
            self.ui.tblResult.setItem(row, 0, item001)
            self.ui.tblResult.setItem(row, 1, item002)
            self.ui.tblRes
        printer.setPageSize(QtGui.QPrinter.A4)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName("/tmp/file.pdf")
            #web.print_(printer)
        def convertIt():
            web.print_(printer)
            print "Pdf generated"
        QtCore.QObject.connect(web, SIGNAL("loadFinishe
        painter.drawText(0, 0, u"Índice de gravedad forestat")

        painter.end()
        """

        """
        # Option low level
        image = QtGui.QImage("/tmp/image001.png")
        printer = QtGui.QPrinter()
        printer.setResolution(300)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName("/tmp/report001.pdf")

        painter = QtGui.QPainter()
        painter.begin(printer)
        painter.drawImage(QtCore.QRect(0, 0, self.width(), self.height()), image)

        painter.setPen(QtGui.QColor(168, 43, 3))
        painter.setFont(QtGui.QFont('Decorative', 10))
        painter.drawText(0, 0, u"Índice de gravedad forestat")

        painter.end()
        """

        # center
        pto = QgsPoint(float(self.ui.txtCoord.text().split(',')[0].strip()),
                       float(self.ui.txtCoord.text().split(',')[1].strip()))

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

        # prepare print
        mapRenderer = self.canvas.mapRenderer()
        c = QgsComposition(mapRenderer)
        c.setPlotStyle(QgsComposition.Print)

        # map
        x, y = 0, 0
        w, h = c.paperWidth(), c.paperHeight()
        composerMap = QgsComposerMap(c, x, y, w, h)
        c.addItem(composerMap)

        composerLabel = QgsComposerLabel(c)
        composerLabel.setText("Hello world")
        composerLabel.adjustSizeToText()
        c.addItem(composerLabel)

        savePDFFileName = QtGui.QFileDialog.getSaveFileName(None, u'save as PDF', '.', 'PDF files (*.pdf)')

        printer = QtGui.QPrinter()
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName(savePDFFileName)
        printer.setPaperSize(QtCore.QSizeF(c.paperWidth(), c.paperHeight()), QtGui.QPrinter.Millimeter)
        printer.setFullPage(True)
        printer.setColorMode(QtGui.QPrinter.Color)
        printer.setResolution(c.printResolution())

        pdfPainter = QtGui.QPainter(printer)
        paperRectMM = printer.pageRect(QtGui.QPrinter.Millimeter)
        paperRectPixel = printer.pageRect(QtGui.QPrinter.DevicePixel)
        c.render(pdfPainter, paperRectPixel, paperRectMM)
        pdfPainter.end()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = IGPDialog(None)
    dlg.show()
    sys.exit(app.exec_())