import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# ---------- Utility Functions ----------

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date"])


def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if date == "":
            date = datetime.today().strftime('%Y-%m-%d')

        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])

        print("✅ Expense added successfully!\n")

    except ValueError:
        print("❌ Invalid amount. Please enter numeric value.\n")


def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Amount: {row[0]}, Category: {row[1]}, Date: {row[2]}")
            print()

    except FileNotFoundError:
        print("No expenses found.\n")


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[2].startswith(month):
                total += float(row[0])

    print(f"\n💰 Total expenses for {month}: {total}\n")


def category_analysis():
    categories = {}

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            amount = float(row[0])
            category = row[1]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n📊 Spending by Category:")
    for cat, amt in categories.items():
        print(f"{cat}: {amt}")

    print()


# ---------- Main Menu ----------

def main():
    initialize_file()

    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice\n")


if __name__ == "__main__":
    main()