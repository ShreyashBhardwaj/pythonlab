# Function to find duplicates in a list
def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Input: Accept a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find duplicates
duplicates = find_duplicates(numbers)

# Print values
print(f"\nNumbers: {numbers}")
if duplicates:
    print(f"Duplicate Values: {duplicates}")
else:
    print("No duplicate values found.")
