#!/usr/bin/python
import csv
import os
import pandas,numpy
import argparse


pandas.set_option('mode.chained_assignment', None) 

WORKING_FILE='temp.csv'
EMPTY_LM_HASH='aad3b435b51404eeaad3b435b51404ee'

parser=argparse.ArgumentParser(description="Transforms csv output from mimikatz lsadump::dcsync /csv into workable formats")
parser.add_argument('filename')
parser.add_argument('-c','--crackable',action='store_true',default=False, help='output to john/hashcat crackable format')
parser.add_argument('-s','--password_stats',action='store_true',default=False,help='parse password statistics')
parser.add_argument('-p','--reused_pws',action='store_true',default=False,help='get reused passwords and output to file')
parser.add_argument('-b','--hashedby',default='john',help='used with -i, sets format for solved hash file(either john or hashcat, default john)',)
parser.add_argument('-i','--solved_hashes',help='file with solved hashes',)
parser.add_argument('-k','--kerberoastable_users',help='file with kerberoastable users')
parser.add_argument('-r','--regular',action='store_true',default=False,help='perform --crackable --reused_pws and --password-stats')

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



def parse_user_hash_data():
	df=pandas.read_csv(WORKING_FILE,delimiter='\t').sort_values('nthash')
	#print(df)
	reused_pws=df[df['nthash'].map(df['nthash'].value_counts()) > 1]#get only the passwords that are used by more than one user
	

	return reused_pws,df

def print_statistics(df):
	print("\n\n------Statistics-------")
	print("Total number of users reusing passwords: ",len(df))
	print("Number of unique passwords in reuse: ",len(df['nthash'].unique()))
	

def output_to_reportable_format(df,reused):
	df_grouped=reused.groupby('nthash')['ID'].nunique().sort_values(ascending=False).to_frame().reset_index()#group by unique hash, sort, then make dataframe
	df_grouped.columns.values[1]="Occurences"
	df_grouped['Members']='' # add a column to put in list of users who share specific password
	for index,row in df_grouped.iterrows():
		member_users=df[df.nthash.isin([row.nthash])]['samaccountname']
		member_users=''.join(x+'\015' for x in member_users)
		df_grouped['Members'][index]=member_users
		

	return df_grouped

	

def main():
	create_working_file(args.filename)#file that other funcions will refer to
	reused,df=parse_user_hash_data() #get a separate variable just for the reused pws

	if(args.regular):
		args.reused_pws,args.crackable,args.password_stats = True,True,True


	if(args.reused_pws):
		print("[+]----Gathering reused password data...")
		grouped_hashes=output_to_reportable_format(df,reused) #mangle data to the form we want for exporting
		grouped_hashes.index=numpy.arange(1,len(grouped_hashes)+1)
		grouped_hashes.to_excel(args.filename.split(".")[0]+'_grouped_byhash.xlsx')


	if(args.crackable):
		print("[+]----Converting to crackable format...")
		convert_to_crackable()

	if(args.password_stats):
		print("[+]----Printing statistics...")
		print_statistics(reused)


	os.remove(WORKING_FILE)

main()