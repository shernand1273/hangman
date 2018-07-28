# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmbox.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(503, 145)
        Form.setStyleSheet("background-color:rgb(48,43,43)")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(30, 40, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.text.setStyleSheet("color:white")
        self.confirmYes = QtWidgets.QPushButton(Form)
        self.confirmYes.setGeometry(QtCore.QRect(380, 100, 113, 32))
        self.confirmYes.setObjectName("confimrYes")
        self.confirmYes.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.confirmYes.clicked.connect(lambda : self.buttonAction(self.confirmYes,"Yes"))
        self.confirmNo = QtWidgets.QPushButton(Form)
        self.confirmNo.setGeometry(QtCore.QRect(260, 100, 113, 32))
        self.confirmNo.setObjectName("confirmNo")
        self.confirmNo.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.confirmNo.clicked.connect(lambda : self.buttonAction(self.confirmNo,"No"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text.setText(_translate("Form", "Do you want to play another game?"))
        self.confirmYes.setText(_translate("Form", "Yes"))
        self.confirmNo.setText(_translate("Form", "No"))


    def buttonAction(self,button,confirmation):
        button.setStyleSheet("background-color: white; margin: 3px; border-radius: 2px")

        if(confirmation == "Yes"):
            print("Opening new game")

        else:
            print("You are going to exit the game")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
