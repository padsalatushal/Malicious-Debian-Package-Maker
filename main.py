#!/usr/bin/python3

'''
Tool Name ::
Author :: Padsala Trushal #changing this line doesn't make you developer
Date :: 24 Oct 2021
'''

import os


filename = str(input("enter your file name:\n"))
def extractor(filename):
	command = f"dpkg-deb -R {filename} ./test"
	os.system(command) 

extractor(filename)

