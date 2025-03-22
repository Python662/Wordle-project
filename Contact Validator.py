import re
    
def validate_name():
    user_input = input("Enter contact name: ")
    
    if isinstance(user_input, str):
        if re.match(r'^[A-Za-z]+$', user_input):
            print("contact name is valid")

        else:
            print("contact name is invalid")
            quit()
    else:
        print ("Invalid input")
    
print(validate_name())

def validate_phone_number():
    user_input = input("Enter contact phone number: ")
    if re.match(r'^[0-10]+$', user_input):
        print("Contact phone number is valid")
    else:
        print("Contact phone number is invalid")
    

print(validate_phone_number())

def validate_email():
    user_input = input("Enter contact email: ")
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_input):
        print("Contact email is valid")
    else:
        print("Invalid input")
        
print(validate_email())