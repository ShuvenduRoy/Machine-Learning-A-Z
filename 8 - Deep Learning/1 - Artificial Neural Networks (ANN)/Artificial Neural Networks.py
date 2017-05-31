# Step 1 : Data Preprocessing

# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Changing the categorical data into numerical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X_1 = LabelEncoder()
X[:, 1] = labelEncoder_X_1.fit_transform(X[:, 1])

labelEncoder_X_2 = LabelEncoder()
X[:, 2] = labelEncoder_X_2.fit_transform(X[:, 2])

onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding dummy variablee trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Step 2 : Making the ANN
# Fitting classifier to the Training set
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initializing ANN
classifier = Sequential()

# Adding the input and first hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation='relu', input_dim = 11))

# Adding second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation='relu'))

# Adding the last hidden layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation='sigmoid'))


# Compiling the ANN
classifier.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])


# Fitting the ANN to the Training model
classifier.fit(X_train, y_train, batch_size=10, nb_epoch = 100)


# Predicting the Test set results
y_pred = classifier.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)