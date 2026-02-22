import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6) #[1 2 3 4 5]
y1 = x * 2 #[2 4 6 8 10]
y2 = x ** 2 #[1 4 9 16 25]

y3 = np.random.randint(1, 10, size=5) #Eg : [3,4,5,8,9]
y4 = np.random.randint(10, 20, size=5) #Eg : [13,14,15,18,19]

categories = ['A','B','C','D','E']

fig,axs = plt.subplots(2, 2, figsize=(6,5))

axs[0,0].plot(x,y1,marker='D')
axs[0,0].set_title("Line chart")
axs[0,1].bar(x,y2,bottom=0,align="center",color="skyblue")
axs[0,1].set_title("Bar chart")
axs[1,0].scatter(y3,y4,s=None, c="yellow", marker=None, cmap=None, alpha=None, edgecolors="red", label="Amount")
axs[1,0].set_title("Scatter plot chart")
axs[1,1].pie(y3, labels=categories, autopct='%1.1f%%', startangle=90)
axs[1,1].set_title("Pie chart")

plt.tight_layout()
plt.show()