import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
boston_data = pd.read_csv("igbt_noise_removed_normalised.csv")
X,y = boston_data[boston_data.columns.tolist()[:-1]],boston_data[boston_data.columns.tolist()[-1]]
boston_dmatrix = xgb.DMatrix(data=X,label=y)
gbm_param_grid = {
'learning_rate': np.arange(0.05,1.05,.05),
'n_estimators': [200],
'subsample': np.arange(0.05,1.05,.05)}
gbm = xgb.XGBRegressor()
randomized_mse = RandomizedSearchCV(estimator=gbm,
param_distributions=gbm_param_grid, n_iter=25,
scoring='neg_mean_squared_error', cv=4, verbose=1)
randomized_mse.fit(X, y)
print("Best parameters found: ",randomized_mse.best_params_)
print("Lowest RMSE found: ",np.sqrt(np.abs(randomized_mse.best_score_)))
