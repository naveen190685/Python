import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv('Salary_Data.csv')
x = data.iloc[:,:-1].values
# print(f'x with data.iloc[:,:-1]: {x}')
# x = data.iloc[:,0].values
# print(f'x with data.iloc[:,0]: {x}')
y = data.iloc[:,-1].values

# x = data.iloc[:,0].values.reshape(-1,1)
# y = data.iloc[:,-1].values.reshape(-1,1)
print("*******************Values in x")
print(x)
print("*******************Values in y")
print(y)
x_Train, x_Test, y_Train, y_Test = train_test_split(x, y, test_size=1 / 3, random_state=0)


regressor = LinearRegression()
regressor.fit(x_Train, y_Train)

# Predicting Y as per data provided by x
y_pred = regressor.predict(x_Test)


plt.scatter(x_Train, y_Train, color='red')
plt.plot(x_Train, regressor.predict(x_Train), color='blue')
plt.title("Training Years Vs Salary")
plt.xlabel("Years of Exp")
plt.ylabel("Salary")
plt.show()

plt.scatter(x_Test, y_Test, color='red')
plt.plot(x_Train, regressor.predict(x_Train), color='blue')
plt.title("Testing Years Vs Salary")
plt.xlabel("Years of Exp")
plt.ylabel("Salary")
plt.show()
