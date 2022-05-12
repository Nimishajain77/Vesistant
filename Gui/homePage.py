# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import home_page
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1910, 1070)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -30, 1921, 1100))
        self.label.setStyleSheet("background-color: rgb(0, 0,0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 70, 401, 301))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/ai4/ai5.gif);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, -10, 1361, 91))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Nirmala UI\";\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 110, 3, 301))
        self.line.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 121, 51))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"border-radius: 7px;")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 430, 141, 51))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(900, 420, 251, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 470, 171, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"  color: rgb(0, 255, 0);\n"
"  font: 16pt MS Shell Dlg 2;\n"
"  border: 1px solid rgb(0, 255, 0);\n"
"  border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 255, 0);\n"
"  color: rgb(255,255,255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 460, 171, 61))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"  color: rgb(0, 8, 255);\n"
"  font: 16pt MS Shell Dlg 2;\n"
"  border: 1px solid rgb(0, 8, 255);\n"
"  border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(0, 8, 255);\n"
"  color: rgb(255,255,255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(170, 80, 351, 3))
        self.line_2.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 410, 1741, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 120, 351, 251))
        self.textBrowser.setStyleSheet("color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1550, 820, 321, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1180, 530, 31, 31))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image:url(:/website/google.png);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius:20px;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1220, 530, 41, 31))
        self.pushButton_5.setStyleSheet("background-image: url(:/facebook/facebook.png);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1260, 530, 41, 31))
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image: url(:/github/github.png);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1120, 500, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "VESISTANT - A Personalized AI-Assistant of VESIT"))
        self.pushButton.setText(_translate("MainWindow", "About"))
        self.label_4.setText(_translate("MainWindow", "New User ?"))
        self.label_5.setText(_translate("MainWindow", "Already Registered ?"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">An A-I Assistant for VESIT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Get any Info about VESIT just by asking it</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Uses SpeechRecognition and FaceRecognition Models for better experience</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">It is Open-Source, So feel free to contribute </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "          Copyright © 2022-23"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

