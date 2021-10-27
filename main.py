#!/usr/bin/python3

'''
Tool Name ::
Author :: Padsala Trushal #changing this line doesn't make you developer
Date :: 24 Oct 2021
'''

import os
import argparse
import sys


def get_arguments():
	parser = argparse.ArgumentParser(description='Inject bash script in debian package',usage=f'python3 {sys.argv[0]} -p debian_package -s bash_script',epilog=f'EXAMPLE - python3 {sys.argv[0]} -p /tmp/file.deb -s /tmp/script.sh')

	parser.add_argument('-v','--version',action='version',version='1.4',help='show the version of program')

	parser.add_argument('-s',metavar='bash script',dest='bash',help='Enter your bash script path')


	parser.add_argument('-p',metavar='debian package',dest='deb',help='Enter your debian package path')

	args = parser.parse_args()

	if len(sys.argv) < 2:
		parser.print_usage()
		sys.exit(1)
		
	return args













filename = str(input("enter your file name:\n"))
b = filename.split(".deb")

def extractor(filename):
	command = f"dpkg-deb -R {filename} ./{b[0]}"
	os.system(command) 
	print("[*] Package Extract Successfully")

extractor(filename)





