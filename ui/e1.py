# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 751, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.InsertTrail = QtWidgets.QWidget()
        self.InsertTrail.setObjectName("InsertTrail")
        self.parkInput = QtWidgets.QComboBox(self.InsertTrail)
        self.parkInput.setGeometry(QtCore.QRect(70, 130, 201, 22))
        self.parkInput.setObjectName("parkInput")
        self.label_8 = QtWidgets.QLabel(self.InsertTrail)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.InsertTrail)
        self.label_6.setGeometry(QtCore.QRect(170, 170, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.InsertTrail)
        self.label_7.setGeometry(QtCore.QRect(150, 210, 101, 16))
        self.label_7.setObjectName("label_7")
        self.timeInput = QtWidgets.QSpinBox(self.InsertTrail)
        self.timeInput.setGeometry(QtCore.QRect(220, 250, 42, 22))
        self.timeInput.setObjectName("timeInput")
        self.summInput = QtWidgets.QTextEdit(self.InsertTrail)
        self.summInput.setGeometry(QtCore.QRect(280, 50, 331, 291))
        self.summInput.setObjectName("summInput")
        self.label_4 = QtWidgets.QLabel(self.InsertTrail)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.InsertTrail)
        self.label_10.setGeometry(QtCore.QRect(170, 250, 41, 16))
        self.label_10.setObjectName("label_10")
        self.regionInput = QtWidgets.QComboBox(self.InsertTrail)
        self.regionInput.setGeometry(QtCore.QRect(70, 90, 201, 22))
        self.regionInput.setObjectName("regionInput")
        self.gradInput = QtWidgets.QSpinBox(self.InsertTrail)
        self.gradInput.setGeometry(QtCore.QRect(90, 210, 42, 22))
        self.gradInput.setObjectName("gradInput")
        self.starInput = QtWidgets.QSpinBox(self.InsertTrail)
        self.starInput.setGeometry(QtCore.QRect(220, 170, 42, 22))
        self.starInput.setObjectName("starInput")
        self.label = QtWidgets.QLabel(self.InsertTrail)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.InsertTrail)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 101, 16))
        self.label_9.setObjectName("label_9")
        self.diffInput = QtWidgets.QSpinBox(self.InsertTrail)
        self.diffInput.setGeometry(QtCore.QRect(110, 170, 42, 22))
        self.diffInput.setObjectName("diffInput")
        self.surfInput = QtWidgets.QSpinBox(self.InsertTrail)
        self.surfInput.setGeometry(QtCore.QRect(220, 210, 42, 22))
        self.surfInput.setObjectName("surfInput")
        self.label_3 = QtWidgets.QLabel(self.InsertTrail)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.label_3.setObjectName("label_3")
        self.lenInput = QtWidgets.QSpinBox(self.InsertTrail)
        self.lenInput.setGeometry(QtCore.QRect(90, 250, 42, 22))
        self.lenInput.setObjectName("lenInput")
        self.lineEdit = QtWidgets.QLineEdit(self.InsertTrail)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_11 = QtWidgets.QLabel(self.InsertTrail)
        self.label_11.setGeometry(QtCore.QRect(280, 20, 72, 15))
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.InsertTrail)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.InsertTrail)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_5.setObjectName("label_5")
        self.subBtn = QtWidgets.QPushButton(self.InsertTrail)
        self.subBtn.setGeometry(QtCore.QRect(620, 20, 121, 321))
        self.subBtn.setObjectName("subBtn")
        self.label_12 = QtWidgets.QLabel(self.InsertTrail)
        self.label_12.setGeometry(QtCore.QRect(10, 290, 101, 16))
        self.label_12.setObjectName("label_12")
        self.tIDInput = QtWidgets.QLineEdit(self.InsertTrail)
        self.tIDInput.setGeometry(QtCore.QRect(110, 290, 161, 21))
        self.tIDInput.setObjectName("tIDInput")
        self.tabWidget.addTab(self.InsertTrail, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "gradient"))
        self.label_6.setText(_translate("MainWindow", "star"))
        self.label_7.setText(_translate("MainWindow", "surface"))
        self.label_4.setText(_translate("MainWindow", "Park"))
        self.label_10.setText(_translate("MainWindow", "time"))
        self.label.setText(_translate("MainWindow", "Insert a new trail"))
        self.label_9.setText(_translate("MainWindow", "length"))
        self.label_3.setText(_translate("MainWindow", "Region"))
        self.label_11.setText(_translate("MainWindow", "summary"))
        self.label_2.setText(_translate("MainWindow", "Trial Name"))
        self.label_5.setText(_translate("MainWindow", "difficulty"))
        self.subBtn.setText(_translate("MainWindow", "Submit"))
        self.label_12.setText(_translate("MainWindow", "Trial ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InsertTrail), _translate("MainWindow", "Insert Trail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
