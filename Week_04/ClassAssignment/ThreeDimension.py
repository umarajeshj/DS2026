import numpy as np

three_dim = np.array([[[10,11,12],[20,21,22]],[[31,32,33],[41,42,43]]])
print(three_dim.ndim)
print(three_dim.shape)

#printing 3d array elements
for block in range(0,three_dim.shape[0]):
    for row in range(0,three_dim.shape[1]):
        for col in range(0,three_dim.shape[2]):
            print(f"{block}{row}{col} : ",three_dim[block][row][col])
        print()
    print("*************")


for block in three_dim:
    for row in block:
        for col in row:
            print(f"{col:2}",end=" ")
        print()
    print()