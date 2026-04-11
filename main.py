from expense import *

# Show Menu (Add expense, View expenses, Delete expense, Show summary, Exit)
# User Input
# Call other functions

print("\nWelcome to the Expense Tracker Program by Anant Shrey, Class 12-A, DPSGV.")
print("This program supports adding, viewing, deleting and summarising expenses.")


def run():
    while True:
        choices()
        choice = get_choice()
        
        if choice == 1:
            print(f"\nYou have chosen to Add an Expense, sorted into 5 categories.\n")
            for i, cat in enumerate(CATEGORIES, start=1):
                print(f"{i}. {cat}")
            print()
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            delete_expense()
        # elif choice == 4:
        #     summarize()
        else:
            break    
    

def choices():
    print("\nPress 1 to Add an Expense")
    print("Press 2 to View Expenses")
    print("Press 3 to Delete an Expense")
    print("Press 4 to Summarize Expenses")
    print("Press 5 to Exit")


run()