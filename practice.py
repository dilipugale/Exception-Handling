# Initialize a counter variable
counter = 1

# Start a while loop that runs as long as counter is less than or equal to 5
while counter <= 5:
    # Check if the counter is an even number
    if counter % 2 == 0:
        print(counter, "is even")
    else:
        print(counter, "is odd")
    
    # Increment the counter by 1
    counter += 1
