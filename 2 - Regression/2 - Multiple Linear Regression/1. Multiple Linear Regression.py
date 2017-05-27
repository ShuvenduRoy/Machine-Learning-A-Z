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
