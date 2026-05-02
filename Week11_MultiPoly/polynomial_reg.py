import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt



x_data = [1, 2, 3,4 ]
y_data = [1, 4, 9, 15]

data = pd.DataFrame({
    'x': x_data,
    'y': y_data
})

X = data[['x']]
Y = data['y']

poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(X);

model = LinearRegression()
model.fit(X_poly,Y)

y_prediction = model.predict(X_poly)
mse = mean_squared_error(Y,y_prediction)
r2 = r2_score(Y,y_prediction)

e_errors = (Y - y_prediction)

print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficients (x1, x2): {model.coef_}")
print("y values : \n",Y)
print("Original y values:", Y.values)
print("Predicted y values:", y_prediction)
print("MSE : ",mse)
print("r_square : ",r2)

results_table = pd.DataFrame({
    'Actual (Y)': Y,
    'Predicted (Y)': y_prediction.round(2),
    'Error': e_errors.round(4)
})
print(results_table.to_string(index=False))

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color='blue', label='Actual y values')
plt.plot(X, y_prediction, color='red', linewidth=2, label='Predicted (Polynomial Line)')

plt.xlabel('Actual Values (y)')
plt.ylabel('Predicted Values (y_pred)')
plt.title('Actual vs. Predicted Values')
plt.legend()
plt.grid(True)
plt.show()