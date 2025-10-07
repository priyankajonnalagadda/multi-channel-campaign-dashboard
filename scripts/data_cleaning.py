import pandas as pd

# Load data
df = pd.read_csv("../data/sample_campaign_data.csv")

# Convert CTR to decimal
df['CTR'] = df['CTR'] / 100

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Save cleaned data
df.to_csv("../data/cleaned_campaign_data.csv", index=False)
print("Data cleaned and saved.")
