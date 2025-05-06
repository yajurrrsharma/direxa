from datetime import datetime

def intro():

    '''
   Taking basic information of the user, crucial for analysis.
    
    '''

    name=input("Enter your name: ")
    dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
    date_of_birth = datetime.strptime(dob_input, "%d-%m-%Y").date()

    today = datetime.today().date()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    print(f"You are {age} years old.")

    grade = int(input("Enter your grade: "))
    city = input("Enter your city: ")
    
    if grade > 10:
        stream = input("Enter your stream: ")
    
    else:
        pref = input("Enter your preferred stream")

    email = input("Enter your email\n")


def test():
    pass
