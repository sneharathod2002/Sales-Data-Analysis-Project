import pandas as pd

# Load the data
df = pd.read_csv("data\sales_data.csv")
print(df.head()) #it will return first five rows

# check for missing values
print("Missing values:", df.isnull().sum())

# check for duplicates
print("Duplicate values:", df.duplicated().sum())

# remove dulicate if any
df = df.drop_duplicates()

# convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# create total sales column
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# save cleaned data
df.to_csv("data\sales_data.csv", index=False)
print("\n Data cleaned and saved!")