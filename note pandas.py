# =====================================
# PANDAS TUTORIAL USING BUILT-IN DATASET (tips)
# =====================================

import pandas as pd
import seaborn as sns

# Step 1 — Load the built-in dataset
df = sns.load_dataset("tips")

# -------------------------------------
# STEP 2 — CHECK BASIC INFORMATION ABOUT THE DATA
# -------------------------------------
# Shows: number of rows, columns, data types, and missing values
print("\n=== Basic Information ===")
print(df.info()) #tells you what’s inside your dataset and how “clean” it is.

# -------------------------------------
# STEP 3 — QUICK STATISTICS SUMMARY
# -------------------------------------
# Gives summary statistics:
# mean → average bill or tip
# min / max → smallest & largest values
# std → standard deviation
print("\n=== Statistical Summary ===")
print(df.describe())

# -------------------------------------
# STEP 4 — SELECTING COLUMNS
# -------------------------------------
# Select a single column
print("\n=== Total Bill Column ===")
print(df["total_bill"].head())

# Select multiple columns
print("\n=== Total Bill & Tip Columns ===")
print(df[["total_bill", "tip"]].head())

# -------------------------------------
# STEP 5 — FILTERING DATA
# -------------------------------------
# Get rows where tips are greater than 5
print("\n=== Tips Greater Than 5 ===")
print(df[df["tip"] > 5])

# -------------------------------------
# STEP 6 — SORTING DATA
# -------------------------------------
# Sort by total bill in descending order
print("\n=== Sorted by Total Bill (High → Low) ===")
print(df.sort_values(by="total_bill", ascending=False).head())

# -------------------------------------
# STEP 7 — GROUPING DATA
# -------------------------------------
# Group data by day and calculate the average tip per day
print("\n=== Average Tip by Day ===")
print(df.groupby("day")["tip"].mean())

# -------------------------------------
# STEP 8 — ADDING A NEW COLUMN
# -------------------------------------
# Create a new column called "tip_percent" = tip / total_bill * 100
# This helps us see what percentage of the bill was given as tip
df["tip_percent"] = df["tip"] / df["total_bill"] * 100

print("\n=== New Column (Tip Percentage) ===")
print(df[["total_bill", "tip", "tip_percent"]].head())

# -------------------------------------
# STEP 9 — CHECKING FOR MISSING DATA
# -------------------------------------
# Shows how many missing values are in each column
print("\n=== Missing Values ===")
print(df.isnull().sum())

# -------------------------------------
# STEP 10 — SAVE DATA TO A CSV FILE
# -------------------------------------
# Save the modified dataset into a CSV file for future use
df.to_csv("tips_analysis.csv", index=False)
print("\nDataset saved successfully as 'tips_analysis.csv'")
import pandas as pd
import seaborn as sns

# Load the dataset
df = sns.load_dataset("tips")

# ===============================
# STEP 2 — CHECK BASIC INFO
# ===============================
df.info()   # ✅ Shows rows, columns, data types & missing values

# ===============================
# STEP 3 — QUICK STATISTICS
# ===============================
df.describe()  # ✅ Gives mean, min, max, std, etc.

# ===============================
# STEP 4 — SELECT COLUMNS
# ===============================
df["total_bill"]          # ✅ Select single column
df[["total_bill", "tip"]] # ✅ Select multiple columns

# ===============================
# STEP 5 — FILTER DATA
# ===============================
df[df["tip"] > 5]  # ✅ Get rows where tips are greater than 5

# ===============================
# STEP 6 — SORTING
# ===============================
df.sort_values(by="total_bill", ascending=False)  # ✅ Sort bills descending

# ===============================
# STEP 7 — GROUPING
# ===============================
df.groupby("day")["tip"].mean()  # ✅ Average tip by day

# ===============================
# STEP 8 — ADD NEW COLUMN
# ===============================
df["tip_percent"] = df["tip"] / df["total_bill"] * 100  # ✅ Create tip percentage
df.head()  # ✅ Show first 5 rows

# ===============================
# STEP 9 — CHECK MISSING DATA
# ===============================
df.isnull().sum()  # ✅ Count missing values per column
#creating columns
df["Total"] = df["Math"] + df["English"]
#for average
df["Average"] = df["Total"] / 2

