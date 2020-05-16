import numpy as np
import matplotlib.pyplot as plt

X = np.fromfile("X.bin")
Y = np.fromfile("Y.bin")

plt.figure()

plt.plot(X[::10], Y[::10], label="Earth")
plt.plot(0, 0, 'bo', label="Sun")

plt.xlabel("AU")
plt.ylabel("AU")
plt.title("Earth orbit")
plt.axis('equal')
plt.legend()
plt.grid()

plt.show()
