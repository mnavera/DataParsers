#!/usr/bin/python
import csv
import os
import pandas
import argparse


WORKING_FILE='temp.csv'
EMPTY_LM_HASH='aad3b435b51404eeaad3b435b51404ee'

parser=argparse.ArgumentParser(description="Transforms csv output from mimikatz lsadump::dcsync /csv into workable formats")
parser.add_argument('filename')
parser.add_argument('-c','--crackable',action='store_true',default=False, help='output to john/hashcat crackable format')
parser.add_argument('-s','--password-stats',action='store_true',default=False,help='parse password statistics')
parser.add_argument('-b','--hashedby',default='john',help='used with -i, sets format for solved hash file(either john or hashcat, default john)',)
parser.add_argument('-i','--input_hashes',help='file with solved hashes',)
parser.add_argument('-r','--regular',action='store_true',default=False,help='perform --crackable and --password-stats')

args = parser.parse_args()

def create_working_file(fname):
	count=0;
	csv_headers=["ID","samaccountname","nthash","Number"]
	read_file_handle=open(fname,'r')#read the input line by line so we don't eat memory
	write_file_handle=open(WORKING_FILE,'w',newline='')#temporary working file to put on disk
	
	csv_writer = csv.writer(write_file_handle, delimiter='\t')
	csv_writer.writerow(csv_headers)
	

	for line in read_file_handle:#iterate through mimikatz file and make new temp file
		count+=1
		if count<9: #skip junk
			continue
		else:
			s=line.split("\t")
			csv_writer.writerow(s)



	read_file_handle.close();
	write_file_handle.close();

def convert_to_crackable():#convert the working file into a format that can be cracked by john/hashcat
	with open(WORKING_FILE,'r') as file:
		csv_reader=csv.DictReader(file,delimiter="\t")
		output_file=open('crackable.hashes','w') #file to put our lines in
		for line in csv_reader:
			output_file.write(line["samaccountname"]+"::"+EMPTY_LM_HASH+":"+line["nthash"]+":::"+'\n') # write line by line
		


		output_file.close()

def parse_user_hash_statistics():
	df=pandas.read_csv(WORKING_FILE,delimiter='\t')
	unique_hashes=df['nthash'].value_counts()#make Series of all unique hashes and their number of occurences
	
#sample hashes
#440431	liushunlin	1476373a33475c5cd08ad94a6c37d610	514	691
#976678	yolandalin	32ed87bdb5fdc5e9cba88547376818d4	514	238


create_working_file(args.filename)
df=parse_user_hash_statistics()
os.remove(WORKING_FILE)