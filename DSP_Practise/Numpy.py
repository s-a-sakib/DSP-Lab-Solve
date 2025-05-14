import matplotlib.pyplot as plt
import numpy as np

A = 5        # Amplitude
f = .5       # Frequency in Hz
W = np.pi/2  # Phase shift (90 degrees)
t = np.linspace(-2, 2, 1000)  # Time from -2 to 2 seconds, 1000 points

# Compute the signal
x = A * np.cos(2 * np.pi * f * t + W)
y = A * np.sin(2 * np.pi * f * t + W)
plt.figure(figsize=(8, 4))
plt.plot(t, x, label=r'$x = 5 \cos(2\pi (0.5)t + \pi/2)$', color='b')
plt.plot(t, y, label=r'$x = x * x', color='r')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Cosine Wave with Frequency & Phase Shift")
plt.legend()
plt.grid(True)
plt.show()