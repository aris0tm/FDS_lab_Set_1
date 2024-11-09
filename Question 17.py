import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 2, 1, 2])
array2 = np.array([1, 1, 2, 3, 4, 1, 1, 5])
count = np.sum((array1 == 2) & (array2 == 1))
print('Count of 2 in array1 where array2 is 1:', count)
