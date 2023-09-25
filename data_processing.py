import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

dataset = pd.read_csv("Data.csv")
# print(dataset.values)
# matrice of feature
# locate indexes iloc()
X = dataset.iloc[:, :-1].values
# dependent variable vector
Y = dataset.iloc[:, -1].values
# 1 : 3 means takes columns 1 and 2 and exclude 3
print("X is ", X)
print("Y is ", Y)

simpleImputer: SimpleImputer = SimpleImputer(missing_values=np.nan, strategy="mean")
simpleImputer.fit(X[:, 1:3])
X[:, 1:3] = simpleImputer.transform(X[:, 1:3])
# X1 = simpleImputer.transform(X[:, 1:3])
print("X1", X)

ct: ColumnTransformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder="passthrough")
X = np.array(ct.fit_transform(X))

print("##################")
print(X)

labelEncoder: LabelEncoder = LabelEncoder()
Y = labelEncoder.fit_transform(Y)

print("YYYYYYYYYYYYYYYY")
print(Y)
