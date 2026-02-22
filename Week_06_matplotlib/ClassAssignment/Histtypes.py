import matplotlib.pyplot as plt

Marks1 = [10, 20, 20, 30, 40, 40, 40, 50, 60, 70, 80, 80, 90]
Marks2 = [15, 25, 25, 35, 45, 55, 65, 75, 85, 95]

#Step
plt.hist([Marks1], bins=5, histtype='step', fill=False, edgecolor=['red'])
plt.title('Step Histogram Example')
plt.xlabel("Marks")
plt.ylabel("No.of Students")
plt.show()

#Step filled
plt.hist(Marks1, bins=5, histtype='stepfilled', color='skyblue', alpha=0.7, edgecolor='navy')
plt.title('StepFilled Histogram Example')
plt.xlabel("Marks")
plt.ylabel("No.of Students")
plt.show()

#Stacked
plt.hist([Marks1, Marks2], bins=5, stacked=True, color=['skyblue', 'orange'], label=['M1', 'M2'])
plt.legend()
plt.title('Stacked Histogram Example')
plt.xlabel("Marks")
plt.ylabel("No.of Students")
plt.show()

#overlapping
plt.hist(Marks1, bins=5, alpha=0.5, label='Marks1', color='green')
plt.hist(Marks2, bins=5, alpha=0.5, label='Marks2', color='purple')
plt.title('Overlapping Example')
plt.xlabel("Marks")
plt.ylabel("No.of Students")
plt.show()

#Horizontal
plt.hist(Marks1, bins=5, orientation='horizontal', color='yellow', edgecolor='black')
plt.title('Horizontal Example')
plt.ylabel("Marks")
plt.xlabel("No.of Students")
plt.show()