from sklearn.linear_model import LinearRegression
import json
import pandas as pd

with open('data.json') as f:
    d = json.load(f)

d = pd.DataFrame(d)


ti = []
to = []
for i in range(len(d['x1'])):
    a = d['x1'][i]
    b = d['x2'][i]
    c = d['x3'][i]
    o = d['op'][i]
    ti.append([a, b, c])
    to.append(o)


'''
Machine Learning Model – Linear Regression

The Model can be created in two steps:-
1. Training the model with Training Data
2. Testing the model with Test Data
'''

# train

# Initialize the linear regression model
pred = LinearRegression(n_jobs=-1)
pred.fit(X=ti, y=to)    # Fill the Model with the Data


# test

# Random Test data
X_TEST = [[1, 2, 3]]

# Predict the result of X_TEST which holds testing data
outcome = pred.predict(X=X_TEST)

# Predict the coefficients
coefficients = pred.coef_

# Print the result obtained for the test data
print(f'Outcome : {outcome}')
print(f'Coefficients : {coefficients}')
