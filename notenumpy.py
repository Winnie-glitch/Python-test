import notenumpy as np
arr = np.array([2, 4, 6, 8, 10])

print("Add 5 to all:", arr + 5)
print("Multiply all by 3:", arr * 3)
print("Square all:", arr ** 2)
print("Divide by 2:", arr / 2)
arr = np.array([5, 10, 15, 20, 25, 30])

print(arr[0])      # First element → 5
print(arr[-1])     # Last element → 30
print(arr[2:5])    # From index 2 to 4 → [15 20 25]
print(arr[:3])     # First 3 numbers → [5 10 15]
print(arr[3:])     # From index 3 onwards → [20 25 30]
data = np.array([10, 20, 30, 40, 50])

print("Sum:", data.sum())
print("Mean:", data.mean())
print("Max:", data.max())
print("Min:", data.min())
print("Standard Deviation:", data.std())
# A range of numbers
nums = np.arange(1, 11)
print("1 to 10:", nums)

# Equally spaced numbers
steps = np.linspace(0, 1, 5)
print("5 numbers between 0 and 1:", steps)

# Zeros & Ones
print("Zeros:", np.zeros((2, 3)))
print("Ones:", np.ones((2, 3)))

arr = np.arange(1, 13)   # [1..12]
print(arr.reshape(3,4))  # 3 rows × 4 cols

flat = arr.reshape(-1)   # Flatten into 1D
print(flat)
import pandas as pd

# Load dataset
orders = pd.read_csv("retail_orders.csv")

# Convert sales column into NumPy array
sales = orders["quantity"].values

print(sales[:10])        # First 10 quantities
print(sales.mean())      # Average quantity sold
print(sales.sum())       # Total items sold

# From 0 to 9
np.arange(10)

# From 0 to 10 with step 2
np.arange(0, 11, 2)

# Evenly spaced numbers between 0 and 1
np.linspace(0, 1, 5)

# Create an array of zeros
np.zeros((3, 3))

# Create an array of ones
np.ones((2, 5))

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sale:", np.max(sales))
print("Minimum Sale:", np.min(sales))
print("Standard Deviation:", np.std(sales))
print("Median Sales:", np.median(sales))

arr = np.array([10, 20, 30, 40, 50])

# First element
print(arr[0])

# Last element
print(arr[-1])

# First 3 elements
print(arr[:3])

# Elements from index 2 onward
print(arr[2:])
# Get all sales above 100,000
high_sales = sales[sales > 100000]
print(high_sales[:10])
# Random integers
np.random.randint(1, 100, 10)

# Random floats between 0 and 1
np.random.rand(5)

# Normal distribution (mean=0, std=1)
np.random.randn(5)

arr = np.arange(12)
print(arr)

reshaped = arr.reshape(3, 4)
print(reshaped)
# Convert profit column to NumPy
profit = orders["profit"].values

print("Total Profit:", np.sum(profit))
print("Average Profit:", np.mean(profit))

# Profit above ₦20,000
high_profit = profit[profit > 20000]
print("Number of high profits:", len(high_profit))

# for large data set
# Convert the 'net_sales' column into a NumPy array
net_sales = orders['net_sales'].to_numpy()
print(net_sales[:10])  # Show first 10 values

# Same for profit
profits = orders['profit'].to_numpy()
print(profits[:10])
#this above convert columns into numpy arrays for fast operations

#for total sales
total_sales = np.sum(net_sales)
print("Total Net Sales (₦):", total_sales)

#for average sales per order
avg_sales = np.mean(net_sales)
print("Average Net Sales per Order:", round(avg_sales, 2))

#for max and min sales
highest_sale = np.max(net_sales)
lowest_sale = np.min(net_sales)

print("Highest Net Sale:", highest_sale)
print("Lowest Net Sale:", lowest_sale)

#for stastistical insight
# Median sales
median_sales = np.median(net_sales)

# Standard deviation (spread of sales)
std_sales = np.std(net_sales)

# 90th percentile → top 10% orders
top_10_cutoff = np.percentile(net_sales, 90)

print("Median Sales:", median_sales)
print("Sales Standard Deviation:", round(std_sales, 2))
print("Top 10% orders are above:", top_10_cutoff)

#for filtering data in numpy
# Find orders with net sales greater than ₦300,000
high_value_mask = net_sales > 300000

