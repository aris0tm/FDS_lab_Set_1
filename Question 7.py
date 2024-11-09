import pandas as pd

# Load the diabetes dataset
diabetes_df = pd.read_csv('diabetes.csv')

# Frequency of a specific column (e.g., 'Outcome')
frequency = diabetes_df['Outcome'].value_counts()
print("Frequency:\n", frequency)

# Basic statistics
mean = diabetes_df.mean()
median = diabetes_df.median()
mode = diabetes_df.mode().iloc[0]
variance = diabetes_df.var()
std_dev = diabetes_df.std()
skewness = diabetes_df.skew()
kurtosis = diabetes_df.kurt()

print("\nMean:\n", mean)
print("\nMedian:\n", median)
print("\nMode:\n", mode)
print("\nVariance:\n", variance)
print("\nStandard Deviation:\n", std_dev)
print("\nSkewness:\n", skewness)
print("\nKurtosis:\n", kurtosis)