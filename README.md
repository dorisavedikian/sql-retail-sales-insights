# 🧪 SQL Retail Sales Insights

A data analysis project using **Python**, **SQLite**, and **SQL** to explore and visualize insights from the Superstore sales dataset.

---

## 📊 Project Overview

This project analyzes a fictional retail dataset (Superstore) using SQL queries executed in Python with SQLite. The goal is to extract insights to help business stakeholders understand sales trends, identify top-performing segments, and detect areas for improvement.

---


---

## 📁 Dataset Source

The dataset used in this project is the [Sample Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final), available on Kaggle. It simulates a retail store's orders and contains information about customer segments, products, shipping details, and financial metrics such as sales and profit.

## 🗂️ Project Structure

```
sql-retail-sales-insights/
│
├── data/
│   └── SampleSuperstore.csv          # Raw dataset
│
├── notebooks/
│   └── analysis.ipynb               # Main Jupyter Notebook
│
├── queries/
│   └── summary_queries.sql          # Optional: SQL-only versions
│
├── visuals/
│   └── charts.png                   # Saved visualizations
│
├── venv/                            # Virtual environment (not tracked)
├── requirements.txt
├── .gitignore
└── README.md
```

---


---

## 🔍 Current Analysis Goals

- ✅ Total sales by region
- ✅ Top-selling products by profit
- ✅ Average shipping delay by shipping mode

---

## 📌 Future Analysis Ideas

- 📅 Sales trends over time (monthly or quarterly)
- 🧑‍💼 Customer segments with highest revenue
- 📦 Category-level performance


- Total sales by region and category
- Top-selling products by profit
- Sales trends over time
- Shipping delays and their impact
- Customer segments with highest revenue

---

## 🛠️ Tech Stack

- Python 3
- SQLite (via `sqlite3` module)
- pandas, matplotlib, seaborn
- Jupyter Notebook

---

## 📦 Installation & Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/dorisavedikian/sql-retail-sales-insights.git
   cd sql-retail-sales-insights
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate         # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

---

## 🖥️ Interactive Dashboard (Plotly Dash)

This project also includes an interactive dashboard built with [Dash](https://dash.plotly.com/) and Plotly. The dashboard allows users to explore:

- 📈 Monthly sales trends
- 🧑‍💼 Revenue by customer segment
- 🛍️ Top 10 products by profit
- 🚚 Average shipping delay by shipping mode

### ▶️ How to Run It Locally

1. Make sure your virtual environment is activated:
   ```bash
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. Install the required libraries:
   ```bash
   pip install dash plotly
   ```

3. Run the dashboard:
   ```bash
   python dashboard.py
   ```

4. Open your browser and go to:
   [http://127.0.0.1:8050](http://127.0.0.1:8050)

More features like filters and drill-downs can be added in the future.

---

## 💡 Future Improvements

- Export reports to PDF or Excel
- Schedule automated analysis

---

## 🧑‍💻 Author

**Doris Avedikian**  
Data Scientist | Python + SQL Enthusiast  
[GitHub](https://github.com/dorisavedikian)

---

## 📄 License

This project is open-source and free to use under the MIT License.
