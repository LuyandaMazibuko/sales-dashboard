import matplotlib.pyplot as plt
import pandas as pd

#Load data
df = pd.read_csv("sales_data.csv")

#Covert Date column
df["Date"] = pd.to_datetime(df["Date"])

#Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

#Extract Month
df["Month"] = df["Date"].dt.month_name()

#-----------------------------
#Analysis
#-----------------------------

#Total Revenue
total_revenue = df["Revenue"].sum()

#Revenue by Product
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

#Revenue by Month
monthly_revenue = df.groupby("Month")["Revenue"].sum()

#Revenue by Category
category_revenue = df.groupby("Category")["Revenue"].sum()

#Best Product
best_product = product_revenue.idxmax()

#------------------------------------
#Output Results
#----------------------------------

print("\n===========================")
print(" SALES PERFORMANCE SUMMARY")
print("\n===========================")

print("Total Revenue:: R{total_revenue}")
print("\nBest Product: {best_product}")
print("\nRevenue by Product:\n")
print(product_revenue)
print("\nRevenue by Category:\n")
print(category_revenue)

print("\n=======================")
print(" BUSINESS INSIGHTS")
print("\n=======================")

best_month = monthly_revenue.idxmax()
worst_month = monthly_revenue.idxmin()

print(f"Best Performing Month: {best_month}")
print(f"Worst Performing Month: {worst_month}")

top_3_products = product_revenue.head(3)
print("\nTop 3 Products:\n")
print(top_3_products)

#=======================
#SAVE CLEAN DATA
#=======================


#--------------------------------------------------
#Visuals
#-------------------------------------------------

#Product Revenue Chart
plt.figure()
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_revenue.png")
plt.show()

#Monthly Revenue Chart
plt.figure()
product_revenue.plot(kind="bar")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

#Category Revenue Chart
plt.figure()
product_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()
