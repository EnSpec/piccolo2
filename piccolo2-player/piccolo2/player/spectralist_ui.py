# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mwestphall/piccolo2/piccolo2-player/piccolo2/player/spectralist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_SpectraListDialog(object):
    def setupUi(self, SpectraListDialog):
        SpectraListDialog.setObjectName(_fromUtf8("SpectraListDialog"))
        SpectraListDialog.resize(571, 447)
        SpectraListDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SpectraListDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(SpectraListDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.listWidget = QtGui.QListWidget(SpectraListDialog)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_4.addWidget(self.listWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(SpectraListDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.listWidget_2 = QtGui.QListWidget(SpectraListDialog)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.verticalLayout_5.addWidget(self.listWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lightButton = QtGui.QRadioButton(SpectraListDialog)
        self.lightButton.setChecked(True)
        self.lightButton.setObjectName(_fromUtf8("lightButton"))
        self.horizontalLayout.addWidget(self.lightButton)
        self.darkButton = QtGui.QRadioButton(SpectraListDialog)
        self.darkButton.setObjectName(_fromUtf8("darkButton"))
        self.horizontalLayout.addWidget(self.darkButton)
        self.bothButton = QtGui.QRadioButton(SpectraListDialog)
        self.bothButton.setChecked(False)
        self.bothButton.setObjectName(_fromUtf8("bothButton"))
        self.horizontalLayout.addWidget(self.bothButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SpectraListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SpectraListDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SpectraListDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SpectraListDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SpectraListDialog)

    def retranslateUi(self, SpectraListDialog):
        SpectraListDialog.setWindowTitle(_translate("SpectraListDialog", "spectra list", None))
        self.label.setText(_translate("SpectraListDialog", "Batch:", None))
        self.label_2.setText(_translate("SpectraListDialog", "Spectrum:", None))
        self.lightButton.setText(_translate("SpectraListDialog", "light", None))
        self.darkButton.setText(_translate("SpectraListDialog", "dark", None))
        self.bothButton.setText(_translate("SpectraListDialog", "both", None))

