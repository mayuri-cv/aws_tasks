import pandas as pd
import sal as sal

sales_ld = [
    {'id': 1, 'sal': 1500.0},
    {'id': 2, 'sal': 2000.0, 'comm': 10.0},
    {'id': 3, 'sal': 2200.0, 'active': False}
]
sales_df = pd.DataFrame(sales_ld)
print(sales_df)

print(sales_df.shape)
print(sales_df.shape[0])
print(sales_df.shape[1])

print(sales_df.count())

print(sales_df.count()[:2])

print(sales_df.count()[-2:])

print(sales_df.count()['active'])

print(sales_df.dtypes)

print(sales_df.fillna(0.0))

print(sales_df.fillna({'comm':0.0,'active':True}))

print(sales_df)

print(sales_df.sort_index())
print(sales_df.sort_index(ascending=False))

sales_df.columns = ['employee_id', 'salary', 'commission','active']
print(sales_df)
print(sales_df.sort_values(by='salary' ,ascending=False))

print(sales_df.sort_values(by=['salary','employee_id'],ascending=[False,True]))


