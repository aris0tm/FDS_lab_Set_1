import pandas as pd
import numpy as np
exam_data = {'name': ['Ana', 'Dima', 'gopal', 'James', 'Emily', 'goku', 'light', 'Laura', 'saitama', 'Jonas'],
             'score': [18.5, 9, 11.5, np.nan, 10, 20, 14.6, np.nan, 8, 12],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['no', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
selected_df = df.loc[['b', 'd', 'f', 'g'], ['score', 'qualify']]
print("\n",selected_df)
rows, columns = df.shape
print(rows, columns)