import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
boston_data = pd.read_csv("igbt_heatsink_removed.csv")
X, y = boston_data.iloc[:,:-1],boston_data.iloc[:,-1]
boston_dmatrix = xgb.DMatrix(data=X,label=y)
X_train, X_test, y_train, y_test= train_test_split(X, y,test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective='reg:linear',n_estimators=10, seed=123)
DM_train = xgb.DMatrix(data=X_train,label=y_train)
DM_test =xgb.DMatrix(data=X_test,label=y_test)
params = {"booster":"gblinear","objective":"reg:linear","max_depth":4}
l1_params = [1,10,1000]
rmses_l1=[]
for reg in l1_params:
    params["alpha"] = reg
    cv_results = xgb.cv(dtrain=boston_dmatrix,
    params=params,nfold=10,
    num_boost_round=10,metrics="rmse",as_pandas=True,seed=123)
    rmses_l1.append(cv_results["test-rmse-mean"] \
    .tail(1).values[0])
print("Best rmse as a function of l1:")
print(pd.DataFrame(list(zip(l1_params,rmses_l1)),
columns=["l1","rmse"]))
