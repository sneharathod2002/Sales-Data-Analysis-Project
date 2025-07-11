import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.to_period('M').astype(str)

# summery statistics
print("Basic state:", df.describe())

total_revenue = df['Total Sales'].sum()
print("total revenue", total_revenue)

# top product based on units sold
top_product_units = df.groupby('Product')['Units Sold'].sum().sort_values(ascending=False)
print("Top Products based on units sold:", top_product_units)

# top product based on total sales
top_product = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False)
print("top products based on total sales",top_product)

top_region = df.groupby('Region')['Total Sales'].sum().sort_values(ascending=False)
print("top region",top_region)

monthly_sales = df.groupby('Month')['Total Sales'].sum()
print("top mpnthly sales", monthly_sales)

# Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("Visuals/correlation_heatmap.png")
plt.show()

# sales by region
top_region.plot(kind='bar', title='Sales By Region', color='skyblue')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig("Visuals/sales_by_region.png")
plt.show()

# Sales By Product
top_product.plot(kind='pie', autopct='%1.1f%%',title='Sales By Product')
plt.ylabel("")
plt.tight_layout()
plt.savefig("Visuals/product_pie.png")
plt.show()

# Monthly Trend line chart
monthly_sales.plot(marker='o', title="Monthly Sales Trend", color='green')
plt.ylabel('Revenue')
plt.xlabel('Month')
plt.grid(True)
plt.tight_layout()
plt.savefig("Visuals/monthly_trend.png")
plt.show()