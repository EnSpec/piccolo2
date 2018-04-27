# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mwestphall/piccolo2/piccolo2-player/piccolo2/player/connect.ui'
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

class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        ConnectDialog.setObjectName(_fromUtf8("ConnectDialog"))
        ConnectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConnectDialog.resize(400, 233)
        self.verticalLayout = QtGui.QVBoxLayout(ConnectDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.connectHTTP = QtGui.QRadioButton(ConnectDialog)
        self.connectHTTP.setChecked(True)
        self.connectHTTP.setObjectName(_fromUtf8("connectHTTP"))
        self.verticalLayout.addWidget(self.connectHTTP)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ConnectDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.serverURL = QtGui.QLineEdit(ConnectDialog)
        self.serverURL.setStatusTip(_fromUtf8(""))
        self.serverURL.setObjectName(_fromUtf8("serverURL"))
        self.horizontalLayout.addWidget(self.serverURL)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(ConnectDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.connectXBee = QtGui.QRadioButton(ConnectDialog)
        self.connectXBee.setObjectName(_fromUtf8("connectXBee"))
        self.verticalLayout.addWidget(self.connectXBee)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(ConnectDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.xbeeSerial = QtGui.QLineEdit(ConnectDialog)
        self.xbeeSerial.setStatusTip(_fromUtf8(""))
        self.xbeeSerial.setObjectName(_fromUtf8("xbeeSerial"))
        self.horizontalLayout_2.addWidget(self.xbeeSerial)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(ConnectDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.connectXBeeAuto = QtGui.QRadioButton(ConnectDialog)
        self.connectXBeeAuto.setObjectName(_fromUtf8("connectXBeeAuto"))
        self.verticalLayout.addWidget(self.connectXBeeAuto)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(ConnectDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.xbeeBaud = QtGui.QLineEdit(ConnectDialog)
        self.xbeeBaud.setObjectName(_fromUtf8("xbeeBaud"))
        self.horizontalLayout_3.addWidget(self.xbeeBaud)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(ConnectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ConnectDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConnectDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConnectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectDialog)

    def retranslateUi(self, ConnectDialog):
        ConnectDialog.setWindowTitle(_translate("ConnectDialog", "Connect", None))
        self.connectHTTP.setText(_translate("ConnectDialog", "Connect via http", None))
        self.label.setText(_translate("ConnectDialog", "Server URL", None))
        self.serverURL.setToolTip(_translate("ConnectDialog", "enter the server URL", None))
        self.serverURL.setText(_translate("ConnectDialog", "http://localhost:8080", None))
        self.connectXBee.setText(_translate("ConnectDialog", "Connect via XBee Radio directly", None))
        self.label_2.setText(_translate("ConnectDialog", "Server XBee Serial Number: ", None))
        self.xbeeSerial.setToolTip(_translate("ConnectDialog", "enter XBee serial number", None))
        self.connectXBeeAuto.setText(_translate("ConnectDialog", "Connect via XBee Radio network scan", None))
        self.label_3.setText(_translate("ConnectDialog", "Server XBee Baudrate: ", None))
        self.xbeeBaud.setText(_translate("ConnectDialog", "115200", None))

