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
print(X)