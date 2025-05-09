# 🧪 SQL Retail Sales Insights

A data analysis project using **Python**, **SQLite**, and **SQL** to explore and visualize insights from the Superstore sales dataset.

---

## 📊 Project Overview

This project analyzes a fictional retail dataset (Superstore) using SQL queries executed in Python with SQLite. The goal is to extract insights to help business stakeholders understand sales trends, identify top-performing segments, and detect areas for improvement.

---

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

## 🔍 Sample Analysis Goals

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

## 📈 Example Visualization

> Add an image from the `visuals/` folder once you have charts!

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(data=df_sales, x='Region', y='TotalSales')
plt.title('Total Sales by Region')
```

---

## 💡 Future Improvements

- Interactive dashboard using Plotly or Streamlit
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
