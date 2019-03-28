import os
import sys
import time

def clearScreen():
    os.system("cls")

def restart():
    time.sleep(2)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
