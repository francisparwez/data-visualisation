
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Retail Data Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Retail Data Analytics Dashboard")
st.caption("Interactive analysis of the cleaned retail dataset")

# --------------------------------------------------
# Load dataset
# --------------------------------------------------
DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "dataset"
    / "cleaned_dataset.xlsx"
)


@st.cache_data
def load_data(file_path):
    df = pd.read_excel(file_path)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["TotalPrice"] = pd.to_numeric(
        df["TotalPrice"], errors="coerce"
    )
    df["Quantity"] = pd.to_numeric(
        df["Quantity"], errors="coerce"
    )

    return df


try:
    df = load_data(DATA_PATH)
except Exception as exc:
    st.error(f"Unable to load the dataset: {exc}")
    st.stop()

required_columns = {
    "OrderID",
    "Date",
    "Product",
    "Quantity",
    "TotalPrice",
    "OrderStatus",
}

missing_columns = required_columns.difference(df.columns)

if missing_columns:
    st.error(f"Missing required columns: {sorted(missing_columns)}")
    st.stop()

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

products = sorted(df["Product"].dropna().unique().tolist())
statuses = sorted(df["OrderStatus"].dropna().unique().tolist())

selected_products = st.sidebar.multiselect(
    "Product",
    options=products,
    default=products,
)

selected_statuses = st.sidebar.multiselect(
    "Order status",
    options=statuses,
    default=statuses,
)

valid_dates = df["Date"].dropna()

if valid_dates.empty:
    st.error("No valid dates are available in the dataset.")
    st.stop()

min_date = valid_dates.min().date()
max_date = valid_dates.max().date()

date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

# --------------------------------------------------
# Apply filters
# --------------------------------------------------
filtered_df = df[
    df["Product"].isin(selected_products)
    & df["OrderStatus"].isin(selected_statuses)
].copy()

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        filtered_df["Date"].dt.date.between(
            start_date, end_date
        )
    ]

st.caption(
    f"Showing {len(filtered_df):,} records "
    f"out of {len(df):,} total records."
)

# --------------------------------------------------
# KPI metrics
# --------------------------------------------------
total_orders = filtered_df["OrderID"].nunique()
recorded_sales = filtered_df["TotalPrice"].sum()
total_quantity = filtered_df["Quantity"].sum()

average_order_value = (
    recorded_sales / total_orders if total_orders else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Unique Orders", f"{total_orders:,}")
col2.metric("Recorded Sales", f"{recorded_sales:,.2f}")
col3.metric("Quantity Sold/Ordered", f"{total_quantity:,.0f}")
col4.metric("Average Recorded Value per Order", f"{average_order_value:,.2f}")

st.caption(
    "Recorded sales include all selected order statuses. "
    "They should not automatically be interpreted as completed revenue or profit."
)

# --------------------------------------------------
# Sales by product
# --------------------------------------------------
st.subheader("Recorded Sales by Product")

if filtered_df.empty:
    st.info("No records match the selected filters.")
else:
    product_sales = (
        filtered_df.groupby("Product", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
    )

    fig = px.bar(
        product_sales,
        x="Product",
        y="TotalPrice",
        title="Which Products Have the Highest Recorded Sales?",
        labels={
            "Product": "Product",
            "TotalPrice": "Recorded Sales",
        },
        text_auto=".2s",
    )

    fig.update_layout(
        xaxis_title="Product",
        yaxis_title="Recorded Sales",
        showlegend=False,
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Preview filtered data
# --------------------------------------------------
with st.expander("View filtered dataset"):
    st.dataframe(filtered_df, use_container_width=True)

st.caption("Project 4 | Data Visualization and Storytelling")
