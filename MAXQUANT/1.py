import os
import csv

with open('processed-1.csv','wt') as wtfile:
	writer = csv.writer(wtfile,delimiter=',')
	with open('processed-0.csv') as readfile:
		reader = csv.reader(readfile,delimiter=",")
		for row in reader:
			# proteins=row[1]
			prots=row[1].split(';')
			for protein in prots:
				writer.writerow([protein,row[0]]+row[2:])

