try:
    # Prompt user for their name
    user_name = input("Please enter your name: ")
    
    # Check if the input is a string
    if not isinstance(user_name, str):
        raise ValueError("The input is not a valid string.")
    
    print("Hello, " + user_name + "!")
except ValueError as e:
    print(e)
