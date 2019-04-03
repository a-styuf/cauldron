# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mb110_224_win.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(600, 350))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tempTWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempTWidget.sizePolicy().hasHeightForWidth())
        self.tempTWidget.setSizePolicy(sizePolicy)
        self.tempTWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.tempTWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tempTWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tempTWidget.setRowCount(20)
        self.tempTWidget.setObjectName("tempTWidget")
        self.tempTWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tempTWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tempTWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tempTWidget.setItem(0, 1, item)
        self.tempTWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tempTWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tempTWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tempTWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tempTWidget.horizontalHeader().setStretchLastSection(True)
        self.tempTWidget.verticalHeader().setDefaultSectionSize(30)
        self.tempTWidget.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout.addWidget(self.tempTWidget, 0, 2, 4, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.devNameLabel = QtWidgets.QLabel(Form)
        self.devNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.devNameLabel.setObjectName("devNameLabel")
        self.gridLayout.addWidget(self.devNameLabel, 0, 0, 1, 2)
        self.reconnectPButt = QtWidgets.QPushButton(Form)
        self.reconnectPButt.setObjectName("reconnectPButt")
        self.gridLayout.addWidget(self.reconnectPButt, 3, 0, 1, 2)
        self.singleReadPButt = QtWidgets.QPushButton(Form)
        self.singleReadPButt.setMinimumSize(QtCore.QSize(200, 0))
        self.singleReadPButt.setObjectName("singleReadPButt")
        self.gridLayout.addWidget(self.singleReadPButt, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tempTWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.tempTWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Значение"))
        __sortingEnabled = self.tempTWidget.isSortingEnabled()
        self.tempTWidget.setSortingEnabled(False)
        self.tempTWidget.setSortingEnabled(__sortingEnabled)
        self.devNameLabel.setText(_translate("Form", "МВ110-224.8А"))
        self.reconnectPButt.setText(_translate("Form", "Переподключение"))
        self.singleReadPButt.setText(_translate("Form", "Чтение"))


