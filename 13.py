from functools import reduce

# List Comprehension: Generate a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("List of squares:", squares)

# Map: Convert Celsius to Fahrenheit
temps_celsius = [0, 10, 20, 30, 40]
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
print("Temperatures in Fahrenheit:", temps_fahrenheit)

# Filter: Get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Reduce: Find the product of all numbers in a list
num_list = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, num_list)
print("Product of numbers:", product)
