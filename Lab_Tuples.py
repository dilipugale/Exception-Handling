Tuple_Lab_Dilip_Ugale

#Q1)

# Create a tuple of studentId
student_ids = (101, 102, 103, 104, 105)

# Print the data
print("Student IDs:", student_ids)

#Q2)

# Create a tuple of hotel names in Mumbai
hotels_mumbai_1 = ("Taj", "Oberoi", "Marriott", "Hyatt", "Trident")
hotels_mumbai_2 = ("Marriott", "Taj", "Hilton", "ITC Grand", "Four Seasons")

# Concatenate the tuples
all_hotels_mumbai = hotels_mumbai_1 + hotels_mumbai_2

# Create a set from the concatenated tuple to remove duplicates
unique_hotels_mumbai = tuple(set(all_hotels_mumbai))

# Print the unique hotels
print("Unique Hotels in Mumbai:", unique_hotels_mumbai)

# Check for repetitions and print the count
for hotel in hotels_mumbai_2:
    if all_hotels_mumbai.count(hotel) > 1:
        print(f"{hotel} repeats {all_hotels_mumbai.count(hotel)} times")

#Q3)

# Creating a mixed type tuple
mixed_tuple = (101, "Mumbai", 23.5, "Delhi", 101)

# Membership operation
print(101 in mixed_tuple)  # True
print("Mumbai" not in mixed_tuple)  # False

# Repetition operation
repeated_tuple = mixed_tuple * 2
print("Repeated Tuple:", repeated_tuple)

#Q4)

import sys

# Creating a tuple
sample_tuple = (1, 2, 3, 4, 5)

# Finding the length of the tuple
length_of_tuple = len(sample_tuple)
print("Length of Tuple:", length_of_tuple)

# Finding the size of the tuple in memory
size_of_tuple = sys.getsizeof(sample_tuple)
print("Size of Tuple in Memory:", size_of_tuple, "bytes")

#Q5)

# Creating a tuple
sample_tuple = ("apple", "banana", "cherry", "date")

# Printing the tuple using different approaches
print("Tuple using print:", sample_tuple)

for item in sample_tuple:
    print("Tuple using loop:", item)

print("Tuple using join:", ", ".join(sample_tuple))

# Finding the value of a specific element
index = 2
specific_value = sample_tuple[index]
print(f"Value at index {index}:", specific_value)
