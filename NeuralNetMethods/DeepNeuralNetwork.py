# RMSE at 0.14 with SD 0.07

import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from keras import backend
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# load dataset
print("[>] Loading Dataset ...")
dataframe = pandas.read_csv("igbt_noise_removed_normalised.csv",dtype='float64', header=0)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:6]
Y = dataset[:,6]
print("[+] Dataset Loaded ...")

def root_mean_squared_error(y_true, y_pred):
	return backend.sqrt(backend.mean(backend.square(y_pred - y_true)))

## define base model
#def baseline_model():
	## create model
	#model = Sequential()
	#model.add(Dense(6, input_dim=6, kernel_initializer='normal', activation='relu'))
	#model.add(Dense(1, kernel_initializer='normal'))
	## Compile model
	#model.compile(loss='mean_squared_error', optimizer='RMSProp')
	#return model

# define the model
def larger_model():
	# create model
	model = Sequential()
	model.add(Dense(60, input_dim=6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(50, kernel_initializer='normal', activation='relu'))
	model.add(Dense(40, kernel_initializer='normal', activation='relu'))
	model.add(Dense(30, kernel_initializer='normal', activation='relu'))
	model.add(Dense(20, kernel_initializer='normal', activation='relu'))
	model.add(Dense(10, kernel_initializer='normal', activation='relu'))
	model.add(Dense(5,  kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
	# Compile model
	model.compile(loss=root_mean_squared_error, optimizer='adamax')
	return model

## define wider model
#def wider_model():
	## create model
	#model = Sequential()
	#model.add(Dense(20, input_dim=6, kernel_initializer='normal', activation='relu'))
	#model.add(Dense(1, kernel_initializer='normal'))
	## Compile model
	#model.compile(loss='mean_squared_error', optimizer='adam')
	#return model

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# evaluate model with standardized dataset
# Pipeline that first standardizes the dataset then creates and evaluate the baseline neural network model
print("[>] Training Started ...")
#estimator = KerasRegressor(build_fn=baseline_model, epochs=1, batch_size=5, verbose=1)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=larger_model, epochs=5, batch_size=5, verbose=1)))
pipeline = Pipeline(estimators)
print("[+] Training Ended ...")

# 10-fold cross validation to evaluate the model
kfold = KFold(n_splits=10, random_state=seed)

print("[>] Cross-Validation Started ...")
#results = cross_val_score(estimator, X, Y, cv=kfold)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print("[+] Cross-Validation Ended ...")


print("\n Standardized: %.2f (%.2f) RMSE" % (results.mean(), results.std()))
