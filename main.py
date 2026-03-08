import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81  # gravity (m/s^2)
y0 = 100  # initial height (meters)

# time array
t = np.linspace(0, 5, 100)

# falling sphere equation
y = y0 - 0.5 * g * t**2

# prevent negative height
y[y < 0] = 0

# plot
plt.plot(t, y)
plt.title("Falling Sphere Simulation")
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.grid()

plt.show()