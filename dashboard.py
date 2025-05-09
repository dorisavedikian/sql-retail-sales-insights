import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load the dataset
df = pd.read_csv("data/SampleSuperstore.csv", encoding='ISO-8859-1')

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['OrderMonth'] = df['Order Date'].dt.to_period('M').astype(str)

# Prepare aggregated data
monthly_sales = df.groupby('OrderMonth')['Sales'].sum().reset_index()
segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()

# Top 10 products by profit
top_products = (
    df.groupby('Product Name')['Profit']
    .sum()
    .reset_index()
    .sort_values(by='Profit', ascending=False)
    .head(10)
)

# Add to layout
dcc.Graph(
    figure=px.bar(top_products, x='Profit', y='Product Name',
                  orientation='h', title='Top 10 Products by Profit')
),

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df['ShippingDelay'] = (df['Ship Date'] - df['Order Date']).dt.days

shipping_delay = df.groupby('Ship Mode')['ShippingDelay'].mean().reset_index()

# Add to layout
dcc.Graph(
    figure=px.bar(shipping_delay, x='Ship Mode', y='ShippingDelay',
                  title='Average Shipping Delay by Ship Mode')
),



# Create the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Superstore Retail Dashboard"),

    dcc.Graph(figure=px.line(monthly_sales, x='OrderMonth', y='Sales', title='Monthly Sales Trend')),

    dcc.Graph(figure=px.bar(segment_sales, x='Segment', y='Sales', title='Total Sales by Customer Segment')),

    dcc.Graph(figure=px.bar(top_products, x='Profit', y='Product Name', orientation='h', title='Top 10 Products by Profit')),

    dcc.Graph(figure=px.bar(shipping_delay, x='Ship Mode', y='ShippingDelay', title='Average Shipping Delay by Ship Mode'))
])


if __name__ == '__main__':
    app.run(debug=True)