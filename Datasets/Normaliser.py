import csv

infile  = 'igbt_noise_removed.csv'
outfile = 'igbt_noise_removed_normalised.csv'
column_max=[8.2339,9.9833,0.01112,2.7296,0.94934,287.58,14359]
with open(infile,'r') as csvinput:
	with open(outfile, 'w') as csvoutput:
		writer = csv.writer(csvoutput)
		for row in csv.reader(csvinput):
			for i in range(len(row)):
				try:
					row[i] = str(float(row[i]) / column_max[i])
				except (ValueError):
					print ("error on line",i)
			writer.writerow(row)
