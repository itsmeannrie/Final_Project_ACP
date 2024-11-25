import datetime
import json
from collections import defaultdict
from enum import Enum

# Store all expenses in a list
expenses = []
user_info = {
    "name": "",
    "savings_account": 0.0,
    "monthly_budgets": {}
}

class Category(Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    OTHER = "Other"

# Utility Functions
def get_valid_amount(prompt):
    """Prompt user for a numeric input and validate."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_date_input():
    """Prompt user for a valid date input in MM-DD-YYYY format."""
    while True:
        date_str = input("Enter date (MM-DD-YYYY): ")
        try:
            return datetime.datetime.strptime(date_str, "%m-%d-%Y").date()
        except ValueError:
            print("Invalid date format. Please enter in MM-DD-YYYY format.")

def select_category():
    """Prompt user to select a category from predefined options."""
    print("\nCategories:")
    for idx, category in enumerate(Category, start=1):
        print(f"{idx}. {category.value}")
    while True:
        choice = input("Choose a category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(Category):
            return list(Category)[int(choice) - 1].value
        print("Invalid choice. Please select a valid category number.")

# Expense Management Functions
def load_expenses():
    """Load expenses and user info from a JSON file."""
    global expenses, user_info
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
            expenses = data.get("expenses", [])
            
            # Convert the string keys back to (year, month) tuple
            user_info.update(data.get("user_info", {}))
            if "monthly_budgets" in user_info:
                user_info["monthly_budgets"] = {
                    tuple(map(int, key.split('-'))): value
                    for key, value in user_info["monthly_budgets"].items()
                }
            print("\n------ Expenses and budget loaded successfully. ------")
    except FileNotFoundError:
        print("\n------ No saved data found. Starting fresh. ------")
    except json.JSONDecodeError:
        print("\n------ Data corrupted. Starting fresh. ------")
    
    # Check if the current month budget is set
    current_year_month = (datetime.datetime.now().year, datetime.datetime.now().month)
    if current_year_month not in user_info["monthly_budgets"]:
        set_user_budget()  # Prompt user for the current month's budget if not set

def save_expenses():
    """Save expenses and user info to a JSON file."""
    try:
        # Convert the (year, month) tuple keys back to string for JSON serialization
        user_info["monthly_budgets"] = {
            f"{year}-{month:02d}": budget
            for (year, month), budget in user_info["monthly_budgets"].items()
        }
        
        with open("expenses.json", "w") as file:
            json.dump({"expenses": expenses, "user_info": user_info}, file)
            print("-------- Data saved successfully. --------")
    except IOError as e:
        print(f"An error occurred while saving data: {e}")
    finally:
        # Restore monthly_budgets format for further use
        user_info["monthly_budgets"] = {
            (int(year_month.split("-")[0]), int(year_month.split("-")[1])): budget
            for year_month, budget in user_info["monthly_budgets"].items()
        }

def set_user_budget():
    """Prompt user to set a monthly budget when starting fresh."""
    monthly_budget = get_valid_amount("Enter your monthly budget: ")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    user_info["monthly_budgets"][(year, month)] = monthly_budget
    print(f"Budget set to: ₱{monthly_budget:.2f}")
    save_expenses()

def modify_monthly_budget():
    """Allow the user to modify the budget for a specific month."""
    print("\nModify Monthly Budget:")
    try:
        year_input = input("Enter the year (ex: 2024): ")
        if not year_input.isdigit():
            print("Invalid year. Please enter a valid 4-digit number (ex: 2024).")
            return
        year = int(year_input)
        
        month_input = input("Enter the month number (1-12): ")
        if not month_input.isdigit():
            print("Invalid month. Please enter a number between 1 and 12.")
            return
        month = int(month_input)
        
        if not (1 <= month <= 12):
            print("Invalid month. Please enter a number between 1 and 12.")
            return
        
        monthly_budget = get_valid_amount(f"Enter the new budget for {datetime.datetime(year, month, 1).strftime('%B %Y')}: ")
        user_info["monthly_budgets"][(year, month)] = monthly_budget
        print(f"Budget for {datetime.datetime(year, month, 1).strftime('%B %Y')} updated to: ₱{monthly_budget:.2f}")
        save_expenses()
    except ValueError:
        print("Invalid input. Please enter valid numeric values for year and month.")

def reset_data():
    """Reset all expenses and user information."""
    global expenses, user_info
    expenses.clear()  
    user_info = {  
        "name": "",
        "savings_account": 0.0,
        "monthly_budgets": {}
    }
    save_expenses()
    print("All data has been reset.")

def add_expense():
    """Prompt user to add a new expense with validation and budget check."""
    if not user_info["monthly_budgets"]:
        print("No budget set for the current month. Please set a budget first.")
        set_user_budget()
    
    print("\n--- Adding a New Expense ---")
    category = select_category()
    description = input("\nEnter expense description: ")
    amount = get_valid_amount("Enter expense amount: ")
    date = get_date_input()

    expense = {
        "description": description,
        "amount": amount,
        "date": date.strftime("%m-%d-%Y"),
        "category": category
    }
    expenses.append(expense)
    save_expenses()

    print("\nNew Expense Added:")
    print(f"  Description: {description}")
    print(f"  Amount: ₱{amount:.2f}")
    print(f"  Date: {date.strftime('%m-%d-%Y')}")
    print(f"  Category: {category}")

def view_expenses():
    """Display all expenses in a formatted table."""
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n-------------------------- LIST OF EXPENSES ----------------------------------------")
    print(f"+-----+---------------------------------+------------+------------+-----------------+")
    print(f"| No. | {'Description':<31} | {'Amount':<10} | {'Date':<10} | {'Category':<15} |")
    print(f"+-----+---------------------------------+------------+------------+-----------------+")
    
    for idx, expense in enumerate(expenses, start=1):
        print(f"| {idx:<3} | {expense['description']:<31} | ₱{expense['amount']:<9.2f} | {expense['date']:<10} | {expense['category']:<15} |")
        print(f"+-----+---------------------------------+------------+------------+-----------------+")

def delete_expense():
    """Prompt user to delete an expense by its index."""
    if not expenses:
        print("No expenses to delete.")
        return

    try:
        index = int(input("\nEnter the no. of the expense to delete: ")) -1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"Deleted expense: {deleted['description']} - ₱{deleted['amount']} on {deleted['date']} [{deleted['category']}]")
            save_expenses()
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

def generate_report():
    """Generate a user-friendly report of monthly expenses with budget warnings."""
    if not expenses:
        print("No expenses found. Please add some expenses to generate a report.")
        return

    print("\n===== EXPENSE REPORT BY MONTH =====")
    monthly_expenses = defaultdict(lambda: defaultdict(float))
    for expense in expenses:
        date = datetime.datetime.strptime(expense["date"], "%m-%d-%Y")
        year_month = (date.year, date.month)
        category = expense["category"]
        monthly_expenses[year_month][category] += expense["amount"]

    for (year, month), categories in sorted(monthly_expenses.items()):
        month_name = datetime.datetime(year, month, 1).strftime('%B %Y')
        monthly_total = sum(categories.values())
        budget = user_info["monthly_budgets"].get((year, month), 0)
        remaining_budget = budget - monthly_total
        status = "Over Budget" if remaining_budget < 0 else "Within Budget"

        print(f"\n *********** {month_name} **********")
        print(f"{'Category':<15} {'Amount Spent':<15} {'Budget':<10} {'Remaining Budget':<20} {'Status':<15}")
        print("-" * 80)
        for category, total in categories.items():
            print(f"{category:<15} ₱{total:<14.2f} ₱{budget:<10.2f} ₱{remaining_budget:<19.2f} {status:<15}")
        print("-" * 80)
        print(f"TOTAL EXPENSES: ₱{monthly_total:.2f} ")    
        print(f"REMAINING BUDGET: ₱{remaining_budget:.2f}")
        if remaining_budget < 0:
            print(f"WARNING: Over budget by ₱{-remaining_budget:.2f}!")

def display_menu():
    """Display the main menu."""
    print("\nXPENSE TRACKER MENU")
    print("1. Add Expense")
    print("2. View List of Expenses")
    print("3. Delete Expense")
    print("4. Generate Monthly Report")
    print("5. Modify Monthly Budget")
    print("6. Reset Data")
    print("7. Exit")
    return input("Choose an option: ")

def main():
    print("╔" + "═" * 50 + "╗")
    print("║{:^50}║".format("Welcome to Xpense Tracker"))
    print("╚" + "═" * 50 + "╝")
    user_info["name"] = input("\nPlease enter your name: ").strip()
    print(f"\n{'Hello, ' + user_info['name'] + '!':^50}")
    print(f"{'Let\'s get started.':^50}")
    print("\n" + "═" * 50)  #

    load_expenses()

    while True:
        choice = display_menu()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            modify_monthly_budget()
        elif choice == "6":
            if input("Are you sure you want to reset all data? (yes/no): ").strip().lower() == "yes":
                reset_data()
        elif choice == "7":
            print("Exiting...")
            save_expenses()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()
