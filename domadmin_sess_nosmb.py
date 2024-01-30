#!/usr/bin/python3 
import os
import sys
import json


def main():
	serv=[]
	bl=[]
	print("Usage:",os.path.basename(__file__), "<nosmbserverlist> <bloodhoundoutput>")

	with open(sys.argv[2]) as f:
		d=json.load(f)
		for node in d["nodes"]:
			cname = node["props"]["name"]
			osname=""
			if "operatingsystem" in node["props"]:
				osname = node["props"]["operatingsystem"]

			if(node["type"] == "Computer"):
				#bl[cname.lower()] = node["props"]["operatingsystem"]
				bl.append(cname.lower() + ":" + osname)

	
	with open(sys.argv[1]) as f:
		for line in f:
			l = line.lower().strip()
			serv.append(l)


	#remove duplicates
	bl = list(set(bl))
	serv = list(set(serv))

	count=0
	for b in bl:
		cname = b.split(':')[0]
		if(cname in serv):
			print(b)
			count+=1
		

	print("Non DC Servers with Domain Admin Sessions: ",len(bl))
	print("No SMB, Non DC Servers with Domain Admin Sessions: ",count)
	#for line in serv:
	#	print(line)




if __name__ == '__main__':
	main()