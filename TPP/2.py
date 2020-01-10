from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 
import csv




with open('db.tsv','wt') as out_file:
	tsv_writer=csv.writer(out_file,delimiter='\t')
	file = open("database.fasta") 

	records = parse(file, "fasta") 

	for record in records: 
		id=record.id
		print(id)   
		seq=record.seq
		print(seq)
		tsv_writer.writerow([id,seq])
		
   # print(record.id) 
   # print("Name: %s" % record.name) 
   # print("Description: %s" % record.description) 
   # print("Annotations: %s" % record.annotations) 
   # print(record.seq) 
   # tsv_writer.writerow([record.id,record.seq])
   # print("Sequence Alphabet: %s" % record.seq.alphabet)
   