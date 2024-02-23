
def generate_flask_app():
    app_name = input("Enter your Flask app name: ")
    port = "" # input("Enter the port to run the server (default is 5000): ")
    if not port:
        port = 5000

    code = f"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port={port})
"""

    with open(f"{app_name}.py", "w") as file:
        file.write(code)

    print(f"Flask app '{app_name}' created in '{app_name}.py'!")

def generate_rest_api():
    api_name = input("Enter your REST API name: ")
    port = "" #input("Enter the port to run the API (default is 5000): ")
    if not port:
        port = 5000

    code = f"""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {{"message": "Hello, World!"}}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port={port})
"""

    with open(f"{api_name}.py", "w") as file:
        file.write(code)

    print(f"REST API '{api_name}' created in '{api_name}.py'!")


def generate_calculator_app():
    app_name = input("Enter your Calculator App name: ")
    port = "" #input("Enter the port to run the API (default is 5000): ")
    if not port:
        port = 5000

    code = f"""
import tkinter as tk

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

def calculate():
    operation = operation_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == "+":
        result_var.set(add(num1, num2))
    elif operation == "-":
        result_var.set(sub(num1, num2))
    elif operation == "*":
        result_var.set(multi(num1, num2))
    elif operation == "/":
        result_var.set(div(num1, num2))
    elif operation == "**":
        result_var.set(exp(num1, num2))
    elif operation == "%":
        result_var.set(mod(num1, num2))
    else:
        result_var.set("Invalid operation")

# Create the main Tkinter window
window = tk.Tk()
window.title("Calculator")

# Entry fields for numbers and result
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var)

# Operation dropdown menu
operation_var = tk.StringVar()
operation_var.set("+")  # Default operation
operations = ["+", "-", "*", "/", "%", "**"]
operation_menu = tk.OptionMenu(window, operation_var, *operations)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Arrange widgets in the window
entry_num1.pack()
entry_num2.pack()
operation_menu.pack()
calculate_button.pack()
result_label.pack()

window.mainloop()

"""

    with open(f"{app_name}.py", "w") as file:
        file.write(code)

    print(f"Calculator App '{app_name}' created in '{app_name}.py'!")

if __name__ == "__main__":
    while True:
        print("Code Generator Menu:")
        print("1. Generate Flask App")
        print("2. Generate REST API")
        print("3. Generate Calculator App")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_flask_app()
        elif choice == "2":
            generate_rest_api()
        elif choice == "3":
            generate_calculator_app()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
