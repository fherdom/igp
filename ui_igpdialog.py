# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_igpdialog.ui'
#
# Created: Mon Jun 16 15:25:52 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_IGPDialog(object):
    def setupUi(self, IGPDialog):
        IGPDialog.setObjectName(_fromUtf8("IGPDialog"))
        IGPDialog.resize(487, 295)
        self.tabWidget = QtGui.QTabWidget(IGPDialog)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 476, 286))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(476, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(476, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab001 = QtGui.QWidget()
        self.tab001.setMinimumSize(QtCore.QSize(472, 0))
        self.tab001.setObjectName(_fromUtf8("tab001"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab001)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtSearch = QtGui.QLineEdit(self.tab001)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.verticalLayout.addWidget(self.txtSearch)
        self.chkBBOX = QtGui.QCheckBox(self.tab001)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkBBOX.sizePolicy().hasHeightForWidth())
        self.chkBBOX.setSizePolicy(sizePolicy)
        self.chkBBOX.setObjectName(_fromUtf8("chkBBOX"))
        self.verticalLayout.addWidget(self.chkBBOX)
        self.tblResult = QtGui.QTableWidget(self.tab001)
        self.tblResult.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblResult.sizePolicy().hasHeightForWidth())
        self.tblResult.setSizePolicy(sizePolicy)
        self.tblResult.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblResult.setShowGrid(True)
        self.tblResult.setColumnCount(3)
        self.tblResult.setObjectName(_fromUtf8("tblResult"))
        self.tblResult.setRowCount(0)
        self.verticalLayout.addWidget(self.tblResult)
        self.lblResult = QtGui.QLabel(self.tab001)
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.verticalLayout.addWidget(self.lblResult)
        self.tabWidget.addTab(self.tab001, _fromUtf8(""))
        self.tab002 = QtGui.QWidget()
        self.tab002.setObjectName(_fromUtf8("tab002"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab002)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab002)
        self.groupBox_7.setEnabled(True)
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 235, 52))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioutm = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioutm.setObjectName(_fromUtf8("radioutm"))
        self.gridLayout_3.addWidget(self.radioutm, 1, 0, 1, 1)
        self.radiodms = QtGui.QRadioButton(self.layoutWidget_2)
        self.radiodms.setChecked(True)
        self.radiodms.setObjectName(_fromUtf8("radiodms"))
        self.gridLayout_3.addWidget(self.radiodms, 0, 0, 1, 1)
        self.radiodm = QtGui.QRadioButton(self.layoutWidget_2)
        self.radiodm.setObjectName(_fromUtf8("radiodm"))
        self.gridLayout_3.addWidget(self.radiodm, 0, 1, 1, 1)
        self.radiod = QtGui.QRadioButton(self.layoutWidget_2)
        self.radiod.setObjectName(_fromUtf8("radiod"))
        self.gridLayout_3.addWidget(self.radiod, 1, 1, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 55, 301, 128))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.txtCoordinates = QtGui.QLineEdit(self.layoutWidget)
        self.txtCoordinates.setObjectName(_fromUtf8("txtCoordinates"))
        self.gridLayout_2.addWidget(self.txtCoordinates, 0, 0, 1, 1)
        self.btnGet = QtGui.QPushButton(self.layoutWidget)
        self.btnGet.setObjectName(_fromUtf8("btnGet"))
        self.gridLayout_2.addWidget(self.btnGet, 3, 0, 1, 1)
        self.btnClipboard = QtGui.QPushButton(self.layoutWidget)
        self.btnClipboard.setObjectName(_fromUtf8("btnClipboard"))
        self.gridLayout_2.addWidget(self.btnClipboard, 2, 0, 1, 1)
        self.btnGo = QtGui.QPushButton(self.layoutWidget)
        self.btnGo.setObjectName(_fromUtf8("btnGo"))
        self.gridLayout_2.addWidget(self.btnGo, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.tabWidget.addTab(self.tab002, _fromUtf8(""))
        self.tab003 = QtGui.QWidget()
        self.tab003.setObjectName(_fromUtf8("tab003"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab003)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(25, 20, 416, 66))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab003, _fromUtf8(""))

        self.retranslateUi(IGPDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(IGPDialog)

    def retranslateUi(self, IGPDialog):
        IGPDialog.setWindowTitle(QtGui.QApplication.translate("IGPDialog", "IGP - Índice de gravedad potencial", None, QtGui.QApplication.UnicodeUTF8))
        self.chkBBOX.setText(QtGui.QApplication.translate("IGPDialog", "Limitar la búsqueda a la extensión actual", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResult.setText(QtGui.QApplication.translate("IGPDialog", "Encontrado (s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab001), QtGui.QApplication.translate("IGPDialog", "Lugar", None, QtGui.QApplication.UnicodeUTF8))
        self.radioutm.setText(QtGui.QApplication.translate("IGPDialog", "UTM", None, QtGui.QApplication.UnicodeUTF8))
        self.radiodms.setText(QtGui.QApplication.translate("IGPDialog", "Grad. Min. Seg.", None, QtGui.QApplication.UnicodeUTF8))
        self.radiodm.setText(QtGui.QApplication.translate("IGPDialog", "Grad. Min.", None, QtGui.QApplication.UnicodeUTF8))
        self.radiod.setText(QtGui.QApplication.translate("IGPDialog", "Grados", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGet.setText(QtGui.QApplication.translate("IGPDialog", "Empezar captura", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClipboard.setText(QtGui.QApplication.translate("IGPDialog", "Copiar al portapapeles", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGo.setText(QtGui.QApplication.translate("IGPDialog", "Ir", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab002), QtGui.QApplication.translate("IGPDialog", "Coordenadas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IGPDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("IGPDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab003), QtGui.QApplication.translate("IGPDialog", "IGP", None, QtGui.QApplication.UnicodeUTF8))

