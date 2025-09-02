"""
Requirements:
Application should run from the command line and should have the following features:

Users can add an expense with a description and amount.
Users can update an expense.
Users can delete an expense.
Users can view all expenses.
Users can view a summary of all expenses.
Users can view a summary of expenses for a specific month (of current year).
Allow users to export expenses to a CSV file.

"""
import csv
import sys
import os
from datetime import datetime

csv_columns = [
    ['ID', 'Date', 'Description', 'Amount (USD)']
]

expenses = []

if not os.path.exists("expenses.csv"):
    with open("expenses.csv", "w", newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(csv_columns)

with open("expenses.csv", "r") as expenses_csv:
    csv_content = list(csv.reader(expenses_csv))
    if len(csv_content) < 2:
        expenses = []
    else:
        for row in csv_content[1:]:
            expenses.append(row)

if len(sys.argv) < 2:
    print("Usage: python3 expense_tracker.py <command> --<additional options>")
    print("""
            ** Commands: **
            - add --description <description> --amount <amount_in_USD>
            - list
            - summary, options: --month <month_number, e.g. August: 8>
            - delete --id <expense_id> or all
            """)
    exit(0)

match sys.argv[1]:
    case "add":
        try:
            if len(sys.argv) != 6:
                print("Usage: python3 expense_tracker.py add --description <description> --amount <amount_in_USD>")
                exit(0)
            else:
                add_id = 0
                if not expenses:
                    add_id = 1
                else:
                    max_id = max([int(exp[0]) for exp in expenses])
                    add_id = max_id + 1
                
                add_date = datetime.now().strftime("%Y-%m-%d")
                add_description = sys.argv[3]
                add_amount = sys.argv[5]
                expenses.append([add_id, add_date, add_description, add_amount])
                print(f"Expense of amount ${add_amount} for {add_description} added sucessfully to expenses.csv")


        except Exception as e:
            print("An error occured during expense adding process:", e)
            exit(1)


    case "list":
        try:
            print("ID  Date  Description  Amount")
            for expense in expenses:
                print(f"{expense[0]}  {expense[1]}  {expense[2]}  ${expense[3]}")
            exit(0)
        except Exception as e:
            print("An error occured during expenses listing.", e)
            exit(1)

    case "summary":
        try:
            if len(sys.argv) < 4:
                total = 0
                for expense in expenses:
                    total += float(expense[3])
                print(f"Total expenses: ${total:.2f}")
                exit(0)
            else:
                input_month = sys.argv[3]
                month_total = 0
                for expense in expenses:
                    expense_date = datetime.strptime(expense[1], "%Y-%m-%d")
                    if expense_date.month == int(input_month):
                        month_total += float(expense[3])

                month_name = datetime.strptime(input_month, "%m").strftime("%B")
                print(f"Total expenses for {month_name}: ${month_total:.2f}")
                exit(0)
                    
        except Exception as e:
            print("Error in printing expense summary:", e)

    case "delete":
        if sys.argv[2] == "all":
            expenses = []
            print("All expenses deleted successfully.")
        elif len(sys.argv) != 4 or sys.argv[2] != "--id":
            print("""Usage: python3 expense_tracker.py delete --id <expense_id>
- To know all expenses along with their id's run python3 expense_tracker.py list""")
            exit(0)
        else:
            try:
                delete_id = sys.argv[3]
                initial_len = len(expenses)
                expenses = [expense for expense in expenses if expense[0] != delete_id]

                if len(expenses) < initial_len:
                    print(f"Expense with id {delete_id} successfully deleted.")
                else:
                    print(f"Expense with id {delete_id} not found.")
                exit(0)
            except Exception as e:
                print("An error occured during expense deletion:", e)

expenses = csv_columns + expenses

with open("expenses.csv", "w", newline='') as expenses_csv:
    csv_writer = csv.writer(expenses_csv)
    csv_writer.writerows(expenses)



                    


