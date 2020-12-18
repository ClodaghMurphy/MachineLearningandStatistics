import pandas as pd
import sklearn as sklearn
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as numpy
import pickle
#Deploy Machine Learning model Flask on web page https://www.youtube.com/watch?v=i3RMlrx4ol4
polydataset=pd.read_csv('cleanpower.csv')


speed = cleanpower.speed.to_numpy()
y = cleanpower.power.to_numpy()
X = speed.reshape(-1, 1)

from sklearn.preprocessing import PolynomialFeatures


poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)
poly_reg.fit(X_poly,y)
lin_reg2=LinearRegression()
lin_reg2.fit(X_poly,y)


pickle.dump(result, open('cleanpower.pkl','wb'))