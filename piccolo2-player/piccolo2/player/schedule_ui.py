# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mwestphall/piccolo2/piccolo2-player/piccolo2/player/schedule.ui'
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

class Ui_ScheduleDialog(object):
    def setupUi(self, ScheduleDialog):
        ScheduleDialog.setObjectName(_fromUtf8("ScheduleDialog"))
        ScheduleDialog.resize(314, 200)
        ScheduleDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(ScheduleDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ScheduleDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.startTimeEdit = QtGui.QDateTimeEdit(ScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTimeEdit.sizePolicy().hasHeightForWidth())
        self.startTimeEdit.setSizePolicy(sizePolicy)
        self.startTimeEdit.setCalendarPopup(True)
        self.startTimeEdit.setObjectName(_fromUtf8("startTimeEdit"))
        self.gridLayout.addWidget(self.startTimeEdit, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.repeatSchedule = QtGui.QCheckBox(ScheduleDialog)
        self.repeatSchedule.setObjectName(_fromUtf8("repeatSchedule"))
        self.gridLayout.addWidget(self.repeatSchedule, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ScheduleDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.endTimeEdit = QtGui.QDateTimeEdit(ScheduleDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endTimeEdit.sizePolicy().hasHeightForWidth())
        self.endTimeEdit.setSizePolicy(sizePolicy)
        self.endTimeEdit.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.endTimeEdit.setCalendarPopup(True)
        self.endTimeEdit.setObjectName(_fromUtf8("endTimeEdit"))
        self.gridLayout.addWidget(self.endTimeEdit, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ScheduleDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.intervalEdit = QtGui.QTimeEdit(ScheduleDialog)
        self.intervalEdit.setObjectName(_fromUtf8("intervalEdit"))
        self.gridLayout.addWidget(self.intervalEdit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ScheduleDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ScheduleDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ScheduleDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ScheduleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ScheduleDialog)

    def retranslateUi(self, ScheduleDialog):
        ScheduleDialog.setWindowTitle(_translate("ScheduleDialog", "new schedule", None))
        self.label.setText(_translate("ScheduleDialog", "start time", None))
        self.startTimeEdit.setDisplayFormat(_translate("ScheduleDialog", "dd/MM/yyyy HH:mm:ss", None))
        self.repeatSchedule.setText(_translate("ScheduleDialog", "repeat schedule", None))
        self.label_2.setText(_translate("ScheduleDialog", "end time", None))
        self.endTimeEdit.setDisplayFormat(_translate("ScheduleDialog", "dd/MM/yyyy HH:mm:ss", None))
        self.label_3.setText(_translate("ScheduleDialog", "interval (sec)", None))
        self.intervalEdit.setDisplayFormat(_translate("ScheduleDialog", "HH:mm:ss", None))

