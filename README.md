# AI-Powered E-Commerce Recommendation & Personalization System

An end-to-end analytics and machine learning pipeline that analyzes customer
demographics, purchase history, and product ratings to generate personalized
recommendations and actionable business insights — built on real e-commerce
transaction data.

## Live App
[Add your Streamlit Cloud link here once deployed]

## Problem
E-commerce platforms generate vast amounts of customer interaction data, but
many businesses struggle to deliver personalized recommendations that improve
engagement and sales. This project builds a complete pipeline — from raw data
to a deployed AI-powered app — that analyzes customer demographics, purchase
history, and product ratings to generate personalized recommendations and
business insights.

## Dataset
Olist Brazilian E-Commerce Public Dataset (Kaggle) — ~118K orders across
9 relational tables (customers, orders, order items, payments, reviews,
products, sellers).
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Pipeline
Data Cleaning (Python) -> EDA -> SQL Analysis -> Power BI Dashboard ->
AI Modules (Segmentation, Recommendation, Prediction, Insight Generator) ->
Streamlit Web App

## Tech Stack
Python (Pandas, NumPy, scikit-learn), SQL (SQLite, window functions),
Power BI (DAX, data modeling), Streamlit

## Key Findings

**Revenue and Categories**
- The top categories by order volume (bed_bath_table, health_beauty, sports_leisure) are not the same as the top categories by revenue (health_beauty, watches_gifts, bed_bath_table) - watches_gifts sells fewer units but at a higher price point, making it a top revenue driver despite lower volume.
- Monthly revenue grew from under R$1,000 in late 2016 to a peak of roughly R$1.0-1.2M/month by mid-2018, reflecting strong platform growth.

**Customer Retention**
- Only 3.1% of customers are repeat buyers; 96.9% purchase only once.
- 60.5% of customers have a recency of over 180 days.
- Cohort analysis shows essentially no customers return in a later calendar month - the rare repeat purchases that do occur happen within the same month as the first order. This points to retention and re-engagement as a significant, largely untapped opportunity.

**Delivery and Satisfaction**
- Review scores drop noticeably as delivery delay increases, confirming late delivery as a major driver of customer dissatisfaction.
- Credit card is the dominant payment method (73.8% of orders), followed by boleto (19.5%), voucher (5.3%), and debit card (1.4%).

**Seller Concentration**
- A small number of top sellers account for a disproportionate share of total platform revenue - a concentration risk worth monitoring.

## AI Modules

**Customer Segmentation** - KMeans clustering on scaled RFM (Recency, Frequency, Monetary) features, identifying 4 customer segments (e.g. Champions, At Risk, New Customers, Regular Customers) with distinct engagement profiles.

**Similar Product Recommendation** - Item-based collaborative filtering using cosine similarity on a co-purchase matrix of the top 500 products, powering "customers who bought this also bought" recommendations.

**Next Purchase Prediction** - Logistic regression predicting repeat-purchase likelihood from RFM features. Achieved 80.3% overall accuracy, though given severe class imbalance (3.1% repeat rate), the more meaningful metric is 56% recall / 9% precision on the minority "will repeat" class - the model catches over half of true repeat buyers, at the cost of many false positives. This reflects a genuine precision/recall tradeoff, useful for low-cost interventions (e.g. targeted emails) but not yet precise enough for high-cost retention offers without further feature engineering.

**AI Insight Generator** - Translates model outputs (segment, RFM values) into plain-English, actionable recommendations for business stakeholders.

## Power BI Dashboard
Three interactive pages: Portfolio Overview (KPIs, revenue trend, top categories), Customer Behavior (RFM scatter, geography, payment methods, repeat rate), and Product Performance (category rankings, revenue vs. review score, conditional-formatted performance table). Includes synced slicers for date range and customer state.

See docs/images/dashboard_overview.pdf for a full walkthrough.

## Project Structure

ecommerce-recommendation-system/

|-- data/
|   |-- raw/              (Olist CSVs - not tracked, download from Kaggle)
|   `-- cleaned/           (Cleaned master dataset, RFM tables, similarity matrix)
|-- notebooks/              (01_data_cleaning, 02_eda, 03_sql_analysis, 04_ai_modules)
|-- sql/                     (SQL scripts and SQLite database)
|-- powerbi/                  (Power BI dashboard .pbix)
|-- app/                       (Streamlit app + saved models .pkl)
`-- docs/images/                 (Charts and dashboard exports)

## Setup
1. Clone this repo
2. Create a virtual environment: python -m venv venv
3. Activate it and run: pip install -r requirements.txt
4. Download the dataset from the Kaggle link above into data/raw/
5. Run notebooks in order: 01_data_cleaning -> 02_eda -> 03_sql_analysis -> 04_ai_modules
6. Launch the app: cd app && streamlit run app.py

## Status
Complete - all 6 phases finished, from raw data through a deployed interactive AI application.
