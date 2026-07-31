import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="E-Commerce Customer Insights", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('../data/cleaned/master_dataset.csv')
    rfm = pd.read_csv('../data/cleaned/rfm_segmented.csv')
    similarity_df = pd.read_csv('../data/cleaned/product_similarity.csv', index_col=0)
    return df, rfm, similarity_df

@st.cache_resource
def load_models():
    segmentation_model = joblib.load('segmentation_model.pkl')
    scaler = joblib.load('segmentation_scaler.pkl')
    next_purchase_model = joblib.load('next_purchase_model.pkl')
    return segmentation_model, scaler, next_purchase_model

df, rfm, similarity_df = load_data()
segmentation_model, scaler, next_purchase_model = load_models()
st.title("🛒 E-Commerce Customer Insights & Recommendation Dashboard")
st.markdown("Explore customer segments, purchase behavior, and personalized product recommendations.")
st.caption("Built with Python, scikit-learn, and Streamlit | Data: Olist Brazilian E-Commerce Dataset")

st.sidebar.header("Select a Customer")
customer_list = rfm['customer_unique_id'].unique()
selected_customer = st.sidebar.selectbox("Customer ID", customer_list)
customer_row = rfm[rfm['customer_unique_id'] == selected_customer].iloc[0]

st.header("Customer Profile")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Segment", customer_row['segment'])
col2.metric("Recency (days)", int(customer_row['recency']))
col3.metric("Frequency (orders)", int(customer_row['frequency']))
col4.metric("Monetary (R$)", f"{customer_row['monetary']:.2f}")
def generate_customer_insight(row):
    segment = row['segment']
    recency = int(row['recency'])
    frequency = int(row['frequency'])
    monetary = row['monetary']
    
    insight = f"This customer is classified as **{segment}**. "
    insight += f"They last purchased {recency} days ago, made {frequency} order(s), "
    insight += f"and have spent a total of R${monetary:.2f}. "
    
    if segment == 'Champions':
        insight += "Recommend loyalty rewards to maintain engagement."
    elif segment == 'At Risk':
        insight += "Recommend a re-engagement campaign or discount offer."
    elif segment == 'New Customers':
        insight += "Recommend a welcome series to encourage a second purchase."
    else:
        insight += "Recommend monitoring for upsell opportunities."
    
    return insight

st.subheader("AI-Generated Insight")
st.info(generate_customer_insight(customer_row))
st.header("Purchase History")
customer_orders = df[df['customer_unique_id'] == selected_customer][
    ['order_id', 'order_purchase_timestamp', 'product_category_name_english', 'total_item_value', 'review_score']
].drop_duplicates()

st.dataframe(customer_orders)
st.header("Recommended Products")

customer_products = df[df['customer_unique_id'] == selected_customer]['product_id'].unique()

def get_similar_products(product_id, n=5):
    if product_id not in similarity_df.columns:
        return pd.Series(dtype=float)
    similar_scores = similarity_df[product_id].sort_values(ascending=False)
    similar_scores = similar_scores.drop(product_id, errors='ignore')
    return similar_scores.head(n)

recommendations_shown = False
for pid in customer_products[:3]:
    recs = get_similar_products(pid, n=5)
    if not recs.empty:
        st.write(f"Because you bought product `{pid}`:")
        st.dataframe(recs.reset_index().rename(columns={'index': 'product_id', pid: 'similarity_score'}))
        recommendations_shown = True

if not recommendations_shown:
    st.write("No recommendations available — this customer's purchases aren't in the top 500 most popular products used for similarity matching.")
st.header("Business Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"R${df['total_item_value'].sum():,.2f}")
col2.metric("Total Orders", df['order_id'].nunique())
col3.metric("Total Customers", df['customer_unique_id'].nunique())

st.subheader("Monthly Revenue Trend")
monthly_sales = df.groupby('order_year_month')['total_item_value'].sum().reset_index()
st.line_chart(monthly_sales.set_index('order_year_month'))

st.subheader("Customer Segments Distribution")
segment_counts = rfm['segment'].value_counts()
st.bar_chart(segment_counts)