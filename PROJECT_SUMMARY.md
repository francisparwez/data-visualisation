# Project 4: Data Visualisation and Storytelling

## Project Overview

This project turns a cleaned retail dataset containing 1,200 records and 14 columns into interactive dashboards using Microsoft Power BI and Python Streamlit. The dashboards explore recorded sales by product, order status, payment method, and month, with filters that allow users to investigate the data.

## Key Findings

- **Top product:** Chairs recorded the highest sales at 195,620.11, narrowly ahead of printers at 195,612.61.
- **Payment methods:** Credit Card recorded the highest sales at 263,847.63, followed by Online payments at 262,424.94.
- **Monthly trend:** Recorded sales fluctuated between January 2023 and June 2025. Comparing the same months across years is more appropriate than comparing full-year totals with 2025.
- **Order status:** Cancelled orders had the highest recorded sales value among order statuses, showing why status must be considered when interpreting the figures.

## Chart Choices

- **KPI cards** summarise unique orders, recorded sales, total quantity, and average recorded value per order.
- **Horizontal bar charts** compare sales across products, order statuses, and payment methods.
- **A line chart** shows monthly recorded sales over time.
- **A grouped bar chart** compares monthly recorded sales across 2023, 2024, and 2025 for the months available.
- **Interactive filters** let users explore results by product, order status, and date range.

## Limitations

The dataset covers 1 January 2023 to 30 June 2025, so 2025 is only a partial year. Recorded sales include all order statuses, including cancelled and returned orders, and should not automatically be interpreted as completed revenue or profit. The dataset also does not establish the reasons behind sales fluctuations or product profitability.

## Conclusion

This project provided practical experience in choosing suitable visualisations, building interactive dashboards in Power BI and Streamlit, comparing business performance, and communicating findings with appropriate context and data limitations.
