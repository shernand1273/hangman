#This module is used to handle the user input from the confirmationbox module
#if the user selects 'New Game' from the confirmbox module, the module will call the restart button with and pass the 'y' parameter
#if the user selects 'Miain Menu', the confirmbox module will call this function and pass it the 'n' parameter
import os
import platform
import sys

def restart(arg):

    if(arg == "y"):
        #the process will be terminated and the shell will rerun this scipt to take its place
        os.execl(sys.executable,'python3',"mainwindow.py", * sys.argv)

    elif(arg == "n"):
        #the current process will be replaced by launching the launcher module
        os.execl(sys.executable,'python3','launcher.py', * sys.argv)
