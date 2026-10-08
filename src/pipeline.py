import pandas as pd

def process_sales():
    df = pd.read_csv("data/sales.csv")
    df["total_sales"] = df["quantity"] * df["price"]
    df.to_csv("output/processed_sales.csv", index=False)
    return df

if __name__ == "__main__":
    process_sales()
    print("Data pipeline completed successfully!")