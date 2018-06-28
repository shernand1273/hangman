#FUNCTION LIST in this module
    #enableBackup()
    #fromBackup()
    #viewContent()
    #getWord()

#SPECIAL PARAMETERS
    #VIEW_CONTENT  used as a trigger within fromBackup() to call the viewContent()
    #GET_WORD  used as a trigger within the fromBackup()  to call the getWord()



import random

#if the database test fails, then this function will test the backupFile, if this backup file test fails the program cannot return so then
#user is notified of the fatal error and the program will quit via tkinter.messagebox
def enableBackup():
    try:
        file = open("../wordFiles/wordListBackup.txt","r")
        file.close()


    except FileNotFoundError:
        print("The backup file was not found, cannot proceed wit the game at this time")#use tkinter message box with exit code

#gets called from the main and passed a parameter that will determine whether the program wants the word or to display the content of the file
def fromBackup(action):
    #GET_WORD
    #VIEW_CONTENT
    backupFile=open("../wordFiles/wordListBackup.txt","r")
    content = backupFile.read()
    lines=content.splitlines()
    backupFile.close()
    #determine what function to call based on the parameter's value passed by the main function
    if(action == "GET_WORD"):
        return getWord(lines)
    elif(action == "VIEW_CONTENT"):
        viewContent(lines)

#this function gets called by the fromBackup() when its action parameter is equal to VIEW_CONTENT
def viewContent(theLines):
    for i in range(len(theLines)):
        print("%d. %s" % (i+1,theLines[i]))

#this function gets called by the fromBackup() when its action parameter is equal to GET_WORD
def getWord(list):
    randomNum = random.randint(0,len(list))
    print("Word came from text backup file")
    return(list[randomNum])
