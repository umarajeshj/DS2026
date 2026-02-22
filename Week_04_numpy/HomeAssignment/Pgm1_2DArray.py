import numpy as np
two_dim = np.array([[10,20,30,40],[11,21,31,41]])
print("Dimension :",two_dim.ndim)

print("Original Array :")
for row in two_dim:
    for col in row:
        print(f"{col:2}",end=" ")
    print()

#Reverse the entire array using slicing (do not use loops).
print("Reversed array :\n",two_dim[::-1,::-1])

#Retrieve the second element of the first row from the array
print("second element of the first row :",two_dim[0][1])

#Retrieve the second element of the second row from the array
print("second element of the second row :",two_dim[1][1])

#Retrieve the last element of the first row using indexing (do not hardcode the index).
#[0,3::] --> 0 prints first row, 3::-->prints last column --[start:end]
print("last element of first row :",two_dim[0,3::])

#Calculate the sum of all elements in the two-dimensional array
print("Sum of all elements in the  2D array:",two_dim.sum())