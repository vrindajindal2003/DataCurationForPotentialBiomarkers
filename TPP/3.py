import os
import csv
counter=0;
dict={}
numfile=0
	
row1=['PROTEIN','PEPTIDE','SHARED/UNIQUE']

for filename in os.listdir("o-files"):

	if filename.endswith(".tsv"):
		# print(counter)
		with open("o-files/"+filename) as tsvfile:
			numfile=numfile+1
			row1=row1+[filename[1:]]
			reader = csv.reader(tsvfile,delimiter="\t")
			for row in reader:
				prot=row[0]
				peps=row[1]
				if(prot=="PROTEINS"):
					continue
				pepl=peps.split('+')
				if(dict.get(prot,-1)==-1):
					dict[prot]=[]
				for i in range(len(pepl)):
					if pepl[i] not in dict[prot]:
						dict[prot]=dict[prot]+[pepl[i]]

	counter=counter+1
# cnt=0
# for i in dict:
# 	print(i)
# 	cnt+=1
# 	# print(dict[i])
# 	# print(type(dict[i]))
# 	dict[i].sort()
# 	# for j in range(len(dict[i])):
# 	print(dict[i])
# 	print("---------")
# 	# print(dict[i])
# print(cnt)


num=numfile
with open('final.tsv','wt') as file:
	writer = csv.writer(file,delimiter='\t')
	writer.writerow(row1)
	
	for protein in dict:
		dict[protein].sort()
		print("................")
		print(protein)
		for j in range(len(dict[protein])):
			peptide=dict[protein][j]
			print(peptide)
			ctotal=0
			c=[]
			for x in range(num):
				c=c+[0];

			with open('db.tsv') as dbfile:
				reader = csv.reader(dbfile,delimiter="\t")
				for row in reader:
					if peptide in row[1]:
						ctotal=ctotal+1;
			o=0
			for file in os.listdir("o-files"):
				with open("o-files/"+file) as f:
					# print(f)
					reader=csv.reader(f,delimiter="\t")
					for row in reader:
						if peptide in row[1]:
							# print(f)
							c[o]=c[o]+1
					o+=1
			
			s=''
			if(ctotal==1):
				s='unique'
			elif(ctotal==0):
				s='-------'
			else:
				s='shared'+str(ctotal)
			writer.writerow([protein,peptide,s,]+c)

