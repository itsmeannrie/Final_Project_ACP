# Xpense Tracker
![Xpense Tracker Logo](./logo.png "Xpense Tracker Logo")


-----------------
## 📖 Project Overview

**Xpense Tracker** is a Python-based financial management system designed to help users effectively track their expenses, set monthly budgets, and monitor spending patterns. It integrates user-friendly features like categorizing expenses, generating reports, and alerting users when their spending exceeds budget limits. With a focus on financial literacy and empowerment, this project supports individuals in making informed decisions about their finances.

 Xpense Tracker helps users stay informed, disciplined, and financially literate. The system aligns with the United Nations Sustainable Development Goal 12 by encouraging mindful financial habits through responsible tracking and budgeting.

---
## 🖥️ Features

- **User-Friendly Interface:** Navigate effortlessly with a clear, menu-driven system.  
- **Expense Categorization:** Organize expenses into predefined categories for better insights.  
- **Automatic Data Persistence:** Save data seamlessly to ensure consistent tracking over time.  
- **Budget Comparison and Alerts:** Compare expenses against budgets and receive warnings for overspending.  
- **Detailed Monthly Reports:** Generate comprehensive financial summaries to track spending patterns.  
- **Reset Functionality:** Start fresh anytime by resetting all data with ease.
  
------

## 🗂 Table of Contents
1. [Project Overview](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=Xpense%20Tracker-,%F0%9F%93%96%20Project%20Overview,-Xpense%20Tracker%20is)
2. [Features](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=tracking%20and%20budgeting.-,%F0%9F%96%A5%EF%B8%8F%20Features,-User%2DFriendly%20Interface)
3. [Application of Python Concepts and Libraries](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=Instructions,Concepts%20and%20Libraries)
4. [SDG Integration](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=%F0%9F%8C%8D%20SDG%20Integration%3A%20Goal%2012%20%2D%20Responsible%20Consumption%20and%20Production)  
5. [Getting Started](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=mindful%20consumption%20practices.-,%F0%9F%9A%80%20Getting%20Started,-1.%20Prerequisite%3A)  
6. [Menu Options](#🌟-menu-options)  
7. [Sample Outputs](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#:~:text=the%20program%20safely.-,%F0%9F%93%8A%20Sample%20Outputs,-View%20Examples%3A)  
8. [General Instructions](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#-general-instructions)
9. [Conclusion](https://github.com/itsmeannrie/Final_Project_ACP/blob/main/README.md#-conclusion)  

-----
## 🛠️ Application of Python Concepts and Libraries
The Xpense Tracker application is designed with fundamental Python concepts and libraries to deliver a simple, efficient, and user-friendly experience:

### 1. Core Python Concepts
- **Functions:**
  - Modular functions (`add_expense`, `view_expenses`, `generate_report`) divide the program into manageable components, improving readability.
  - Utility functions like `get_valid_amount` and `get_date_input` ensure user inputs are accurate and correctly formatted.

- **Control Flow:**
  - Conditional statements (`if-else`) process user menu selections and handle various program operations.
  - Loops (`while`) maintain interactivity, allowing the program to run continuously until the user exits.

- **Enumerations:**
  - The `Enum` class standardizes expense categories (ex: Food, Transport) for better data consistency and validation.

### 2. Data Structures
- **Lists:** Store expense entries dynamically, enabling efficient addition, modification, and deletion.
- **Dictionaries:** Organize user information and monthly budgets, offering quick access and updates.
- **DefaultDict:** From the `collections` module,  it simplifies data grouping and calculations, especially for monthly expense summaries.
### 3. Key Libraries
- **`datetime`:** Validates and handles dates for accurate logging and tracking.
- **`json`:**  Ensures data persistence by saving user details and expense records in a structured format for future use.
- **`collections`:** Simplifies advanced data handling with `DefaultDict`, making data grouping and calculations easier.
### 4. Error Handling
- **Input Validation:**
- Ensures all user inputs are correctly formatted to prevent unexpected errors:
  - **Numeric Inputs:** Functions like `get_valid_amount` validate that only numeric values are accepted for expenses and budgets.
  - **Date Validation:** The `get_date_input` function ensures users enter dates in the correct `MM-DD-YYYY` format using the `datetime` module.
  - **Menu Choices:** User selections for categories and menu options are validated to prevent invalid inputs.
- **File Handling:**
  - Uses try-except blocks to manage missing or corrupted files:
    Initializes fresh data if expenses.json is missing.
    Resets corrupted files to maintain functionality.
-**Exception Handling**
- Detects and gracefully handles common runtime errors:
  - **Invalid Numeric Inputs:** Prevents crashes when users enter non-numeric values where numbers are required (ex: budgets or expense amounts).
  - **Out-of-Range Inputs:** Ensures user inputs like category selections are within valid ranges.
  - **Empty Data Scenarios:** Handles operations on empty datasets (ex: generating reports or viewing expenses) by displaying user-friendly messages.
- **User Feedback:**
- Provides clear and actionable feedback for errors:
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

## 2. Clone or Download the Repository:
```bash
git clone https://github.com/your-username/xpense-tracker.git
cd xpense-tracker
```

## 3. Run the program:
Open a terminal or command prompt.
Execute the following command:
```bash
python main.py
```
## 4. Using the Program

Once launched, the program will prompt you to enter your name and guide you through a menu of options.  
Use the corresponding numbers to navigate the menu:

```plaintext
XPENSE TRACKER MENU
1. Add Expense
2. View List of Expenses
3. Delete Expense
4. Generate Monthly Report
5. Modify Monthly Budget
6. Reset Data
7. Exit
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
| **Exit**                      | Save your progress and exit the program safely.                                      |

---
# 📊 **Sample Outputs**
<details>
  <summary>View Examples:</summary>
   
## **Adding Expense Example** 
  ```plaintext
  --- Adding a New Expense ---
  New Expense Added:
    Description: Lunch
    Amount: ₱120.00
    Date: 11-22-2024
    Category: Food
```

## **View List of Expense Example**  
```plaintext
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
```plaintext
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
```plaintext
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
```plaintext
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




