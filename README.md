# Xpense Tracker
![Xpense Tracker Logo](./logo.png "Xpense Tracker Logo")


-----------------
## 📖 Project Overview

**Xpense Tracker** is a Python-based financial management system designed to help users effectively track their expenses, set monthly budgets, and monitor spending patterns. It integrates user-friendly features like categorizing expenses, generating reports, and alerting users when their spending exceeds budget limits. With a focus on financial literacy and empowerment, this project supports individuals in making informed decisions about their finances.

 Xpense Tracker helps users stay informed, disciplined, and financially literate. The system aligns with the United Nations Sustainable Development Goal 12 by encouraging mindful financial habits through responsible tracking and budgeting.

---
## 🖥️ Features
- **User Authentication**: Allows users to sign up, log in, and log out securely with username and password.
- **Expense Categorization:** Organize expenses into predefined categories for better insights.  
- **Automatic Data Persistence:** Save data seamlessly to ensure consistent tracking over time.  
- **Budget Comparison and Alerts:** Compare expenses against budgets and receive warnings for overspending.  
- **Detailed Monthly Reports:** Generate comprehensive financial summaries to track spending patterns.  
- **Reset Functionality:** Start fresh anytime by resetting all data with ease.
- **Data Persistence**: User data, including credentials, expenses, and budgets, are stored in JSON files for persistent storage.
  
------

