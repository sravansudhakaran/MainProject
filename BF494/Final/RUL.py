import csv
import math

infile  = 'BF494.csv'
outfile = 'BF494_new.csv'

# vbe -> 1.00 to 1.70
# vce -> 0.15 to 0.99
# rul -> 100 to 1
samples = 50000

vbe_step = (1.70-1.00)/samples
vce_step = (0.99-0.15)/samples
#rul_step = (1-100)/samples
vbe_start = 1.00
vce_start = 0.15
rul_start = 100

with open(infile,'r') as csvinput:
	with open(outfile, 'w') as csvoutput:
		writer = csv.writer(csvoutput)
		for row in csv.reader(csvinput):
			writer.writerow([vbe_start]+[vce_start]+[rul_start])
			vbe_start = vbe_start+vbe_step
			vce_start = vce_start+vce_step
			rul_start = rul_start+rul_step
			print('Current RUL: ',rul_start)
