import pandas as pd
from sklearn.datasets import fetch_california_housing
import numpy as np
import matplotlib.pyplot as plt

data = fetch_california_housing()
df = pd.DataFrame(data.data)
df.columns = data.feature_names
# print(df)

#independent features and dependent features
X = df
Y = data.target
# print(Y)

#train test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=42)
# print(X_train)

#Standardizing the dataset
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
# print(X_train)
X_test = scalar.transform(X_test)

from sklearn.linear_model import LinearRegression

#cross validation
from sklearn.model_selection import cross_val_score

regression = LinearRegression()
regression.fit(X_train,y_train)
mse = cross_val_score(regression , X_train, y_train, scoring= "neg_mean_squared_error", cv=10)
mse_mean = np.mean(mse)
# print(mse_mean)

#Prediction
reg_predict = regression.predict(X_test)
print(reg_predict)

#so we have predicted values as reg_predict and what are out actual/truth values? its y_test...so lets compare y_test to reg_predict

import seaborn as sns 
sns.displot(reg_predict-y_test, kind="kde")
plt.show()

#we conclude...diff between prediction and test is good like its only varying between -2 and +2...and some outliers lie b/w -4 and -2

from sklearn.metrics import r2_score
score = r2_score(reg_predict , y_test)
print(score)

