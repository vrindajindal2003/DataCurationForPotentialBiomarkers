import os
import csv


with open('final.csv','wt') as file:
	writer=csv.writer(file)
	with open('processed-final.csv') as readfile:
		reader = csv.reader(readfile,delimiter=",")
		for row in reader:
			prot=row[0]
			pept=row[1]
			print("PROTEIN: "+prot)
			print("PEPTIDE: "+pept)
			
			if(prot=="Proteins"):
				writer.writerow(row[0:2]+['unique/shared']+row[2:])
			elif(prot==""):
				continue
			else:
				cnts=[]
				for val in row[2:]:
					if(int(val)>0):
						cnts=cnts+[1]
					else:
						cnts=cnts+[0]
				foundprot=0
				count=0
				with open('db.tsv') as dbfile:
					dbreader=csv.reader(dbfile,delimiter='\t')
					for dbrow in dbreader:
						if pept in dbrow[1]:
							count=count+1
							if prot in dbrow[0]:
								foundprot=1
				if(foundprot==0):
					continue
				else:
					if(count==0):
						s='---'
					elif(count==1):
						s='unique'
					else:
						s='shared'+str(count)
					
					crow=[prot,pept]+[s]+cnts
					writer.writerow(crow)



						


	