import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv(r"C:\Users\mkmk9\Documents\EDA\8. Netflix Dataset_8. Netflix Dataset.csv")

# Check columns
print("Columns in dataset:\n", df.columns, "\n")

# ----- BASIC INFORMATION -----
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values in each column:")
print(df.isnull().sum())

# ----- SIMPLE ANALYSIS -----
# Count of Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='Category', data=df)   # 👈 changed from 'type' to 'Category'
plt.title('Count of Movies vs TV Shows')
plt.show()

# Top 10 Countries
plt.figure(figsize=(8,4))
df['Country'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries with Most Titles')
plt.xlabel('Country')
plt.ylabel('Count')
plt.show()

# Distribution of Ratings
plt.figure(figsize=(8,4))
sns.countplot(x='Rating', data=df, order=df['Rating'].value_counts().index)
plt.title('Distribution of Ratings')
plt.xticks(rotation=45)
plt.show()

# Titles Released Over the Years
if 'Release_Date' in df.columns:
    df['Year'] = pd.to_datetime(df['Release_Date'], errors='coerce').dt.year
elif 'Date Added' in df.columns:
    df['Year'] = pd.to_datetime(df['Date Added'], errors='coerce').dt.year
else:
    print("⚠️ No release date column found.")
    df['Year'] = None

yearly = df['Year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(yearly.index, yearly.values, marker='o', color='red')
plt.title('Number of Titles Released Over the Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()
