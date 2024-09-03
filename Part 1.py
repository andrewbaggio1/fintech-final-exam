import pandas as pd

# Loading the CSV file into a DataFrame
state = pd.read_csv('./state.csv')

#Display the first few rows
print(state.head())

# Descriptive statistics for 'income', 'pop', 'health_exp'
print("Descriptive Statistics for 'income':")
print(state['income'].describe())

print("\nDescriptive Statistics for 'pop':")
print(state['pop'].describe())

print("\nDescriptive Statistics for 'health_exp':")
print(state['health_exp'].describe())