import numpy as np

array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[7], [8], [9]])
combined_array = np.vstack((array_a[-1], array_b[0]))
print('Combined Array:\n', combined_array)
