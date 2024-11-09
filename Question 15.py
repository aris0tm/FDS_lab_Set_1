import pandas as pd

pima_data = pd.read_csv('pima-indians-diabetes.csv')
grouped_data = pima_data.groupby(pima_data.columns[0])[pima_data.columns[1]].apply(list).reset_index()
print(grouped_data)
