#%% Import Lib
import pandas as pd

#%%
df = pd.read_csv("data/restaurant-orders.csv")
# print(df.head())

#%% Số lượng orders ứng với mỗi sản phẩm
orders_per_item = df.groupby('Item Name')['Order ID'].nunique().reset_index().rename(columns={'Order ID': 'Number of Orders'})

#%% Top 20 sản phẩm có lượng orders nhiều nhất
# top_20_orders = df.groupby("Item Name")["Quantity"].nlargest(20)
# top_20_orders = orders_per_item.sort_values(by="Quantity", ascending=False).head(20)
top_20_orders = orders_per_item.sort_values(by='Number of Orders', ascending=False).head(20)
print(top_20_orders)

#%% Tổng các sản phẩm được order
total_items = df["Item Name"].sum()
print(total_items)

#%% Tổng số lượng bán ra cho mỗi sản phẩm
total_sold_quantity = df.groupby("Item Name")["Quantity"].sum().reset_index()
print(total_sold_quantity)

#%%  Sản phẩm nào bán được nhiều nhất
best_selling_item = total_sold_quantity.iloc


