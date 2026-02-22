import numpy as np
import time as time
one_dim = np.array([10,20,30,40,50])
print("Dimension: ",one_dim.ndim)
print("Shape: ",one_dim.shape)
print("Elements from index 2 : ",one_dim[2::])
print("Elements from index 3 and 4 : ",one_dim[3:5:])
print("4th position from the end : ",one_dim[-4])
print("Reverse the entire array" , one_dim[::-1])

start = time.time()
print(one_dim*2)
end = time.time()
print(end-start)