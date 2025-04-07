# Initialize an empty dictionary to store student data
students = {}

# Function to display all student records
def display_dict(data):
    print("\nCurrent student records:")
    for name, score in data.items():
        print(f"{name}: {score}")

# Create (C)
n = int(input("Enter the number of students to add: "))
for _ in range(n):
    name = input("Enter student name: ")
    score = int(input(f"Enter {name}'s score: "))
    students[name] = score

display_dict(students)

# Read (R)
print("\nReading a specific student's score:")
name = input("Enter the student name to look up: ")
if name in students:
    print(f"{name}'s score is {students[name]}")
else:
    print(f"No record found for {name}.")

# Update (U)
print("\nUpdating a student's score:")
name = input("Enter the student name to update: ")
if name in students:
    new_score = int(input(f"Enter the new score for {name}: "))
    students[name] = new_score
    print(f"{name}'s score has been updated.")
else:
    print(f"No record found for {name}.")

display_dict(students)

# Delete (D)
print("\nDeleting a student's record:")
name = input("Enter the student name to delete: ")
if name in students:
    del students[name]
    print(f"Record for {name} has been deleted.")
else:
    print(f"No record found for {name}.")

display_dict(students)
