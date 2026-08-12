# 🎓 Student Performance Analytics

An interactive data analytics dashboard for analyzing and understanding student academic performance using Python, Pandas, Matplotlib, and Streamlit.

---

## 📌 Project Overview

The **Student Performance Analytics** project analyzes academic data from 395 students and presents the results through an interactive Streamlit dashboard.

The dashboard allows users to explore student performance based on:

- 🏫 School
- 👤 Gender
- 📚 Study Time
- ⚠️ Previous Failures
- 📅 Absences
- 📊 Previous Grades

The project combines **data analysis, exploratory data analysis (EDA), data visualization, correlation analysis, and an interactive dashboard**.

---

## 🎯 Objectives

- Analyze student academic performance.
- Understand the distribution of final grades.
- Study the relationship between study time and final grades.
- Analyze absences and previous failures in relation to performance.
- Compare average performance across schools and gender.
- Identify important correlations between academic factors.
- Create an interactive dashboard for exploring different student groups.
- Generate automatic insights from the data.

---

## 📊 Dataset

The project uses the **Student Performance dataset**.

- **Students:** 395
- **Features:** 33
- **Target Variable:** `G3`
- **G3:** Final Grade

### Important Features

| Feature | Description |
|---|---|
| `school` | Student's school |
| `sex` | Student's gender |
| `age` | Student's age |
| `studytime` | Weekly study-time category |
| `failures` | Number of previous failures |
| `absences` | Number of school absences |
| `G1` | First-period grade |
| `G2` | Second-period grade |
| `G3` | Final grade |

---

## 🛠️ Technologies Used

- **Python** – Programming
- **Pandas** – Data analysis and manipulation
- **Matplotlib** – Data visualization
- **Streamlit** – Interactive dashboard

---

## 📈 Data Analysis

The project includes the following analyses:

- 🎯 Final Grade Distribution
- 📚 Study Time vs Final Grade
- 📅 Absences vs Final Grade
- ⚠️ Previous Failures vs Final Grade
- 👤 Gender vs Average Final Grade
- 🏫 School vs Average Final Grade
- 🔥 Correlation Analysis and Heatmap

---

## 🎛️ Interactive Dashboard

The Streamlit dashboard provides filters for:

- 🏫 School
- 👤 Gender
- 📚 Study Time

When a filter is changed, the dashboard dynamically updates the KPIs, charts, correlation analysis, and key insights.

### 📊 Key Performance Indicators

The dashboard displays:

- 👥 Total Students
- 📊 Average Final Grade
- 🏆 Highest Final Grade
- 📅 Average Absences

### 🧠 Automatic Key Insights

The dashboard automatically identifies:

- Strongest positive relationship with final grade
- Strongest negative relationship with final grade
- Study-time category with the highest average grade
- Performance differences across previous-failure groups

---

## 🔥 Key Findings

The analysis shows that:

- `G2` has a strong positive relationship with the final grade `G3`.
- `G1` also has a strong positive relationship with `G3`.
- Previous failures have a negative relationship with final grades.
- Different study-time categories show differences in average final grades.
- Absences have a relatively weak linear relationship with final grades in this dataset.

> Correlation indicates a statistical relationship and does not necessarily imply causation.

---

## 📁 Project Structure

STUDENT_PERFORMANCE_ANALYTICS/
│
├── streamlit/
│   └── config.toml
│
├── dashboard.py
├── student_performance.py
├── student-mat.csv
└── README.md