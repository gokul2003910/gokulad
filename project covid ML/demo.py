# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Imagefield(object):
    def setupUi(self, Imagefield):
        Imagefield.setObjectName("Imagefield")
        Imagefield.resize(880, 735)
        Imagefield.setStyleSheet("background:rgb(255, 196, 253)\n"
"rgb(151, 156, 255)")
        self.label = QtWidgets.QLabel(Imagefield)
        self.label.setGeometry(QtCore.QRect(260, 69, 301, 41))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.textfield = QtWidgets.QLineEdit(Imagefield)
        self.textfield.setGeometry(QtCore.QRect(120, 200, 181, 31))
        self.textfield.setStyleSheet("BACKGROUND:rgb(254, 233, 255)")
        self.textfield.setObjectName("textfield")
        self.nameInput_2 = QtWidgets.QLabel(Imagefield)
        self.nameInput_2.setGeometry(QtCore.QRect(50, 200, 51, 31))
        self.nameInput_2.setStyleSheet("\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.nameInput_2.setObjectName("nameInput_2")
        self.ageInput = QtWidgets.QLabel(Imagefield)
        self.ageInput.setGeometry(QtCore.QRect(50, 290, 41, 21))
        self.ageInput.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.ageInput.setObjectName("ageInput")
        self.IntegerField_2 = QtWidgets.QLineEdit(Imagefield)
        self.IntegerField_2.setGeometry(QtCore.QRect(120, 280, 181, 31))
        self.IntegerField_2.setStyleSheet("BACKGROUND:rgb(254, 233, 255)")
        self.IntegerField_2.setObjectName("IntegerField_2")
        self.dobInput = QtWidgets.QLabel(Imagefield)
        self.dobInput.setGeometry(QtCore.QRect(44, 390, 41, 20))
        self.dobInput.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.dobInput.setObjectName("dobInput")
        self.IntegerField = QtWidgets.QDateEdit(Imagefield)
        self.IntegerField.setGeometry(QtCore.QRect(120, 381, 181, 31))
        self.IntegerField.setStyleSheet("BACKGROUND:rgb(254, 233, 255)")
        self.IntegerField.setObjectName("IntegerField")
        self.textfieldInput_2 = QtWidgets.QLineEdit(Imagefield)
        self.textfieldInput_2.setGeometry(QtCore.QRect(120, 470, 181, 31))
        self.textfieldInput_2.setStyleSheet("BACKGROUND:rgb(254, 233, 255)")
        self.textfieldInput_2.setObjectName("textfieldInput_2")
        self.countryInput = QtWidgets.QLabel(Imagefield)
        self.countryInput.setGeometry(QtCore.QRect(14, 480, 81, 20))
        self.countryInput.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.countryInput.setObjectName("countryInput")
        self.STATEInput = QtWidgets.QLabel(Imagefield)
        self.STATEInput.setGeometry(QtCore.QRect(30, 550, 55, 16))
        self.STATEInput.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.STATEInput.setObjectName("STATEInput")
        self.textfieldInput = QtWidgets.QLineEdit(Imagefield)
        self.textfieldInput.setGeometry(QtCore.QRect(120, 541, 181, 31))
        self.textfieldInput.setStyleSheet("BACKGROUND:rgb(254, 233, 255)")
        self.textfieldInput.setObjectName("textfieldInput")
        self.graphicsView = QtWidgets.QGraphicsView(Imagefield)
        self.graphicsView.setGeometry(QtCore.QRect(460, 210, 281, 261))
        self.graphicsView.setStyleSheet("background-color: rgb(249, 246, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.radioButton = QtWidgets.QRadioButton(Imagefield)
        self.radioButton.setGeometry(QtCore.QRect(120, 620, 61, 20))
        self.radioButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Imagefield)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 620, 95, 20))
        self.radioButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(Imagefield)
        self.label_2.setGeometry(QtCore.QRect(30, 620, 55, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Imagefield)
        self.pushButton.setGeometry(QtCore.QRect(550, 530, 141, 28))
        self.pushButton.setStyleSheet("background-color: rgb(249, 246, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Imagefield)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 680, 141, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(249, 246, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Imagefield)
        self.pushButton_3.setGeometry(QtCore.QRect(572, 670, 131, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(249, 246, 255);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Imagefield)
        QtCore.QMetaObject.connectSlotsByName(Imagefield)
     


    def retranslateUi(self, Imagefield):
        _translate = QtCore.QCoreApplication.translate
        Imagefield.setWindowTitle(_translate("Imagefield", "Dialog"))
        self.label.setText(_translate("Imagefield", "COVID-19 DETECTION"))
        self.nameInput_2.setText(_translate("Imagefield", "NAME"))
        self.ageInput.setText(_translate("Imagefield", "AGE"))
        self.dobInput.setText(_translate("Imagefield", "DOB"))
        self.countryInput.setText(_translate("Imagefield", "COUNTRY"))
        self.STATEInput.setText(_translate("Imagefield", "STATE"))
        self.radioButton.setText(_translate("Imagefield", "male"))
        self.radioButton_2.setText(_translate("Imagefield", "Female"))
        self.label_2.setText(_translate("Imagefield", "Gender"))
        self.pushButton.setText(_translate("Imagefield", "UPLOAD IMAGE"))
        self.pushButton_2.setText(_translate("Imagefield", "NEXT"))
        self.pushButton_3.setText(_translate("Imagefield", "CANCEL"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Imagefield = QtWidgets.QDialog()
    ui = Ui_Imagefield()
    ui.setupUi(Imagefield)
    Imagefield.show()
    sys.exit(app.exec_())
