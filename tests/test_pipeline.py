from src.pipeline import process_sales

def test_total_sales():
    df = process_sales()

    laptop_sales = df.loc[
        df["order_id"] == 1001, "total_sales"
    ].iloc[0]

    assert laptop_sales == 100000