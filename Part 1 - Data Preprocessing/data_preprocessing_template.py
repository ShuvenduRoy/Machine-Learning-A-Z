# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
print(dataset)

X = dataset.iloc[:, :-1].values     # All row, all column except last one
y = dataset.iloc[:, 3].values       # All row, last column

print('X => ', X)
print('y => ', y)