

from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow#this imports the hangman(mainwindow) file and its class (UI_MainWindow) so that we can open it
import sys




class objRef():
    def __init__(self):

        self.objectRef = None

    def setObjectRef(self,theObject):
        self.objectRef= theObject

    def getObjectRef(self):
        return self.objectRef


hangmanOBJ=objRef()

def getObjRef():
    return hangmanOBJ.getObjectRef()


class Ui_launcherWin(object):

    #this function will be called when the hangman button on the launcher window is pressed to open the hangman class
    #if the window we are opening is not of the QtWidgets class (i.e. QtDialog, then we replace that where the QtWidgets is located)
    def openHangman(self):

        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()#this is the name of the UI class for the hangman game
        self.ui.setupUi(self.window)#this is the method from the UI_MainWindow class, in the parenthesis we put our new window variable, which is self.window in this case
        hangmanOBJ.setObjectRef(self.window)#call the hangmanOBJ and have it store the self.window object
        self.window =hangmanOBJ.getObjectRef()
        launcherWin.hide()#this hides the launcer window when the hangman game is opened up
        self.value=self.window.show()#this will show the new window after hiding the launcher





    def setupUi(self, launcherWin):
        launcherWin.setObjectName("launcherWin")
        launcherWin.resize(271, 352)
        launcherWin.setStyleSheet("background-color: rgb(48, 43, 43);")
        self.exit = QtWidgets.QPushButton(launcherWin)
        self.exit.setGeometry(QtCore.QRect(10, 240, 251, 101))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setMouseTracking(True)
        self.exit.setAutoFillBackground(False)
        self.exit.setStyleSheet("background-color: rgb(108,108,108);color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"")
        self.exit.setAutoDefault(False)
        self.exit.setDefault(False)
        self.exit.setFlat(False)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.quit)
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
        self.exit.setText(_translate("launcherWin", "Exit"))
        self.game2.setText(_translate("launcherWin", "Game 2"))
        self.hangman.setText(_translate("launcherWin", "Hangman"))
        self.hangman.clicked.connect(self.openHangman)#this is the signal for calling the openHangman function, which opoens the game

    def quit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    launcherWin = QtWidgets.QWidget()
    ui = Ui_launcherWin()
    ui.setupUi(launcherWin)
    launcherWin.show()
    sys.exit(app.exec_())
