import matplotlib.pyplot as plt
import numpy as np

# Sample data for bar graph
categories = ['A', 'B', 'C', 'D']
values = [20, 34, 30, 35]

# 1. Bar Graph
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=['red', 'blue', 'green', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Graph")
plt.legend(["Values"], loc="upper right")
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()

# 2. Line Chart
x = ['A', 'B', 'C', 'D']
y = [20, 34, 30, 35] # Quadratic function

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b', label="y = x^2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Chart")
plt.legend()
plt.grid(True)
plt.show()

# 3. Histogram
data = np.random.randn(1000)  # Generating random data

plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='green', edgecolor='black', alpha=0.7)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()

# 4. Pie Chart
labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [35, 30, 20, 15]
colors = ["gold", "skyblue", "lightcoral", "lightgreen"]
explode = (0.1, 0, 0, 0)  # Highlight the first slice

plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
        startangle=140, explode=explode, shadow=True)
plt.title("Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
