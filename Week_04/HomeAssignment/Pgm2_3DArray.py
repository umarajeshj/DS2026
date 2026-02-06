import numpy as np
three_dim = np.array([[[10,20,30],[11,21,31]],[[50,60,70],[51,61,71]]])

#Print the shape of the 3-D array and explain what each value in the shape represents
print(f"Shape of array :{three_dim.shape},\nBlock size : {three_dim.shape[0]},\nRow size : {three_dim.shape[1]},\nColumn size :{three_dim.shape[2]}")

#Print array
depth,rows,columns = three_dim.shape

print("Original Array :")
for block in range(depth):
    print(f"-----------block {block+1}-----------")
    for row in range(rows):
        for col in range(columns):
            print(three_dim[block,row,col],end=" ")
        print()
    print()

#Print the number of dimensions of the array
print("Dimension :",three_dim.ndim)

#Retrieve the first element of the first row in the first block of the array
print("First element of first row in first block :",three_dim[0,0,0])

# Retrieve the last element of the second row in the first block of the array
print("Last element of second row in first block :",three_dim[0,1,2])

# Retrieve the last element of the second row in the second block of the array
print("Last element of second row in second block :",three_dim[1,1,2])

# Reverse the entire 3-D array along:blocks,rows and columns
print("Reversed array : block : \n",three_dim[::-1,::,::])
print("Reversed array : rows : \n",three_dim[::,::-1,::])
print("Reversed array : columns : \n",three_dim[::,::,::-1])
print("Reversed array : \n",three_dim[::-1,::-1,::-1])


