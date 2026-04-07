# from .main import *


# def run_again():
#     x = input("Do you want to restart the program: (y/n): ").lower()
#     if x == 'y':
#         n = input("Do you want to repeat the choices? (y/n): ").lower()
#         if n == 'y':
#             choices()
# #         else:
#             menu()


def get_expense_input():
    while True:
        try:
            amt = float(input("\nExpense amount: "))
            break
        except ValueError:
            print("Invalid. (input was not a number)")
    return amt



def add():
    print("\nYou have chosen to add an expense.")
    print("There are 4 expense categories (Food/Travel/Study/Other)")

    categories = ('food', 'travel', 'study', 'other')

    amt = get_expense_input()

    # while True:
    #     ctgry = input("\nCategory: ").lower()
    #     if ctgry in categories:
    #         break
    #     else:
    #         print("Invalid category")

    # while True:



add()