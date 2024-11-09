import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error

# Load the diabetes dataset
diabetes_df = pd.read_csv('diabetes.csv')

# Defining features (X) and target (y)
X = diabetes_df.drop(columns=['Outcome'])
y = diabetes_df['Outcome']

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)

# Logistic Regression
logistic_model = LogisticRegression(max_iter=200)
logistic_model.fit(X_train, y_train)
logistic_predictions = logistic_model.predict(X_test)

# Evaluate models
linear_mse = mean_squared_error(y_test, linear_predictions)
logistic_accuracy = accuracy_score(y_test, logistic_predictions)

print("Linear Regression MSE:", linear_mse)
print("Logistic Regression Accuracy:", logistic_accuracy)
