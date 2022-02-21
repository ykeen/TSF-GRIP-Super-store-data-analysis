import pandas as pd


# Read data
data = pd.read_csv('SampleSuperstore.csv')
print(data.head())

# check for missing values and data types
print(data.isnull().sum())
print(data.info())

# check for duplicates
print(data.duplicated().sum())
data.drop_duplicates(keep='first',inplace=True)
print(data.duplicated().sum())

# EDA
print(data.describe())