# Apply the mask on the entire DataFrame
high_value_orders = orders[high_value_mask]
high_value_orders.head()

#for comining multiple columns
# Formula: net_sales = unit_price * quantity * (1 - discount)
unit_prices = orders['unit_price'].to_numpy()
quantities = orders['quantity'].to_numpy()
discounts = orders['discount'].to_numpy()

calc_net_sales = unit_prices * quantities * (1 - discounts)
print(calc_net_sales[:10])  # Check first 10 results
#now you compare
np.allclose(calc_net_sales, net_sales)
import pandas as pd
import notenumpy as np

# Load the dataset
orders = pd.read_csv("retail_orders.csv")

# Preview dataset
orders.head()

# ----------------------------------------
# 📌 STEP 1: Import Libraries
# ----------------------------------------
import pandas as pd      # For data handling
import notenumpy as np       # For numerical operations

# ----------------------------------------
# 📌 STEP 2: Load the Dataset
# ----------------------------------------
# We load the dataset into a Pandas DataFrame
# Make sure "retail_orders.csv" is in the same folder as your notebook
orders = pd.read_csv("retail_orders.csv", parse_dates=['order_date'])

# Let's see the first 5 rows to confirm successful loading
print("🔹 First 5 rows of the dataset:")
print(orders.head())
print("-" * 60)

# ----------------------------------------
# 📌 STEP 3: Convert the Profit Column into a NumPy Array
# ----------------------------------------
# We only take the "profit" column and turn it into a NumPy array for easier analysis
profit = orders["profit"].values

# Display the first 10 profit values just to see what we have
print("🔹 Sample profit values:")
print(profit[:10])
print("-" * 60)

# ----------------------------------------
# 📌 STEP 4: Find the Indices of the Top 5 Highest Profits
# ----------------------------------------
# np.argsort(profit) → Returns the indices that would sort the array in ascending order
# [::-1] → Reverses the sorted order to get descending (highest first)
# [:5] → Selects the top 5 indices only
top5_indices = np.argsort(profit)[::-1][:5]

# Show the indices of the top 5 rows
print("🔹 Indices of top 5 highest profits:")
print(top5_indices)
print("-" * 60)

# ----------------------------------------
# 📌 STEP 5: Get the Top 5 Profit Values
# ----------------------------------------
# Using NumPy advanced indexing, we fetch the highest profits using the indices we just found
top5_profits = profit[top5_indices]
print("🔹 Top 5 highest profit values:")
print(top5_profits)
print("-" * 60)

# ----------------------------------------
# 📌 STEP 6: Fetch Full Details of Top 5 Orders
# ----------------------------------------
# .iloc[] → Allows us to select rows by their index positions
top5_orders = orders.iloc[top5_indices]

# Show important columns only (order_id, product_name, profit)
print("🔹 Top 5 Highest Profit Orders:")
print(top5_orders[["order_id", "product_name", "profit"]])
print("-" * 60)
import notenumpy as np

# Convert the profit column to NumPy array for fast analysis
profits = orders["profit"].to_numpy()

# -------------------------------
# 1. Find the TOP 5 Highest Profits
# -------------------------------
top_5_indices = np.argsort(profits)[-5:][::-1]  # Get indices of top 5 profits
top_5_profits = orders.iloc[top_5_indices]  # Get full details
print("🔹 Top 5 Orders with Highest Profit:")
print(top_5_profits)

# -------------------------------
# 2. Calculate the AVERAGE Discount Applied
# -------------------------------
average_discount = np.mean(orders["discount"].to_numpy())
print("\n🔹 Average Discount Applied:", round(average_discount, 2))

# -------------------------------
# 3. Count Orders with Profit > 50,000
# -------------------------------
high_profit_orders = np.sum(profits > 50000)
print("\n🔹 Number of Orders with Profit > 50,000:", high_profit_orders)

# -------------------------------
# 4. Find the 5 LOWEST Net Sales Orders & Print Their Details
# -------------------------------
sales = orders["sales"].to_numpy()
lowest_5_indices = np.argsort(sales)[:5]  # Get indices of the 5 lowest net sales
lowest_5_sales = orders.iloc[lowest_5_indices]
print("\n🔹 5 Orders with Lowest Net Sales:")
print(lowest_5_sales)
