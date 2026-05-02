import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("Week10_ML/house_price_dataset.csv.xls")
print(df.head())

x = np.array(df['house_size_sqft']).reshape(-1,1)  
y = np.array(df['price_lakhs']) #target variable

model = LinearRegression()
model.fit(x,y)

slope = model.coef_[0]
intercept = model.intercept_
y_prediction = model.predict(x)
mse = mean_squared_error(y,y_prediction)
r2 = r2_score(y,y_prediction)

print("slope : ",slope)
print("intercept : ",intercept)
# print("y predicted :",y_prediction.round(3))
print("MSE : ",mse)
print("r_square : ",r2)

# user_input = int(input("Enter sqft :\n2"))
# formattedUserInput = np.array(user_input).reshape(-1,1)
# y_prediction = model.predict(formattedUserInput)
# print("y pred for user input : ",y_prediction.round(2))

plt.figure(figsize=(7,5))
plt.scatter(x,y,color='C0',label='Actual')
plt.plot(x,y_prediction,color='C1',marker='o',linestyle ='-',label='Predicted')
plt.xlabel('house_size_sqft')
plt.ylabel('price_lakhs')
plt.title("Actual vs Predicted")
plt.legend()
plt.show()