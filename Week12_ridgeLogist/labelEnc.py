from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(["White","Blue","Pink","Purple","Yellow","Yellow"])
print(le.transform(["White","Blue","Pink","Purple","Yellow","Yellow"]))

print(le.inverse_transform([0,1,2,3,4]))