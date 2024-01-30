#!/usr/bin/python3
import os
import sys
import re




def main():
	buff=[]
	pattern = re.compile(r"^\S{16,}$")

	if(len(sys.argv != 2)):
		print("Usage:",os.path.basename(__file__), "<input file>")
		return;

	with open(sys.argv[1], mode='r') as f:
		for line in f:
			res = pattern.search(line.strip())
			if res is not None and line.strip():
				print(line)
				buff.append(line)

			#if res is None and line.strip():
			#	buff.append(line)


	with open("desc_32chars", mode="w") as f:
		for i in buff:
			f.writelines(i+"\n")
if __name__ == '__main__':
	main()
