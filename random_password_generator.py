import random
import string

def generator_password(length=12):
       # Define the character sets to choose from
    letters= string.ascii_letters  # a-z, A-Z
    digits = string.digits         # 0-9
    symbols = string.punctuation   # !@#$%^*() etc.
    
    #Combine all possible characters
    all_characters = letters + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
try:
    user_length = int(input("Enter desired password length: "))
    if user_length < 4:
        print("Password length should be at least 4 characters.")
    else:
        new_password = generator_password(user_length)
        print(f"Your Generated password is: {new_password}")
except ValueError:
    
    print("Please enter a valid number.")
    
