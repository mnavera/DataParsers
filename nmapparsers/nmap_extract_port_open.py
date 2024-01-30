#!/usr/bin/python3

import os
import sys
import re
import xml.etree.ElementTree as ET
from helper import * 



def main():
	if(len(sys.argv)!=3):
		print("Usage:",os.path.basename(__file__), "<nmap xml output> <portnum>")
		return;

	pnum=sys.argv[2];
	hosts=getHostElement(sys.argv[1])
	for host in hosts:
		ports=findOpenPorts(host)
		name=findHostName(host)
		if pnum in ports:
			print(name)



if __name__ == '__main__':
	main()