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
dataframe = pandas.read_csv("BF494_new.csv",dtype='float64', header=0)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:2]
Y = dataset[:,2]
print("[+] Dataset Loaded ...")

def root_mean_squared_error(y_true, y_pred):
	return backend.sqrt(backend.mean(backend.square(y_pred - y_true)))

model = Sequential()
model.add(Dense(10, input_dim=2, kernel_initializer='normal', activation='relu'))
model.add(Dense(5, kernel_initializer='normal', activation='relu'))
model.add(Dense(2, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal',activation='linear'))
model.compile(loss=root_mean_squared_error, optimizer='adamax',metrics=['mean_absolute_error'])
model.fit(X, Y, epochs=100, batch_size=10, verbose=1)
scores = model.evaluate(X, Y, verbose=1)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
model.save("BF494_1.h5") 
print("Saved model to disk")
