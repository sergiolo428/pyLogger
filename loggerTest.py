from dataclasses import asdict
import string
import datetime
from xml.dom.pulldom import SAX2DOM

def logger(text):
    print("1")
    now=datetime.datetime.now()
    print("2")
    my_file=open("C:\\Users\\sergi\Desktop\\TestLogger\\logs.txt","a")
    print("3")
    my_file.write(str(now) + "\n")
    print("4")
    my_file.close()
    print("5")

if __name__=='__main__':
    miTexto="Esto es texto"
    logger(miTexto)