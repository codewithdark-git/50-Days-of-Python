# Intermediate Python Practice Tasks

## String Manipulation Tasks

1. **String Reversal**
   - Create a function that reverses a string without using the built-in reversed() function
   - Handle empty strings and single characters
   - Example: "hello" → "olleh"

2. **Word Counter**
   - Write a function that counts the occurrence of each word in a sentence
   - Ignore case sensitivity
   - Remove punctuation
   - Example: "Hello hello WORLD!" → {'hello': 2, 'world': 1}

## List & Dictionary Comprehension Tasks

1. **Matrix Transformation**
   - Create a 3x3 matrix using list comprehension
   - Write a comprehension to transpose the matrix
   - Example: [[1,2,3], [4,5,6], [7,8,9]] → [[1,4,7], [2,5,8], [3,6,9]]

2. **Dictionary Filtering**
   - Given a dictionary of student scores, use comprehension to create a new dictionary with only passing grades (>60)
   - Example: {'John': 75, 'Jane': 55} → {'John': 75}

## Exception Handling Tasks

1. **Safe File Reader**
   - Create a function that safely reads a file
   - Handle FileNotFoundError, PermissionError, and other potential errors
   - Return None if file cannot be read
   - Log all errors to a separate error.log file

2. **Input Validator**
   - Create a custom exception class for input validation
   - Write a function that validates user age (must be between 0 and 150)
   - Handle TypeError for non-numeric inputs

## Lambda & Built-ins Practice

1. **Data Processing**
   - Given a list of dictionaries containing student information:
   ```python
   students = [
       {'name': 'Alice', 'age': 20, 'grade': 85},
       {'name': 'Bob', 'age': 22, 'grade': 91},
       {'name': 'Charlie', 'age': 21, 'grade': 82}
   ]
   ```
   - Use map to extract all names
   - Use filter to get students with grades above 85
   - Use reduce to calculate average age

2. **Function Composition**
   - Create three lambda functions that:
     - Doubles a number
     - Adds 5 to a number
     - Squares a number
   - Compose these functions to create a pipeline

## Final Project: Task Manager

Create a command-line task manager that demonstrates all learned concepts:

1. **Requirements:**
   - Store tasks in a JSON file
   - Use classes for Task and TaskManager
   - Implement exception handling for all operations
   - Use list comprehensions for task filtering
   - Implement lambda functions for task sorting

2. **Features:**
   - Add/remove tasks
   - Mark tasks as complete
   - List tasks with filters
   - Search tasks
   - Sort tasks by different criteria

3. **Bonus:**
   - Add due dates to tasks
   - Implement priority levels
   - Add task categories
   - Generate task statistics
