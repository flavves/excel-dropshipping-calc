# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılımileilgilihersey/onluk/excel_islemler/giris.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.giris = QtWidgets.QLabel(self.centralwidget)
        self.giris.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.giris.setText("")
        self.giris.setObjectName("giris")
        self.lisans = QtWidgets.QTextEdit(self.centralwidget)
        self.lisans.setGeometry(QtCore.QRect(110, 340, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lisans.setFont(font)
        self.lisans.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(151, 188, 199);")
        self.lisans.setObjectName("lisans")
        self.giris_buton = QtWidgets.QPushButton(self.centralwidget)
        self.giris_buton.setGeometry(QtCore.QRect(190, 440, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.giris_buton.setFont(font)
        self.giris_buton.setStyleSheet("background-color: rgb(252, 210, 79);\n"
"color: rgb(0, 0, 0);")
        self.giris_buton.setObjectName("giris_buton")
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.giris_buton.setText(_translate("MainWindow2", "GİRİŞ"))

