import pandas as pd

pima_data = pd.read_csv('pima-indians-diabetes.csv')
print('Number of columns:', pima_data.shape[1])
