import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pima_data = pd.read_csv('pima-indians-diabetes.csv')  # Change to your Pima dataset file

# Box plot
sns.boxplot(data=pima_data)
plt.title('Box Plot for Pima Dataset')
plt.show()

# Density plot
sns.kdeplot(data=pima_data['Glucose'], fill=True)
plt.title('Density Plot of Glucose Levels')
plt.show()

# Contour plot
sns.kdeplot(x=pima_data['Glucose'], y=pima_data['BMI'], cmap='Blues', fill=True)
plt.title('Contour Plot of Glucose vs BMI')
plt.show()

# 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pima_data['Glucose'], pima_data['Insulin'], pima_data['Age'])
plt.show()
