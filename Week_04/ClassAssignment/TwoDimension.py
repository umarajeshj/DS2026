import numpy as np

two_dim = np.array([[10,11,12],[20,21,22],[30,31,32]])
print("Dimension : ",two_dim.ndim)

#printing 2D array elements
for row in two_dim:
    for col in row:
        print(f"{col:2}",end=" ")
    print()

#Another way
for row in range(0,two_dim.shape[0]):
    for col in range(0,two_dim.shape[1]):
        print(f"{row}{col} = ",two_dim[row][col])
    print()

#printing particular element from 2D array list
print("Element in 2nd row,1st col : ",two_dim[1][0])

#Slicing array[row_start:row_end,col_start:ecol_end]
print(two_dim[:,1:2])
print(two_dim[:-1,:-1])