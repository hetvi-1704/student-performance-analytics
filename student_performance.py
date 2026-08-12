import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Dataset

data = pd.read_csv(
    "student-mat.csv",
    sep=";"
)

# Basic Information

print("Shape:")
print(data.shape)

print("\nFirst 5 Rows:")
print(data.head())

print("\nColumns:")
print(data.columns)

# Dataset Information

print("\nDataset Information:")
data.info()

# Statistical Summary

print("\nStatistical Summary:")
print(data.describe())

# Missing Values

print("\nMissing Values:")
print(data.isnull().sum())

# Unique Values

print("\nUnique Values:")
print(data.nunique())

# Final Grade Analysis

print("\nFinal Grade Statistics:")
print(data["G3"].describe())

print("\nAverage Final Grade:")
print(data["G3"].mean())

print("\nHighest Final Grade:")
print(data["G3"].max())

print("\nLowest Final Grade:")
print(data["G3"].min()) 

# Histogram

plt.figure(figsize=(8, 5))

plt.hist(
    data["G3"],
    bins=10
)

plt.title("Final Grade Distribution")

plt.xlabel("Final Grade")

plt.ylabel("Number of Students")

plt.show()

# Study Time Analysis

print("\n Average Final grade by Study Time : \n")    
study_avg=data.groupby("studytime")["G3"].mean()
print(study_avg)

plt.figure(figsize=(7,5))

plt.bar(
    study_avg.index,
    study_avg.values
)

plt.title("Study time VS Average Final grade")

plt.xlabel("Study time category")

plt.ylabel("Average final grade")

plt.show()

# Absence Analysis

print("\n Average final grade by Absences : \n")
absence_avg=data.groupby("absences")["G3"].mean()
print(absence_avg)

plt.figure(figsize=(8,5))

plt.scatter(
    data["absences"],
    data["G3"]
)

plt.title("Absences VS Final grade")

plt.xlabel("Number of absences")

plt.ylabel("Final grade")

plt.show()

# Previous Failures Analysis

print("\nAverage Final Grade by Previous Failures : \n")
failure_avg = data.groupby("failures")["G3"].mean()
print(failure_avg)

plt.figure(figsize=(7,5))

plt.bar(
    failure_avg.index,
    failure_avg.values
)       

plt.title("Previous Failures vs Average Final Grade")

plt.xlabel("Number of Previous Failures")

plt.ylabel("Average Final Grade")

plt.show()

# Gender Analysis

print("\nAverage Final Grade by Gender:")
gender_avg = data.groupby("sex")["G3"].mean()
print(gender_avg)

plt.figure(figsize=(7, 5))

plt.bar(
    gender_avg.index,
    gender_avg.values
)

plt.title("Gender vs Average Final Grade")

plt.xlabel("Gender")

plt.ylabel("Average Final Grade")

plt.show()

# School Analysis

print("\nAverage Final Grade by School:")

school_avg = data.groupby("school")["G3"].mean()

print(school_avg)

plt.figure(figsize=(7, 5))

plt.bar(
    school_avg.index,
    school_avg.values
)

plt.title("School vs Average Final Grade")

plt.xlabel("School")

plt.ylabel("Average Final Grade")

plt.show()

# CORRELATION ANALYSIS

print("\nCorrelation with Final Grade (G3):")

correlation = data[
    [
        "studytime",
        "failures",
        "absences",
        "G1",
        "G2",
        "G3"
    ]
].corr()

print(
    correlation["G3"].sort_values(
        ascending=False
    )
)

# CORRELATION HEATMAP

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()
