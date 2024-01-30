#!/usr/bin/python3 
import os
import sys
import json


def main():
	bl=[]
	print("Get names from neo4j console output of SharpHound dump")
	print("Usage:",os.path.basename(__file__), "<bloodhound output>")
	with open(sys.argv[1], encoding='utf-8-sig') as f:
		d=json.load(f)
		for item in d:
			props=item["n"]["properties"]
			bl.append(props["name"].lower())


	#remove duplicates
	bl = list(set(bl))

	for b in bl:
		print(b)

	print("Count: ",len(bl))
	#for line in serv:
	#	print(line)




if __name__ == '__main__':
	main()