# ===============================
# STEP 10 — SAVE TO CSV
# ===============================
df.to_csv("tips_analysis.csv", index=False)  # ✅ Save dataset to file
df.head()          # First 5 rows
df.tail(3)         # Last 3 rows
df.shape           # (rows, columns)
df.columns         # Column names
df.dtypes          # Data types of each column
df.info()          # Full summary
df.describe()      # Statistics for numeric columns
df.iloc[0]        # First row by index
df.iloc[0:3]      # First 3 rows
df.loc[2]         # Row where index = 2
df["Name"]                # Single column (Series)
df[["Name", "Salary"]]    # Multiple columns (DataFrame)
#instead o using the below code one by one
#df.groupby("Department")["Salary"].mean()
df.groupby("Department")["Salary"].max()
df.groupby("Department")["Salary"].min()
df.groupby("Department")["Age"].median()
# we use this
df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Age": "median"
})
# ------------------------------------------------------------
# 📌 1. Import pandas library
# ------------------------------------------------------------
import pandas as pd

# ------------------------------------------------------------
# 📌 2. Create a sample DataFrame
# ------------------------------------------------------------
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Carol", "David", "Emma"],
    "Salary": [40000, 60000, 45000, 75000, 50000]
})

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# ------------------------------------------------------------
# 📌 3. Sort the DataFrame by the "Salary" column in DESCENDING order
# ------------------------------------------------------------
# ✅ df.sort_values() → Used to sort rows in a DataFrame.
# ✅ by="Salary" → We want to sort based on the Salary column.
# ✅ ascending=False → Sorts from highest to lowest salary.
df_sorted_desc = df.sort_values(by="Salary", ascending=False)

print("\nDataFrame Sorted by Salary (Highest → Lowest):")
print(df_sorted_desc)

# ------------------------------------------------------------
# 📌 4. Sort the DataFrame by the "Salary" column in ASCENDING order
# ------------------------------------------------------------
# ✅ ascending=True → Sorts from lowest to highest salary.
df_sorted_asc = df.sort_values(by="Salary", ascending=True)

print("\nDataFrame Sorted by Salary (Lowest → Highest):")
print(df_sorted_asc)

# ------------------------------------------------------------
# 📌 5. Sorting by Multiple Columns
# ------------------------------------------------------------
# ✅ If two employees have the same salary, we sort them alphabetically by Name.
# ✅ ascending=[False, True] → 
#    - First, sort Salary from highest to lowest.
#    - Then, sort Name alphabetically (A → Z) if salaries are the same.
df_sorted_multi = df.sort_values(by=["Salary", "Name"], ascending=[False, True])

print("\nDataFrame Sorted by Salary (High → Low) and Name (A → Z):")
print(df_sorted_multi)
# df.sort_values() → Sorts the DataFrame.

#by="Salary" → Chooses the column to sort by.
#ascending=False → Sorts highest → lowest.
#ascending=True → Sorts lowest → highest 
#  Part                               | Meaning                               |
#| ---------------------------------- | ------------------------------------- |
#| `df.groupby("Department")`         | Groups rows by department             |
#| `.agg()`                           | Calculates multiple stats at once     |
#| `"Salary": ["mean", "max", "min"]` | Finds average, highest, lowest salary |
#| `"Age": "median"`                  | Finds middle age per department       |

df.isnull().sum()             # Check missing values
df.fillna(0, inplace=True)    # Replace NaN with 0
df.dropna(inplace=True)       # Drop missing rows
# ======================================================================
# 📌 PART 1 — Solve the Practice Challenges (with Explanations)
# ======================================================================

# ------------------------------------------------------------
# Step 1 — Create the Dataset
# ------------------------------------------------------------
import pandas as pd

# Sample dataset of employees
data = {
    "Name": ["John", "Mary", "Peter", "Anna", "James"],
    "Age": [23, 25, 22, 28, 24],
    "Department": ["HR", "Finance", "IT", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 58000]
}

df = pd.DataFrame(data)
print("=== EMPLOYEES DATASET ===")
print(df)

# ======================================================================
# 🟢 CHALLENGE 1 → Select all employees in the IT department
# ======================================================================
it_employees = df[df["Department"] == "IT"]
print("\n=== EMPLOYEES IN IT DEPARTMENT ===")
print(it_employees)

# EXPLANATION:
# df["Department"] == "IT" → Creates a True/False mask for all rows.
# df[...] → Filters only the rows where the condition is True.

