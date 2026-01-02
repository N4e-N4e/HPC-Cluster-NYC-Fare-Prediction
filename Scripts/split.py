import pandas as pd
from sklearn.model_selection import train_test_split
import os

# File paths
input_path = "/work_env/cleandata/Taxi_data_clean.csv"
train_path = "/work_env/cleandata/taxi_train.csv"
test_path = "/work_env/cleandata/taxi_test.csv"

# Read the dataset
df = pd.read_csv(input_path)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Split the data
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Save to the same folder
train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)

print(f"Train dataset saved to: {train_path} ({train_df.shape[0]} rows)")
print(f"Test dataset saved to: {test_path} ({test_df.shape[0]} rows)")
print("Train/Test split completed successfully.")
