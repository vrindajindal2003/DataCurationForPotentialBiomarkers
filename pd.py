import xlrd
import csv
# import re
import os
from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 


os.mkdir("o-files")

row1=["PROTEIN","PEPTIDE"]		


for filename in os.listdir("input-files"):
	print("formatting "+filename+" to suitable format.....")
	


	with open("o-files/o-"+filename[:-5]+".tsv",'wt') as file:
		writer = csv.writer(file,delimiter='\t')
		writer.writerow(row1)
		wb=xlrd.open_workbook("input-files/"+filename)
		sheet=wb.sheet_by_index(0)
		nrows=sheet.nrows
		ncols=sheet.ncols
		for i in range(ncols):
			if(str(sheet.cell_value(4,i))=="Annotated Sequence"):
				pepcolno=i

			elif(str(sheet.cell_value(4,i))=="Master Protein Accessions"):
				protcolno=i

		for i in range(nrows):
			val=str(sheet.cell_value(i,pepcolno))
			if(val[0]=="["):
				pept=val.split(".")[1]
				# pept=val2[1]
				protl=str(sheet.cell_value(i,protcolno)).split(";")
				for prot in protl:
					row=[prot.strip(), pept]
					writer.writerow(row)





with open('db.tsv','wt') as out_file:
	print("formatting database to usable format")
	tsv_writer=csv.writer(out_file,delimiter='\t')
	file = open("database.fasta") 

	records = parse(file, "fasta") 

	for record in records: 
		id=record.id
		# print(id)   
		seq=record.seq
		# print(seq)
		tsv_writer.writerow([id,seq])
		
   # print(record.id) 
   # print("Name: %s" % record.name) 
   # print("Description: %s" % record.description) 
   # print("Annotations: %s" % record.annotations) 
   # print(record.seq) 
   # tsv_writer.writerow([record.id,record.seq])
   # print("Sequence Alphabet: %s" % record.seq.alphabet)
   


			
	

numfile=0
row1=['PROTEIN','PEPTIDE','SHARED/UNIQUE']
dict={}

l=[]
for filename in os.listdir("o-files"):
	with open("o-files/"+filename) as tsvfile:
		numfile=numfile+1
		l=l+[0]
		row1=row1+[filename[2:-4]]
		reader=csv.reader(tsvfile,delimiter="\t")
		for row in reader:
			prot=row[0]
			pept=row[1]
			if prot=='PROTEIN':
				continue
			if(dict.get(prot,-1)==-1):
				dict[prot]={}
			if(dict[prot].get(pept,-1)==-1):
				lh=l.copy()
				lh[-1]=1
				dict[prot][pept]=lh
			else:
				# print(len(dict[prot][pept]))
				# print(numfile)
				# print(".......")
				while len(dict[prot][pept])<numfile:
					dict[prot][pept]=dict[prot][pept]+[0]
				dict[prot][pept][-1]=1
				# if(len(dict[prot][pept])!=numfile-1):
				# 	while(len(dict[prot][pept])!=numfile-1):
				# 		dict[prot][pept]=dict[prot][pept]+[0]
				# dict[prot][pept]=dict[prot][pept]+[1]

with open("final.tsv","wt") as file:
	writer=csv.writer(file,delimiter="\t")
	writer.writerow(row1)
	for prot in sorted(dict.keys()):
		print('..........')
		print(prot)
		for pept in sorted(dict[prot].keys()):
			# list=dict[prot][pept]
			while len(dict[prot][pept])<numfile:
				dict[prot][pept]=dict[prot][pept]+[0]
			print(pept)
			ctotal=0
			with open("db.tsv") as db:
				reader=csv.reader(db,delimiter="\t")
				for dbrow in reader:
					# print(dbrow)
					if pept in dbrow[1]:
						ctotal=ctotal+1
			s=''
			if(ctotal==1):
				s='unique'
			elif(ctotal==0):
				s='-------'
			else:
				s='shared'+str(ctotal)
			# b=[]
			# for i in c:
			# 	if(i>0):
			# 		b=b+[1]
			# 	elif(i==0):
			# 		b=b+[0]

			row=[prot,pept,s]+dict[prot][pept]
			writer.writerow(row)




