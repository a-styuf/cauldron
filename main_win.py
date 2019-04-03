# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cauldron(object):
    def setupUi(self, Cauldron):
        Cauldron.setObjectName("Cauldron")
        Cauldron.resize(900, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Cauldron.sizePolicy().hasHeightForWidth())
        Cauldron.setSizePolicy(sizePolicy)
        Cauldron.setMinimumSize(QtCore.QSize(900, 400))
        self.centralwidget = QtWidgets.QWidget(Cauldron)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.devGBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devGBox.sizePolicy().hasHeightForWidth())
        self.devGBox.setSizePolicy(sizePolicy)
        self.devGBox.setMinimumSize(QtCore.QSize(620, 370))
        self.devGBox.setObjectName("devGBox")
        self.gridLayout.addWidget(self.devGBox, 0, 0, 10, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.periodLabel = QtWidgets.QLabel(self.centralwidget)
        self.periodLabel.setObjectName("periodLabel")
        self.gridLayout.addWidget(self.periodLabel, 3, 1, 1, 1)
        self.startCyclePButt = QtWidgets.QPushButton(self.centralwidget)
        self.startCyclePButt.setObjectName("startCyclePButt")
        self.gridLayout.addWidget(self.startCyclePButt, 2, 1, 1, 1)
        self.restartLogPButt = QtWidgets.QPushButton(self.centralwidget)
        self.restartLogPButt.setObjectName("restartLogPButt")
        self.gridLayout.addWidget(self.restartLogPButt, 4, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 1, 1, 2)
        self.periodSBox = QtWidgets.QSpinBox(self.centralwidget)
        self.periodSBox.setMinimum(1)
        self.periodSBox.setMaximum(3600)
        self.periodSBox.setObjectName("periodSBox")
        self.gridLayout.addWidget(self.periodSBox, 3, 2, 1, 1)
        self.stopCyclePButt = QtWidgets.QPushButton(self.centralwidget)
        self.stopCyclePButt.setObjectName("stopCyclePButt")
        self.gridLayout.addWidget(self.stopCyclePButt, 2, 2, 1, 1)
        self.restartGraphPButt = QtWidgets.QPushButton(self.centralwidget)
        self.restartGraphPButt.setObjectName("restartGraphPButt")
        self.gridLayout.addWidget(self.restartGraphPButt, 5, 1, 1, 2)
        self.graphPButt = QtWidgets.QPushButton(self.centralwidget)
        self.graphPButt.setObjectName("graphPButt")
        self.gridLayout.addWidget(self.graphPButt, 6, 1, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        Cauldron.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cauldron)
        QtCore.QMetaObject.connectSlotsByName(Cauldron)

    def retranslateUi(self, Cauldron):
        _translate = QtCore.QCoreApplication.translate
        Cauldron.setWindowTitle(_translate("Cauldron", "Cauldron"))
        self.devGBox.setTitle(_translate("Cauldron", "Устройства"))
        self.label.setText(_translate("Cauldron", "Циклический опрос"))
        self.periodLabel.setText(_translate("Cauldron", "Период"))
        self.startCyclePButt.setText(_translate("Cauldron", "Старт"))
        self.restartLogPButt.setText(_translate("Cauldron", "Перезапуск лога"))
        self.stopCyclePButt.setText(_translate("Cauldron", "Стоп"))
        self.restartGraphPButt.setText(_translate("Cauldron", "Перезапуск графика"))
        self.graphPButt.setText(_translate("Cauldron", "Открыть графики"))


