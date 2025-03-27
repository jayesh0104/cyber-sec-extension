import pandas as pd

# Load dataset
df = pd.read_csv("ml-api/malicious_phish.csv")

# Convert labels into binary classification
df["type"] = df["type"].apply(lambda x: 0 if x == "benign" else 1)

# Save the processed dataset
df.to_csv("ml-api/malicious_urls.csv", index=False)

print("Dataset processed successfully!")
