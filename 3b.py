# Tuple Packing
name = "Alice"
age = 30
country = "Wonderland"
packed_tuple = (name, age, country)
print("Packed Tuple:", packed_tuple)

# Tuple Unpacking
name, age, country = packed_tuple
print("\nUnpacked Values:")
print("Name:", name)
print("Age:", age)
print("Country:", country)

# Nested Tuples
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
print("\nNested Tuple:", nested_tuple)

# Accessing Elements in Nested Tuples
print("\nAccessing Elements in Nested Tuple:")
print("First element of first tuple:", nested_tuple[0][0])
print("Second element of second tuple:", nested_tuple[1][1])

# Safe access with index check
try:
    print("Third element of third tuple:", nested_tuple[2][2])
except IndexError:
    print("Third element of third tuple: IndexError - element does not exist.")

# Iterating Over Nested Tuples
print("\nIterating over nested tuple:")
for sub_tuple in nested_tuple:
    print("Sub-tuple:", sub_tuple)
