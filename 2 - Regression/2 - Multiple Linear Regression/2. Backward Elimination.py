# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Handling categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
one_hot_encoder = OneHotEncoder(categorical_features = [3])
X = one_hot_encoder.fit_transform(X).toarray()


# Avoiding summy variable trap
X = X[:, 1:]



# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# print(X_train, X_test, y_train, y_test)



# Fitting Multiple linear regression to the training set
from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# Predicting with the model
y_pred = regressor.predict(X_test)


# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)

# find the Sl values that are above the define SL say 0.05 in this case, the the highest amg them
# *** Note here we taking full data set to have good prediction of which columns are statistically important ***
X_opt = X[:, [0,1,2,3,4,5]]
regression_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regression_OLS.summary()

# Here the hight is in column 2, so remove it and fit it again
X_opt = X[:, [0,1,3,4,5]]
regression_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regression_OLS.summary()

# Again the hight is in column 1, so remove it and fit it again
X_opt = X[:, [0,3,4,5]]
regression_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regression_OLS.summary()


# Again there is one > 0.05, so remove it and fit it again
X_opt = X[:, [0,3,5]]
regression_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regression_OLS.summary()

# Now we have one with 0.06 > 0.05, so remove it and fit it again
X_opt = X[:, [0,3]]
regression_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regression_OLS.summary()


