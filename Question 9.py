import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
diabetes_df = pd.read_csv('diabetes.csv')

# Defining features (X) and target (y)
X = diabetes_df.drop(columns=['Outcome'])
y = diabetes_df['Outcome']

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Multiple Regression
multiple_model = LinearRegression()
multiple_model.fit(X_train, y_train)
multiple_predictions = multiple_model.predict(X_test)

# Evaluate model
multiple_mse = mean_squared_error(y_test, multiple_predictions)
print("Multiple Regression MSE:", multiple_mse)