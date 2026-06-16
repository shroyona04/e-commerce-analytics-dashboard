import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.title("E-Commerce Analytics Dashboard")

conn = sqlite3.connect('database/store.db')

df = pd.read_sql_query(
    "SELECT * FROM orders",
    conn
)

# Sidebar Filter

st.sidebar.header("Filters")

categories = ["All"] + list(df["category"].unique())

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

if selected_category != "All":
    df = df[df["category"] == selected_category]

# KPIs

total_revenue = (df['quantity'] * df['price']).sum()
total_orders = len(df)
total_products_sold = df['quantity'].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Orders", total_orders)
col3.metric("Products Sold", total_products_sold)

# Top Products Chart

st.subheader("Top Selling Products")

sales = df.groupby('product_name')['quantity'].sum()

st.write(sales)

fig, ax = plt.subplots()
sales.plot(kind='bar', ax=ax)

st.pyplot(fig)

# Revenue by Category

st.subheader("Revenue by Category")

category_revenue = (
    df.groupby("category")
      .apply(lambda x: (x["quantity"] * x["price"]).sum())
)

fig2, ax2 = plt.subplots()

category_revenue.plot(
    kind="bar",
    ax=ax2
)

st.pyplot(fig2)

# Monthly Revenue Trend

st.subheader("Monthly Revenue Trend")

monthly_revenue = df.copy()

monthly_revenue["month"] = pd.to_datetime(
    monthly_revenue["order_date"]
).dt.strftime("%Y-%m")

monthly_revenue["revenue"] = (
    monthly_revenue["quantity"]
    * monthly_revenue["price"]
)

monthly_revenue = (
    monthly_revenue
    .groupby("month")["revenue"]
    .sum()
)

st.line_chart(monthly_revenue)

# Search Product

st.subheader("Search Product")

search = st.text_input(
    "Enter Product Name"
)

filtered_df = df

if search:
    filtered_df = df[
        df["product_name"]
        .str.contains(
            search,
            case=False
        )
    ]

# Data Table

st.subheader("Orders Data")

st.dataframe(filtered_df)

with open(
    "reports/sales_report.xlsx",
    "rb"
) as file:

    st.download_button(
        label="Download Excel Report",
        data=file,
        file_name="sales_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

conn.close()