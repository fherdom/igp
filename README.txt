Plugin IGP

designer ui_igpdialog.ui

pyuic4 ui_igpdialog.ui -o ui_igpdialog.py

pyrcc4 resources.qrc -o resources_rc.py

ln -s /home/felix/dev/qgis/igp ~/.qgis2/python/plugins/igp

Links:
http://snorf.net/blog/2013/12/07/multithreading-in-qgis-python-plugins/	
http://www.qgisworkshop.org/html/workshop/plugins_tutorial.html
http://pyqt.sourceforge.net/Docs/PyQt4/introduction.html

PDF
http://bharatikunal.wordpress.com/2010/01/31/converting-html-to-pdf-with-python-and-qt/
http://www.riverbankcomputing.com/pipermail/pyqt/2010-September/027709.html
https://www.mail-archive.com/pyqt@riverbankcomputing.com/msg18918.html

Puse una pregunta
http://www.qgistutorials.com/es/docs/getting_started_with_pyqgis.html

Painting
http://zetcode.com/gui/pyqt4/drawing/

Accessing Qgis, layer, info
http://www.qgisworkshop.org/html/workshop/python_in_qgis_tutorial2.html

Cook-book
http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/
http://www.qgistutorials.com/es/docs/getting_started_with_pyqgis.html





rLayer = qgis.utils.iface.mapCanvas().layer(0)
rLayer.name()
u'180_OEM25_EH'
pt001 = QgsPoint(210635.25, 3074409.58)
pt001
(210635,3.07441e+06)
rLayer.dataProvider().identify(pt001, QgsRaster.IdentifyFormatValue).results()
{1: 143.0, 2: 130.0, 3: 119.0}


# get layers by name
ll = QgsMapLayerRegistry().instance().mapLayersByName('180_OEM25_EH')
l = ll[0]
print l.name()