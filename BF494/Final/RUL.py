import csv
import math

infile  = 'BF494_new.csv'
outfile = 'BF494_new_2.csv'

# vbe -> 0.90 to 1.15
# vce -> 0.15 to 0.60
# rul -> 100 to 1
vbe_min = 0.90
vbe_max = 1.15
vce_min = 0.15
vce_max = 0.60

samples = 50000

vbe_step = (vbe_max-vbe_min)/samples
vce_step = (vce_max-vce_min)/samples
rul_step = (1-100)/samples
vbe_start = vbe_min
vce_start = vce_min
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
