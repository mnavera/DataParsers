#!/usr/bin/python3

import os
import sys
import xml.etree.ElementTree as ET

def getHostElement(xmlfile):
	# create element tree object
	tree = ET.parse(sys.argv[1])

	# get root element
	root = tree.getroot()

	# create empty list for news items
	hosts = []

	# iterate news items
	for host in root.findall('./host'):
		hosts.append(host)

	return hosts

def findOpenPorts(hostelem):

	openports = []
	for p in hostelem[3]:
		#skip the 'extraports' element
		if(p.tag == 'extraports'):
			continue

		portnum=p.attrib['portid']
		portstatus=p[0].attrib['state']

		if(portstatus=='open'):
			openports.append(portnum)

	return openports

def findHostName(hostelem):
	for host in hostelem[2]:
		if(host.attrib['type']=="user"):
			hname = host.attrib['name']
		else:
			continue

	return(hname)

def getScripts(hostelem,scriptname=""):#optionally specify script name as well
	hscript=hostelem[4]
	if (hostelem[4].tag != "hostscript"):#if nmap scan applied scripts
		return "None"

	scripts=hostelem[4][0]

	if (scriptname==""):
		return (scripts.attrib['id'],scripts.attrib['output'])

	else:
		for s in hscript:
			if (s.attrib['id'] == scriptname):
				return(s.attrib['id'],s.attrib['output'])
		




def main():
	if(len(sys.argv)!=2):
		print("Usage:",os.path.basename(__file__), "<nmap xml output>")
		return;

	hosts=getHostElement(sys.argv[1])
	for host in hosts:
		ports=findOpenPorts(host)
		name=findHostName(host)
		hscript=getScripts(host)
		print(hscript)

	


if __name__ == '__main__':
	main()