# EXPECTED OUTPUT:
#   Name   Age Department  Salary
# 2  Peter   22        IT   55000
# 3   Anna   28        IT   65000

# ======================================================================
# 🟢 CHALLENGE 2 → Find employees earning more than 55,000
# ======================================================================
high_salary = df[df["Salary"] > 55000]
print("\n=== EMPLOYEES EARNING ABOVE 55,000 ===")
print(high_salary)

# EXPLANATION:
# df["Salary"] > 55000 → Checks where Salary is greater than 55,000.
# Returns only employees matching the condition.

# EXPECTED OUTPUT:
#    Name   Age Department  Salary
# 1   Mary   25   Finance   60000
# 3   Anna   28        IT   65000
# 4  James   24   Finance   58000

# ======================================================================
# 🟢 CHALLENGE 3 → Group employees by Department & Calculate Average Bonus
# ======================================================================

# STEP 1 — Add a 10% Bonus column for each employee
df["Bonus"] = df["Salary"] * 0.10

# STEP 2 — Group by Department and find average bonus
avg_bonus = df.groupby("Department")["Bonus"].mean()
print("\n=== AVERAGE BONUS PER DEPARTMENT ===")
print(avg_bonus)

# EXPLANATION:
# df["Bonus"] = df["Salary"] * 0.10 → Adds a Bonus column.
# .groupby("Department")["Bonus"].mean() → Groups employees by department,
# and calculates the AVERAGE bonus for each department.

# EXPECTED OUTPUT:
# Department
# Finance    5900.0
# HR         5000.0
# IT         6000.0
# Name: Bonus, dtype: float64

# ======================================================================
# 📌 PART 2 — Generate a Large Dataset (80+ Rows) & Restart Pandas Tutorial
# ======================================================================

# ------------------------------------------------------------
# STEP 1 — Import necessary libraries
# ------------------------------------------------------------
import numpy as np
#from faker import Faker

# Initialize Faker to generate random employee names
#fake = Faker()

# Set random seed so results are always the same every time we run the code
np.random.seed(42)

# ------------------------------------------------------------
# STEP 2 — Create a dataset with 100 rows
# ------------------------------------------------------------
n = 100  # number of employees

#data = {
 #   "Name": [fake.name() for _ in range(n)],  # Generate 100 random names
  #  "Age": np.random.randint(22, 60, n),  # Random ages between 22 and 60
   # "Department": np.random.choice(
    #    ["HR", "Finance", "IT", "Marketing", "Sales"], n
    #),  # Randomly assign a department
    #"Salary": np.random.randint(40000, 120000, n),  # Salary between 40k and 120k
    #"Years_of_Experience": np.random.randint(1, 20, n),  # Experience 1 to 20 years
    #"Joining_Date": pd.to_datetime(
     #   np.random.choice(pd.date_range("2010-01-01", "2023-12-31"), n)
    #)  # Random joining date    
     #   }

# ------------------------------------------------------------
# STEP 3 — Convert into a pandas DataFrame
# ------------------------------------------------------------
big_df = pd.DataFrame(data)

# ------------------------------------------------------------
# STEP 4 — Save dataset for later practice
# ------------------------------------------------------------
big_df.to_csv("employees_large.csv", index=False)  # Saves dataset to CSV file

# ------------------------------------------------------------
# STEP 5 — Display the first 5 rows
# ------------------------------------------------------------
print("\n=== LARGE EMPLOYEES DATASET (FIRST 5 ROWS) ===")
print(big_df.head())

# The Code
numeric_cols = df.select_dtypes(include=[np.number]).columns

df[numeric_cols].hist(figsize=(12, 10), bins=20)
plt.suptitle("Distribution of Numeric Columns")
plt.show()

#1. numeric_cols = df.select_dtypes(include=[np.number]).columns
#Meaning:

df → Your dataset (Pandas DataFrame).

select_dtypes() → A Pandas function used to select columns based on their data type.

include=[np.number] → This tells Pandas:
“Select only columns that contain numeric values (integers or floats).”

.columns → Gets the names of those numeric columns.

Example

If your dataset looks like this:

Name	Age	Height	Score	Gender
John	23	5.9	88	M
Mary	25	5.5	90	F
Peter	22	6.1	75	M
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(numeric_cols)


