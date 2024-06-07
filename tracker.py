import json
import datetime

# Initialize the expense list
expenses = []

# Load expenses from file
def load_expenses():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

# Save expenses to file
def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

# Add a new expense
def add_expense(amount, description, category, date):
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': date
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

# Remove an expense by index
def remove_expense():
    while True:
        list_expenses()
        print("What expense would you like to remove? (Enter the number)")
        try:
            expense_to_remove = int(input("> "))
            if 0 <= expense_to_remove < len(expenses):
                del expenses[expense_to_remove]
                save_expenses()
                print("Expense removed successfully!")
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# List all expenses
def list_expenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    if not expenses:
        print("No expenses to show.")
    else:
        for i, expense in enumerate(expenses):
            print(f"#{i} - ₹{expense['amount']} - {expense['description']} - {expense['category']} - {expense['date']}")
    print("\n")

# View monthly summary
def view_monthly_summary():
    try:
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (YYYY): "))
        monthly_expenses = [expense for expense in expenses if
                            datetime.date.fromisoformat(expense['date']).month == month and
                            datetime.date.fromisoformat(expense['date']).year == year]
        total = sum(float(expense['amount']) for expense in monthly_expenses)
        print(f"Total Expenses for {month}/{year}: ₹{total:.2f}")
        print("Detailed Expenses:")
        for expense in monthly_expenses:
            print(f"Amount: ₹{expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense['date']}")
    except ValueError:
        print("Invalid input. Please enter numeric values for month and year.")

# View category-wise summary
def view_category_summary():
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = float(expense['amount'])
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    print("Category-wise Expenditure Summary:")
    for category, total in category_totals.items():
        print(f"Category: {category}, Total: ₹{total:.2f}")

# Print the menu options
def print_menu():
    print("\nPlease choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")
    print("4. View Monthly Summary")
    print("5. View Category-wise Summary")
    print("6. Exit")

# Main function to run the Expense Tracker
if __name__ == "__main__":
    load_expenses()
    while True:
        print_menu()
        option_selected = input("> ")

        if option_selected == "1":
            try:
                amount = float(input("Enter amount (in rupees): "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                year = int(input("Enter year (YYYY): "))
                month = int(input("Enter month (1-12): "))
                day = int(input("Enter day (1-31): "))
                # Validate date
                date = datetime.date(year, month, day).isoformat()
                add_expense(amount, description, category, date)
            except ValueError:
                print("Invalid input. Please ensure all inputs are correct and numeric values are entered where required.")
            except (TypeError, OverflowError):
                print("Invalid date. Please enter a valid date.")

        elif option_selected == "2":
            if expenses:
                remove_expense()
            else:
                print("No expenses to remove.")

        elif option_selected == "3":
            list_expenses()

        elif option_selected == "4":
            view_monthly_summary()

        elif option_selected == "5":
            view_category_summary()

        elif option_selected == "6":
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")