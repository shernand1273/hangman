#This is the main file of the program Hangman.py this will be called by the mainMenu.py interface if the user chooses this gaem

#custom modules
import dbBackup
import db



def checkDb():
    datasource = ""
    if(db.testDb()==True):
        datasource = "db"
        return datasource
    elif(db.testDb()==False):
        dbBackup.enableBackup()
        datasource ="backup"
        return datasource

def main():
    gameWord=""
    dbSource =checkDb()

    if(dbSource == "db"):
        gameWord=db.getWordFromDb(db.fromDb("RET_LENGTH"))
        print(gameWord)
    elif(dbSource =="backup"):
        gameWord =dbBackup.fromBackup("GET_WORD")
        print(gameWord)



main()
