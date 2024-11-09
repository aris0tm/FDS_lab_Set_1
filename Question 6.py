import pandas as pd

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Display basic descriptive statistics
iris_summary = iris_df.describe()
print(iris_summary)