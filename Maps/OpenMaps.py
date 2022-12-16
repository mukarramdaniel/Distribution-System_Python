#webbrowser module helps in open default web browser of os
from webbrowser import open
#sys contains command line arguments
from sys import argv
#pyperclip is a third party module used to access clipbord
#pip3 install pyperclip
#python3 -m pip install pyperclip
from pyperclip import paste
if len(argv)>1:
	address = " ".join(argv[1:])
else:
	address = paste()
open("http://www.google.com/maps/place/"+address)
