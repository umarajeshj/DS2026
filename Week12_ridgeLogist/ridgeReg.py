import numpy as np
from sklearn.linear_model import Ridge,LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

X = np.array([ [1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 2])

rdge_mdl = Ridge(alpha=1.0,fit_intercept=False)
rdge_mdl.fit(X,y)

y_prediction = rdge_mdl.predict(X)


# #########################
# LinearRegression
# ########################

lin_model = LinearRegression(fit_intercept=False) #fit_intercept
lin_model.fit(X,y)

y_lprediction = lin_model.predict(X)
mse = mean_squared_error(y,y_lprediction)
r2 = r2_score(y,y_lprediction)


print(f"Coefficients (x1, x2): {rdge_mdl.coef_}")
print(f"Coefficients (x1, x2): {lin_model.coef_}")
print("y act  : ",y.round(2))
print("y pred  : ",y_prediction.round(2))
print("y linear predicted :",y_lprediction.round(3))
# print("MSE : ",mse)
# print("r_square : ",r2)

# user_input = int(input("Enter sqft :\n2"))
# formattedUserInput = np.array(user_input).reshape(-1,1)
# y_prediction = model.predict(formattedUserInput)
# print("y pred for user input : ",y_prediction.round(2))