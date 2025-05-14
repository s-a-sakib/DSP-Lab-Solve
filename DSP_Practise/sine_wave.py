import matplotlib.pyplot as plt
import numpy as np
A = 5         # Amplitude
f = 2         # Frequency in Hz
W = np.pi/2   # Phase shift (90 degrees)
t = np.linspace(0, 2, 1000)  # Time from 0 to 2 seconds, 1000 points

# Compute the signal
x = A * np.sin(2 * np.pi * f * t + W)
y = x*x
# Plot the signal
plt.figure(figsize=(8, 4))
plt.plot(t, y, label=r'$x = 5 \sin(2\pi (2)t + \pi/2)$', color='b')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave with Frequency & Phase Shift")
plt.legend()
plt.grid(True)
plt.show()