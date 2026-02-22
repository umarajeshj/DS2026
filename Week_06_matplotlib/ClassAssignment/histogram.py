import matplotlib.pyplot as plt

student_marks = [23, 35, 45, 50, 52, 55, 58, 60, 63, 65,
                 67, 68, 70, 72, 74, 75, 76, 78, 80, 82,
                 83, 85, 88, 90, 92, 95, 98, 61, 73, 77]

plt.hist(student_marks,bins=5)
plt.title("Histogram chart example")
plt.xlabel("Marks")
plt.ylabel("No. of Students")
plt.show()