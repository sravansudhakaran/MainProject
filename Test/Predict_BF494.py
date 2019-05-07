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
	print("[+] Connecting with Sensors ...")
	vce,vbe,ambient_temp = pi_server.get_data()
	print('[+] Sensor Readings Obtained ...')

	print('[+] Vbe = ',vbe)
	print('[+] Vce = ', vce)
	print('[+] Ambient Temperature = ',ambient_temp)
	
	vce_max = 13.0
	vce_min = min(vce)
	vbe_max = max(vbe)
	vbe_min = 0
	temp_max = max(ambient_temp)
	
	sensor_values = [vbe,vce,ambient_temp,vce_max,vce_min,vbe_max,vbe_min,temp_max]
	return sensor_values

def root_mean_squared_error(y_true, y_pred):
	return backend.sqrt(backend.mean(backend.square(y_pred - y_true)))

def predict_rul():
	no_samples = 20
	print("[+] Loading trained model ...")
	model = load_model('BF494_new.hdf5', custom_objects ={'root_mean_squared_error':root_mean_squared_error})
	print("[+] Predicting RUL ...")
	rul = []
	[vbe,vce,ambient_temp,vce_max,vce_min,vbe_max,vbe_min,temp_max] = get_params()
	samples = []
	for i in range(0,no_samples):
		samples.append([vbe[i],vce[i]])
	for i in range(0,no_samples):
		X = np.array([samples[i]])
		Y = model.predict(X)
		rul.append(Y.tolist()[0][0])
		rul[i] = rul[i] * (10000000000)
	rul_avg = 0.0
	count = 0
	for i in range(0,no_samples):
		if (rul[i] == 0):
			continue
		rul_avg = rul[i]+rul_avg
		count = count+1
	if count != 0:
		rul_avg = rul_avg / count
	print(rul,rul_avg)
	return (vce_max,vce_min,vbe_max,vbe_min,temp_max,rul_avg)

predict_rul()
