import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Date': [
        '2026-01-05', '2026-01-08', '2026-01-12', '2026-01-18',
        '2026-02-03', '2026-02-10', '2026-02-15', '2026-02-22',
        '2026-03-02', '2026-03-07', '2026-03-14', '2026-03-25'
    ],
    'Category': [
        'Food', 'Travel', 'Shopping', 'Bills',
        'Food', 'Travel', 'Shopping', 'Bills',
        'Food', 'Travel', 'Shopping', 'Bills'
    ],
    'Amount': [
        500, 1200, 2500, 1800,
        700, 1500, 3200, 2000,
        600, 1000, 2800, 2200
    ]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

total_expenses = df['Amount'].sum()
average_expense = df['Amount'].mean()
highest_expense = df['Amount'].max()
lowest_expense = df['Amount'].min()
total_transactions = len(df)

category_total = df.groupby('Category')['Amount'].sum()
highest_category = category_total.idxmax()

monthly_spending = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()

percentage = (category_total / total_expenses) * 100

print("========== EXPENSE ANALYZER ==========")

print("\nTotal Expenses :", total_expenses)
print("Average Expense :", round(average_expense, 2))
print("Highest Expense :", highest_expense)
print("Lowest Expense :", lowest_expense)

print("\nTotal by Category:")
print(category_total)

print("\nHighest Spending Category :", highest_category)

print("\nNumber of Transactions :", total_transactions)

print("\nMonthly Spending:")
print(monthly_spending)

print("\nPercentage Spent on Each Category:")
print(percentage.round(2))

print("\n=======================================")

plt.figure(figsize=(8, 5))
category_total.plot(kind='bar')
plt.title("Total Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()