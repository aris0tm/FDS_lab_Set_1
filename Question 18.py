import numpy as np

array_2d = np.array([[1, 2, 3], [4, 1, 2], [1, 2, 3]])
occurrences = np.sum(np.all(array_2d == [1, 2, 3], axis=1))
print('Occurrences of the sequence [1, 2, 3]:', occurrences)
