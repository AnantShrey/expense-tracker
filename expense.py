from utils import *
from database import get_connection

# Add expense
# view expense
# delete expense


def add_expense():
    amt = get_amount()
    category = get_category()
    date = get_date()

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)"
    values = (amt, category, date)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    print("Expense added successfully!")


def view_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    for row in records:
        print(row)

    cursor.close()
    conn.close()


def delete_expense():
    view_expenses()

    try:
        expense_id = int(input("Enter Expense ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM expenses WHERE id = %s"
    cursor.execute(query, (expense_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No expense found with that ID.")
    else:
        print("Expense deleted successfully.")

    cursor.close()
    conn.close()


# def summarize():
#     if not expenses:
#         print("\nNo expenses to summarize")
#         return
    
#     total = 0
#     for i in expenses:
#         total += i["amount"]
#     print(f"\nTotal spends: {total}")

#     category_total = {}

#     for exp in expenses:
#         cat = exp["category"]
#         category_total[cat] = category_total.get(cat, 0) + exp["amount"]

#     print("\nSpending by category:")
#     for cat, amt in category_total.items():
#         print(f"{cat}: ₹{amt}")
