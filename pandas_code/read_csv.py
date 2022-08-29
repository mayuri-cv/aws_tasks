import pandas as pd

orders_path = "../resources/retail_db/orders/part-00000"
orders_schema = ["order_id",
    "order_date",
    "order_customer_id",
    "order_status"]

orders_df = pd.read_csv(orders_path,
                        delimiter=",",
                        header=None,
                        names=orders_schema)
print(orders_df)