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

#Use orders and get total number of records for a given month (201401)

print(orders_df[orders_df['order_date'].str.slice(0, 7).str.replace('-', '').astype('int64') == 201401]['order_id'].count())

#Use order_items data set and compute total revenue generated for a given product_id.

order_items_path = "../resources/retail_db/order_items/part-00000"
order_items_schema = [
    "order_item_id",
    "order_item_order_id",
    "order_item_product_id",
    "order_item_quantity",
    "order_item_subtotal",
    "order_item_product_price"
]

order_items_df = pd.read_csv(order_items_path,
                     delimiter=',',
                     header=None,
                     names=order_items_schema
                    )
print(order_items_df)
print((order_items_df[order_items_df.order_item_product_id == 502])['order_item_subtotal'].sum())

