Plugin IGP

designer ui_igpdialog.ui

pyuic4 ui_igpdialog.ui -o ui_igpdialog.py

pyrcc4 resources.qrc -o resources_rc.py

ln -s /home/felix/dev/qgis/igp ~/.qgis2/python/plugins/igp


Links:
http://snorf.net/blog/2013/12/07/multithreading-in-qgis-python-plugins/	
http://www.qgisworkshop.org/html/workshop/plugins_tutorial.html