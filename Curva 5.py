import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 4 * np.pi, 1000)

# Parameter b for the logarithmic spiral
b = 0.2  # You can change the value of 'b' to any positive number

# Original logarithmic spiral parametric equations
x = np.exp(b * t) * np.cos(t)
y = np.exp(b * t) * np.sin(t)

# Involute of the logarithmic spiral parametric equations
xi = (np.exp(b * t) * np.sin(t)) / b
yi = -(np.exp(b * t) * np.cos(t)) / b

# Plotting the curves
plt.figure(figsize=(8, 8))

# Plot the original logarithmic spiral
plt.plot(x, y, label="Logarithmic Spiral", color='blue')

# Plot the involute of the logarithmic spiral
plt.plot(xi, yi, label="Involute (Scaled & Rotated Spiral)", color='red', linestyle='--')

# Axis settings
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Logarithmic Spiral and its Involute')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
