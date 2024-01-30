#!/usr/bin/python3

import os
import sys
import re
import xml.etree.ElementTree as ET
from helper import * 



def main():
	if(len(sys.argv)!=2):
		print("Usage:",os.path.basename(__file__), "<nmap xml output>")
		return;

	hosts=getHostElement(sys.argv[1])
	for host in hosts:
		ports=findOpenPorts(host)
		name=findHostName(host)
		if '445' in ports:
			s=getScripts(host,'cve-2020-0796')
			vuln=re.search(r'Vulnerable\sto\sCVE\-2020\-0796\sSMBGhost',s[1])#s[1] is the SMB dialects supported
			if(vuln is not None):
				print("VULN",name)
			else:
				print("SAFE",name)



if __name__ == '__main__':
	main()