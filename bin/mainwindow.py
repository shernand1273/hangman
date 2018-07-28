# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowv1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import db
import dbBackup

#This is the function that will be pulling the word from the database or backup file its called by the UI_MainWindow ___init__ constructor
def pickWordFromFile():
    dbSource =db.checkFile()
    if(dbSource == "db"):
        gameWord=db.getWordFromDb(db.fromDb("RET_LENGTH"))


    elif(dbSource =="backup"):
        gameWord =dbBackup.fromBackup("GET_WORD")

    return gameWord

#this class will hold all the buttons in a list so that we can later use it to check the button state(enabled, disabled)
#we use this class so that when a user either wins or looses, the buttons will be disabled
class ButtonList():
    def __init__(self):
        self.buttonList=[]

    #in the UI_mainWindow class the buttons are created, each time a button is created it is added to this list
    def addButton(self,theButton):
        self.buttonList.append(theButton)

    #when the user either wins or looses the game, this class function will be called to disable all buttons
    def disableAllButtons(self):
        for button in self.buttonList:
            if button.isEnabled():
                button.setEnabled(False)



#The tries are being put into a class to avoid using a global variable, now we can easily update the value
class GameSession():

    def __init__(self):
        self.word= pickWordFromFile()
        self.tries=7
        self.rightGuesses=0
        self.guessField=" ___ "*len(self.word)#temporary string field that will be added to the guess Label on the main GUI
        self.guessList=self.guessField.split()
        self.guessField2=""

    def setTries(self,arg):
        self.tries = arg


    def getTries(self):
        return self.tries


    def setRightGuessess(self,arg2):
        self.rightGuesses=arg2


    def getRightGuessess(self):
        return self.rightGuesses


    def getWord(self):
        return self.word


    def setGuessField(self):
        self.guessField = " ___ "*len(self.word)


    def getGuessField(self):
        return self.guessField


    def getGuessFieldList(self):
        return self.guessList

