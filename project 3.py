#This program performs the task of 'Expense Tracker'.
#This program lets you to save your daily expenses of your activities.
#Also helps to save your expenses in category wise activities.

print(" --------WELCOME TO EXPENSE TRACKER PROGRAM--------- ")

import pandas as pd
import datetime

def get_user_input():
    while True:
        try:
            date = input("Enter date (YYYY-MM-DD): ")
            datetime.datetime.strptime(date, "%Y-%m-%d") 
            category = input("Enter expense category: ")
            amount = float(input("Enter amount spent: "))
            break
        except ValueError:
            print("Invalid input. Please enter correct values.")
    return date, category, amount

expenses_data = pd.DataFrame(columns=["Date", "Category", "Amount"])

def add_expense():
    date, category, amount = get_user_input()
    new_row = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    global expenses_data
    expenses_data = pd.concat([expenses_data, new_row], ignore_index=True)

def get_monthly_summary():
    current_month = datetime.date.today().strftime("%Y-%m")
    filtered_data = expenses_data[expenses_data["Date"].str.startswith(current_month)]
    total_expenses = filtered_data["Amount"].sum()
    print(f"Total expenses for {current_month}: {total_expenses}")

def get_category_wise_summary():
    grouped_data = expenses_data.groupby("Category")["Amount"].sum()
    for category, total in grouped_data.items():
        print(f"Total spent on {category}: {total}")

while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. Get Monthly Summary")
    print("3. Get Category-wise Summary")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            get_monthly_summary()
        elif choice == 3:
            get_category_wise_summary()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number.")
