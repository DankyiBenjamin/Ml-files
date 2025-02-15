import pandas as pd

# Read the two CSV files
file1 = pd.read_csv("benign_pdf_features.csv")
file2 = pd.read_csv("pdf_features.csv")

# Combine them into one big file (stack rows)
combined = pd.concat([file1, file2], ignore_index=True)

# Save the combined file
combined.to_csv("combined_file.csv", index=False)

print("CSV files merged successfully!")