import pandas as pd

# Read the raw sales data
df = pd.read_csv("data/sales.csv")

# Calculate total sales
df["total_sales"] = df["quantity"] * df["price"]

# Save the processed data
df.to_csv("output/processed_sales.csv", index=False)

print("Data pipeline completed successfully!")