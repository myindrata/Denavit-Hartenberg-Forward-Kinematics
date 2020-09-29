# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'armgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(740, 190, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(840, 190, 75, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(810, 240, 181, 41))
        self.label1.setObjectName("label1")
        self.hslider1 = QtWidgets.QSlider(self.centralwidget)
        self.hslider1.setGeometry(QtCore.QRect(729, 70, 271, 22))
        self.hslider1.setMinimum(0)
        self.hslider1.setMaximum(180)
        self.hslider1.setSingleStep(1)
        self.hslider1.setProperty("value", 90)
        self.hslider1.setOrientation(QtCore.Qt.Horizontal)
        self.hslider1.setObjectName("hslider1")
        self.hslider2 = QtWidgets.QSlider(self.centralwidget)
        self.hslider2.setGeometry(QtCore.QRect(729, 100, 271, 22))
        self.hslider2.setMinimum(-90)
        self.hslider2.setMaximum(90)
        self.hslider2.setProperty("value", 60)
        self.hslider2.setOrientation(QtCore.Qt.Horizontal)
        self.hslider2.setObjectName("hslider2")
        self.hslider3 = QtWidgets.QSlider(self.centralwidget)
        self.hslider3.setGeometry(QtCore.QRect(729, 130, 271, 22))
        self.hslider3.setMinimum(-90)
        self.hslider3.setMaximum(90)
        self.hslider3.setProperty("value", -60)
        self.hslider3.setOrientation(QtCore.Qt.Horizontal)
        self.hslider3.setObjectName("hslider3")
        self.labels1 = QtWidgets.QLabel(self.centralwidget)
        self.labels1.setGeometry(QtCore.QRect(620, 70, 91, 16))
        self.labels1.setObjectName("labels1")
        self.labels2 = QtWidgets.QLabel(self.centralwidget)
        self.labels2.setGeometry(QtCore.QRect(620, 100, 91, 16))
        self.labels2.setObjectName("labels2")
        self.labels3 = QtWidgets.QLabel(self.centralwidget)
        self.labels3.setGeometry(QtCore.QRect(620, 130, 91, 16))
        self.labels3.setObjectName("labels3")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setEnabled(True)
        self.MplWidget.setGeometry(QtCore.QRect(20, 30, 581, 491))
        self.MplWidget.setMouseTracking(True)
        self.MplWidget.setTabletTracking(True)
        self.MplWidget.setObjectName("MplWidget")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(740, 30, 221, 23))
        self.pushButton_reset.setObjectName("pushButton_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "but1"))
        self.pushButton2.setText(_translate("MainWindow", "but2"))
        self.label1.setText(_translate("MainWindow", "Indra Agustian - TE Unib"))
        self.labels1.setText(_translate("MainWindow", "Joint 1 Angle:"))
        self.labels2.setText(_translate("MainWindow", "Joint 2 angle:"))
        self.labels3.setText(_translate("MainWindow", "Joint 3 angle:"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

