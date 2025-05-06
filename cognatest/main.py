from datetime import datetime 

def intro():
    name=input("Enter your name:")
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
    date_of_birth = datetime.strptime(dob_input, "%d-%m-%Y").date()
    print(f"Your date of birth is: {date_of_birth}")

    today = datetime.today().date()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    print(f"You are {age} years old.")

intro
