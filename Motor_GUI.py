# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mr. NoNo\Desktop\interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ue9
import time
import LabJackPython
import copy
import threading
#from functools import partial


    
myUE9 = ue9.UE9(ethernet = True, ipAddress = "10.32.89.146")

#timeStop = threading.Thread(target = pushButton, name = "pushButton")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        fio_mask = 0b00111
        fio_dir = 0b11111
        fio_state = 0b11000
        results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 243)
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushStop.setGeometry(QtCore.QRect(170, 120, 75, 61))
        self.pushStop.setObjectName("pushStop")
        self.sliderSpeed = QtWidgets.QSlider(self.centralwidget)
        self.sliderSpeed.setGeometry(QtCore.QRect(130, 40, 291, 22))
        self.sliderSpeed.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sliderSpeed.setToolTipDuration(-1)
        self.sliderSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSpeed.setInvertedControls(False)
        self.sliderSpeed.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderSpeed.setMinimum(0)
        self.sliderSpeed.setMaximum(4)
        self.sliderSpeed.setTickInterval(1)
        self.sliderSpeed.setObjectName("sliderSpeed")
        self.pushLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pushLeft.setGeometry(QtCore.QRect(30, 120, 75, 61))
        self.pushLeft.setObjectName("pushLeft")
        self.pushRight = QtWidgets.QPushButton(self.centralwidget)
        self.pushRight.setGeometry(QtCore.QRect(30, 40, 75, 61))
        self.pushRight.setObjectName("pushRight")
        self.pushReset = QtWidgets.QPushButton(self.centralwidget)
        self.pushReset.setGeometry(QtCore.QRect(310, 120, 75, 61))
        self.pushReset.setObjectName("pushReset")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 51, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 70, 51, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 70, 51, 21))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #GUI buttons/slider/timer with Functions
        self.qTimer = QtCore.QTimer()
        self.qTimer.setInterval(300)
        self.qTimer.timeout.connect(self.pushButton)
        self.qTimer.start(10)
        clickReset = self.pushReset
        clickReset.clicked.connect(self.reset_application)
        clickRight = self.pushRight
        clickRight.clicked.connect(self.clockwise_application)
        clickLeft = self.pushLeft
        clickLeft.clicked.connect(self.otherwise_application)
        slide = self.sliderSpeed
        slide.valueChanged.connect(self.speed_application)
        clickStop = self.pushStop
        clickStop.clicked.connect(self.stop_application)

        # disable reset button
        self.pushRight.setEnabled(False)
        self.pushLeft.setEnabled(False)
        self.sliderSpeed.setEnabled(False)
        self.pushStop.setEnabled(False)
        clickReset.setEnabled(True)
    #end def
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushStop.setText(_translate("MainWindow", "Stop"))
        self.pushLeft.setText(_translate("MainWindow", "Otherwise"))
        self.pushRight.setText(_translate("MainWindow", "Clockwise"))
        self.pushReset.setText(_translate("MainWindow", "Reset"))
        self.label_2.setText(_translate("MainWindow", "Speed"))
        self.label.setText(_translate("MainWindow", "Slowest"))
        self.label_3.setText(_translate("MainWindow", "Slow"))
        self.label_4.setText(_translate("MainWindow", "Middle"))
        self.label_5.setText(_translate("MainWindow", "Fast"))
        self.label_6.setText(_translate("MainWindow", "Fastest"))
    #end def

    def otherwise_application (self) :
        fio_mask = 0b00111
        fio_dir = 0b11111
        fio_state = 0b11100
        myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
        results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
    #end def

    def clockwise_application (self) :
        fio_mask = 0b00111
        fio_dir = 0b11111
        fio_state = 0b11010
        results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
    #end def

    def stop_application (self) :
        fio_mask = 0b00111
        fio_dir = 0b11111
        fio_state = 0b11000
        results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
        myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 0)
        self.pushRight.setEnabled(False)
        self.pushLeft.setEnabled(False)
        self.sliderSpeed.setEnabled(False)
        self.pushStop.setEnabled(False)
        self.pushReset.setEnabled(True)
    #end def

    def speed_application(self):
        speedValue = self.sliderSpeed.value()
        if speedValue == 0 :
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 15002)
        elif speedValue == 1 :
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 25000)
        elif speedValue == 2 :
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 32500)    
        elif speedValue == 3 :
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 45000)
        else :
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 62000)
        #end if/else
    #end def    
        
    def reset_application (self):
        fio_mask = 0b00111
        fio_dir = 0b11111
        fio_state = 0b11010
        results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
        myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 32500)
        self.pushRight.setEnabled(True)
        self.pushLeft.setEnabled(True)
        self.sliderSpeed.setEnabled(True)
        self.pushReset.setEnabled(False)
        self.pushStop.setEnabled(True)
    #end def
        
    def pushButton(self) :
        fio_mask = 0b11000
        fio_dir = 0b00111
        fio_state = 0b11000
        results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
        binaryResult = results["FIOState"]
        binary_string = str(bin(binaryResult))
        if binary_string[6]  == '0':
            fio_mask = 0b11000
            fio_dir = 0b00111
            fio_state = 0b11000
            results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 0)
            stopNotification = QtWidgets.QMessageBox()
            stopNotification.setIcon(stopNotification.Information)
            stopNotification.setWindowTitle("Notification")
            stopNotification.setText("You clicked emergency stop button")
            stopNotification.setStandardButtons(stopNotification.Ok)
            stopNotification.exec_()
            MainWindow.setVisible(False)
        #end if
        if (binary_string[5] == '0') and (MainWindow.isVisible() == False):
            # another window part
            password_Window.show()
        #end if
    #end def

    def callMainWindow (self):
        MainWindow.show()
    #end def

