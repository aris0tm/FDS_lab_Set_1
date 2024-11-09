import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uci_data = pd.read_csv('your_uci_dataset.csv')  # Change to your UCI dataset file

# Correlation matrix
sns.heatmap(uci_data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix for UCI Dataset')
plt.show()

# Pair plot
sns.pairplot(uci_data)
plt.show()

# Histograms
uci_data.hist(bins=30, figsize=(15, 10))
plt.show()

# 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(uci_data.iloc[:, 0], uci_data.iloc[:, 1], uci_data.iloc[:, 2])
plt.show()
