import os
import platform
import sys

def restart(arg):

    if(arg == "y"):

        os.execl(sys.executable,'python3',"mainwindow.py", * sys.argv)

    elif(arg == "n"):
        os.execl(sys.executable,'python3','launcher.py', * sys.argv)
