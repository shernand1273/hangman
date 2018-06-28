#FUNCTION LIST in this module
    #testdb()
    #viewDb()

#SPECIAL PARAMETERS
    #VIEW_CONTENT to viwe the entire database, parameter used in fromDb FUNCTION
    #RET_LENGTH to get the length of the database, parameter used in the fromDb function

#DATABASE INFORMATION
    #database name: wordList
    #column to hold word: word
    #colum to hold word number: theNum

    #structure: wordList(theNum , word)

import sqlite3
import random


#This functin tests that the db file is found so that the main function can decide to either use the db or backup
def testDb():
        try:
            dbFile = open("wordList.db","r")
            dbFile.close()

            return True

        except FileNotFoundError:
            return False


#This function is used to view the contents of the file should someone modifying this source code choose to do so
def fromDb(action_arg):
    #VIEW_CONTENT parameter will show the entire content of the database
    #RET_LENGTH will return the length of the database table
    viewConn=sqlite3.connect("wordList.db")
    viewCur=viewConn.cursor()
    viewCur.execute("SELECT * FROM wordList")
    rows =viewCur.fetchall()
    viewConn.close()

    if(action_arg == "RET_CONTENT"):
        return rows
    elif(action_arg== "RET_LENGTH"):
        return (len(rows))

def getWordFromDb(db_length):
    #generate a random number between 1 and length of db table holding words
    randNumber = random.randint(1,db_length)


    #conenct to database to retrieve the word from the row that matches the random number to theNum in the database
    try:
        getConn=sqlite3.connect("wordList.db")
        getCursor=getConn.cursor()
        getCursor.execute("SELECT word FROM wordList WHERE theNum =? ", (str(randNumber),))
        theWord=getCursor.fetchone()
        getConn.close()

        #the database is returning the word as a tuple, so we have to extract the word from it using index 0
        print("Word came from database")
        return theWord[0]



    except FileNotFoundError:
        print("there was an error getting the word from the database")# after this call the function to get the word from the text file
