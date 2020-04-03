# Visualization of Data in Python
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

x1 = [2, 4, 6, 8, 10]
y1 = [5, 1, 3, 7, 4]

plt.title("My First Diagram With Python")

# Coordinates
plt.xlabel("Coordinate X")
plt.ylabel("Coordinate Y")

plt.bar(x, y, label="Group 1")
plt.bar(x1, y1, label="Group 2")
plt.show()
