from datetime import datetime

# validate amount
# validate date
# format output


def get_choice():
    t1 = (1,2,3,4,5)
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
    categories = ("food","travel","study","entertainment","others")
    while True:
        x = input("Category: ").lower()
        if x in categories:
            break
        else:
            print("Enter a valid categories. (Food, Travel, Study, Entertainment, Others)")
    return x


def get_date():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")
    return date_str