from utils import *

# Add expense
# view expense
# delete expense
expenses = []

def add_expense():
    amt = get_amount()
    category = get_category()
    date = get_date()

    expense = {'amount':amt, 'category':category, 'date':date}
    expenses.append(expense)


def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return
    
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']}")


def delete_expense():
    view_expenses()
    
    if not expenses:
        return
    
    while True:
        try:
            index = int(input("Enter expense id number to delete: "))
            if index >= 0 and index <= len(expenses):
                removed = expenses.pop(index - 1)
                print("Deleted:", removed)
                break
            else:
                print("Invalid value.")
        except ValueError:
            print("Invalid value.")


def summarize():
    if not expenses:
        print("\nNo expenses to summarize")
        return
    
    total = 0
    for i in expenses:
        total += i["amount"]
    print(f"\nTotal spends: {total}")

    category_total = {}

    for exp in expenses:
        cat = exp["category"]
        category_total[cat] = category_total.get(cat, 0) + exp["amount"]

    print("\nSpending by category:")
    for cat, amt in category_total.items():
        print(f"{cat}: ₹{amt}")
