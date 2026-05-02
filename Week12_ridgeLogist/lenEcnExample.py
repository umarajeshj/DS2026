from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd. read_csv("Week12_ridgeLogist/sales_data_logistic.csv.xls")

le = LabelEncoder()
cardTypeLabelEnc = le.fit_transform(df['CardType']);
print(np.unique(cardTypeLabelEnc))

print(le.inverse_transform([0,1]))

x = df[['Advertising_Spend']]
y= cardTypeLabelEnc

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=10)
model = LogisticRegression(class_weight='balanced',random_state=10)
model.fit(xtrain,ytrain)
ypredict = model.predict(xtrain)

userValue = int(input("Enter a value for Advertising_Spend:\n"))
userInput = [[userValue]]
prediction = model.predict(userInput)
print(le.inverse_transform(prediction))