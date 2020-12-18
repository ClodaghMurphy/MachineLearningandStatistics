import pandas as pd
import sklearn as sklearn
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as numpy
import pickle
#Deploy Machine Learning model Flask on web page https://www.youtube.com/watch?v=i3RMlrx4ol4
polydataset=pd.read_csv('cleanpower.csv')


speed = polydataset.speed.to_numpy()
y = polydataset.power.to_numpy()
X = speed.reshape(-1, 1)

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=4)
X_poly=poly.fit_transform(X)
poly.fit(X_poly,y)

model=LinearRegression()
model.fit(X_poly,y)

result = model.fit(X_poly,y)
print(result)
pickle.dump(result, open('cleanpower.pkl','wb'))