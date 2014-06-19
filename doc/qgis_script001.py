canvas = qgis.utils.iface.mapCanvas()
#rLayer = qgis.utils.iface.mapCanvas().layer(0)
#rLayer.name()
#pt001 = QgsPoint(210635.25, 3074409.58)
#print rLayer.dataProvider().identify(pt001, QgsRaster.IdentifyFormatValue).results()

#for i in canvas.layers():
#    print i.name()
#    print i.id()
#    

ll = QgsMapLayerRegistry().instance().mapLayersByName('180_OEM25_EH')

l = ll[0]

print l.name()

