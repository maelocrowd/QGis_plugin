# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/src/qgis/python/plugins/GdalTools/tools/widgetTranslate.ui'
#
# Created: Wed Jul 29 01:08:13 2015
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

class Ui_GdalToolsWidget(object):
    def setupUi(self, GdalToolsWidget):
        GdalToolsWidget.setObjectName(_fromUtf8("GdalToolsWidget"))
        GdalToolsWidget.resize(335, 429)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GdalToolsWidget.sizePolicy().hasHeightForWidth())
        GdalToolsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(GdalToolsWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.batchCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.batchCheck.setObjectName(_fromUtf8("batchCheck"))
        self.verticalLayout_2.addWidget(self.batchCheck)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(GdalToolsWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(GdalToolsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.formatLabel = QtGui.QLabel(GdalToolsWidget)
        self.formatLabel.setObjectName(_fromUtf8("formatLabel"))
        self.gridLayout.addWidget(self.formatLabel, 2, 0, 1, 1)
        self.formatCombo = QtGui.QComboBox(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatCombo.sizePolicy().hasHeightForWidth())
        self.formatCombo.setSizePolicy(sizePolicy)
        self.formatCombo.setObjectName(_fromUtf8("formatCombo"))
        self.gridLayout.addWidget(self.formatCombo, 2, 1, 1, 1)
        self.targetSRSCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.targetSRSCheck.setObjectName(_fromUtf8("targetSRSCheck"))
        self.gridLayout.addWidget(self.targetSRSCheck, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.targetSRSEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.targetSRSEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.targetSRSEdit.setObjectName(_fromUtf8("targetSRSEdit"))
        self.horizontalLayout.addWidget(self.targetSRSEdit)
        self.selectTargetSRSButton = QtGui.QPushButton(GdalToolsWidget)
        self.selectTargetSRSButton.setObjectName(_fromUtf8("selectTargetSRSButton"))
        self.horizontalLayout.addWidget(self.selectTargetSRSButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.outsizeCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.outsizeCheck.setMaximumSize(QtCore.QSize(100, 16777215))
        self.outsizeCheck.setObjectName(_fromUtf8("outsizeCheck"))
        self.gridLayout.addWidget(self.outsizeCheck, 4, 0, 1, 1)
        self.outsizeSpin = QtGui.QSpinBox(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outsizeSpin.sizePolicy().hasHeightForWidth())
        self.outsizeSpin.setSizePolicy(sizePolicy)
        self.outsizeSpin.setMinimum(1)
        self.outsizeSpin.setMaximum(1000)
        self.outsizeSpin.setObjectName(_fromUtf8("outsizeSpin"))
        self.gridLayout.addWidget(self.outsizeSpin, 4, 1, 1, 1)
        self.nodataCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.nodataCheck.setObjectName(_fromUtf8("nodataCheck"))
        self.gridLayout.addWidget(self.nodataCheck, 5, 0, 1, 1)
        self.expandCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.expandCheck.setObjectName(_fromUtf8("expandCheck"))
        self.gridLayout.addWidget(self.expandCheck, 6, 0, 1, 1)
        self.expandCombo = QtGui.QComboBox(GdalToolsWidget)
        self.expandCombo.setObjectName(_fromUtf8("expandCombo"))
        self.expandCombo.addItem(_fromUtf8(""))
        self.expandCombo.addItem(_fromUtf8(""))
        self.expandCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.expandCombo, 6, 1, 1, 1)
        self.srcwinCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.srcwinCheck.setObjectName(_fromUtf8("srcwinCheck"))
        self.gridLayout.addWidget(self.srcwinCheck, 7, 0, 1, 1)
        self.srcwinEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.srcwinEdit.setObjectName(_fromUtf8("srcwinEdit"))
        self.gridLayout.addWidget(self.srcwinEdit, 7, 1, 1, 1)
        self.prjwinCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.prjwinCheck.setObjectName(_fromUtf8("prjwinCheck"))
        self.gridLayout.addWidget(self.prjwinCheck, 8, 0, 1, 1)
        self.prjwinEdit = QtGui.QLineEdit(GdalToolsWidget)
        self.prjwinEdit.setObjectName(_fromUtf8("prjwinEdit"))
        self.gridLayout.addWidget(self.prjwinEdit, 8, 1, 1, 1)
        self.sdsCheck = QtGui.QCheckBox(GdalToolsWidget)
        self.sdsCheck.setObjectName(_fromUtf8("sdsCheck"))
        self.gridLayout.addWidget(self.sdsCheck, 9, 0, 1, 1)
        self.nodataSpin = QtGui.QSpinBox(GdalToolsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodataSpin.sizePolicy().hasHeightForWidth())
        self.nodataSpin.setSizePolicy(sizePolicy)
        self.nodataSpin.setMinimum(-999999999)
        self.nodataSpin.setMaximum(999999999)
        self.nodataSpin.setObjectName(_fromUtf8("nodataSpin"))
        self.gridLayout.addWidget(self.nodataSpin, 5, 1, 1, 1)
        self.inSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.inSelector.setObjectName(_fromUtf8("inSelector"))
        self.gridLayout.addWidget(self.inSelector, 0, 1, 1, 1)
        self.outSelector = GdalToolsInOutSelector(GdalToolsWidget)
        self.outSelector.setObjectName(_fromUtf8("outSelector"))
        self.gridLayout.addWidget(self.outSelector, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.creationOptionsGroupBox = QgsCollapsibleGroupBox(GdalToolsWidget)
        self.creationOptionsGroupBox.setProperty("collapsed", False)
        self.creationOptionsGroupBox.setProperty("saveCollapsedState", True)
        self.creationOptionsGroupBox.setCheckable(True)
        self.creationOptionsGroupBox.setChecked(False)
        self.creationOptionsGroupBox.setObjectName(_fromUtf8("creationOptionsGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.creationOptionsGroupBox)
        self.verticalLayout.setContentsMargins(9, -1, -1, 9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.creationOptionsWidget = QgsRasterFormatSaveOptionsWidget(self.creationOptionsGroupBox)
        self.creationOptionsWidget.setObjectName(_fromUtf8("creationOptionsWidget"))
        self.verticalLayout.addWidget(self.creationOptionsWidget)
        self.verticalLayout_2.addWidget(self.creationOptionsGroupBox)
        self.progressBar = QtGui.QProgressBar(GdalToolsWidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.label_3.setBuddy(self.inSelector)
        self.label_2.setBuddy(self.outSelector)

        self.retranslateUi(GdalToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(GdalToolsWidget)

    def retranslateUi(self, GdalToolsWidget):
        GdalToolsWidget.setWindowTitle(_translate("GdalToolsWidget", "Translate (Convert format)", None))
        self.batchCheck.setText(_translate("GdalToolsWidget", "Batch mode (for processing whole directory)", None))
        self.label_3.setText(_translate("GdalToolsWidget", "&Input Layer", None))
        self.label_2.setText(_translate("GdalToolsWidget", "&Output file", None))
        self.formatLabel.setText(_translate("GdalToolsWidget", "Output format", None))
        self.targetSRSCheck.setText(_translate("GdalToolsWidget", "&Target SRS", None))
        self.selectTargetSRSButton.setText(_translate("GdalToolsWidget", "Select...", None))
        self.outsizeCheck.setToolTip(_translate("GdalToolsWidget", "Percentage to resize image. This will change pixel size/image resolution accordingly: 25% will create an image with pixels 4x larger.", None))
        self.outsizeCheck.setText(_translate("GdalToolsWidget", "Outsize", None))
        self.outsizeSpin.setToolTip(_translate("GdalToolsWidget", "Percentage to resize image. This will change pixel size/image resolution accordingly: 25% will create an image with pixels 4x larger.", None))
        self.outsizeSpin.setSuffix(_translate("GdalToolsWidget", "%", None))
        self.nodataCheck.setToolTip(_translate("GdalToolsWidget", "Assign a specified nodata value to output bands.", None))
        self.nodataCheck.setText(_translate("GdalToolsWidget", "No data", None))
        self.expandCheck.setToolTip(_translate("GdalToolsWidget", "To expose a dataset with 1 band with a color table as a dataset with 3 (RGB) or 4 (RGBA) bands. \n"
"Useful for output drivers such as JPEG, JPEG2000, MrSID, ECW that don\'t support color indexed datasets. \n"
"The \'gray\' value (from GDAL 1.7.0) enables to expand a dataset with a color table that only contains gray levels to a gray indexed dataset.", None))
        self.expandCheck.setText(_translate("GdalToolsWidget", "Expand", None))
        self.expandCombo.setToolTip(_translate("GdalToolsWidget", "To expose a dataset with 1 band with a color table as a dataset with 3 (RGB) or 4 (RGBA) bands. \n"
"Useful for output drivers such as JPEG, JPEG2000, MrSID, ECW that don\'t support color indexed datasets. \n"
"The \'gray\' value (from GDAL 1.7.0) enables to expand a dataset with a color table that only contains gray levels to a gray indexed dataset.", None))
        self.expandCombo.setItemText(0, _translate("GdalToolsWidget", "Gray", None))
        self.expandCombo.setItemText(1, _translate("GdalToolsWidget", "RGB", None))
        self.expandCombo.setItemText(2, _translate("GdalToolsWidget", "RGBA", None))
        self.srcwinCheck.setToolTip(_translate("GdalToolsWidget", "Selects a subwindow from the source image for copying based on pixel/line location. (Enter Xoff Yoff Xsize Ysize)", None))
        self.srcwinCheck.setText(_translate("GdalToolsWidget", "Srcwin", None))
        self.srcwinEdit.setToolTip(_translate("GdalToolsWidget", "Selects a subwindow from the source image for copying based on pixel/line location. (Enter Xoff Yoff Xsize Ysize)", None))
        self.prjwinCheck.setToolTip(_translate("GdalToolsWidget", "Selects a subwindow from the source image for copying (like -srcwin) but with the corners given in georeferenced coordinates. (Enter ulx uly lrx lry)", None))
        self.prjwinCheck.setText(_translate("GdalToolsWidget", "Prjwin", None))
        self.prjwinEdit.setToolTip(_translate("GdalToolsWidget", "Selects a subwindow from the source image for copying (like -srcwin) but with the corners given in georeferenced coordinates. (Enter ulx uly lrx lry)", None))
        self.sdsCheck.setToolTip(_translate("GdalToolsWidget", "Copy all subdatasets of this file to individual output files. Use with formats like HDF or OGDI that have subdatasets.", None))
        self.sdsCheck.setText(_translate("GdalToolsWidget", "Sds", None))
        self.nodataSpin.setToolTip(_translate("GdalToolsWidget", "Assign a specified nodata value to output bands.", None))
        self.creationOptionsGroupBox.setTitle(_translate("GdalToolsWidget", "&Creation Options", None))

from qgis.gui import QgsCollapsibleGroupBox, QgsRasterFormatSaveOptionsWidget
from inOutSelector import GdalToolsInOutSelector