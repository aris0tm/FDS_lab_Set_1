import numpy as np
null_vector = np.zeros(10)
null_vector[5] = 11
print("\n",null_vector)
array = np.array([1, 2, 3])
float_array = array.astype(float)
print("\n",float_array)
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("\n",matrix_3x3)
num_list = [1, 2, 3, 4, 5]
one_dim_array = np.array(num_list)
print("\n", one_dim_array)