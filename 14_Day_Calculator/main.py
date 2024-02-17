def add(x, y):
  return x + y


def sub(x, y):
  return x - y


def multi(x, y):
  return x * y


def div(x, y):
  if y == 0:
    return "Cannot divide by zero"
  return x / y


def exp(x, y):
  return x**y


def mod(x, y):
  return x % y


while True:
  print("Options:")
  print("Enter '+' for addition")
  print("Enter '-' for subtraction")
  print("Enter '*' for multiplication")
  print("Enter '/' for division")
  print("Enter '**' for Exponential ")
  print("Enter '%' for Modulus")
  print("Enter 'quit' to end the program")

  user_input = input(" Enter The Operation : ")

  if user_input == "quit":
    break
  elif user_input in ("+", "-", "*", "/", "%", "**"):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if user_input == "+":
      print("Result:", add(num1, num2))
    elif user_input == "-":
      print("Result:", sub(num1, num2))
    elif user_input == "*":
      print("Result:", multi(num1, num2))
    elif user_input == "/":
      print("Result:", div(num1, num2))
    elif user_input == "**":
      print("Result:", exp(num1, num2))
    elif user_input == "%":
      print("Result:", mod(num1, num2))
  else:
    print("Invalid input")
