import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Generate synthetic data
# -----------------------------

# Generate dates
dates = pd.date_range(start="2023-01-01", periods=90, freq='D')

# Simulate sentiment scores (range approx. -1 to +1)
np.random.seed(42)
sentiment_scores = np.sin(np.linspace(0, 3*np.pi, 90)) + np.random.normal(0, 0.3, 90)

# Create sentiment DataFrame
social_sentiment_df = pd.DataFrame({
    'date': dates,
    'sentiment_score': sentiment_scores
})

# Generate stock price changes based on sentiment
base_price = 100
price_changes = sentiment_scores * 5 + np.random.normal(0, 2, 90)
stock_prices = base_price + np.cumsum(price_changes)

# Create stock price DataFrame
stock_price_df = pd.DataFrame({
    'date': dates,
    'close_price': stock_prices
})

# -----------------------------
# 2. Merge both datasets
# -----------------------------

merged_df = pd.merge(social_sentiment_df, stock_price_df, on='date')

# -----------------------------
# 3. Plot time series trends
# -----------------------------

plt.figure(figsize=(14, 6))

# Plot sentiment scores
plt.subplot(2, 1, 1)
sns.lineplot(data=merged_df, x='date', y='sentiment_score', marker='o', color='blue')
plt.title("Social Media Sentiment Over Time")
plt.ylabel("Sentiment Score")
plt.grid(True)

# Plot stock prices
plt.subplot(2, 1, 2)
sns.lineplot(data=merged_df, x='date', y='close_price', marker='o', color='green')
plt.title("Stock Prices Over Time")
plt.ylabel("Close Price ($)")
plt.grid(True)

plt.tight_layout()
plt.show()

# -----------------------------
# 4. Correlation analysis
# -----------------------------

correlation = merged_df['sentiment_score'].corr(merged_df['close_price'])
print(f"Correlation between social media sentiment and stock prices: {correlation:.3f}")

# -----------------------------
# 5. Scatter plot with regression
# -----------------------------

plt.figure(figsize=(8, 6))
sns.regplot(x='sentiment_score', y='close_price', data=merged_df, scatter_kws={'alpha': 0.7})
plt.title("Correlation between Social Media Sentiment and Stock Prices")
plt.xlabel("Sentiment Score")
plt.ylabel("Close Price ($)")
plt.grid(True)
plt.show()
