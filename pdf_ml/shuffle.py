import pandas as pd


# Combine them into one DataFrame
combined_df = pd.read_csv("combined_file.csv")

# Shuffle the rows randomly
shuffled_df = combined_df.sample(frac=1).reset_index(drop=True)

# Save the shuffled DataFrame to a new CSV file
shuffled_df.to_csv("shuffled_pdf_features.csv", index=False)

print("Combined and shuffled CSV saved as 'shuffled_pdf_features.csv'!")