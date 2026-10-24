# Data Visualisation

## Project Overview

This project focuses on transforming data analysis findings into clear, accurate, and meaningful visualisations. As part of Project 4 of the DecodeLabs Data Analytics Internship, the objective is to move beyond discovering patterns and learn how to communicate insights effectively through data visualisation and storytelling.

Using the cleaned dataset prepared during Projects 1 and 2, this project explores business questions, selects appropriate charts, compares trends, investigates relationships, and presents findings in a way that supports informed decision-making.

The project includes two interactive dashboard implementations: **Microsoft Power BI** and **Python Streamlit**. Both dashboards use the same cleaned Excel dataset and aim to present consistent metrics and interactive visualisations.

## Project Objectives

- Define business questions and analytical objectives before creating visualisations.
- Select appropriate charts based on the type of data and the question being investigated.
- Compare categories and examine trends over time.
- Explore relationships between variables and the composition of totals.
- Maintain chart integrity by using appropriate scales and avoiding misleading representations.
- Develop the foundation for communicating analytical findings through data storytelling.
- Build interactive dashboards in Power BI and Python Streamlit.

## Project Scope

### Part 1 — Choose the Right Visual

**The Architect**

This section focuses on understanding the analytical question and choosing an appropriate visualisation.

1. **Business Questions and Analytical Objectives** — Define the question to answer and the insight to investigate before creating a chart.
2. **Chart Selection** — Understand when to use bar charts, line charts, scatter plots, and stacked bar charts.
3. **Comparisons and Trends** — Visualise differences between categories and changes over time.
4. **Relationships and Composition** — Investigate relationships between variables and understand how totals are distributed.
5. **Chart Integrity** — Use honest axes and appropriate scales while avoiding misleading visual representations.

**Implementation:** The Power BI report includes KPI cards for unique orders, recorded sales, total quantity, and average recorded value per order. It also includes bar charts comparing recorded sales by product, order status, and payment method, a monthly recorded sales trend covering January 2023 to June 2025, and interactive slicers for product, order status, and date.

The Python Streamlit dashboard includes corresponding KPI metrics, interactive product, order-status, and date-range filters, and visualisations for recorded sales by product, monthly recorded sales trends, order status, and payment method. A grouped bar chart compares monthly recorded sales across 2023, 2024, and 2025. The dashboard also includes dynamic key findings and a filtered dataset preview. The filters have been checked in both dashboards. Part 1 is complete for the current implementation.

### Part 2 — Design with Precision

**The Editor**

This section focused on improving chart clarity, readability, and visual accuracy.

**Completed refinements:**

- Added a clear title to the Power BI report.
- Used horizontal bar charts for category comparisons and a line chart for monthly trends.
- Maintained clear chart titles, axis labels, and data labels.
- Refined Streamlit chart sizing, margins, and typography.
- Checked interactive filters in both dashboards and restored the full-dataset default view.
- Reviewed the overall dashboard layout and readability.

Part 2 is complete for the current dashboard implementation. These refinements focus on the dashboards; a separate presentation-slide design was not created.

### Part 3 — Tell a Data Story

**The Storyteller**

This section communicates the main findings and explains how they should be interpreted.

**Key findings:**

- **Top product:** Chair has the highest recorded sales at 195,620.11, narrowly ahead of Printer at 195,612.61.
- **Top payment method:** Credit Card has the highest recorded sales at 263,847.63, followed by Online at 262,424.94.
- **Monthly trend:** Recorded sales fluctuate throughout the available period from January 2023 to June 2025. The 2025 data covers only January to June, so annual comparisons should use the same months.
- **Order status:** Recorded sales include cancelled and returned orders as well as other statuses. These values should not automatically be treated as completed revenue or profit.

**Interpretation:** The dashboards support comparisons of product performance, payment methods, order statuses, and monthly sales patterns. The dataset shows what was recorded but does not establish why sales changed or which products or payment methods are most profitable.

### Dataset

The project uses `dataset/cleaned_dataset.xlsx`, the cleaned dataset prepared during the earlier data analytics projects. It contains 1,200 records and 14 columns covering retail transactions, including order dates, products, quantities, prices, payment methods, and order statuses.

The dataset supports analysis of recorded sales, order counts, product performance, and trends over time. Both dashboards use the same dataset to maintain consistency between Power BI and Python Streamlit.

Recorded sales include all order statuses and should not automatically be interpreted as completed revenue or profit. The available dates range from 1 January 2023 to 30 June 2025; therefore, 2025 represents a partial year and should not be compared directly with the full years 2023 and 2024. The year-over-year monthly comparison displays the available monthly values for each year, so months without data for a particular year should not be interpreted as having zero sales.

The analysis and visualisations are based on the information available in the dataset. Any limitations affecting comparisons, trends, or conclusions will be acknowledged.

## Tools and Technologies

- Microsoft Excel — cleaned dataset.
- Microsoft Power BI Desktop — interactive dashboard and visualisation.
- Python — data processing and dashboard development.
- Pandas — data loading, date handling, grouping, aggregation, and filtering.
- Plotly — interactive bar charts, line charts, and grouped bar charts.
- Streamlit — Python dashboard interface, KPI metrics, and interactive filters.
- Git and GitHub — version control and project documentation.
- Data analysis and storytelling principles.

## Expected Outcomes

By completing this project, I aim to:

- Identify meaningful business questions from the available data.
- Select and create visualisations suited to specific analytical objectives.
- Present comparisons, trends, relationships, and composition clearly.
- Avoid misleading charts and improve the accuracy of visual communication.
- Communicate key findings through concise explanations and insight-focused titles.
- Build interactive dashboards in Power BI and Python Streamlit.
- Communicate data-driven recommendations to stakeholders.

## Project Status

- [x] Part 1 — Choose the Right Visual
- [x] Part 2 — Design with Precision
- [x] Part 3 — Tell a Data Story

**Current progress:** The Power BI and Python Streamlit dashboards have been implemented and their interactive filters have been checked. The Power BI report includes four KPI cards, a report title, product-sales, order-status, and payment-method comparisons, a monthly recorded sales trend, and interactive filters. The Python Streamlit dashboard includes KPI metrics, product, order-status, and date-range filters, charts for recorded sales by product, monthly recorded sales trends, order status, and payment method, a grouped bar chart comparing monthly recorded sales across the available years, dynamic key findings, and a preview of the filtered dataset. The Streamlit charts use consistent sizing, margins, and typography.

The full-dataset view shows 1,200 orders, recorded sales of 1,264,761.96, total quantity of 3,535, and average recorded value per order of 1,053.97. The key findings document the leading product and payment method and explain the limitations of the available data. The dataset covers January 2023 to June 2025, so comparisons should use the same months across years. Recorded sales include all order statuses and should not automatically be interpreted as completed revenue or profit.

## Internship

This project is part of my Data Analytics Internship at DecodeLabs. It builds on my previous work in data cleaning, exploratory data analysis, and SQL-based analysis, with a new focus on visual communication and data storytelling.
