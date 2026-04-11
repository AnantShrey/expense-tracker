from datetime import datetime
from config import *


# validate amount
# validate date
# format output


def get_choice():
    while True:
        try:
            choice = int(input("\nChoice: "))
            if choice in t1:
                break
            else:
                print("Invalid choice. Try again")
        except ValueError:
            print("Invalid choice. Try again.")
    return choice


def get_amount():
    while True:
        try:
            x = float(input("Amount: "))
            if x > 0:
                break
            else:
                print("Invalid value.")
        except ValueError:
            print("Invalid value.")
    return x


def get_category():
    while True:
        x = input("Category: ").lower()
        print()
        if x in CATEGORIES:
            break
        else:
            print(f"Enter a valid categories.")
            for i, cat in enumerate(CATEGORIES, start=1):
                print(f"{i}. {cat}")
            print()
    return x


def get_date():
    while True:
        date_str = input(f"Enter date in ({DATE_FORMAT}) format: ")
        
        try:
            date_obj = datetime.strptime(date_str, DATE_FORMAT)
            break
        except ValueError:
            print(f"Invalid date. Please use ({DATE_FORMAT}) format.")
    return date_str