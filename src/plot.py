import numpy as np
import matplotlib.pyplot as plt

N = 80000000
r = np.zeros((9, N, 2))
name = np.array(["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"])

for i in range(9):
    r[i, :, 0] = np.fromfile("X%i.bin" % i)
    r[i, :, 1] = np.fromfile("Y%i.bin" % i)

plt.figure()

for i in range(9):
    plt.plot(r[i, ::1000, 0], r[i, ::1000, 1], label="%s" % name[i])

plt.plot(0, 0, 'bo', label="Sun")

plt.xlabel("AU")
plt.ylabel("AU")
plt.title("Orbits of the Solar System")
plt.axis('equal')
plt.legend(loc=1)
plt.grid()

plt.show()
