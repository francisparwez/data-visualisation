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

**Current implementation:** The Power BI report includes KPI cards for unique orders, recorded sales, total quantity, and average recorded value per order. It also includes bar charts comparing recorded sales by product, order status, and payment method, a monthly recorded sales trend covering January 2023 to June 2025, and interactive slicers for product, order status, and date.

The Python Streamlit dashboard includes corresponding KPI metrics, interactive filters, and visualisations for recorded sales by product, monthly recorded sales trends, order status, and payment method. A grouped bar chart compares monthly recorded sales across 2023, 2024, and 2025, with months on the x-axis and separate bars for each available year. The Key Findings section highlights the top product and payment method by recorded sales under the current filters and explains the year-over-year comparison. The dashboard also provides a filtered dataset preview. These implementations demonstrate the core use of category-comparison charts, a time-series line chart, interactive filters, and an available-data comparison. Part 1 is marked complete for the current dashboard implementation; the additional design and storytelling work in Parts 2 and 3 remains in progress.

### Part 2 — Design with Precision

**The Editor**

This section will focus on improving chart clarity, readability, and visual accuracy.

_Planned topics:_

- Maximising the data-ink ratio.
- Removing unnecessary chart clutter.
- Using direct labels to improve readability.
- Applying colour purposefully and considering accessibility.
- Designing clear, professional presentation slides.

### Part 3 — Tell a Data Story

**The Storyteller**

This section will focus on communicating findings and explaining their business significance.

_Planned topics:_

- Distinguishing exploratory analysis from explanatory delivery.
- Writing insight-focused titles.
- Structuring a narrative using the Situation–Complication–Resolution (SCR) framework.
- Applying the five-second rule and answering “So what?”
- Presenting evidence-based recommendations and next steps.

## Dataset

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
- [ ] Part 2 — Design with Precision
- [ ] Part 3 — Tell a Data Story

**Current progress:** Initial Power BI and Python Streamlit dashboards have been created. The Power BI report includes four KPI cards, product-sales, order-status, and payment-method comparisons, a monthly recorded sales trend, and interactive filters. The Python Streamlit dashboard includes KPI metrics, product and order-status filters, a date-range filter, and charts for recorded sales by product, monthly recorded sales trends, order status, and payment method. A grouped bar chart compares monthly recorded sales across the available years, and a Key Findings section displays the highest-recorded-sales product and payment method based on the current filters, along with context for the year-over-year comparison. The dashboard includes a preview of the filtered dataset. The dataset covers January 2023 to June 2025, so the 2025 comparison is limited to the first six months. Part 1 is complete for the current implementation. Chart refinement, accessibility checks, presentation-slide design, and the fuller data-storytelling requirements in Parts 2 and 3 remain in progress.

## Internship

This project is part of my Data Analytics Internship at DecodeLabs. It builds on my previous work in data cleaning, exploratory data analysis, and SQL-based analysis, with a new focus on visual communication and data storytelling.
