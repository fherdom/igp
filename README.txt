Plugin IGP

designer ui_igpdialog.ui

pyuic4 ui_igpdialog.ui -o ui_igpdialog.py

pyrcc4 resources.qrc -o resources_rc.py

ln -s /home/felix/dev/qgis/igp ~/.qgis2/python/plugins/igp


Plugin reloader
git clone https://github.com/borysiasty/plugin_reloader.git
ln -s /home/felix/dev/qgis/plugin_reloader ~/.qgis2/python/plugins/plugin_reloader


Links:
http://snorf.net/blog/2013/12/07/multithreading-in-qgis-python-plugins/	
http://www.qgisworkshop.org/html/workshop/plugins_tutorial.html
http://pyqt.sourceforge.net/Docs/PyQt4/introduction.html
http://qt-project.org/doc/qt-4.8/qtablewidget.html#details

PDF
http://bharatikunal.wordpress.com/2010/01/31/converting-html-to-pdf-with-python-and-qt/
http://www.riverbankcomputing.com/pipermail/pyqt/2010-September/027709.html
https://www.mail-archive.com/pyqt@riverbankcomputing.com/msg18918.html

Composer / Composition
http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/composer.html#output-using-map-composer
http://gis.stackexchange.com/questions/69626/how-to-use-map-composer-in-a-stand-alone-script
http://osgeo-org.1560.x6.nabble.com/Printing-multi-page-PDFs-from-QgsComposition-object-td5044041.html

!!!
http://gis.stackexchange.com/questions/77848/programmatically-load-composer-from-template-and-generate-atlas-using-pyqgis

!!! Examples python
https://github.com/qgis/QGIS/blob/master/tests/src/python/test_qgscomposition.py


Puse una pregunta
http://www.qgistutorials.com/es/docs/getting_started_with_pyqgis.html
QgsComposition es la clave
https://github.com/AIFDR/inasafe/blob/202e7142e02679da084fb3ebbbb787db516f9dfc/safe_qgis/report/map.py#L164

Painting
http://zetcode.com/gui/pyqt4/drawing/

Accessing Qgis, layer, info
http://www.qgisworkshop.org/html/workshop/python_in_qgis_tutorial2.html

Cook-book
!!!
http://qgis.readthedocs.org/en/latest/docs/pyqgis_developer_cookbook/03_vector.html
http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/
http://www.qgistutorials.com/es/docs/getting_started_with_pyqgis.html

!!! print
http://inasafe.org/en/_modules/safe_qgis/report/map.html


# Identify
http://3nids.wordpress.com/2013/02/14/identify-feature-on-map/

Stand-Alone
https://gist.github.com/spara/1251012

Vector - Raster
 2012  gdal_rasterize -a pendiente -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/pendiente.tif
 2013  ll
 2014  gdal_rasterize -a accesib -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/accesibilidad.tif
 2015  ll
 2016  gdal_rasterize -a combus -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/combustibilidad.tif
 2017  gdal_rasterize -a continuida -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/continuidad.tif
 2018  gdal_rasterize -a ede -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/ede.tif
 2019  gdal_rasterize -a iier -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/iier.tif
 2020  gdal_rasterize -a evac -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/evacuacion.tif
 2021  gdal_rasterize -a patrimonio -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/patrimonio.tif
 2022  gdal_rasterize -a ecologico -tr 1000.0 1000.0 -l icd_muns /home/felix/dev/qgis/igp/doc/municipios/icd_muns.shp /home/felix/dev/qgis/igp/doc/capas/ecologico.tif






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


458233.02, 3110465.86
