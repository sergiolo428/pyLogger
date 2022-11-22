# pyLogger
from dataclasses import asdict
import string
import datetime
from xml.dom.pulldom import SAX2DOM
import os
import sys

os.chdir(sys.path[0]) # Change to current .py file path

def logger(text):
    now = datetime.datetime.now() # Get current date and time
    with open("./logs.txt","a") as f:
        f.write(str(now) + " ||| " + text + "\n") # Write "now"

if __name__=='__main__':    
    text="MyText."
    logger(text)