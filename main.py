import datetime
import json
import hashlib
from collections import defaultdict
from enum import Enum
import os
import re

# Store all expenses in a list
expenses = []
user_info = {
    "name": "",
    "savings_account": 0.0,
    "monthly_budgets": {}
}

# To store user credentials (username and password)
USER_CREDENTIALS_FILE = "accounts.json" 

current_user = None

# Load user credentials from the JSON file
def load_user_credentials(): 
    """ To Check if the file containing user credentials exists"""
    if os.path.exists(USER_CREDENTIALS_FILE):
        with open(USER_CREDENTIALS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save user credentials to the JSON file
def save_user_credentials():
    with open(USER_CREDENTIALS_FILE, 'w') as f:
        json.dump(USER_CREDENTIALS, f, indent=4)

USER_CREDENTIALS = load_user_credentials()

# User Authentication Functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# To validate an email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def sign_up():
    """Sign up new user with username, password, and name."""
    print("\n-------- Sign Up --------")
    name = input("\n\tEnter your full name: ")
    
    while True:
        email = input("\tEnter Your Email: ")
        if not is_valid_email(email):
            print("\n\tInvalid email format. Please enter a valid email address.")
        elif email in USER_CREDENTIALS:
            print("\n\tEmail already exists. Please enter another.")
        else:
            break
    
    password = input("\tChoose a password (at least 8 characters): ")
    while len(password) < 8:
        print("\tPassword must be at least 8 characters.")
        password = input("\tChoose a password (at least 8 characters): ")

    hashed_password = hash_password(password)
    USER_CREDENTIALS[email] = {"name": name, "password": hashed_password}

    print("\nSign-up successful! You can now log in.")
    save_user_credentials()  

def log_in():
    """Allow user to log in with username and password."""
    print("\nLOG IN")
    email = input("\tEnter your Email: ")
    
    # Validate email format
    if not is_valid_email(email):
        raise ValueError("Invalid email format. Please enter a valid email address.")
    
    password = input("\tEnter your password: ")
    
    # To Check if email exists in the user credentials
    if email not in USER_CREDENTIALS:
        raise ValueError("Invalid email. User not found.")  #
    
    # To Check if the password matches
    if hash_password(password) == USER_CREDENTIALS[email]["password"]:
        print(f"\tWelcome, {USER_CREDENTIALS[email]['name']}!")
        global current_user
        current_user = email  
        return email
    else:
        print("Invalid password.")
    return None  

def log_out():
    """Log out the user by ending the session."""
    global current_user
    print("\n-------- Log Out --------")
    if current_user:
        print(f"Goodbye, {USER_CREDENTIALS[current_user]['name']}!")
        current_user = None
    else:
        print("No user is currently logged in.")
    exit()

class Category(Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    OTHER = "Other"

# Utility Functions
def get_valid_amount(prompt):
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
    
    # To Check if the current month budget is set
    current_year_month = (datetime.datetime.now().year, datetime.datetime.now().month)
    if current_year_month not in user_info["monthly_budgets"]:
        set_user_budget()  

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
    print(f"+-----+--------------------------------+-------------+-------------------+-----------+")
    print(f"| No. | Description                    | Amount      | Date              | Category  |")
    print(f"+-----+--------------------------------+-------------+-------------------+-----------+")
    for idx, expense in enumerate(expenses, start=1):
        print(f"| {idx: <3} | {expense['description'][:30]: <30} | ₱{expense['amount']: <10.2f} | {expense['date']}        | {expense['category'][:9]: <9} |")
    print(f"+-----+--------------------------------+-------------+-------------------+-----------+")

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


def main_menu():
    """Main menu for the expense tracker."""
    while True:
        print("\n════════════════════════════════════════════════")
        print("       EXPENSE TRACKER MENU".center(40))
        print("\n════════════════════════════════════════════════")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Modify Monthly Budget")
        print("5. Generate Monthly Report ")
        print("6. Reset Data")
        print("7. Log Out")
        choice = input("\nEnter your choice: ")
        print("════════════════════════════════════════════════")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            modify_monthly_budget()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            reset_data()
        elif choice == '7':
            log_out()
            break  
        else:
            print("Invalid choice. Please select an option between 1 and 7.")

if __name__ == "__main__":
    current_user = None
    while True:
        if current_user is None:  
            print("    ")
            print("\n╔" + "═" * 80 + "╗")
            print("\n║{:^80}║".format("Welcome to Xpense Tracker"))
            print("\n╚" + "═" * 80 + "╝")
            print("1. Sign Up")
            print("2. Log In")
            print("3. Exit")
            choice = input("\n   Enter your choice: ")

            if choice == '1':
                sign_up() 
            elif choice == '2':
                print("\n" + "═" * 50)  
                current_user = log_in()
                if current_user:
                    load_expenses()  
                    print("\n" + "═" * 50)  
                    main_menu() 
            elif choice == '3':
                print("\tGoodbye!")
                print("\n" + "═" * 50)  
                break
            else:
                print("Invalid choice. Please select an option between 1 and 3.")