#enable all classess
buttonList=ButtonList()
game=GameSession()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 440)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(48,43,43)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.l_button = QtWidgets.QPushButton(self.centralwidget)
        self.l_button.setGeometry(QtCore.QRect(460, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.l_button.setFont(font)
        self.l_button.setStyleSheet("margin: 5px")
        self.l_button.setDefault(False)
        self.l_button.setFlat(False)
        self.l_button.setObjectName("l_button")
        self.l_button.clicked.connect(lambda :self.testLetter(self.l_button,self.tries,"L"))###########################
        buttonList.addButton(self.l_button)

        self.m_button = QtWidgets.QPushButton(self.centralwidget)
        self.m_button.setGeometry(QtCore.QRect(500, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.m_button.setFont(font)
        self.m_button.setStyleSheet("margin: 5px")
        self.m_button.setDefault(False)
        self.m_button.setFlat(False)
        self.m_button.setObjectName("m_button")
        self.m_button.clicked.connect(lambda :self.testLetter(self.m_button,self.tries,"M"))
        buttonList.addButton(self.m_button)

        self.q_button = QtWidgets.QPushButton(self.centralwidget)
        self.q_button.setGeometry(QtCore.QRect(140, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.q_button.setFont(font)
        self.q_button.setStyleSheet("margin: 5px")
        self.q_button.setDefault(False)
        self.q_button.setFlat(False)
        self.q_button.setObjectName("q_button")
        self.q_button.clicked.connect(lambda :self.testLetter(self.q_button,self.tries,"Q"))
        buttonList.addButton(self.q_button)

        self.b_button = QtWidgets.QPushButton(self.centralwidget)
        self.b_button.setGeometry(QtCore.QRect(60, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.b_button.setFont(font)
        self.b_button.setStyleSheet("margin: 5px")
        self.b_button.setDefault(False)
        self.b_button.setFlat(False)
        self.b_button.setObjectName("b_button")
        self.b_button.clicked.connect(lambda :self.testLetter(self.b_button,self.tries,"B"))
        buttonList.addButton(self.b_button)

        self.z_button = QtWidgets.QPushButton(self.centralwidget)
        self.z_button.setGeometry(QtCore.QRect(500, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.z_button.setFont(font)
        self.z_button.setStyleSheet("margin: 5px")
        self.z_button.setDefault(False)
        self.z_button.setFlat(False)
        self.z_button.setObjectName("z_button")
        self.z_button.clicked.connect(lambda :self.testLetter(self.z_button,self.tries,"Z"))
        buttonList.addButton(self.z_button)

        self.w_button = QtWidgets.QPushButton(self.centralwidget)
        self.w_button.setGeometry(QtCore.QRect(380, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.w_button.setFont(font)
        self.w_button.setStyleSheet("margin: 5px")
        self.w_button.setDefault(False)
        self.w_button.setFlat(False)
        self.w_button.setObjectName("w_button")
        self.w_button.clicked.connect(lambda :self.testLetter(self.w_button,self.tries,"W"))
        buttonList.addButton(self.w_button)

        self.r_button = QtWidgets.QPushButton(self.centralwidget)
        self.r_button.setGeometry(QtCore.QRect(180, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.r_button.setFont(font)
        self.r_button.setStyleSheet("margin: 5px")
        self.r_button.setDefault(False)
        self.r_button.setFlat(False)
        self.r_button.setObjectName("r_button")
        self.r_button.clicked.connect(lambda :self.testLetter(self.r_button,self.tries,"R"))
        buttonList.addButton(self.r_button)

        self.d_button = QtWidgets.QPushButton(self.centralwidget)
        self.d_button.setGeometry(QtCore.QRect(140, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.d_button.setFont(font)
        self.d_button.setStyleSheet("margin: 5px")
        self.d_button.setDefault(False)
        self.d_button.setFlat(False)
        self.d_button.setObjectName("d_button")
        self.d_button.clicked.connect(lambda :self.testLetter(self.d_button,self.tries,"D"))
        buttonList.addButton(self.d_button)

        self.p_button = QtWidgets.QPushButton(self.centralwidget)
        self.p_button.setGeometry(QtCore.QRect(100, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.p_button.setFont(font)
        self.p_button.setStyleSheet("margin: 5px")
        self.p_button.setDefault(False)
        self.p_button.setFlat(False)
        self.p_button.setObjectName("p_button")
        self.p_button.clicked.connect(lambda :self.testLetter(self.p_button,self.tries,"P"))
        buttonList.addButton(self.p_button)

        self.g_button = QtWidgets.QPushButton(self.centralwidget)
        self.g_button.setGeometry(QtCore.QRect(260, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.g_button.setFont(font)
        self.g_button.setStyleSheet("margin: 5px")
        self.g_button.setDefault(False)
        self.g_button.setFlat(False)
        self.g_button.setObjectName("g_button")
        self.g_button.clicked.connect(lambda :self.testLetter(self.g_button,self.tries,"G"))
        buttonList.addButton(self.g_button)

        self.k_button = QtWidgets.QPushButton(self.centralwidget)
        self.k_button.setGeometry(QtCore.QRect(420, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.k_button.setFont(font)
        self.k_button.setStyleSheet("margin: 5px")
        self.k_button.setDefault(False)
        self.k_button.setFlat(False)
        self.k_button.setObjectName("k_button")
        self.k_button.clicked.connect(lambda :self.testLetter(self.k_button,self.tries,"K"))
        buttonList.addButton(self.k_button)

        self.o_button = QtWidgets.QPushButton(self.centralwidget)
        self.o_button.setGeometry(QtCore.QRect(60, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.o_button.setFont(font)
        self.o_button.setStyleSheet("margin: 5px")
        self.o_button.setDefault(False)
        self.o_button.setFlat(False)
        self.o_button.setObjectName("o_button")
        self.o_button.clicked.connect(lambda :self.testLetter(self.o_button,self.tries,"O"))
        buttonList.addButton(self.o_button)

        self.x_button = QtWidgets.QPushButton(self.centralwidget)
        self.x_button.setGeometry(QtCore.QRect(420, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.x_button.setFont(font)
        self.x_button.setStyleSheet("margin: 5px")
        self.x_button.setDefault(False)
        self.x_button.setFlat(False)
        self.x_button.setObjectName("x_button")
        self.x_button.clicked.connect(lambda :self.testLetter(self.x_button,self.tries,"X"))
        buttonList.addButton(self.x_button)

        self.t_button = QtWidgets.QPushButton(self.centralwidget)
        self.t_button.setGeometry(QtCore.QRect(260, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.t_button.setFont(font)
        self.t_button.setStyleSheet("margin: 5px")
        self.t_button.setDefault(False)
        self.t_button.setFlat(False)
        self.t_button.setObjectName("t_button")
        self.t_button.clicked.connect(lambda :self.testLetter(self.t_button,self.tries,"T"))
        buttonList.addButton(self.t_button)

        self.u_button = QtWidgets.QPushButton(self.centralwidget)
        self.u_button.setGeometry(QtCore.QRect(300, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.u_button.setFont(font)
        self.u_button.setStyleSheet("margin: 5px")
        self.u_button.setDefault(False)
        self.u_button.setFlat(False)
        self.u_button.setObjectName("u_button")
        self.u_button.clicked.connect(lambda :self.testLetter(self.u_button,self.tries,"U"))
        buttonList.addButton(self.u_button)

        self.i_button = QtWidgets.QPushButton(self.centralwidget)
        self.i_button.setGeometry(QtCore.QRect(340, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.i_button.setFont(font)
        self.i_button.setStyleSheet("margin: 5px")
        self.i_button.setDefault(False)
        self.i_button.setFlat(False)
        self.i_button.setObjectName("i_button")
        self.i_button.clicked.connect(lambda :self.testLetter(self.i_button,self.tries,"I"))
        buttonList.addButton(self.i_button)

        self.a_button = QtWidgets.QPushButton(self.centralwidget)
        self.a_button.setGeometry(QtCore.QRect(20, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.a_button.setFont(font)
        self.a_button.setStyleSheet("margin: 5px")
        self.a_button.setDefault(False)
        self.a_button.setFlat(False)
        self.a_button.setObjectName("a_button")
        self.a_button.clicked.connect(lambda :self.testLetter(self.a_button,self.tries,"A"))
        buttonList.addButton(self.a_button)

        self.v_button = QtWidgets.QPushButton(self.centralwidget)
        self.v_button.setGeometry(QtCore.QRect(340, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.v_button.setFont(font)
        self.v_button.setStyleSheet("margin: 5px")
        self.v_button.setDefault(False)
        self.v_button.setFlat(False)
        self.v_button.setObjectName("v_button")
        self.v_button.clicked.connect(lambda :self.testLetter(self.v_button,self.tries,"V"))
        buttonList.addButton(self.v_button)

        self.animationFrame = QtWidgets.QFrame(self.centralwidget)
        self.animationFrame.setGeometry(QtCore.QRect(10, 20, 541, 261))
        self.animationFrame.setStyleSheet("background-color: \'white\';\n"
"margin:5px")
        self.animationFrame.setObjectName("animationFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.animationFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.test_text = QtWidgets.QLabel(self.animationFrame)#to be removed on final version
        self.test_text.setStyleSheet("color: black ;margin:2px")#to be removed on final version

        self.test_text.setAlignment(QtCore.Qt.AlignCenter)###To be removed on final version
        self.test_text.setObjectName("test_text")#to be removed on final version
        self.verticalLayout.addWidget(self.test_text)#to be removed on final version


        self.s_button = QtWidgets.QPushButton(self.centralwidget)
        self.s_button.setGeometry(QtCore.QRect(220, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.s_button.setFont(font)
        self.s_button.setStyleSheet("margin: 5px")
        self.s_button.setDefault(False)
        self.s_button.setFlat(False)
        self.s_button.setObjectName("s_button")
        self.s_button.clicked.connect(lambda :self.testLetter(self.s_button,self.tries,"S"))
        buttonList.addButton(self.s_button)

        self.j_button = QtWidgets.QPushButton(self.centralwidget)
        self.j_button.setGeometry(QtCore.QRect(380, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.j_button.setFont(font)
        self.j_button.setStyleSheet("margin: 5px")
        self.j_button.setDefault(False)
        self.j_button.setFlat(False)
        self.j_button.setObjectName("j_button")
        self.j_button.clicked.connect(lambda :self.testLetter(self.j_button,self.tries,"J"))
        buttonList.addButton(self.j_button)

        self.e_button = QtWidgets.QPushButton(self.centralwidget)
        self.e_button.setGeometry(QtCore.QRect(180, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.e_button.setFont(font)
        self.e_button.setStyleSheet("margin: 5px")
        self.e_button.setDefault(False)
        self.e_button.setFlat(False)
        self.e_button.setObjectName("e_button")
        self.e_button.clicked.connect(lambda :self.testLetter(self.e_button,self.tries,"E"))
        buttonList.addButton(self.e_button)

        self.n_button = QtWidgets.QPushButton(self.centralwidget)
        self.n_button.setGeometry(QtCore.QRect(20, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.n_button.setFont(font)
        self.n_button.setStyleSheet("margin: 5px")
        self.n_button.setDefault(False)
        self.n_button.setFlat(False)
        self.n_button.setObjectName("n_button")
        self.n_button.clicked.connect(lambda :self.testLetter(self.n_button,self.tries,"N"))
        buttonList.addButton(self.n_button)

        self.y_button = QtWidgets.QPushButton(self.centralwidget)
        self.y_button.setGeometry(QtCore.QRect(460, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.y_button.setFont(font)
        self.y_button.setStyleSheet("margin: 5px")
        self.y_button.setDefault(False)
        self.y_button.setFlat(False)
        self.y_button.setObjectName("y_button")
        self.y_button.clicked.connect(lambda :self.testLetter(self.y_button,self.tries,"Y"))
        buttonList.addButton(self.y_button)

        self.h_button = QtWidgets.QPushButton(self.centralwidget)
        self.h_button.setGeometry(QtCore.QRect(300, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.h_button.setFont(font)
        self.h_button.setStyleSheet("margin: 5px")
        self.h_button.setDefault(False)
        self.h_button.setFlat(False)
        self.h_button.setObjectName("h_button")
        self.h_button.clicked.connect(lambda :self.testLetter(self.h_button,self.tries,"H"))
        buttonList.addButton(self.h_button)

        self.c_button = QtWidgets.QPushButton(self.centralwidget)
        self.c_button.setGeometry(QtCore.QRect(100, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.c_button.setFont(font)
        self.c_button.setStyleSheet("margin: 5px")
        self.c_button.setDefault(False)
        self.c_button.setFlat(False)
        self.c_button.setObjectName("c_button")
        self.c_button.clicked.connect(lambda :self.testLetter(self.c_button,self.tries,"C"))
        buttonList.addButton(self.c_button)

        self.f_button = QtWidgets.QPushButton(self.centralwidget)
        self.f_button.setGeometry(QtCore.QRect(220, 340, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.f_button.setFont(font)
        self.f_button.setStyleSheet("margin: 5px")
        self.f_button.setDefault(False)
        self.f_button.setFlat(False)
        self.f_button.setObjectName("f_button")
        self.f_button.clicked.connect(lambda :self.testLetter(self.f_button,self.tries,"F"))
        buttonList.addButton(self.f_button)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 280, 551, 59))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.guessWord = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.guessWord.setFont(font)
        self.guessWord.setStyleSheet("font: 12pt \".SF NS Text\";\n"
"color: rgb(255, 255, 255);")
        self.guessWord.setObjectName("guessWord")#####################################################
        self.horizontalLayout_2.addWidget(self.guessWord, 0, QtCore.Qt.AlignHCenter)
        self.tries = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tries.setFont(font)
        self.tries.setStyleSheet("color: rgb(255, 255, 255);")
        self.tries.setObjectName("tries")
        self.horizontalLayout_2.addWidget(self.tries, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionrestart = QtWidgets.QAction(MainWindow)
        self.actionrestart.setCheckable(False)
        self.actionrestart.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.actionrestart.setFont(font)
        self.actionrestart.setObjectName("actionrestart")
        self.actionexit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionexit.setFont(font)
        self.actionexit.setObjectName("actionexit")
        self.actioninformation = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actioninformation.setFont(font)
        self.actioninformation.setObjectName("actioninformation")
        self.actionhangman_information = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionhangman_information.setFont(font)
        self.actionhangman_information.setObjectName("actionhangman_information")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_button.setText(_translate("MainWindow", "L"))
        self.m_button.setText(_translate("MainWindow", "M"))
        self.q_button.setText(_translate("MainWindow", "Q"))
        self.b_button.setText(_translate("MainWindow", "B"))
        self.z_button.setText(_translate("MainWindow", "Z"))
        self.w_button.setText(_translate("MainWindow", "W"))
        self.r_button.setText(_translate("MainWindow", "R"))
        self.d_button.setText(_translate("MainWindow", "D"))
        self.p_button.setText(_translate("MainWindow", "P"))
        self.g_button.setText(_translate("MainWindow", "G"))
        self.k_button.setText(_translate("MainWindow", "K"))
        self.o_button.setText(_translate("MainWindow", "O"))
        self.x_button.setText(_translate("MainWindow", "X"))
        self.t_button.setText(_translate("MainWindow", "T"))
        self.u_button.setText(_translate("MainWindow", "U"))
        self.i_button.setText(_translate("MainWindow", "I"))
        self.a_button.setText(_translate("MainWindow", "A"))
        self.v_button.setText(_translate("MainWindow", "V"))
        self.test_text.setText(_translate("MainWindow", "Animation Frame"))
        self.s_button.setText(_translate("MainWindow", "S"))
        self.j_button.setText(_translate("MainWindow", "J"))
        self.e_button.setText(_translate("MainWindow", "E"))
        self.n_button.setText(_translate("MainWindow", "N"))
        self.y_button.setText(_translate("MainWindow", "Y"))
        self.h_button.setText(_translate("MainWindow", "H"))
        self.c_button.setText(_translate("MainWindow", "C"))
        self.f_button.setText(_translate("MainWindow", "F"))
        self.guessWord.setText(game.getGuessField())################
        self.tries.setText("Tries Left: "+str(game.getTries()))
        self.actionrestart.setText(_translate("MainWindow", "New Game"))
        self.actionexit.setText(_translate("MainWindow", "Exit"))
        self.actioninformation.setText(_translate("MainWindow", "How to play"))
        self.actionhangman_information.setText(_translate("MainWindow", "Information"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.a_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.b_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.c_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.d_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.e_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.f_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.g_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.h_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.i_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.j_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.k_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.l_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.m_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.n_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.o_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.p_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.q_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.r_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.s_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.t_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.u_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.v_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.w_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.x_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.y_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")
        self.z_button.setStyleSheet("background-color:rgb(160, 219, 100);margin:3px;border-radius:2px")


    def testLetter(self,theButton,trieslabel,theLetter):##################test function##########
        #theButton - represents the button calling this FUNCTION
        #trieslabel - represents the self.tries label widget
        #theLetter- this is the specific letter passed in as a parameter by its corresponding button
        theButton.setStyleSheet("color:gray;background-color:rgb(160,219,100);margin:3px;border-radius:2px")
        theButton.setEnabled(False)
        word=game.getWord().upper()
        guessList=game.getGuessFieldList()
        newTriesTextlabel="Tries Left: " +str(game.getTries())
        guessString=""###############i don't think this is being used or needed, check code before deleting###########


        if(theLetter in word):

            for i in range(len(word)):
                if(theLetter==word[i]):
                    rightLetter=game.getRightGuessess()
                    rightLetter=rightLetter+1
                    game.setRightGuessess(rightLetter)
                    guessList[i] = theLetter
                    self.guessWord.setStyleSheet("font:18pt;color:white")
                    self.guessWord.setText(' '.join(guessList))

        else:
            theTries = game.getTries()
            theTries= theTries -1
            #now we have to update the Tries class object and the Tries Label
            print(theTries)
            game.setTries(theTries)
            update=str(game.getTries())
            trieslabel.setText("Tries Left: %s" % (update))

            #if the amount of tries left is 0, the program will generate a messge lettring the user know he/she lost
            if(theTries==0):
                print("You have lost the game")
                buttonList.disableAllButtons()
                #function to close the game session

        #here it test if all the right Guessess so far are equal to the length of the word, the user has won the game
        if(game.getRightGuessess() == len(word)):
            print("You have won the game")
            buttonList.disableAllButtons()
            #call a function in mainwindow that will close this game session


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#bug 1 (Fixed 7/27/2018)
#when the user clicks on a button for the first time, the tries lable is not being updated
#the second time the user clicks on a button, the tries label is updated
#internally, the game is making the right calculations, but the label is not being set accordingly until the next button is clicked
