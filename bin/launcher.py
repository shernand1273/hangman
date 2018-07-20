# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow#this imports the hangman(mainwindow) file and its class (UI_MainWindow) so that we can open it
import sys

class Ui_launcherWin(object):

    #this function will be called when the hangman button on the launcher window is pressed to open the hangman class
    #if the window we are opening is not of the QtWidgets class (i.e. QtDialog, then we replace that where the QtWidgets is located)
    def openHangman(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()#this is the name of the UI class for the hangman game
        self.ui.setupUi(self.window)#this is the method from the UI_MainWindow class, in the parenthesis we put our new window variable, which is self.window in this case
        launcherWin.hide()#this hides the launcer window when the hangman game is opened up
        self.window.show()#this will show the new window after hiding the launcher

    def setupUi(self, launcherWin):
        launcherWin.setObjectName("launcherWin")
        launcherWin.resize(271, 352)
        launcherWin.setStyleSheet("background-color: rgb(48, 43, 43);")
        self.game3 = QtWidgets.QPushButton(launcherWin)
        self.game3.setGeometry(QtCore.QRect(10, 240, 251, 101))
        self.game3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game3.setMouseTracking(True)
        self.game3.setAutoFillBackground(False)
        self.game3.setStyleSheet("background-color: rgb(108,108,108);color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"")
        self.game3.setAutoDefault(False)
        self.game3.setDefault(False)
        self.game3.setFlat(False)
        self.game3.setObjectName("game3")
        self.game2 = QtWidgets.QPushButton(launcherWin)
        self.game2.setGeometry(QtCore.QRect(10, 130, 251, 101))
        self.game2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game2.setAutoFillBackground(False)
        self.game2.setStyleSheet("background-color: rgb(108,108,108);color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.game2.setObjectName("game2")
        self.hangman = QtWidgets.QPushButton(launcherWin)
        self.hangman.setGeometry(QtCore.QRect(10, 20, 251, 101))
        self.hangman.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hangman.setStyleSheet("background-color: rgb(108,108,108);color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.hangman.setObjectName("hangman")

        self.retranslateUi(launcherWin)
        QtCore.QMetaObject.connectSlotsByName(launcherWin)

    def retranslateUi(self, launcherWin):
        _translate = QtCore.QCoreApplication.translate
        launcherWin.setWindowTitle(_translate("launcherWin", "Games"))
        self.game3.setText(_translate("launcherWin", "Game 3"))
        self.game2.setText(_translate("launcherWin", "Game 2"))
        self.hangman.setText(_translate("launcherWin", "Hangman"))
        self.hangman.clicked.connect(self.openHangman)#this is the signal for calling the openHangman function, which opoens the game



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    launcherWin = QtWidgets.QWidget()
    ui = Ui_launcherWin()
    ui.setupUi(launcherWin)
    launcherWin.show()
    sys.exit(app.exec_())
