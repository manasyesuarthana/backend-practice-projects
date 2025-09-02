# Command-Line Expense Tracker

A simple CLI tool built with Python to track daily expenses. This script allows you to add, list, delete, and summarize your expenses directly from the terminal. All data is saved locally in an `expenses.csv` file.

---

## Features

-   **Add an Expense**: Record a new expense with a description and amount.
-   **List All Expenses**: View a formatted list of all your recorded expenses.
-   **Delete Expenses**: Remove a specific expense by its ID, or clear all entries at once.
-   **View Summaries**: Calculate the total of all expenses, or filter the summary for a specific month.
-   **CSV Storage**: All data is stored in a simple, portable `expenses.csv` file.

---

## Prerequisites

-   Python 3 (No external libraries needed)

---

## Usage

Run the script from your terminal using the commands below.

**NOTE:**
- There is no input validation, so the program may crash or behave incorrectly if you input something weird :v
- Make sure you run the file in the same directory where the source code exists. If not the csv file will be created outside of the source code environemnt which will causes errors.

### General Help
To see the list of available commands:
```bash
python3 expense_tracker.py
```

### Add an Expense
**Note:** The arguments must be in this specific order.
```bash
python3 expense_tracker.py add --description "Groceries" --amount 55.75
```

### List All Expenses
```bash
python3 expense_tracker.py list
```

### View Summaries
-   **To view the grand total of all expenses:**
    ```bash
    python3 expense_tracker.py summary
    ```
-   **To view the total for a specific month (e.g., August = 8):**
    ```bash
    python3 expense_tracker.py summary --month 8
    ```

### Delete an Expense
-   **To delete a single expense by its ID:**
    ```bash
    python3 expense_tracker.py delete --id 3
    ```
-   **To delete ALL expenses:**
    ```bash
    python3 expense_tracker.py delete all
    ```

---

## Data File

All entries are stored in an `expenses.csv` file that is automatically created in the same directory as the script. The file has the following columns: `ID`, `Date`, `Description`, `Amount (USD)`.