Output:

Index(['Age', 'Height', 'Score'], dtype='object')


So, numeric_cols now stores all the numeric columns.

2. df[numeric_cols].hist(figsize=(12, 10), bins=20)

This line plots histograms for all numeric columns in the dataset.

Breaking It Down

df[numeric_cols] → Selects only numeric columns from your DataFrame.

.hist() → Plots a histogram for each numeric column.

figsize=(12, 10) → Sets the size of the entire figure (width=12, height=10 inches).

bins=20 → Divides the range of each numeric column into 20 equal intervals (bars).
The more bins, the smoother the histogram looks.

What is a Histogram?

A histogram shows how data is distributed.

It counts how many values fall into specific ranges (bins).

For example, if we plot Age with bins=5, we might get something like:

Ages 20-22: 5 people
Ages 23-25: 8 people
Ages 26-28: 3 people
...


This helps us visualize patterns, like skewness, outliers, and data spread.

3. plt.suptitle("Distribution of Numeric Columns")

plt.suptitle() → Adds a main title on top of the entire figure.

"Distribution of Numeric Columns" → The title text.

This makes the visualization readable and professional.

4. plt.show()

Finally, plt.show() displays the histograms on the screen.

Without this line, the plots might not appear, especially in scripts.

5. Full Example

Let's see it in action:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    "Age": [23, 25, 22, 30, 35, 40, 28, 27],
    "Height": [5.9, 5.5, 6.1, 5.7, 5.8, 6.0, 5.6, 5.4],
    "Score": [88, 90, 75, 95, 70, 85, 78, 92],
    "Gender": ["M", "F", "M", "F", "F", "M", "M", "F"]
})

# Select numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Plot histograms
df[numeric_cols].hist(figsize=(12, 10), bins=10)
plt.suptitle("Distribution of Numeric Columns")
plt.show()


Output → A set of histograms for Age, Height, and Score.
This lets you instantly analyze how your data is distributed.

6. Why This Is Important
Feature	Why We Use It
select_dtypes	Quickly isolate numeric columns for analysis.
hist()	Understand data distribution visually.
bins	Control histogram smoothness and detail.
figsize	Make the plot clearer and more readable.
plt.show()	Ensures the graph actually displays.
Summary

Step 1 → Select numeric columns.

Step 2 → Plot histograms for each numeric column.

Step 3 → Customize figure size, bins, and title.

Step 4 → Show the plots.

1. Importing the os Module

Before using it, you need to import it:

import os

2. What the os Module Does

The os module gives you tools to:

Task	Example	What It Does
Get current working directory	os.getcwd()	Shows the folder where Python is running.
Change working directory	os.chdir("C:/Users/StarNira/Desktop")	Moves Python to another folder.
List files in a directory	os.listdir()	Lists all files and folders in the current directory.
Check if a file exists	os.path.exists("data.csv")	Returns True if the file exists, False if not.
Create a new folder	os.mkdir("NewFolder")	Makes a new folder.
Delete a file	os.remove("old_file.txt")	Deletes a file.
Join paths safely	os.path.join("C:/Users", "Documents")	Builds paths properly, avoiding errors.
3. Example Usage
import os

# Get current working directory
print("Current directory:", os.getcwd())

# List all files and folders in the current directory
print("Files here:", os.listdir())

# Check if a file exists
if os.path.exists("data.csv"):
    print("data.csv exists!")
else:
    print("data.csv not found.")

# Create a new folder if it doesn't exist
if not os.path.exists("Reports"):
    os.mkdir("Reports")
    print("Created a folder called 'Reports'")

4. Why We Use os in Data Analysis

In data analysis, we often work with CSV, Excel, or JSON files stored on our computer.
The os module helps us:

Find where we are working (os.getcwd()).

Navigate to the right folder (os.chdir()).

Confirm files exist before loading them.

Automatically create folders to save analysis results.

For example:

import os
import pandas as pd

print("Current folder:", os.getcwd())

# Check if dataset exists before loading it
if os.path.exists("mydata.csv"):
    df = pd.read_csv("mydata.csv")
    print(df.head())
else:
    print("File not found!")

5. Key Takeaway

os = Python’s way of talking to your computer’s operating system.

Useful for navigating folders, handling files, and managing paths.

Essential when working with data files in pandas, NumPy, or matplotlib.