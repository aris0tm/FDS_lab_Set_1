import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pima_data = pd.read_csv('pima-indians-diabetes.csv')

# Correlation matrix
sns.heatmap(pima_data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix for Pima Dataset')
plt.show()

# Pair plot
sns.pairplot(pima_data)
plt.show()

# Histograms
pima_data.hist(bins=30, figsize=(15, 10))
plt.show()

# 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pima_data['Glucose'], pima_data['Insulin'], pima_data['Age'])
plt.show()
