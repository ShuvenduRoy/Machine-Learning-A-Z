# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
# Strategy is to replace the column where there is missing data with mean of that column0
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy= 'mean', axis=0)

# fitting the imputer in out data set
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Changing the categorical data into numerical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])


# How ever as it is numerical, lebel having greater values seams greater in mathematic modeling
# So, we create dummy variable/column
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()


# Lets do it for y
labelEncoder_y = LabelEncoder()
y = labelEncoder_y.fit_transform(y)

