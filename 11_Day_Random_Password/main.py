import random
import string

length =  8 #int(input("Enter Password length : "))
characters = string.ascii_letters + string.digits + '!@#$%&?~'  # Includes letters, digits, and special characters
# for _ in range(10):   generate different passwords in one time 
password = ''.join(random.choice(characters) for _ in range(length))
print(password)
    
   
    
