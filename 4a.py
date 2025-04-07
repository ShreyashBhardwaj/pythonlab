from statistics import mean, median, mode

# Function to calculate mean
def calculate_mean(numbers):
    return mean(numbers)

# Function to calculate median
def calculate_median(numbers):
    return median(numbers)

# Function to calculate mode
def calculate_mode(numbers):
    try:
        return mode(numbers)
    except:
        return "No unique mode (multiple or no repeating elements)"

# Input: Accept a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculations
mean_value = calculate_mean(numbers)
median_value = calculate_median(numbers)
mode_value = calculate_mode(numbers)

# Output results
print(f"\nNumbers: {numbers}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
