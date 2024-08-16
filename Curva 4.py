import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t for the deltoid
t = np.linspace(0, 2 * np.pi, 1000)

# Original deltoid parametric equations
x = (1/3) * (2 * np.cos(t) - np.cos(2 * t))
y = (1/3) * (2 * np.sin(t) - np.sin(2 * t))

# Involute of the deltoid parametric equations
xi = (1/9) * (2 * np.cos(t) - np.cos(2 * t))
yi = (1/9) * (2 * np.sin(t) + np.sin(2 * t))

# Rotation of the involute by 1/6 of a turn (π/3 radians)
theta_rotation = np.pi / 3
xi_rot = xi * np.cos(theta_rotation) - yi * np.sin(theta_rotation)
yi_rot = xi * np.sin(theta_rotation) + yi * np.cos(theta_rotation)

# Plotting the curves
plt.figure(figsize=(8, 8))

# Plot the original deltoid
plt.plot(x, y, label="Deltoid", color='blue')

# Plot the involute of the deltoid
plt.plot(xi_rot, yi_rot, label="Involute (Rotated & Scaled Deltoid)", color='red', linestyle='--')

# Axis settings
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Deltoid and its Involute')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
