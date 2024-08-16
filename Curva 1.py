import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 2 * np.pi, 1000)

# Original astroid
x = np.cos(t)**3
y = np.sin(t)**3

# Involute of the astroid
xi = 1/8 * (3 * np.cos(t) - np.cos(3 * t))
yi = 1/8 * (3 * np.sin(t) + np.sin(3 * t))

# Plotting the original astroid and its involute
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Original Astroid', color='blue')
plt.plot(xi, yi, label='Involute of Astroid', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Original Astroid and Its Involute')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()