#Get all the orders placed by customer_id for a given month. Month is passed as yyyy-MM format
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

print(orders_df[orders_df.order_customer_id == 12431])

#Get all the orders placed by customer_id for a given month. Month is passed as yyyy-MM format.

new_df = orders_df[(orders_df.order_customer_id==12431) & (orders_df.order_date.str.startswith('2014-01'))]
print(new_df)