import re
from datetime import datetime
from error_messages import ERROR  # Import the ERROR class with constants

player_details = {
    "username": str,
    "password": str,
    "email": str,
    "phone_number": int,
    "age": int,
    "credit_card_number": str,
    "date_of_birth": str
}

def validate_username(username):
    if (len(username) < 5) or not(username.isalnum()):
        return False
    return True

def validate_password(password):
    uppercase_letters = 0
    lowercase_letters = 0
    digits = 0

    for char in password:
        if char.islower(): lowercase_letters += 1
        if char.isupper(): uppercase_letters += 1
        if char.isdigit(): digits += 1

    if (len(password) < 8) or (lowercase_letters < 1) or (uppercase_letters < 1) or (digits < 1):
        return False
    return True
    
def validate_email(email):
    # Email format
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, email):
        return True
    return False

def validate_phone_number(phone_number):
    if (len(phone_number) < 11) or not(phone_number.isdigit()):
        return False
    return True

def validate_age(age):
    if (age < 18) or (age > 100):
        return False
    return True

def validate_credit_card_number(credit_card_number):
    # TODO:
    pass

def calculate_age_from_date_of_birth(date_of_birth):
    today = datetime.today()
    birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def validate_date_of_birth(date_of_birth, age):
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    
    # Check if the format is correct
    if not re.match(date_pattern, date_of_birth):
        return False
    
    try:
        # Try and convert string to object
        date_obj = datetime.strptime(date_of_birth, "%Y-%m-%d")
        
        # Check if year is valid
        if date_obj.year < 1900 or date_obj.year > 2023:
            return False
        
        calculated_age = calculate_age_from_date_of_birth(date_of_birth)
        if calculated_age != age:
            return False
        
    except ValueError:
        # If the date is invalid (e.g., Feb 30 or wrong leap year), return False
        return False
    
    return True

def main():

    valid_username = False
    valid_password = False
    valid_email = False
    valid_phone_number = False
    valid_age = False
    valid_credit_card_number = False
    valid_date_of_birth = False

    # check if username is valid
    while not valid_username:
        username = input("Enter your username: ")
        valid_username = validate_username(username)
        if valid_username:
            player_details["username"] = username
        else:
            print(ERROR.INVALID_USERNAME)
    
    # check if password is valid
    while not valid_password:
        password = input("Enter your password: ")
        valid_password = validate_password(password)
        if valid_password:
            player_details["password"] = password
        else:
            print(ERROR.INVALID_PASSWORD)
    
    # check if email is valid
    while not valid_email:
        email = input("Enter your email: ")
        valid_email = validate_email(email)
        if valid_email:
            player_details["email"] = email
        else:
            print(ERROR.INVALID_EMAIL)
    
    # check if date of birth is valid
    while not valid_date_of_birth:
        date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
        age = int(input("Enter your age: "))
        if (age < 18) or (age > 100): print(ERROR.INVALID_AGE)
        valid_date_of_birth = validate_date_of_birth(date_of_birth, age)
        if valid_date_of_birth:
            player_details["date_of_brith"] = date_of_birth
        else:
            print(ERROR.INVALID_DATE_OF_BIRTH)


main()