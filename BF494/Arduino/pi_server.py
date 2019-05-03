import time
import serial

def get_data():
	vce_array = []
	vbe_array = []
	temp_array = []
	ser = serial.Serial('/dev/ttyACM0', 9600)         			# enable the serial port
	for i in range(0,10):                                                         	# execute the loop forever
		incoming_stream = ser.readline()                                # read the serial data sent by the UNO
		# print (incoming_stream)                                       # print the serial data sent by UNO
		try:
			values = incoming_stream.decode("utf-8")			# decode bytes to string
			(temp,vbe,vce) = values.split(',')
			temp_array.append(float(temp))
			vbe_array.append(float(vbe))
			vce_array.append(float(vce))

		except:
			continue

	return (vce_array,vbe_array,temp_array)

print(get_data())
