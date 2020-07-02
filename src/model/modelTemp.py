# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data.csv')

X = dataset.iloc[:, :3]

y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk

import pickle

pickle.dump(regressor, open('model.pkl','wb'))


# Loading model to compare the results
import pickle
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1,2,3]]))
