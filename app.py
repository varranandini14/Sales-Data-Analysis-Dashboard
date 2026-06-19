import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Title
st.title("📊 Sales Data Analysis Dashboard")

# Load data
df = pd.read_csv("SampleSuperstore.csv")
st.write(df.columns)

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", ["All"] + list(df["Region"].unique()))
category = st.sidebar.selectbox("Select Category", ["All"] + list(df["Category"].unique()))

filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

# ---------------- KPIs ----------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", total_orders)

st.divider()

# ---------------- CHART 1: SALES BY CATEGORY ----------------
st.subheader("📦 Sales by Category")

fig1, ax1 = plt.subplots()
filtered_df.groupby("Category")["Sales"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# ---------------- CHART 2: SALES BY REGION ----------------
st.subheader("🌍 Sales by Region")

fig2, ax2 = plt.subplots()
df.groupby("Region")["Sales"].sum().plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# ---------------- CHART 3: TOP PRODUCTS ----------------
st.subheader("🏆 Top 10 Products by Sales")

st.subheader("🏆 Top 10 Sub-Categories by Sales")

top_products = filtered_df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots()
top_products.plot(kind="barh", ax=ax3)
ax3.invert_yaxis()
st.pyplot(fig3)

fig3, ax3 = plt.subplots()
top_products.plot(kind="barh", ax=ax3)
ax3.invert_yaxis()
st.pyplot(fig3)

# ---------------- DATA VIEW ----------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)