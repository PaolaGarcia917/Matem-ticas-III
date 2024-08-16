import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t for the cardioid
t = np.linspace(0, 2 * np.pi, 1000)
a = 1  # You can change the value of 'a' to any positive number

# Original cardioid parametric equations
x = a * (1 + np.cos(t)) * np.cos(t)
y = a * (1 + np.cos(t)) * np.sin(t)

# Involute parametric equations
xi = 2 * a + 3 * a * np.cos(t) * (1 - np.cos(t))
yi = 3 * a * np.sin(t) * (1 - np.cos(t))

# Plotting the curves
plt.figure(figsize=(8, 8))

# Plot the original cardioid
plt.plot(x, y, label="Cardioid", color='blue')

# Plot the involute
plt.plot(xi, yi, label="Involute", color='red', linestyle='--')

# Axis settings
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Cardioid and its Involute')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()