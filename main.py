player_details = {
    "username": str,
    "password": str,
    "email": str,
    "phone_number": int,
    "age": int,
    "credit_card_number": str,
    "date_of_brith": str
}

#test = player_details["age"]
#test = "test"
#print(test)

def validate_username(username):
    if (len(username) < 5) or not(username.isalnum()) :
        return False
    else:
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
    else:
        return True
    
def validate_email(email):
    dot_com_part = email[-4]
    at_symbol_index = 0
    index = 0

    for index in email:
      if email[index] == "@":
          pass

def validate_phone_number(phone_number):
    if (len(phone_number) < 11) or not(phone_number.isdigit()):
        return False
    else:
        return True

def validate_age(age):
    if (age < 18) or (age > 100):
        return False
    else:
        return True

def validate_credit_card_number(credit_card_number):
    pass

def validate_date_of_birth(date_of_birth):
    pass

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
            print("Username should be at least 5 characters long and only contain alphanumeric characters.")
    
    # check if password is valid
    while not valid_password:
        password = input("Enter your password: ")
        valid_password = validate_password(password)
        if valid_password:
            player_details["password"] = password
        else:
            print("Password should be at least 8 characters, with 1 uppercase, 1 lowercase and 1 digit.")
    
    # check if age is valid
    while not valid_age:
        age = int(input("Enter your age: "))
        valid_age = validate_age(age)
        if valid_age:
            player_details["age"] = age
        else:
            print("Age must be a number between 18 and 100.")


main()