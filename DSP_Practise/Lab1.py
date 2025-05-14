import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 15)
omega_vals = [0.25*np.pi, 0.50*np.pi, 0.75*np.pi, 0.90*np.pi]
offset = 0.0

plt.figure(figsize=(6,5))
for i, omega in enumerate(omega_vals):
    plt.plot(n, np.sin(omega*n) + i*2, '-o', label=fr'$\omega={omega/np.pi:.2f}\pi$')
plt.legend(loc='upper right')
plt.xlabel('n')
plt.ylabel('Offset + sin($\omega n$)')
plt.title('Sinusoids at increasing $\omega$ (offset for clarity)')
plt.grid(True)
plt.show()

