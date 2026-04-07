from .expense import *


print("\nWelcome to the expense tracker by Anant Shrey, Class 12-A")


def choices():
    print("\n====== Expense Tracker Menu ======")
    print("\nPress 1 to Add Expense")
    print("Press 2 to View All Expenses")
    print("Press 3 to View Expenses by Category")
    print("Press 4 to Search Expense by Date")
    print("Press 5 to Show Summary")
    print("Press 6 to Delete an Expense")
    print("Press 9 to Exit")
    menu()


def menu():
    while True:
        try:
            choice = int(input("\nChoice: "))
            if choice in [1,2,3,4,5,6,9]:
                break
            else:
                print("Enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number")
    
    rerun = True
    if choice == 1:
        add()
    elif choice == 2:
        view_all()
    elif choice == 3:
        view_by_category()
    elif choice == 4:
        search()
    elif choice == 5:
        summary()
    elif choice == 6:
        delete()
    elif choice == 9:
        rerun = False
        pass

    if rerun == True:
        run_again()





choices()