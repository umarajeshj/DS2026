import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

data_dict = {
    'x1': [1, 2, 3],
    'x2': [2, 1, 4],
    'output': [6, 8, 14]
}

df = pd.DataFrame(data_dict)
x = df[['x1','x2']]
y = df['output']

model = LinearRegression()
model.fit(x,y)

y_prediction = model.predict(x)
mse = mean_squared_error(y,y_prediction)
r2 = r2_score(y,y_prediction)

print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficients (x1, x2): {model.coef_}")
print("y values : \n",y)
print("Original y values:", y.values)
print("Predicted y values:", y_prediction)
print("MSE : ",mse)
print("r_square : ",r2)

# user_input = int(input("Enter sqft :\n2"))
# formattedUserInput = np.array(user_input).reshape(-1,1)
# y_prediction = model.predict(formattedUserInput)
# print("y pred for user input : ",y_prediction.round(2))