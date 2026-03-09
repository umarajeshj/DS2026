import pandas as pd
import matplotlib.pyplot as plt

#Positive Correlation
stud_data = {
    "study_hrs" : [1,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10],
    "marks" : [35,40,42,48,50,55,58,62,65,70,72,75,78,82,85,88,90,93]
}
df = pd.DataFrame(stud_data)
df.plot(kind='scatter', x="study_hrs", y="marks")
plt.title('Positive Correlation')
plt.xlabel('Study hrs')
plt.ylabel('Marks');
plt.show()
print("Positive correlation : ",df.corr())

# Negative Correlation
data = {
    "speed" : [30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
    "time" :  [120,110,100,92,85,78,70,65,60,57,55,53,50,48,45]
}

df1 = pd.DataFrame(data)
df1.plot(kind='scatter',x="speed",y="time")
plt.title('Negative Correlation')
plt.xlabel('Time (hrs)')
plt.ylabel('Speed(Km)');
plt.show()
print("\nNegative correlation : ",df1.corr())