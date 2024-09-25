# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
-->
# Program to handle ZeroDivisionError
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)

Output :-
Enter numerator: 10
Enter denominator: 0
Error: Cannot divide by zero.


# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 
-->
# Program to handle ValueError for invalid integer input
try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("You entered:", number)

Output :-
Enter an integer: abc
Error: Invalid input. Please enter a valid integer.


# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
-->
# Program to handle FileNotFoundError
try:
    file_name = input("Enter the file name to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File content:\n", content)

Output :-
Enter the file name to open: non_existent_file.txt
Error: File not found.


# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
-->
# Program to handle TypeError for non-numeric inputs
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = float(num1) + float(num2)
except ValueError:
    print("Error: Invalid input. Please enter numerical values.")
else:
    print("Sum:", result)

Output :-
Enter the first number: 12
Enter the second number: abc
Error: Invalid input. Please enter numerical values.
