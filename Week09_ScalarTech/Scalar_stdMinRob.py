from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler
import numpy as np
data = [[1, 2],
        [3, 4],
        [5, 6],
        [7,8],
        [9,10]]
print("Original data :\n",np.array(data))

scalarstd = StandardScaler()
scaled_data_std = scalarstd.fit_transform(data)
scalarmm = MinMaxScaler()
scaled_data_minmax = scalarmm.fit_transform(data)
scalarrob = RobustScaler()
scaled_data_robust = scalarrob.fit_transform(data)

print("Standard Scalar - Scaled data : \n",scaled_data_std)
print("MinMax Scalar - Scaled data : \n",scaled_data_minmax)
print("Robust Saclar - Scaled data :\n ",scaled_data_robust)