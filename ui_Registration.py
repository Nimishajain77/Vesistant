# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import homePage
import cv2
import mysql.connector
from txttsp import speak
import numpy as np
import os
from PIL import Image
import homePage


class Window1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 732)
        width = 1124
        height = 732
        Form.setFixedSize(width, height)
        Form.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                           "background-color: rgb(0, 0, 0);")
        Form.setWindowIcon(QtGui.QIcon("images/window_logo.jpg"))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 731))
        self.label.setStyleSheet("color: rgb(0, 0, 255);\n"
                                 "font: 12pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/ai23456.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(640, 210, 401, 41))
        self.pushButton.setStyleSheet("\n"
                                      "QPushButton{\n"
                                      "background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                      "border:1px solid rgb(0,0,255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(0,0,255);\n"
                                      "color: #fff\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(600, 310, 171, 51))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(600, 390, 191, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(600, 460, 191, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 550, 151, 41))
        self.pushButton_2.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(0,0,0);\n"
                                        "color: #fff;\n"
                                        "border:0.5px solid rgb(0,255,0);\n"
                                        "border-radius: 10px;\n"
                                        "font: 75 8pt ;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(0,255,0);\n"
                                        "color: #fff\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 550, 251, 45))
        self.pushButton_3.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(0,0,0);\n"
                                        "color: #fff;\n"
                                        "border:0.5px solid rgb(255,0,0);\n"
                                        "border-radius: 10px;\n"
                                        "font: 75 8pt ;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255,0,0);\n"
                                        "color: #fff\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(820, 320, 261, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(170,170,170);\n"
                                    "border:3px solid #747474;\n"
                                    "border-radius: 10px;\n"
                                    "font:Arial;\n"
                                    "}\n"
                                    "QLineEdit:Focus{\n"
                                    "border:3px solid rgb(0,0,255);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(820, 390, 261, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "background-color: rgb(170,170,170);\n"
                                      "border:3px solid #747474;\n"
                                      "border-radius: 10px;\n"
                                      "font:Arial;\n"
                                      "}\n"
                                      "QLineEdit:Focus{\n"
                                      "border:3px solid rgb(0,0,255);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(820, 460, 261, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "background-color: rgb(170,170,170);\n"
                                      "border:3px solid #747474;\n"
                                      "border-radius: 10px;\n"
                                      "font:Arial;\n"
                                      "}\n"
                                      "QLineEdit:Focus{\n"
                                      "border:3px solid rgb(0,0,255);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(520, 90, 191, 61))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 24pt \"MS Shell Dlg 2\" ;\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "left: 50px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_3.clicked.connect(self.go_to_homePage)
        self.pushButton_3.clicked.connect(Form.close)
        self.pushButton.clicked.connect(self.both_train_dataset)
        # self.pushButton_2.clicked.connect(self.train_classifier)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def go_to_homePage(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = homePage.UI_Window()
        self.ui = homePage.Ui_MainWindow()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def getData(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        print(username, email, password)

    def both_train_dataset(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        msg = QMessageBox()
        if(username == "" or password == "" or email == ""):
            # msg.setText("Please provide complete details of the user")
            # x = msg.exec_()
            speak("Please provide complete details of the user")
        else:
            speak("Generating Face Samples. Please look at the camera..")
            self.generate_dataset()
            speak("Dataset Generation complete..")
            speak("Now training face sample Dataset")
            self.train_classifier()
            speak("Training face samples complete.. Now you can verify using Face Login")

    def generate_dataset(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        msg = QMessageBox()
        if(username == "" or password == "" or email == ""):
            msg.setText("Please provide complete details of the user")
            x = msg.exec_()
            speak("Please provide complete details of the user")
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="face_rec"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * from user_table")
            myresult = mycursor.fetchall()
            id = 1
            for x in myresult:
                id += 1
            sql = "insert into user_table(id,Name,Password,Email) values(%s,%s,%s,%s)"
            val = (id, username, password, email)
            mycursor.execute(sql, val)
            mydb.commit()

            face_classifier = cv2.CascadeClassifier(
                "haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                # scaling factor=1.3
                # Minimum neighbor = 5

                if faces == ():
                    return None
                for(x, y, w, h) in faces:
                    cropped_face = img[y:y+h, x:x+w]
                return cropped_face

            cap = cv2.VideoCapture(0)
            # id = 1
            img_id = 0

            while True:
                ret, frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(frame), (200, 200))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + \
                        str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    # (50,50) is the origin point from where text is to be written
                    # font scale=1
                    # thickness=2

                    cv2.imshow("Cropped face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
            cap.release()
            cv2.destroyAllWindows()
            msg.setText("Generating dataset completed!!!")
            x = msg.exec_()
            speak("Generating dataset completed!!!")

    def train_classifier(self):
        data_dir = "C:/Users/Dell/OneDrive/Face_Recognition/data"
        path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        msg = QMessageBox()
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        msg.setText("Training dataset completed!!!")
        x = msg.exec_()
        speak("Training dataset completed!!!")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REGISTER"))
        self.pushButton.setText(_translate(
            "Form", "CLICK HERE FOR FACE REGISTRATION"))
        self.label_3.setText(_translate("Form", "ENTER USERNAME"))
        self.label_4.setText(_translate("Form", "ENTER PASSWORD"))
        self.label_5.setText(_translate("Form", "ENTER EMAIL"))
        self.pushButton_2.setText(_translate("Form", "REGISTER"))
        self.label_6.setText(_translate("Form", "REGISTER"))
        self.pushButton_3.setText(_translate("Form", "Go Back to Home Page"))


# import test5_rc
# import test7_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
