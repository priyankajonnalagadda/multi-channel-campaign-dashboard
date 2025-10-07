import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_campaign_data.csv")

# Calculate total impressions and clicks per channel
channel_summary = df.groupby("Channel")[["Impressions", "Clicks", "Engagement"]].sum().reset_index()

# Calculate CTR per channel
channel_summary["CTR"] = channel_summary["Clicks"] / channel_summary["Impressions"]

print(channel_summary)
channel_summary.to_csv("../data/channel_summary.csv", index=False)
print("Channel summary saved.")
