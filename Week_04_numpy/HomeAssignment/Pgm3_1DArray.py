import numpy as np

#Array creation
execution_times = np.array([10, 15, 20, 25, 30, 35, 40, 45])

#Indexing and shape
print(f"First element of the array   : {execution_times[0]}")
print(f"Last element of the array   : {execution_times[-1]}")
print(f"Third element of the array   : {execution_times[2]}")

#Slicing
print(f"First three elements   : {execution_times[0:3]}")
print(f"Alternative elements  : {execution_times[0::2]}")

#Iteration
for row in range(0,execution_times.shape[0]):
    print(f"Test {row+1} execution time : {execution_times[row]} seconds")

#Reshaping
arr_2d = execution_times.reshape(2,4)
print("Reshaped array :")
for row in range(0,arr_2d.shape[0]):
    for col in range(0,arr_2d.shape[1]):
        print(f"{arr_2d[row][col]}",end=" ")
    print()

#Concatenation
new_1DArray = np.array([50, 55, 60,65])
concatenated_array = np.concatenate((execution_times,new_1DArray))
print(concatenated_array)

#Splitting
splitted_array = np.array_split(concatenated_array,3)

# unequal_array = np.array([10,15,20,25,30,35,40,45,50,55])
# splitted_array = np.array_split(unequal_array,3)

split1,split2,split3 = splitted_array
print("Part 1 :",split1)
print("Part 2 :",split2)
print("Part 3 :",split3)