class Ui_password_Window(object):
    def anotherSetupUi(self, password_Window):
        password_Window.setObjectName("password_Window")
        password_Window.resize(503, 111)
        self.centralwidget = QtWidgets.QWidget(password_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 20, 271, 20))
        self.lineEdit.setObjectName("lineEdit")

        # check -> if it doesn't work as a password, remove
        self.lineEdit.setEchoMode(self.lineEdit.Password)
        
        self.btnCheckPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheckPassword.setGeometry(QtCore.QRect(380, 50, 75, 23))
        self.btnCheckPassword.setObjectName("btnCheckPassword")
        self.btnCheckPassword.clicked.connect(self.checkPassword)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(100)
        self.label.setFont(font)
        self.label.setObjectName("label")
        password_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(password_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 21))
        self.menubar.setObjectName("menubar")
        password_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(password_Window)
        self.statusbar.setObjectName("statusbar")
        password_Window.setStatusBar(self.statusbar)
        self.retranslateUi(password_Window)
        QtCore.QMetaObject.connectSlotsByName(password_Window)

    def retranslateUi(self, password_Window):
        _translate = QtCore.QCoreApplication.translate
        password_Window.setWindowTitle(_translate("password_Window", "MainWindow"))
        self.btnCheckPassword.setText(_translate("password_Window", "Check"))
        self.label.setText(_translate("password_Window", "Enter password:"))

    def checkPassword(self) :
        password = self.lineEdit.text()
        if password == "ETD555" :
            mainobj = Ui_MainWindow()
            mainobj.callMainWindow()
            fio_mask = 0b11111
            fio_dir = 0b00111
            fio_state = 0b11010
            results = myUE9.feedback(FIOMask = fio_mask, FIODir = fio_dir, FIOState = fio_state)
            myUE9.timerCounter(TimerClockBase = 1, TimerClockDivisor = 1, Timer0Mode = 0, NumTimersEnabled = 1, UpdateConfig = 1, Timer0Value = 32500)
            password_Window.hide()
            self.lineEdit.setText("")
        else :
            self.lineEdit.setText("")
            msgPassword = QtWidgets.QMessageBox()
            msgPassword.setIcon(msgPassword.Warning)
            msgPassword.setWindowTitle("Error_Notification")
            msgPassword.setText("Wrong password")
            msgPassword.setStandardButtons(msgPassword.Ok)
            msgPassword.exec_()
            sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    password_Window = QtWidgets.QMainWindow()
    ui1 = Ui_password_Window()
    ui1.anotherSetupUi(password_Window)
    password_Window.hide()
    sys.exit(app.exec_())

