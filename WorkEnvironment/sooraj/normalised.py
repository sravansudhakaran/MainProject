import csv

with open('igbt_added_RUL.csv','r') as csvinput:
	with open('igbt_norm.csv', 'w') as csvoutput:
		writer = csv.writer(csvoutput)
		for row in csv.reader(csvinput):
			writer.writerow(row[1:])
