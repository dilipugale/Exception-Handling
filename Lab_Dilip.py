Q1)

#Create a list of city names
cities = ["India","Russia","London","Dubai","Mumbai","Toronto","Paris","New York","Sydney"]

#create : Add a new city to the list.
cities.append("Berlin")
print("After adding Berlin:",cities)

#Read : Access a city from the list.
print("The city at index 2 is:",cities[2])

# Update: Change the name of a city
cities[3] = "Kyoto"
print("After updating Tokyo to Kyoto:",cities)

# Delete: Remove a city from the list
cities.remove("Dubai")
print("After removing Dubai:",cities)


Q2)

# Create a mixed list
mixed_list = [1, "two", 3.0, True, None]

# Change the value of the third index to another data type value
mixed_list[2] = "three"
print("After changing the third index to a string:",mixed_list)

Q3)

# Create a list of country names
countries = ["USA", "Canada", "India", "Germany", "Australia", "Brazil", "Japan", "China"]

# Reverse the list
countries.reverse()
print("Reversed list of countries:", countries)

# Print only middle elements from the list
middle_elements = countries[len(countries)//4:3*len(countries)//4]
print("Middle elements from the list:", middle_elements)

Q4)

# Create a list of pin-codes
pin_codes = [110001, 560001, 400001, 600001, 700001, 500001, 380001, 226001]

# Delete the last pin-code
pin_codes.pop()
print("After deleting the last pin-code:", pin_codes)

# Delete the user-required pin-code (let's assume the user wants to delete 400001)
pin_codes.remove(400001)
print("After deleting pin-code 400001:",pin_codes)

Q5)

# Create a list of student names
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Append a new student
students.append("Frank")
print("After appending Frank:", students)

# Insert a student at a specific position
students.insert(2, "Grace")
print("After inserting Grace at index 2:", students)

# Extend the list with another list of students
more_students = ["Hannah", "Ivy"]
students.extend(more_students)
print("After extending with more students:", students)

# Remove a student by name
students.remove("Alice")
print("After removing Alice:", students)

# Pop a student from the list
popped_student = students.pop()
print("After popping a student:", students)
print("Popped student:", popped_student)

# Find the index of a student
index_of_david = students.index("David")
print("Index of David:", index_of_david)

# Count occurrences of a student
count_of_bob = students.count("Bob")
print("Count of Bob:", count_of_bob)

# Sort the list of students
students.sort()
print("After sorting:", students)

# Reverse the list of students
students.reverse()
print("After reversing:", students)

# Clear the list of students
students.clear()
print("After clearing the list:", students)
