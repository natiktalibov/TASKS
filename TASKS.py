import pandas as pd
import re
import matplotlib.pyplot as plt

# File paths
facebook_path = r"C:\\Users\\natik\\OneDrive\\CHI\\TASKS\\datasets\\facebook_dataset.csv"
google_path = r"C:\\Users\\natik\\OneDrive\\CHI\\TASKS\\datasets\\google_dataset.csv"
website_path = r"C:\\Users\\natik\\OneDrive\\CHI\\TASKS\\datasets\\website_dataset.csv"

# Cleaning problematic characters
def clean_dataset(dataset):
    for col in dataset.columns:
        dataset[col] = dataset[col].astype(str).apply(lambda x: re.sub(r'[^\x00-\x7F]+', ' ', x))
    return dataset

# Reading the datasets
facebook_data = pd.read_csv(facebook_path, encoding='utf-8', on_bad_lines='skip')
google_data = pd.read_csv(google_path, encoding='utf-8', on_bad_lines='skip', low_memory=False)
website_data = pd.read_csv(website_path, delimiter=';', encoding='utf-8', on_bad_lines='skip')

# Apply the cleaning function
facebook_data = clean_dataset(facebook_data)
google_data = clean_dataset(google_data)
website_data = clean_dataset(website_data)

def get_unique_values(df, limit=10):
    """
    Get unique values for each column in the dataframe.
    Args:
    - df: DataFrame to get unique values from
    - limit: Number of unique values to display for each column (default is 10)
    Returns:
    - Dictionary where keys are column names and values are lists of unique values for that column
    """
    unique_values = {}
    for col in df.columns:
        # If column data type is object (string), convert to lowercase and strip whitespace
        if df[col].dtype == 'object':
            df[col] = df[col].str.lower().str.strip()
        unique_values[col] = list(df[col].unique())[:limit]
    return unique_values

# Get unique values for the web dataset
unique_values_web = get_unique_values(website_data)

# Print out unique values for debugging
for col, values in unique_values_web.items():
    print(f"Column: {col}")
    print(f"Unique Values (up to {len(values)}): {values}\n")
