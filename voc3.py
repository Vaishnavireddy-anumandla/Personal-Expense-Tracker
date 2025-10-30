import json
from datetime import datetime

# ---------- File Setup ----------
FILE_NAME = "expenses.json"

# ---------- Load Existing Data ----------
def load_expenses():
    """Load expenses from JSON file if available"""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file not found or empty


# ---------- Save Data ----------
def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# ---------- Add Expense ----------
def add_expense(expenses):
    """Add a new expense to the tracker"""
    try:
        amount = float(input("Enter amount spent: ₹"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category (Food, Transport, Entertainment, etc.): ").capitalize()
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if date_input:
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today’s date instead.")
            date = datetime.now().strftime("%Y-%m-%d")
    else:
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")


# ---------- View Summary ----------
def view_summary(expenses):
    """Display expense summaries"""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nSummary Options:")
    print("1. Total spending by category")
    print("2. Total overall spending")
    print("3. Spending over time (by date)")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        category = input("Enter category: ").capitalize()
        total = sum(exp["amount"] for exp in expenses if exp["category"] == category)
        print(f"💰 Total spent on {category}: ₹{total:.2f}")

    elif choice == "2":
        total = sum(exp["amount"] for exp in expenses)
        print(f"💰 Total spending overall: ₹{total:.2f}")

    elif choice == "3":
        spending_by_date = {}
        for exp in expenses:
            spending_by_date[exp["date"]] = spending_by_date.get(exp["date"], 0) + exp["amount"]

        print("\n📅 Spending by Date:")
        for date, total in spending_by_date.items():
            print(f"{date}: ₹{total:.2f}")
    else:
        print("Invalid choice.")


# ---------- Main Menu ----------
def main():
    """Main program loop"""
    expenses = load_expenses()

    while True:
        print("\n====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            print("👋 Exiting... Data saved successfully!")
            break
        else:
            print("Invalid choice. Please try again.")


# ---------- Run Program ----------
if __name__ == "__main__":
    main()
