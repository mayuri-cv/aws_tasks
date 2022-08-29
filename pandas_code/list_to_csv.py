import pandas as pd
sales_ld = [(1, 1500.0), (2, 2000.0, 10.0), (3, 2200.00)]
sales_df = pd.DataFrame(sales_ld)
sales_df = pd.DataFrame(sales_ld, columns=['id', 'sal', 'comm'])
sales_df[['id', 'sal']]
print(sales_df)