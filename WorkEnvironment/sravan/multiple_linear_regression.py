# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('igbt_noise_removed_normalised.csv')
X = dataset.iloc[:, 1:7].values
y = dataset.iloc[:, 0].values

# Encoding categorical data
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder = LabelEncoder()
#X[:, 3] = labelencoder.fit_transform(X[:, 3])
#onehotencoder = OneHotEncoder(categorical_features = [3])
#X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
#X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
#plt.scatter(X_train, y_train, color = 'red')
#plt.plot(X_train, regressor.predict(X_train), color = 'blue')
#plt.title('Time vs Features (Training set)')
#plt.xlabel('All Features')
#plt.ylabel('Time')
#plt.show()

## Visualising the Test set results
#plt.scatter(X_test, y_test, color = 'red')
#plt.plot(X_train, regressor.predict(X_train), color = 'blue')
#plt.title('Time vs Features(Test set)')
#plt.xlabel('All Features')
#plt.ylabel('Time')
#plt.show()



from sklearn.model_selection import cross_val_score
#reg = linear_model.LinearRegression()
cv_results = cross_val_score(regressor,X,y, cv=2)
print(cv_results)


import statsmodels.formula.api as sm
X = np.append( arr= np.ones((301569,1)).astype (int), values= X , axis=1)

