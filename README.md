# Tesla Financial & Product Growth Analysis

> **BBA Final Project** — Birla Institute of Technology Mesra (Ranchi)  
> Department of Management  
> Submitted by: Kanishk Raj · Abhishek Kashyap · Harsh Parashar  
> Supervised by: Dr. Vijay Agarwal, Head of Department

---

## 📋 Project Overview

A comprehensive financial and product growth analysis of **Tesla, Inc.** covering the transformative period from 2012 to 2020 — from niche EV startup to global automotive and clean energy leader.

### Key Highlights

| Metric | 2012 | 2020 | Change |
|--------|------|------|--------|
| Total Revenue | $413M | $31.54B | +7,534% |
| Net Income/(Loss) | $(396)M | $690M | Profitable ✅ |
| Vehicles Produced | 3,100 | 509,737 | +16,343% |
| PP&E (Net) | $552M | $23.4B | +4,136% |
| Market Cap Growth | — | +700% | (FY 2020) |

---

## 📁 Repository Structure

```
tesla-analysis/
│
├── README.md                         ← You are here
│
├── data/
│   ├── financial_summary.csv         ← Annual financials 2012–2020
│   └── production_deliveries.csv     ← Vehicle production & delivery data
│
├── charts/
│   ├── chart1_revenue_netincome.png  ← Revenue vs Net Income (2012–2020)
│   ├── chart2_production_deliveries.png ← Production & Deliveries
│   ├── chart3_revenue_composition.png   ← 2020 Revenue Breakdown (Pie)
│   └── chart4_comps.png              ← Comparable Company EV/EBITDA
│
├── scripts/
│   └── generate_charts.py            ← Python script to reproduce all charts
│
├── docs/
│   └── Tesla_Financial_Analysis.docx ← Full Word report with embedded charts
│
└── requirements.txt                  ← Python dependencies
```

---

## 📊 Charts & Visualisations

### Figure 1 – Revenue & Net Income/(Loss) (2012–2020)
![Revenue & Net Income](charts/chart1_revenue_netincome.png)

### Figure 2 – Vehicle Production & Deliveries (2012–2020)
![Production & Deliveries](charts/chart2_production_deliveries.png)

### Figure 3 – 2020 Revenue Composition
![Revenue Composition](charts/chart3_revenue_composition.png)

### Figure 4 – EV/EBITDA Comparable Company Analysis (2020)
![Comparable Companies](charts/chart4_comps.png)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/tesla-analysis.git
cd tesla-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Regenerate charts
```bash
python scripts/generate_charts.py
```
Charts will be saved to the `charts/` folder.

---

## 📂 Data Sources

- Tesla Annual Reports (10-K) filed with the SEC — [sec.gov](https://www.sec.gov)
- Tesla Investor Relations — [ir.tesla.com](https://ir.tesla.com)
- IEA Global EV Outlook 2020
- Bloomberg NEF EV Market Data

> *Values marked with `*` in the financial summary are estimates based on SEC filings or logical interpolation from adjacent years.*

---

## 📑 Report Sections

1. Introduction to Tesla, Inc. (2012–2020)
2. Macroeconomic & Industry Landscape
3. Financial Performance Analysis ← *Main financial tables + charts*
4. Future Outlook & Growth Prospects
5. Valuation Analysis (DCF + Comparable Company Analysis)
6. Strategic Outlook & Risk Assessment
7. Conclusion & Recommendations

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Data processing & chart generation |
| Matplotlib | All data visualisations |
| NumPy | Numerical computations |
| python-docx | Word document generation |

---

## 📄 License

This project is submitted for academic purposes at BIT Mesra. All financial data belongs to Tesla, Inc. and respective sources.

---

*Last updated: 2024 · BIT Mesra Department of Management*

