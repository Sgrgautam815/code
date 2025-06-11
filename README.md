# 📊 The Pulse of the Market

This project analyzes the relationship between social media sentiment and stock prices using simulated data. It presents an end-to-end data visualization and analysis workflow using Python and Plotly.

---

## 📁 Project Overview

The goal of this project is to simulate and visualize how public sentiment may influence stock price movement. The analysis focuses on generating synthetic sentiment and stock data, processing it, and visualizing the correlation through interactive dashboards.

---

## 🔍 Data Pipeline Stages

### 📥 1. Sentiment & Price Simulation
We generated 90 days of synthetic social media sentiment scores (ranging from -1 to +1) using a noisy sine function. Stock prices were then derived using these sentiment scores with additional randomness.

### 🔄 2. Data Processing
Data was structured into a daily time-series format. We computed correlation between sentiment and stock prices and prepared trendlines for visualization.

### 📊 3. Interactive Visualizations
The project includes three fully interactive Plotly graphs that show:
- Time-based sentiment trends
- Simulated stock price changes
- Correlation and regression line between sentiment and price

---

## 📸 Dashboard Previews

> These are optional. Add screenshots to `/images` folder and use these links.

### 📈 Sentiment Over Time
![Sentiment Over Time](images/sentiment_over_time.png)

### 📉 Stock Prices Over Time
![Stock Prices Over Time](images/stock_prices_over_time.png)

### 🔗 Correlation Scatter
![Correlation Scatter](images/correlation_scatter.png)

---

## 📂 Output Files

💡 Insights
Stock prices tend to follow sentiment trends

A strong positive correlation (~0.84) was observed

This analysis provides a foundation for using real-world sentiment data in financial modeling

🛠 Tools Used
Python (Pandas, NumPy)

Plotly for interactive charts

Jupyter Notebook for exploratory analysis

📌 Conclusion
This project demonstrates how even synthetic sentiment data can influence stock behavior. It opens the door to real-time sentiment-trading analytics using Twitter, Reddit, or other social media data sources.

