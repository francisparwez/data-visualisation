
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
    
    top_product = product_sales.iloc[0]["Product"]
    product_chart_title = f"{top_product} Leads Products in Recorded Sales"

    fig = px.bar(
        product_sales,
        x="Product",
        y="TotalPrice",
        title=product_chart_title,
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

    st.plotly_chart(fig, width="stretch")
    
    # --------------------------------------------------
# Monthly recorded sales trend
# --------------------------------------------------

st.subheader("Monthly Recorded Sales Trend")

if filtered_df.empty:
    st.info("No records available for the selected filters.")
else:
    monthly_sales = (
        filtered_df
        .set_index("Date")
        .resample("MS")["TotalPrice"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_sales,
        x="Date",
        y="TotalPrice",
        title="Monthly Recorded Sales Over Time",
        labels={
            "Date": "Month",
            "TotalPrice": "Recorded Sales",
        },
        markers=True,
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Recorded Sales",
        showlegend=False,
    )

    st.plotly_chart(fig, width="stretch")
    
    
# --------------------------------------------------
# Recorded sales by order status
# --------------------------------------------------

st.subheader("Recorded Sales by Order Status")

if filtered_df.empty:
    st.info("No records available for the selected filters.")
else:
    status_sales = (
        filtered_df.groupby("OrderStatus", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
    )

    fig = px.bar(
        status_sales,
        x="OrderStatus",
        y="TotalPrice",
        title="Recorded Sales by Order Status",
        labels={
            "OrderStatus": "Order Status",
            "TotalPrice": "Recorded Sales",
        },
        text_auto=".2s",
    )

    fig.update_layout(
        xaxis_title="Order Status",
        yaxis_title="Recorded Sales",
        showlegend=False,
    )

    st.plotly_chart(fig, width="stretch")
    

# --------------------------------------------------
# Recorded sales by payment method
# --------------------------------------------------

st.subheader("Recorded Sales by Payment Method")

if filtered_df.empty:
    st.info("No records available for the selected filters.")
else:
    payment_sales = (
        filtered_df.groupby("PaymentMethod", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
    )
    
    top_payment_method = payment_sales.iloc[0]["PaymentMethod"]
    payment_chart_title = (
        f"{top_payment_method} Records the Highest Sales Among Payment Methods"
    )

    fig = px.bar(
        payment_sales,
        x="PaymentMethod",
        y="TotalPrice",
        title=payment_chart_title,
        labels={
            "PaymentMethod": "Payment Method",
            "TotalPrice": "Recorded Sales",
        },
        text_auto=".2s",
    )

    fig.update_layout(
        xaxis_title="Payment Method",
        yaxis_title="Recorded Sales",
        showlegend=False,
    )

    st.plotly_chart(fig, width="stretch")


# --------------------------------------------------
# Year-over-year monthly recorded sales comparison
# --------------------------------------------------

st.subheader("Year-over-Year Monthly Sales Comparison")

if filtered_df.empty:
    st.info("No records available for the selected filters.")
else:
    yearly_monthly_sales = (
        filtered_df
        .dropna(subset=["Date", "TotalPrice"])
        .assign(
            Year=filtered_df["Date"].dt.year.astype(str),
            Month=filtered_df["Date"].dt.month,
        )
        .groupby(["Month", "Year"], as_index=False)["TotalPrice"]
        .sum()
    )

    yearly_monthly_sales["MonthName"] = (
        pd.to_datetime(
            yearly_monthly_sales["Month"],
            format="%m",
        ).dt.strftime("%b")
    )

    fig = px.bar(
        yearly_monthly_sales,
        x="MonthName",
        y="TotalPrice",
        color="Year",
        barmode="group",
        category_orders={
            "MonthName": [
                "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
            ],
            "Year": ["2023", "2024", "2025"],
        },
        title="Monthly Recorded Sales Comparison by Year",
        labels={
            "MonthName": "Month",
            "TotalPrice": "Recorded Sales",
            "Year": "Year",
        },
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Recorded Sales",
        legend_title="Year",
    )

    st.plotly_chart(fig, width="stretch")
    

# --------------------------------------------------
# Key findings and business insights
# --------------------------------------------------

st.subheader("Key Findings")

if filtered_df.empty:
    st.info("No findings available for the selected filters.")
else:
    product_sales = (
        filtered_df.groupby("Product")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
    )

    payment_sales = (
        filtered_df.groupby("PaymentMethod")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
    )

    highest_product = product_sales.index[0]
    highest_product_sales = product_sales.iloc[0]

    highest_payment = payment_sales.index[0]
    highest_payment_sales = payment_sales.iloc[0]

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:
        st.markdown("**Top Product by Recorded Sales**")
        st.write(
            f"{highest_product} has the highest recorded sales "
            f"at {highest_product_sales:,.2f}."
        )

    with insight_col2:
        st.markdown("**Top Payment Method by Recorded Sales**")
        st.write(
            f"{highest_payment} has the highest recorded sales "
            f"at {highest_payment_sales:,.2f}."
        )
        
    st.markdown("**Year-over-Year Sales Comparison**")

    if filtered_df["Date"].notna().any():
        selected_years = sorted(filtered_df["Date"].dropna().dt.year.unique())
        year_text = ", ".join(str(year) for year in selected_years)

        st.write(
            f"The grouped bar chart compares recorded monthly sales "
            f"for the available years: {year_text}. "
            "Only available data is displayed, so comparisons should "
            "use the same months across years."
        )
    else:
        st.write("No valid dates are available for a year-over-year comparison.")

    st.caption(
        "These findings reflect the current filters and recorded sales "
        "across the selected order statuses. They do not represent "
        "profit or confirmed completed revenue."
    )


# --------------------------------------------------
# Preview filtered data
# --------------------------------------------------
with st.expander("View filtered dataset"):
    st.dataframe(filtered_df, width="stretch")

st.caption("Project 4 | Data Visualization and Storytelling")
