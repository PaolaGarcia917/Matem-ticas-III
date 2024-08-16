import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t for the epicycloid
t = np.linspace(0, 2 * np.pi, 1000)

# Parameters for the epicycloid
a = 1  # You can change 'a' to any positive value
b = 0.5  # You can change 'b' to any positive value

# Original epicycloid parametric equations
x = (a + b) * np.cos(t) - b * np.cos((a + b) / b * t)
y = (a + b) * np.sin(t) - b * np.sin((a + b) / b * t)

# Involute parametric equations
xi = (a + 2 * b) / a * ((a + b) * np.cos(t) - b * np.cos((a + b) / b * t))
yi = (a + 2 * b) / a * ((a + b) * np.sin(t) - b * np.sin((a + b) / b * t))

# Plotting the curves
plt.figure(figsize=(8, 8))

# Plot the original epicycloid
plt.plot(x, y, label="Epicycloid", color='blue')

# Plot the involute of the epicycloid
plt.plot(xi, yi, label="Involute of Epicycloid", color='red', linestyle='--')

# Axis settings
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Epicycloid and its Involute')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
