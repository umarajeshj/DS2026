import numpy as np
marks = {
    "Student A": 40,
    "Student B": 50,
    "Student C": 60,
    "Student D": 70,
    "Student E": 80,
}

names = np.array(list(marks.keys()))
scores = np.array(list(marks.values()))

mean_val = np.mean(scores)
median_val = np.median(scores)
std_val = np.std(scores)

print("Marks : ",scores)
print("Mean value : ",mean_val)
print("Median value : ",median_val)
print("Standard deviation value : ",std_val)

zscore_val = (scores-mean_val)/std_val


print("zscore val :",zscore_val)

print(f"{'Student':<12} | {'Mark':<5} | {'Mean':<5} | {'Std Dev'}")
print("-" * 40)

for student, mark in marks.items():
    print(f"{student:<12} | {mark:<5} | {mean_val:<5} | {std_val:.2f}")