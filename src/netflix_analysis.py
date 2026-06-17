import pandas as pd

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Basic information
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())