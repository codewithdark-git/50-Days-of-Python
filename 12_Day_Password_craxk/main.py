import random

length = 4 #int(input("Enter Password Length: "))
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&?¿'

password = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)

g = ""
attempts = 0

while g != password:
    g = ''.join(random.choice(chars) for _ in range(length))
    print(g)
    attempts += 1

    if g == password:
        print(f"{password} is equal to {g}")
        print(f"Number of attempts: {attempts}")
