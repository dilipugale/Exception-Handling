# Initialize the starting number
num = 20

# Start the while loop
while num >= 0:
    # Check if the current number is 9
    if num == 9:
        # Skip the number 9 and decrement the number
        num -= 1
        continue
    
    # Print the current number
    print(num)
    
    # Decrement the number
    num -= 1
