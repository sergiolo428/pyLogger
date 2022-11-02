from dataclasses import asdict
import string
import datetime
from xml.dom.pulldom import SAX2DOM
import os

def logger(text):
    now = datetime.datetime.now() # Get current date and time
    with open("logs.txt","a") as f:
        f.write(str(now) + " ||| " + text + "\n") # Write "now"

if __name__=='__main__':
    pathWindows="C:\\Python_Tests\\pyLogger"
    pathLinux=""

    os.chdir(pathWindows) #Set curent path
    
    text="MyText."
    logger(text)