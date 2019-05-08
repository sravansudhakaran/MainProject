import time
import serial

def get_data():
	no_samples = 10
	vce_array = []
	vbe_array = []
	temp_array = []
	ser = serial.Serial('/dev/ttyACM0', 9600)         			# enable the serial port
	for i in range(0,30):                                                   # execute the loop forever
		incoming_stream = ser.readline()                                # read the serial data sent by the UNO
		#print (incoming_stream)                                         # print the serial data sent by UNO
		try:
			values = incoming_stream.decode("utf-8")		# decode bytes to string
			(temp,vbe,vce) = values.split(',')
			if(len(temp_array) < no_samples):
				temp_array.append(float(temp))
			if(len(vbe_array) < no_samples):
				if(float(vbe) > 0.9):
					vbe_array.append(float(vbe))
			if(len(vce_array) < no_samples):
				if(float(vce) < 2.0):
					vce_array.append(float(vce))

		except:
			continue

	return (vce_array,vbe_array,temp_array)

#print(get_data())
