import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score, cross_val_predict, KFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline

# load dataset

print("[>] Loading Dataset ...")
dataframe = pd.read_csv("igbt_noise_removed_normalised.csv",dtype='float64', header=0)
dataset = dataframe.values

# split into input (X) and output (Y) variables

X = dataset[:,0:6]
y = dataset[:,6]

print("[+] Dataset Loaded ...")

def model(pipeline, parameters, X_train, y_train, X, y):

    grid_obj = GridSearchCV(estimator=pipeline,param_grid=parameters,cv=10,scoring='neg_mean_squared_error',verbose=2,n_jobs=1,return_train_score=True,refit=True)
    grid_obj.fit(X_train, y_train)

    '''Results'''

    results = pd.DataFrame(pd.DataFrame(grid_obj.cv_results_))
    results_sorted = results.sort_values(by=['mean_test_score'], ascending=False)

    print("Results")
    print(results_sorted)

    print("best_index", grid_obj.best_index_)
    print("best_score", grid_obj.best_score_)
    print("best_params", grid_obj.best_params_)

    '''Cross Validation'''

    estimator = grid_obj.best_estimator_
    
    '''
    if estimator.named_steps['scl'] == True:
        X = (X - X.mean()) / (X.std())
        y = (y - y.mean()) / (y.std())
    '''
    
    shuffle = KFold(n_splits=5,shuffle=True,random_state=0)
    cv_scores = cross_val_score(estimator,X,y.ravel(),cv=10,scoring='neg_mean_squared_error',verbose=2)
    print("[+] Cross Validation Results")
    print("Mean: ", np.sqrt(np.abs(cv_scores.mean())),".. Std Deviaiton: ",np.sqrt(np.abs(cv_scores.std())))

    '''Show model coefficients or feature importances
    	

    try:
        print("Model coefficients: ", list(zip(list(X), estimator.named_steps['clf'].coef_)))
    except:
        print("Model does not support model coefficients")

    try:
        print("Feature importances: ", list(zip(list(X), estimator.named_steps['clf'].feature_importances_)))
    except:
        print("Model does not support feature importances")
	
    Predict along CV and plot y vs. y_predicted in scatter'''

    y_pred = cross_val_predict(estimator, X, y, cv=shuffle)

# Pipeline and Parameters - Polynomial Regression
print("[>] Creating Pipeline ...")

pipe_poly = Pipeline([('scl', StandardScaler()),('polynomial', PolynomialFeatures()),('clf', LinearRegression())])
param_poly = {'polynomial__degree': [2, 4]}

print("[+] Pipeline Created ...")

# Execute preprocessing & train/test split

#X, y = preprocessing(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# Execute model hyperparameter tuning and crossvalidation
print("[>] Training Started ...")

model(pipe_poly, param_poly, X_train, y_train, X, y)

print("[+] Training Completed ...")
