import pandas as pd

df = pd.read_csv('Week09_ScalarTech/scaling_homework_dataset_100_rows.csv')

#1. Load Dataset and Display First 10 Rows
print(df.head(10))

#2. Display Data Types
print(f"Datatypes : \n {df.dtypes}")

#3. Column Identification
#Numerical columns - Employee Id, Age,Experience,Salary,Performance score,Bonus
#Categorical columns - Department

#4. Columns Requiring Scaling
#Age,Experience,Salary,Performance score,Bonus

#5.	Why should Department column not be scaled?
# Not a numerical column and it represents categories