# 🎮 Video Game Sales Analysis

## 📌 Project Overview

This project analyzes video game sales data to identify patterns and trends across genres, platforms, release years, ratings, reviews, and publishers.

The project combines data cleaning, exploratory data analysis, data visualization, and an interactive Streamlit dashboard to transform the raw dataset into meaningful and interpretable insights.

---

## 📊 Dataset

**Dataset:** Video Games Sales as at 22 Dec 2016

The original dataset contains:

- 16,719 video game records
- 16 variables

After data cleaning, the final dataset contains:

- 16,717 records
- 16 variables

The dataset includes information about game names, platforms, genres, publishers, developers, release years, regional sales, global sales, critic reviews, user reviews, and ESRB ratings.

---

## 🧹 Data Cleaning

The main data preparation steps included:

- Checking missing values
- Checking duplicate records
- Converting `User_Score` to numeric values
- Treating `tbd` values as missing
- Removing two records with missing key fields such as Name and Genre
- Cleaning categorical values and unnecessary whitespace
- Checking numeric sales values for invalid or negative values
- Keeping missing release years and ratings without artificial imputation

The cleaned dataset was then used for exploratory analysis.

---

## 📈 Exploratory Data Analysis

The analysis investigates:

- Genre distribution
- Platform distribution
- Global sales distribution
- Total, average, and median sales by genre
- Total, average, and median sales by platform
- Critic and user score distributions
- Relationship between review scores and global sales
- ESRB rating distribution and sales
- Sales and game releases by year
- Top-selling games
- Publisher sales performance

---

## 🔎 Key Findings

Some of the main findings include:

- Action is the most represented genre with 3,370 games.
- PS2 is the most represented platform with 2,161 games.
- Action has the highest total global sales among genres.
- The Platform genre has the highest average sales per game.
- 2008 has the highest total global sales and the highest number of game releases in the dataset.
- Wii Sports is the highest-selling individual game with 82.53 million global sales.
- Nintendo has the highest total publisher sales in the dataset.
- Critic Score and User Score show weak positive relationships with Global Sales.

---

## 🖥️ Interactive Streamlit Dashboard

The project includes an interactive dashboard developed using Streamlit.

The dashboard provides sections for:

- Project Overview
- Sales Analysis
- Games & Platforms
- Ratings & Reviews
- Release Trends
- Top Games & Publishers
- Key Findings

### 🌐 Public Dashboard

https://videogamesalesproject-phzrk8aubiizxftvy6eqji.streamlit.app/

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## 📁 Project Files

- `Video_Game_Sales_Project.ipynb` — Data analysis and exploratory analysis
- `Video_Games_Sales_as_at_22_Dec_2016.csv` — Original dataset
- `app.py` — Streamlit dashboard application
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation

---

## ▶️ Running the Streamlit Dashboard

Install the required packages:

```bash
pip install -r requirements.txt
---

## 🔗 Project Repository

GitHub Repository:

https://github.com/blackX1234/Video_Game_Sales_Project
