# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/fTools/tools/frmVisual.ui'
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
        Dialog.resize(370, 531)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vboxlayout.addWidget(self.label_3)
        self.inShape = QtGui.QComboBox(Dialog)
        self.inShape.setObjectName(_fromUtf8("inShape"))
        self.vboxlayout.addWidget(self.inShape)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.useSelected = QtGui.QCheckBox(Dialog)
        self.useSelected.setObjectName(_fromUtf8("useSelected"))
        self.verticalLayout.addWidget(self.useSelected)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout1.addWidget(self.label)
        self.cmbField = QtGui.QComboBox(Dialog)
        self.cmbField.setObjectName(_fromUtf8("cmbField"))
        self.vboxlayout1.addWidget(self.cmbField)
        self.gridLayout.addLayout(self.vboxlayout1, 2, 0, 1, 1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout2.addWidget(self.label_2)
        self.tblUnique = QtGui.QTableWidget(Dialog)
        self.tblUnique.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblUnique.setTabKeyNavigation(False)
        self.tblUnique.setProperty("showDropIndicator", False)
        self.tblUnique.setDragDropOverwriteMode(False)
        self.tblUnique.setAlternatingRowColors(True)
        self.tblUnique.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tblUnique.setShowGrid(False)
        self.tblUnique.setWordWrap(False)
        self.tblUnique.setCornerButtonEnabled(False)
        self.tblUnique.setObjectName(_fromUtf8("tblUnique"))
        self.tblUnique.setColumnCount(0)
        self.tblUnique.setRowCount(0)
        self.tblUnique.horizontalHeader().setVisible(False)
        self.tblUnique.verticalHeader().setVisible(False)
        self.vboxlayout2.addWidget(self.tblUnique)
        self.gridLayout.addLayout(self.vboxlayout2, 3, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.hboxlayout.addWidget(self.label_4)
        self.lstCount = QtGui.QLineEdit(Dialog)
        self.lstCount.setReadOnly(True)
        self.lstCount.setObjectName(_fromUtf8("lstCount"))
        self.hboxlayout.addWidget(self.lstCount)
        self.gridLayout.addLayout(self.hboxlayout, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 6, 0, 1, 1)
        self.ckBoxShpError = QtGui.QCheckBox(Dialog)
        self.ckBoxShpError.setObjectName(_fromUtf8("ckBoxShpError"))
        self.gridLayout.addWidget(self.ckBoxShpError, 7, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditShpError = QtGui.QLineEdit(Dialog)
        self.lineEditShpError.setReadOnly(True)
        self.lineEditShpError.setObjectName(_fromUtf8("lineEditShpError"))
        self.horizontalLayout.addWidget(self.lineEditShpError)
        self.browseShpError = QtGui.QPushButton(Dialog)
        self.browseShpError.setObjectName(_fromUtf8("browseShpError"))
        self.horizontalLayout.addWidget(self.browseShpError)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 1)
        self.addToCanvasCheck = QtGui.QCheckBox(Dialog)
        self.addToCanvasCheck.setChecked(True)
        self.addToCanvasCheck.setObjectName(_fromUtf8("addToCanvasCheck"))
        self.gridLayout.addWidget(self.addToCanvasCheck, 10, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.partProgressBar = QtGui.QProgressBar(Dialog)
        self.partProgressBar.setProperty("value", 24)
        self.partProgressBar.setObjectName(_fromUtf8("partProgressBar"))
        self.verticalLayout_2.addWidget(self.partProgressBar)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.buttonBox_2 = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox_2.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.horizontalLayout_2.addWidget(self.buttonBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 11, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "List Unique Values", None))
        self.label_3.setText(_translate("Dialog", "Input Vector Layer", None))
        self.useSelected.setText(_translate("Dialog", "Use only selected features", None))
        self.label.setText(_translate("Dialog", "Target field", None))
        self.label_2.setText(_translate("Dialog", "Unique values list", None))
        self.label_4.setText(_translate("Dialog", "Unique value count", None))
        self.label_5.setText(_translate("Dialog", "Press Ctrl+C to copy results to the clipboard", None))
        self.ckBoxShpError.setText(_translate("Dialog", "Save errors location", None))
        self.label_6.setText(_translate("Dialog", "Output point shapefile", None))
        self.browseShpError.setText(_translate("Dialog", "Browse", None))
        self.addToCanvasCheck.setText(_translate("Dialog", "Add result to canvas", None))

