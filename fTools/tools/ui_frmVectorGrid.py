# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmVectorGrid.ui'
#
# Created: Wed Jul 29 01:08:22 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(489, 507)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inShape = QtGui.QComboBox(self.groupBox)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.gridLayout.addWidget(self.inShape, 0, 0, 1, 2)
        self.btnUpdate = QtGui.QToolButton(self.groupBox)
        self.btnUpdate.setMinimumSize(QtCore.QSize(0, 30))
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.gridLayout.addWidget(self.btnUpdate, 2, 0, 1, 1)
        self.btnCanvas = QtGui.QToolButton(self.groupBox)
        self.btnCanvas.setMinimumSize(QtCore.QSize(0, 30))
        self.btnCanvas.setObjectName(_fromUtf8("btnCanvas"))
        self.gridLayout.addWidget(self.btnCanvas, 2, 1, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.xMin = QtGui.QLineEdit(self.groupBox)
        self.xMin.setEnabled(True)
        self.xMin.setInputMask(_fromUtf8(""))
        self.xMin.setText(_fromUtf8(""))
        self.xMin.setObjectName(_fromUtf8("xMin"))
        self.hboxlayout.addWidget(self.xMin)
        self.gridLayout.addLayout(self.hboxlayout, 3, 0, 1, 1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.hboxlayout1.addWidget(self.label_4)
        self.yMin = QtGui.QLineEdit(self.groupBox)
        self.yMin.setEnabled(True)
        self.yMin.setInputMask(_fromUtf8(""))
        self.yMin.setText(_fromUtf8(""))
        self.yMin.setObjectName(_fromUtf8("yMin"))
        self.hboxlayout1.addWidget(self.yMin)
        self.gridLayout.addLayout(self.hboxlayout1, 3, 1, 1, 1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.hboxlayout2.addWidget(self.label_3)
        self.xMax = QtGui.QLineEdit(self.groupBox)
        self.xMax.setEnabled(True)
        self.xMax.setInputMask(_fromUtf8(""))
        self.xMax.setText(_fromUtf8(""))
        self.xMax.setObjectName(_fromUtf8("xMax"))
        self.hboxlayout2.addWidget(self.xMax)
        self.gridLayout.addLayout(self.hboxlayout2, 4, 0, 1, 1)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName(_fromUtf8("hboxlayout3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.hboxlayout3.addWidget(self.label_5)
        self.yMax = QtGui.QLineEdit(self.groupBox)
        self.yMax.setEnabled(True)
        self.yMax.setInputMask(_fromUtf8(""))
        self.yMax.setText(_fromUtf8(""))
        self.yMax.setObjectName(_fromUtf8("yMax"))
        self.hboxlayout3.addWidget(self.yMax)
        self.gridLayout.addLayout(self.hboxlayout3, 4, 1, 1, 1)
        self.chkAlign = QtGui.QCheckBox(self.groupBox)
        self.chkAlign.setObjectName(_fromUtf8("chkAlign"))
        self.gridLayout.addWidget(self.chkAlign, 1, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridBox = QtGui.QGroupBox(Dialog)
        self.gridBox.setObjectName(_fromUtf8("gridBox"))
        self.gridlayout = QtGui.QGridLayout(self.gridBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lblX = QtGui.QLabel(self.gridBox)
        self.lblX.setObjectName(_fromUtf8("lblX"))
        self.gridlayout.addWidget(self.lblX, 0, 1, 1, 1)
        self.spnX = QtGui.QDoubleSpinBox(self.gridBox)
        self.spnX.setDecimals(10)
        self.spnX.setMinimum(0.0001)
        self.spnX.setMaximum(1000000000.0)
        self.spnX.setSingleStep(0.0001)
        self.spnX.setObjectName(_fromUtf8("spnX"))
        self.gridlayout.addWidget(self.spnX, 0, 2, 1, 1)
        self.chkLock = QtGui.QCheckBox(self.gridBox)
        self.chkLock.setChecked(True)
        self.chkLock.setObjectName(_fromUtf8("chkLock"))
        self.gridlayout.addWidget(self.chkLock, 0, 3, 2, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.lblY = QtGui.QLabel(self.gridBox)
        self.lblY.setEnabled(False)
        self.lblY.setObjectName(_fromUtf8("lblY"))
        self.gridlayout.addWidget(self.lblY, 1, 1, 1, 1)
        self.spnY = QtGui.QDoubleSpinBox(self.gridBox)
        self.spnY.setEnabled(False)
        self.spnY.setDecimals(10)
        self.spnY.setMinimum(0.0001)
        self.spnY.setMaximum(1000000000.0)
        self.spnY.setSingleStep(0.0001)
        self.spnY.setObjectName(_fromUtf8("spnY"))
        self.gridlayout.addWidget(self.spnY, 1, 2, 1, 1)
        self.rdoPolygons = QtGui.QRadioButton(self.gridBox)
        self.rdoPolygons.setChecked(False)
        self.rdoPolygons.setObjectName(_fromUtf8("rdoPolygons"))
        self.gridlayout.addWidget(self.rdoPolygons, 2, 0, 1, 3)
        self.rdoLines = QtGui.QRadioButton(self.gridBox)
        self.rdoLines.setChecked(True)
        self.rdoLines.setObjectName(_fromUtf8("rdoLines"))
        self.gridlayout.addWidget(self.rdoLines, 3, 0, 1, 3)
        self.gridLayout_2.addWidget(self.gridBox, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName(_fromUtf8("hboxlayout4"))
        self.outShape = QtGui.QLineEdit(Dialog)
        self.outShape.setReadOnly(True)
        self.outShape.setObjectName(_fromUtf8("outShape"))
        self.hboxlayout4.addWidget(self.outShape)
        self.toolOut = QtGui.QPushButton(Dialog)
        self.toolOut.setObjectName(_fromUtf8("toolOut"))
        self.hboxlayout4.addWidget(self.toolOut)
        self.gridLayout_2.addLayout(self.hboxlayout4, 4, 0, 1, 1)
        self.addToCanvasCheck = QtGui.QCheckBox(Dialog)
        self.addToCanvasCheck.setChecked(True)
        self.addToCanvasCheck.setObjectName(_fromUtf8("addToCanvasCheck"))
        self.gridLayout_2.addWidget(self.addToCanvasCheck, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.horizontalLayout.addWidget(self.buttonBox_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QObject.connect(self.chkLock, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spnY.setDisabled)
        QtCore.QObject.connect(self.chkLock, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lblY.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Generate Vector Grid", None))
        self.groupBox.setTitle(_translate("Dialog", "Grid extent", None))
        self.btnUpdate.setText(_translate("Dialog", "Update extents from layer", None))
        self.btnCanvas.setText(_translate("Dialog", "Update extents from canvas", None))
        self.label.setText(_translate("Dialog", "X Min", None))
        self.label_4.setText(_translate("Dialog", "Y Min", None))
        self.label_3.setText(_translate("Dialog", "X Max", None))
        self.label_5.setText(_translate("Dialog", "Y Max", None))
        self.chkAlign.setText(_translate("Dialog", "Align extents and resolution to selected raster layer", None))
        self.gridBox.setTitle(_translate("Dialog", "Parameters", None))
        self.lblX.setText(_translate("Dialog", "X", None))
        self.chkLock.setText(_translate("Dialog", "Lock 1:1 ratio", None))
        self.lblY.setText(_translate("Dialog", "Y", None))
        self.rdoPolygons.setText(_translate("Dialog", "Output grid as polygons", None))
        self.rdoLines.setText(_translate("Dialog", "Output grid as lines", None))
        self.label_2.setText(_translate("Dialog", "Output shapefile", None))
        self.toolOut.setText(_translate("Dialog", "Browse", None))
        self.addToCanvasCheck.setText(_translate("Dialog", "Add result to canvas", None))

