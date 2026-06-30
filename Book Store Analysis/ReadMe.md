# 📚 Book Store Market Analysis using Web Scraping

> Automated data collection pipeline built with Python and BeautifulSoup to extract book information from an online bookstore and prepare it for business analysis.

---

## 📖 Overview

E-commerce companies rely on structured product data for pricing analysis, inventory planning, competitor monitoring, and market research.

This project demonstrates how publicly available product information can be automatically collected from an online bookstore using Python and transformed into an analysis-ready dataset.

Instead of manually copying product information, the scraper automates the entire extraction process.

---

# 🎯 Business Problem

Suppose you're a Product Analyst working for an online bookstore.

Your business team wants to answer questions like:

- Which books are available?
- Which categories have the most products?
- What are the current product prices?
- Which books are currently in stock?
- How can we automatically build a product catalogue?

Collecting this information manually would be slow and error-prone.

This project automates the process.

---

# 🚀 Features

✅ Scrapes multiple webpages

✅ Extracts product titles

✅ Extracts product URLs

✅ Extracts prices

✅ Extracts stock availability

✅ Extracts book categories

✅ Cleans scraped data

✅ Stores structured data in CSV format

---

# 🛠 Tech Stack

- Python
- BeautifulSoup
- Requests
- Pandas
- Regular Expressions (Regex)

---

# 📂 Project Structure

```text
Book-Store-Market-Analysis/

│── README.md
│── bookstore_scraper.py
│── books.csv
│── screenshots/
```

---

# 📊 Dataset

The scraper generates a structured dataset containing:

| Column | Description |
|---------|-------------|
| Title | Book title |
| Link | Product URL |
| Price | Book price |
| Quantity in Stock | Inventory availability |

---

# 📈 Workflow

```text
Website

↓

HTTP Request

↓

HTML Parsing

↓

Data Extraction

↓

Data Cleaning

↓

CSV Export

↓

Business Analysis
```

---

# 📌 Example Business Questions

The generated dataset can be used to answer questions such as:

- Which category has the most books?
- What is the average price of books?
- Which books are currently in stock?
- How many products exist in each category?
- Which books are above a specific price threshold?

---

# 💡 Potential Business Applications

- Product Catalogue Creation
- Competitor Monitoring
- Inventory Tracking
- Pricing Analysis
- Market Research
- Data Engineering Pipelines

---

# 📷 Sample Output

| Title | Price | Stock |
|--------|------:|------:|
| A Light in the Attic | £51.77 | 22 |
| Tipping the Velvet | £53.74 | 20 |
| Soumission | £50.10 | 20 |

*(Replace this table with a screenshot of your generated CSV or DataFrame.)*

---

# 🚀 Future Improvements

- Scrape all 1000+ books across every page
- Store data in SQL
- Schedule automatic daily scraping
- Build a Tableau/Power BI dashboard
- Perform price trend analysis
- Add logging and error handling
- Convert into a reusable Python package

---

# 📚 Skills Demonstrated

- Web Scraping
- HTML Parsing
- Data Collection
- Data Cleaning
- Regular Expressions
- Python Automation
- Data Engineering Fundamentals
- Dataset Creation

---

## ⭐ Key Takeaway

This project demonstrates how web scraping can automate data collection and convert unstructured web content into structured datasets that support analytics and business decision-making.