## 🗂 Table of Contents
1. [Project Overview](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=Xpense%20Tracker-,%F0%9F%93%96%20Project%20Overview,-Xpense%20Tracker%20is)
2. [Features](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=tracking%20and%20budgeting.-,%F0%9F%96%A5%EF%B8%8F%20Features,-User%2DFriendly%20Interface)
3. [Application of Python Concepts and Libraries](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#%EF%B8%8F-application-of-python-concepts-and-libraries)
4. [SDG Integration](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=%F0%9F%8C%8D%20SDG%20Integration%3A%20Goal%2012%20%2D%20Responsible%20Consumption%20and%20Production) 
6. [Getting Started](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=mindful%20consumption%20practices.-,%F0%9F%9A%80%20Getting%20Started,-1.%20Prerequisite%3A)
7. [Sample Output For User Authentication](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#-sample-output-for-user-authentication) 
8. [Menu Options](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#-menu-options)  
9. [Sample Outputs For Menu Options](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=the%20program%20safely.-,%F0%9F%93%8A%20Sample%20Outputs,-View%20Examples%3A)  
10. [General Instructions](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#-general-instructions)
11. [Conclusion](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#-conclusion)  

-----
## 🛠️ Application of Python Concepts and Libraries
The Xpense Tracker application is designed with fundamental Python concepts and libraries to deliver a simple, efficient, and user-friendly experience:

### 1. Core Python Concepts
- **Functions:**
  - Modular functions ( ex: `add_expense`, `view_expenses`, `generate_report`) divide the program into manageable components, improving readability.
  - Utility functions like `get_valid_amount` and `get_date_input` ensure user inputs are accurate and correctly formatted.

- **Control Flow:**
  - Conditional statements (`if-else`) process user menu selections and handle various program operations.
  - Loops (`while`) maintain interactivity, allowing the program to run continuously until the user exits.

### 2. Data Structures
- **Lists:** Stores all expense entries dynamically, enabling efficient addition, modification, and deletion.
- **Dictionaries:** Organize user information and monthly budgets, offering quick access and updates of user's data throughout the program.
- **DefaultDict:** The defaultdict from the collections module is used to group expenses by month and category. This eliminates the need for manual checks to ensure that a category or month exists in the dictionary.
### 3. Key Libraries
- **`datetime`:** Validates and handles dates for accurate logging and tracking.
- **`json`:** The json module provides functionality for saving and loading data in a structured format (JSON). It allows user information (ex: name, savings balance, monthly budgets) and expenses to persist across program runs by saving them to a file.
- **`collections`:** Simplifies advanced data handling with `DefaultDict`, making data grouping and calculations easier.
- **`Enum`:** It is used to define a fixed set of expense categories (ex: Food, Transport) for better data consistency and validation. It also makes the code more readable and easier to maintain.
- **`hashlib`:** It is used to secure user passwords via hashing, ensuring user data privacy.
- **`os`:** This module is used to check if a file already exists in a specific directory. This prevents overwriting existing files and ensures you're using the correct file paths when saving or loading data.
### 4. Error Handling
- **Input Validation:**
  Ensures all user inputs are correctly formatted to prevent unexpected errors:
  - **Numeric Inputs:** Functions like `get_valid_amount` validate that only numeric values are accepted for expenses and budgets.
  - **Date Validation:** The `get_date_input` function ensures users enter dates in the correct `MM-DD-YYYY` format using the `datetime` module.
  - **Menu Choices:** User selections for categories and menu options are validated to prevent invalid inputs.
- **File Handling:**
  - If files are missing or corrupted, try-except blocks are employed to handle the exceptions, ensuring that the program can recover by initializing fresh data or resetting corrupted files.
-**Exception Handling**
  Detects and gracefully handles common runtime errors:
  - **Invalid Numeric Inputs:** Prevents crashes when users enter non-numeric values where numbers are required (ex: budgets or expense amounts).
  - **Out-of-Range Inputs:** Ensures user inputs like category selections are within valid ranges.
  - **Empty Data Scenarios:** Handles operations on empty datasets (ex: generating reports or viewing expenses) by displaying user-friendly messages.
- **User Feedback:**
  Provides clear and actionable feedback for errors:
  - **Input Prompts:** Users are guided to correct invalid inputs without terminating the program.
  - **Error Messages:** Messages like "Invalid input. Please enter a numeric value" help users understand and fix their mistakes.

---

## 🌍 SDG Integration: Goal 12 - Responsible Consumption and Production 
Xpense Tracker supports **SDG Goal 12** by promoting responsible financial habits.
The program:
- **Encourages Awareness:** Tracks and categorizes expenses, helping users monitor consumption patterns.
- **Fosters Discipline:** Helps users set budgets, avoid overspending, and align spending with financial goals.
- **Empowers Decisions:** Generates monthly reports that provide insights into spending trends, enabling informed choices.
  
By addressing these aspects,Xpense Tracker aligns with the global goal of encouraging sustainable and mindful consumption practices.

---

## 🚀 Getting Started
### 1. Prerequisite:
- Install **Python 3.6** or above: [Download Python](https://www.python.org/downloads/)
- Install **Visual Studio Code**: [Download VS Code](https://code.visualstudio.com/)
- Ensure the `expenses.json` file is in the working directory (or let the program create it on the first run).

### 2. Run the program:
   - Open a Terminal or Command Prompt
   - Navigate to the directory containing the `main.py` file.
   - Copy and paste the raw code to execute the program.
     
### 3. Using the Program
3.1 Once launched, the program greets the user with a welcoming message and presents them a user Authentication options.
```
╔════════════════════════════════════════════════════════════════════════════════╗

║                           Welcome to Xpense Tracker                            ║

╚════════════════════════════════════════════════════════════════════════════════╝
1. Sign Up
2. Log In
3. Exit

   Enter your choice: 
```

### 📘 **Sample Output For User Authentication**
<details>
  <summary>View Examples:</summary>
 
#1 SIGN UP 
```
╔════════════════════════════════════════════════════════════════════════════════╗

║                           Welcome to Xpense Tracker                            ║

╚════════════════════════════════════════════════════════════════════════════════╝
1. Sign Up
2. Log In
3. Exit

   Enter your choice: 1
-------- Sign Up --------

        Enter your full name: Annrie Rosales
        Choose a username: itsyourrie   
        Choose a password (at least 8 characters): 01234567 

Sign-up successful! You can now log in.
```
# 2 LOG IN
```
╔════════════════════════════════════════════════════════════════════════════════╗

║                           Welcome to Xpense Tracker                            ║

╚════════════════════════════════════════════════════════════════════════════════╝
1. Sign Up
2. Log In
3. Exit

   Enter your choice: 2
LOG IN
        Enter your username: itsyourrie
        Enter your password: 01234567
        Welcome, Annrie Rosales!

------ Expenses and budget loaded successfully. ------

══════════════════════════════════════════════════
```
# 3 EXIT
```
╔════════════════════════════════════════════════════════════════════════════════╗

║                           Welcome to Xpense Tracker                            ║

╚════════════════════════════════════════════════════════════════════════════════╝
1. Sign Up
2. Log In
3. Exit

   Enter your choice: 3
        Goodbye!

══════════════════════════════════════════════════
```
</details>

#### 3.2 After logging in, the user is directed to the Expense Tracker Menu.
```
════════════════════════════════════════════════
             EXPENSE TRACKER MENU

════════════════════════════════════════════════
1. Add Expense
2. View Expenses
3. Delete Expenses
4. Modify Monthly Budget
5. Generate Monthly Report
6. Reset Data
7. Log Out

Enter your choice:
```

## 🌟 **Menu Options**
| **Feature**                   | **Description**                                                                      |
|------------------------------ |--------------------------------------------------------------------------------------|
| **Add Expense**               | Log a new expense by selecting a category, entering a description, amount, and date. |
| **View List of Expenses**     | Review all recorded expenses in a neat table format.                                 |
| **Delete Expense**            | Remove an unwanted expense by its index number.                                      |
| **Generate Monthly Report**   | View categorized expense summaries and compare them to monthly budgets.              |
| **Modify Monthly Budget**     | Adjust your budget for any specific month as needed.                                 |
| **Reset Data**                | Clear all stored data to start fresh.                                                |
| **Log Out**                   | Save your progress and exit the program safely.                                      |

---
# 📊 **Sample Outputs For Menu Options**
<details>
  <summary>View Examples:</summary>
   
## **Adding Expense Example** 
  ```
  --- Adding a New Expense ---
  New Expense Added:
    Description: Lunch
    Amount: ₱120.00
    Date: 11-22-2024
    Category: Food
```

## **View List of Expense Example**  
```
-------------------------- LIST OF EXPENSES ----------------------------------------
+-----+---------------------------------+------------+------------+-----------------+
| No. | Description                     | Amount     | Date       | Category        |
+-----+---------------------------------+------------+------------+-----------------+
| 1   | coffee                          | ₱50.00     | 11-22-2024 | Food            |
+-----+---------------------------------+------------+------------+-----------------+
| 2   | fare                            | ₱200.00    | 11-22-2024 | Transporation   |
+-----+---------------------------------+------------+------------+-----------------+
```
## **Delete Expense Example** 
```
Enter the no. of the expense to delete: 1
Deleted expense: Lunch - ₱50.00 on 11-22-2024 [Food]  
-------- Data saved successfully. --------
```
## **Generate Monthly Report Example**
```
===== EXPENSE REPORT BY MONTH =====

 *********** November 2024 **********
Category        Amount Spent    Budget     Remaining Budget     Status
--------------------------------------------------------------------------------
Food            ₱74.00          ₱500.00     ₱226.00              Within Budget
Transport       ₱200.00         ₱500.00     ₱226.00              Within Budget
--------------------------------------------------------------------------------
TOTAL EXPENSES: ₱274.00
REMAINING BUDGET: ₱226.00
```
### **Overspending: Monthly Report Example**
```
===== EXPENSE REPORT BY MONTH =====

 *********** November 2024 **********
Category         Amount Spent     Budget          Remaining Budget     Status
--------------------------------------------------------------------------------
Food             ₱ 600.00         ₱ 1000.00       ₱ -100.00            Over Budget
Transport        ₱ 500.00         ₱ 1000.00       ₱ -100.00            Over Budget
--------------------------------------------------------------------------------
TOTAL EXPENSES: ₱1100.00  
REMAINING BUDGET: ₱-100.00  
WARNING: Over budget by ₱100.00!
```
## **Modify Monthly Budget Example:**
```
Modify Monthly Budget:
Enter the year (ex: 2024): 2024
Enter the month number (1-12): 11
Enter the new budget for November 2024: 1000

Budget for November 2024 updated to: ₱1000.00  
-------- Data saved successfully. --------
```
## **Error handling Example:**
```
EXAMPLE 1: Out-of-Range Category Selection

Categories:
1. Food
2. Transport
3. Entertainment
4. Utilities
5. Other
Choose a category number: 6
Invalid choice. Please select a valid category number.
Choose a category number: 2
```
```
EXAMPLE 2: Invalid Date Format

Enter date (MM-DD-YYYY): 22-11-2024
Invalid date format. Please enter in MM-DD-YYYY format.
Enter date (MM-DD-YYYY): 11-22-2024
```
</details>

-------
## 📌 **General Instructions**  
- **Step-by-Step Guide:** Follow the on-screen prompts for each menu option.  
- **Input Validation:** Enter values carefully—any invalid input will prompt you to retry.  
- **Automatic Data Saving:** Your data is saved after every operation.
------
## 🎉 Conclusion
Xpense Tracker simplifies financial management by helping users track expenses and stay within their budgets. 
                             Let's Spend Wise!




