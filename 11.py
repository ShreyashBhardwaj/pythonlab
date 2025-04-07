import sqlite3

# Connect to SQLite (creates a database file if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
""")
conn.commit()

# Insert data
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
               ("Alice", 30, "HR"))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
               ("Bob", 25, "IT"))
conn.commit()

# Fetch and display data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Employee Records:")
for row in rows:
    print(row)

# Update a record
cursor.execute("UPDATE employees SET age = 35 WHERE name = 'Alice'")
conn.commit()

# Delete a record
cursor.execute("DELETE FROM employees WHERE name = 'Bob'")
conn.commit()

# Fetch updated data
cursor.execute("SELECT * FROM employees")
print("\nUpdated Employee Records:")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
