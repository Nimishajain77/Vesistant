# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from Ai_Assistant import AiAssistant
from txttsp import speak
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from assistant import MainThread
import sys
from Assistant.GUIASSISTANT import GUI
import os

startExecution = MainThread()
start_exe=GUI()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 600, 101, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"border-radius:7px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1040, 600, 101, 51))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 0, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"border-radius:7px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -20, 391, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../OneDrive/Desktop/All Folders/JARVIS-master/Jarvis/utils/images/initiating.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(640, 30, 291, 61))
        self.textBrowser.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color:transparent;\n"
"border-radius:none;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(930, 30, 291, 61))
        self.textBrowser_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color:transparent;\n"
"border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(930, 70, 381, 501))
        self.frame.setStyleSheet("background-color:rgb(0.0.0);\n"
"border-radius: 15px;\n"
"border:0.5px solid white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 361, 441))
        self.scrollArea.setStyleSheet("background-color:rgb(0,0,0);\n"
"border-radius:15px;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 361, 441))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(-6, 50, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(39, 39, 39);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(0, 130, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:rgb(39, 39, 39);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(20, 380, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(255,255,255);\n"
"text-align:center;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 380, 71, 41))
        self.pushButton_3.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 20, 341, 61))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 0, 561, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 italic 26pt \"Sitka Subheading\";")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 80, 391, 491))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 50, 331, 421))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.ves_image = QtWidgets.QLabel(self.centralwidget)
        self.ves_image.setGeometry(QtCore.QRect(550, 80, 251, 501))
        self.ves_image.setStyleSheet("background-image:url(:/backGif/images/vesit.png);\n"
"border-radius:20px;")
        self.ves_image.setText("")
        self.ves_image.setObjectName("ves_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "   Me: Wake-up Jarvis"))
        self.label_5.setText(_translate("MainWindow", "  Jarvis: Hello, Sir"))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#111111\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">Say &quot;Wake-Up Jarvis&quot; to activate the assistant</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "         Welcome to Vesistant"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:12pt; color:#ffffff;\">Artificial intelligence was founded as an academic discipline in 1956, and in the years since has experienced several waves of optimism, followed by disappointment and the loss of funding (known as an &quot;AI winter followed by new approaches, success and renewed funding. AI research has tried and discarded many different approaches since its founding, including simulating the brain, modeling human problem solvingformal logic large databases of knowledge and imitating animal behavior. In the first decades of the 21st century, highly mathematical statistical machine learning has dominated the field, and this technique has proved highly successful, helping to solve many challenging problems throughout industry and academia.</span></p></body></html>"))
       
    def start(self):
        self.movie = QtGui.QMovie("images/initiating.gif")
        self.label_2.setMovie(self.movie)
        self.movie.start()
        startExecution.start()
        start_exe.start()
     

    def stop(self):
        self.movie = QtGui.QMovie("images/initiating.gif")
        self.label_2.setMovie(self.movie)
        self.movie.stop()
        sys.exit()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

