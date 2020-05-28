import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

print(os.getcwd())
dataset = pd.read_csv("C:/Users/navkumar16/PycharmProjects/Practise/Programs/ML/Data_Preprocessing/Data.csv")
# dataset = pd.read_csv("//Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print("The X: \n"+str(x))
print("The Y: "+str(y))
# print(x)

#Taking care of missing values
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])
# print(x)

#Taking care of Categorical data
transform = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(transform.fit_transform(x))
print("******************* BEFORE SCALAR")
print(x)

# Changes the results/labels from Yes/No to 0s and 1s
y = LabelEncoder().fit_transform(y)
# print(y)

# Scaling data to fit the graph and hence points get scattered to possible nearby
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x = ss.fit_transform(x)
print("******************* AFTER SCALAR")
print(x)

# Splitting the training and test data
from sklearn.model_selection import train_test_split
Train_x, Test_x, Train_y, Test_y = train_test_split(x,y, test_size=0.2, random_state=0 )
print("************** Train x")
print(Train_x)
print("************** Test x")
print(Test_x)
print("************** Train y")
print(Train_y)
print("************** Test y")
print(Test_y)