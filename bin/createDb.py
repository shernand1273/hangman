#open up the files
import sqlite3

with open("../wordFiles/wordListBackup.txt","r")as readFile:
    content= readFile.read()
    lines = content.splitlines()

#create the database
conn = sqlite3.connect("wordList.db")
cursor= conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS wordList (theNum INTEGER,word TEXT)")
conn.commit()
conn.close()

#insert the contents of the file into the database
insertConn=sqlite3.connect("wordList.db")
insertCursor=insertConn.cursor()

for i in range(len(lines)):
    insertCursor.execute("INSERT INTO wordList VALUES (?,?)", (i+1,lines[i]))
    insertConn.commit()

insertCursor.close()
