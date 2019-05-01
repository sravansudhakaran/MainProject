import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from keras import backend
from keras.models import load_model
import os
import Sensor_controller
import math
import time


def get_params():
	
	vce,vbe,ambient_temp = Sensor_controller.get_values()
	vce = vce / 12.2566
	vbe = vbe / 1.0109
	ambient_temp = ambient_temp / 50.684
	os.system('clear')
	print('[+] Sensor Readings Obtained ...')
	time.sleep(1)
	print('[+] Vbe = ' + str(vbe))
	print('[+] Vce = ' + str(vce))
	print('[+] Ambient Temperature = ' + str(ambient_temp))
	time.sleep(1)
	print('[+] Calculating Additional Parameters ...')
	vcc = 12.0
	vbb = 5.0
	rc = 100.0
	rb = 100.0
	thermal_res = 420.0
	ic = (vcc-vce) /rc
	ib = (vbb-vbe) /rb
	beta = ic / ib
	alpha = beta / (1+beta)
	power_diss = 0.100
	junction_temp = ambient_temp + ( thermal_res * power_diss )
	time.sleep(1)
	print('[+] Additional Parameters Calculated ...')
	sensor_values = [vce,vbe,ic,ib,beta,alpha,ambient_temp,junction_temp]
	return sensor_values

def root_mean_squared_error(y_true, y_pred):
	return backend.sqrt(backend.mean(backend.square(y_pred - y_true)))

def predict_rul():
	print('[+] Loading Trained Model and predicting RUL ...')
	time.sleep(1)
	model = load_model('BF494.hdf5', custom_objects ={'root_mean_squared_error':root_mean_squared_error})
	X = np.array([get_params()])
	Y = model.predict(X)
	os.system('clear')
	print('Remaining Useful Life = ' + str(Y))

predict_rul()
