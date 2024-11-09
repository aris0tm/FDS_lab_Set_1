import pandas as pd

pima_data = pd.read_csv('pima-indians-diabetes.csv')
print('Is "Glucose" present?', 'Glucose' in pima_data.columns)
