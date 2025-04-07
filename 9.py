import pandas as pd

# === Creating a DataFrame from a Dictionary ===
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 29],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 70000, 65000, 48000]
}

df = pd.DataFrame(data)
print("\n=== DataFrame from Dictionary ===")
print(df)

# === Saving DataFrame to a CSV file ===
# This creates 'employees.csv' automatically if it doesn't exist
df.to_csv("employees.csv", index=False)  # Save without index column

# === Reading DataFrame from the CSV file ===
df_csv = pd.read_csv("employees.csv")
print("\n=== DataFrame from CSV ===")
print(df_csv)

# === Filtering Data: Employees with Salary > 50,000 ===
filtered_df = df[df["Salary"] > 50000]
print("\n=== Employees with Salary > 50,000 ===")
print(filtered_df)

# === Grouping Data by Department to get Average Salary ===
grouped_df = df.groupby("Department")["Salary"].mean()
print("\n=== Average Salary per Department ===")
print(grouped_df)
