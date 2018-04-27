# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mwestphall/piccolo2/piccolo2-player/piccolo2/player/schedulelist.ui'
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

class Ui_ScheduleListWindow(object):
    def setupUi(self, ScheduleListWindow):
        ScheduleListWindow.setObjectName(_fromUtf8("ScheduleListWindow"))
        ScheduleListWindow.setWindowModality(QtCore.Qt.NonModal)
        ScheduleListWindow.resize(898, 346)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScheduleListWindow.sizePolicy().hasHeightForWidth())
        ScheduleListWindow.setSizePolicy(sizePolicy)
        ScheduleListWindow.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(ScheduleListWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(ScheduleListWindow)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(ScheduleListWindow)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ScheduleListWindow)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ScheduleListWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ScheduleListWindow)

    def retranslateUi(self, ScheduleListWindow):
        ScheduleListWindow.setWindowTitle(_translate("ScheduleListWindow", "Schedule List", None))
        self.closeButton.setText(_translate("ScheduleListWindow", "Close", None))

