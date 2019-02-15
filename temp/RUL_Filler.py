import csv

limit =21
i = 14359

with open('igbt.csv','r') as csvinput:
	with open('igbt_out.csv', 'w') as csvoutput:
		writer = csv.writer(csvoutput)
		for row in csv.reader(csvinput):
			if limit == 0:
				limit = 21
				i = i-1
			limit = limit - 1
			writer.writerow(row+[str(i)])
