from PyQt5 import QtCore, QtGui, QtWidgets
import sys






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
        Form.setWindowTitle(_translate("Form", "Hangman"))
        self.text.setText(_translate("Form", "What do you want to do?"))
        self.confirmYes.setText(_translate("Form", "New Game"))
        self.confirmNo.setText(_translate("Form", "Main Menu"))




    def buttonAction(self,button,confirmation):
        import restartGame
        button.setStyleSheet("background-color: white; margin: 3px; border-radius: 2px")

        if(confirmation == "Yes"):

            restartGame.restart("y")

        if(confirmation =="No"):
            restartGame.restart("n")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
