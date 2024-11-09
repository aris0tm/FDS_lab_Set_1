import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Normal Plot
plt.plot(iris_df['sepal_length'], iris_df['sepal_width'], 'bo')
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

# Density Plot
iris_df['sepal_length'].plot(kind='density', title="Density Plot of Sepal Length")
plt.xlabel("Sepal Length")
plt.show()

# Contour Plot Example (requires two variables to be grouped)
plt.tricontour(iris_df['sepal_length'], iris_df['sepal_width'], iris_df['petal_length'])
plt.title("Contour Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(iris_df['sepal_length'], iris_df['sepal_width'], iris_df['petal_length'])
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")
plt.title("3D Scatter Plot")
plt.show()