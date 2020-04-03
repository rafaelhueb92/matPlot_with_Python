# Visualization of Data in Python
import matplotlib.pyplot as plt

x=[1,2,5,4,2]
y=[2,3,7,1,0]

plt.title("My First Diagram With Python");

# Coordinates
plt.xlabel("Coordinate X");
plt.ylabel("Coordinate Y");

## plt.plot(x,y)
plt.bar(x,y);
plt.show();
