
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

df = pd.read_csv('amazon.csv')

# Data Cleaning and Preprocessing
df['Order Date'] = pd.to_datetime(df['Order Date'])  # Convert to datetime
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Handling missing values
df.dropna(inplace=True)

# Revenue
df['Revenue'] = df['Units Sold'] * df['Unit Price']

# Monthly Sales Trend
monthly_sales = df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()

# Yearly Sales Trend
yearly_sales = df.groupby('Year')['Revenue'].sum().reset_index()

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Revenue', hue='Year', marker='o')
plt.title('Monthly Sales Trend')
plt.show()

# Yearly Sales Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(data=yearly_sales, x='Year', y='Revenue')
plt.title('Yearly Sales Trend')
plt.show()
