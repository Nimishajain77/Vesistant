# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\homePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
# import login
# import ui_Registration
# import home_page
# # uiR = ui_Registration()
# # uiL = ui_login()


# class UI_Window(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1910, 1070)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(0, -20, 1921, 1100))
#         self.label.setStyleSheet("background-color: rgb(0, 0,0);")
#         self.label.setText("")
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(1390, 340, 401, 301))
#         self.movie = QtGui.QMovie("images/ai5.gif")
#         self.label_2.setMovie(self.movie)
#         self.movie.start()
#         self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
#                                    "background-image: url(images/ai5.gif);")
#         self.label_2.setText("")
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(280, 70, 1361, 91))
#         self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
#                                    "font: 8pt \"Nirmala UI\";\n"
#                                    "font: 36pt \"MS Shell Dlg 2\";")
#         self.label_3.setObjectName("label_3")
#         self.line = QtWidgets.QFrame(self.centralwidget)
#         self.line.setGeometry(QtCore.QRect(140, 360, 3, 301))
#         self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.line.setFrameShape(QtWidgets.QFrame.VLine)
#         self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line.setObjectName("line")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(90, 310, 121, 51))
#         self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
#                                       "font: 12pt \"MS Shell Dlg 2\";\n"
#                                       "background-color: rgb(0, 0, 0);\n"
#                                       "border: 1px solid rgb(255, 255, 255);\n"
#                                       "border-radius: 7px;")
#         self.pushButton.setObjectName("pushButton")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(650, 750, 141, 51))
#         self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
#                                    "font: 16pt \"MS Shell Dlg 2\";")
#         self.label_4.setObjectName("label_4")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(1080, 750, 251, 51))
#         self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
#                                    "font: 16pt \"MS Shell Dlg 2\";")
#         self.label_5.setObjectName("label_5")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(630, 840, 171, 61))
#         self.pushButton_2.setStyleSheet("\n"
#                                         "QPushButton{\n"
#                                         "color: rgb(0, 255, 0);\n"
#                                         "font: 16pt \"MS Shell Dlg 2\";\n"
#                                         "border: 1px solid rgb(0, 255, 0);\n"
#                                         "border-radius: 8px;\n"
#                                         "}\n"
#                                         "QPushButton:hover{\n"
#                                         "background-color: rgb(0, 255, 0);\n"
#                                         # "border:5px solid #cf1f00 ;\n"
#                                         "color: rgb(255,255,255);\n"
#                                         "}")
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(1120, 840, 171, 61))
#         self.pushButton_3.setStyleSheet("\n"
#                                         "QPushButton{\n"
#                                         "color: rgb(0, 8, 255);\n"
#                                         "font: 16pt \"MS Shell Dlg 2\";\n"
#                                         "border: 1px solid rgb(0, 8, 255);\n"
#                                         "border-radius: 8px;\n"
#                                         "}\n"
#                                         "QPushButton:hover{\n"
#                                         "background-color: rgb(0, 8, 255);\n"
#                                         # "border:5px solid #cf1f00 ;\n"
#                                         "color: rgb(255,255,255);\n"
#                                         "}")
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.line_2 = QtWidgets.QFrame(self.centralwidget)
#         self.line_2.setGeometry(QtCore.QRect(210, 330, 351, 3))
#         self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_2.setObjectName("line_2")
#         self.line_3 = QtWidgets.QFrame(self.centralwidget)
#         self.line_3.setGeometry(QtCore.QRect(90, 690, 1741, 20))
#         self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_3.setObjectName("line_3")
#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(210, 390, 341, 251))
#         self.label_6.setText("")
#         self.label_6.setObjectName("label_6")
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(200, 400, 351, 251))
#         self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
#                                        "background-color: rgb(0, 0, 0);")
#         self.textBrowser.setObjectName("textBrowser")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.pushButton_2.clicked.connect(self.go_to_register)
#         self.pushButton_2.clicked.connect(MainWindow.close)
#         self.pushButton_3.clicked.connect(self.go_to_login)
#         self.pushButton_3.clicked.connect(MainWindow.close)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label_3.setText(_translate(
#             "MainWindow", "VESISTANT - A Personalized AI-Assistant of VESIT"))
#         self.pushButton.setText(_translate("MainWindow", "About"))
#         self.label_4.setText(_translate("MainWindow", "New User ?"))
#         self.label_5.setText(_translate("MainWindow", "Already Registered ?"))
#         self.pushButton_2.setText(_translate("MainWindow", "Register"))
#         self.pushButton_3.setText(_translate("MainWindow", "Login"))
#         self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#                                             "p, li { white-space: pre-wrap; }\n"
#                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
#                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">An A-I Assistant for VESIT</span></p>\n"
#                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
#                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Get any Info about VESIT just by asking it</span></p>\n"
#                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
#                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Uses SpeechRecognition and FaceRecognition Models for better experience</span></p>\n"
#                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
#                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">It is Open-Source, So feel free to contribute </span></p></body></html>"))

#     def go_to_login(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = login.Window2()
#         self.ui.setupUi(self.window)
#         # UI_Window.hide()
#         self.window.show()

#     def go_to_register(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = ui_Registration.Window1()
#         self.ui.setupUi(self.window)
#         # UI_Window.hide()
#         self.window.show()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = UI_Window()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
