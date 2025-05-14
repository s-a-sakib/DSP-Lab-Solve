import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x))

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Shift sine wave
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.title("Animated Sine Wave")
plt.grid(True)
plt.show()
