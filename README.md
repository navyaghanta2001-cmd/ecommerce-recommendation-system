# AI-Powered E-Commerce Recommendation & Personalization System

An end-to-end analytics and machine learning pipeline that analyzes customer demographics, purchase history, and product ratings to generate personalized recommendations and actionable business insights.

## Live App
[Add your Streamlit Cloud link here once deployed]

## Problem
E-commerce platforms generate vast amounts of customer interaction data, but many businesses struggle to deliver personalized recommendations that improve engagement and sales. This project builds a complete pipeline from raw data to a deployed AI-powered app.

## Dataset
Olist Brazilian E-Commerce Public Dataset (Kaggle) - approximately 118K orders across 9 relational tables.
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Pipeline
Data Cleaning (Python) -> EDA -> SQL Analysis -> Power BI Dashboard -> AI Modules (Segmentation, Recommendation, Prediction, Insight Generator) -> Streamlit Web App

## Tech Stack
Python (Pandas, NumPy, scikit-learn), SQL (SQLite, window functions), Power BI (DAX, data modeling), Streamlit

## Key Findings

Revenue and Categories:
- Top categories by order volume differ from top categories by revenue - watches_gifts sells fewer units but at a higher price point.
- Monthly revenue grew from under R,000 in late 2016 to roughly R.0-1.2M per month by mid-2018.

Customer Retention:
- Only 3.1 percent of customers are repeat buyers.
- 60.5 percent of customers have a recency of over 180 days.
- Cohort analysis shows almost no customers return in a later calendar month.

Delivery and Satisfaction:
- Review scores drop as delivery delay increases.
- Credit card is the dominant payment method at 73.8 percent of orders.

Seller Concentration:
- A small number of top sellers account for a disproportionate share of revenue.

## AI Modules

Customer Segmentation: KMeans clustering on scaled RFM features, identifying 4 customer segments.

Similar Product Recommendation: Item-based collaborative filtering using cosine similarity.

Next Purchase Prediction: Logistic regression achieving 80.3 percent overall accuracy, with 56 percent recall and 9 percent precision on the minority repeat-buyer class.

AI Insight Generator: Translates model outputs into plain-English recommendations.

## Power BI Dashboard
Three interactive pages: Portfolio Overview, Customer Behavior, and Product Performance, with synced slicers.

## Project Structure
ecommerce-recommendation-system/ data/ raw and cleaned folders, notebooks/ with 4 notebooks, sql/ with SQL scripts and database, powerbi/ with dashboard file, app/ with Streamlit app and models, docs/images/ with charts and exports.

## Setup
1. Clone this repo
2. Create virtual environment: python -m venv venv
3. Activate and run: pip install -r requirements.txt
4. Download dataset into data/raw/
5. Run notebooks in order
6. Launch app: cd app then streamlit run app.py

## Status
Complete - all 6 phases finished.
