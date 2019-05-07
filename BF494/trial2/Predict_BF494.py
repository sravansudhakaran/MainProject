import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from keras import backend
from keras.models import load_model
import os
import pi_server
import math
import time

def get_params():
	no_samples = 10
	print("[+] Connecting with Sensors ...")
	vce,vbe,ambient_temp = pi_server.get_data()
	print('[+] Sensor Readings Obtained ...')

	print('[+] Vbe = ',vbe)
	print('[+] Vce = ', vce)
	print('[+] Ambient Temperature = ',ambient_temp)
	vce_max = max(vce)
	vce_min = min(vce)
	vbe_max = max(vbe)
	vbe_min = min(vbe)
	temp_max = max(ambient_temp)

	print('[+] Calculating Additional Parameters ...')
	vcc = 13.1					#constants
	vbb = 5.0
	rc = 100.0
	rb = 100.0
	thermal_res = 420.0
	old = False
	ic = [0,0,0,0,0,0,0,0,0,0]				#variables
	ib = [0,0,0,0,0,0,0,0,0,0]
	if (max(vbe) > 1.09):
		old = True
	beta = [0,0,0,0,0,0,0,0,0,0]
	alpha = [0,0,0,0,0,0,0,0,0,0]
	junction_temp = [0,0,0,0,0,0,0,0,0,0]
	for i in range(0,no_samples):
		try:
			ic[i] = (vcc-vce[i]) /rc
			ib[i] = (vbb-vbe[i]) /rb
			beta[i] = ic[i] / ib[i]
			alpha[i] = beta[i] / (1+beta[i])
			power_diss = 0.100
			junction_temp[i] = ambient_temp[i] + ( thermal_res * power_diss )
		except:
			continue
	print('[+] Additional Parameters Calculated ...')

	for i in range (0,no_samples):				#Normalising all Params
		vce[i] = vce[i] / 13.1
		vbe[i] = vbe[i] / 1.25
		ambient_temp[i] = ambient_temp[i] / 50.684
		ic[i] = ic[i] / 0.115047272727273
		ib[i] = ib[i] / 0.050313877777778
		beta[i] = beta[i] / 2.878543415715
		alpha[i] = alpha[i] / 0.742171250179071
		junction_temp[i] = junction_temp[i] / 92.6841436918525
	print('[+] All Parameters Normalised...')

	sensor_values = [vce,vbe,ic,ib,beta,alpha,ambient_temp,junction_temp,vce_max,vce_min,vbe_max,vbe_min,temp_max,old]
	# print('[+] Additional Parameters ... \n',sensor_values)
	return sensor_values

def root_mean_squared_error(y_true, y_pred):
	return backend.sqrt(backend.mean(backend.square(y_pred - y_true)))

def predict_rul():
	no_samples = 10
	print("[+] Loading trained model ...")
	time.sleep(1)
	model = load_model('BF494_2.hdf5', custom_objects ={'root_mean_squared_error':root_mean_squared_error})
	print("[+] Predicting RUL ...")
	rul = [0,0,0,0,0,0,0,0,0,0]
	[vce,vbe,ic,ib,beta,alpha,ambient_temp,junction_temp,vce_max,vce_min,vbe_max,vbe_min,temp_max,old] = get_params()
	#print([vce,vbe,ic,ib,beta,alpha,ambient_temp,junction_temp,vce_max,vce_min,vbe_max,vbe_min,temp_max])
	samples = []
	for i in range(0,no_samples):
		samples.append([vce[i],vbe[i],ic[i],ib[i],beta[i],alpha[i],ambient_temp[i],junction_temp[i]])
	for i in range(0,8):
		X = np.array([samples[i]])
		Y = model.predict(X)
		rul[i] = Y.tolist()[0][0]
		rul[i] = rul[i] * (30000000)
	rul_avg = 0.0
	count = 0
	for i in range(0,no_samples):
		if abs(rul[i]) > 1:
			continue
		if abs(rul[i] == 0):
			continue
		rul_avg = abs(rul[i])+rul_avg
		count = count+1
	if count != 0:
		rul_avg = rul_avg / count
	print(rul,rul_avg)
	if (old):
		rul_avg = 0.2
	return (vce_max,vce_min,vbe_max,vbe_min,temp_max,rul_avg*100)
