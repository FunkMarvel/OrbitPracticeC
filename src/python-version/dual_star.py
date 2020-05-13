# 1.B.7 part 2, Anders P. Åsbø
import matplotlib.pyplot as plt
import numpy as np
from numba import jit
from AST2000SolarSystemViewer import AST2000SolarSystemViewer

# Constants
G = 4*np.pi**2  # Gravitational constant in astronomical units.

N = int(1e6)  # Number of time steps
dt = 1.26755059e-5  # time step in years
T = N*dt  # T in years found solving Kepler's 3. law:


@jit(nopython=True)
def a(r0, r1, r2, m1, m2):
    '''
    Function calculating gravitational acceleration in AU/year^2
    from Newton's law of universal gravity.
    '''
    ra = r0-r1
    d1 = np.sqrt(ra[0]**2+ra[1]**2)
    a1 = -ra*G*m1/d1**3

    rb = r0-r2
    d2 = np.sqrt(rb[0]**2+rb[1]**2)
    a2 = -rb*G*m2/d2**3

    return a1+a2


@jit(nopython=True)
def integrate(T, dt, N, rp, r1, r2, vp, v1, v2, G, mass):
    '''
    Function creating arrays for time, position and velocity,
    and solving orbital motion numerically using Euler-Cromer.
    '''
    t = np.linspace(0, T, N)  # array of time values.

    # creating array for exporting orbit data to AST2000SolarSystemViewer:

    mp = mass[0]
    m1 = mass[1]
    m2 = mass[2]
    for i in range(N-1):
        '''
        Looping over time steps, and integrating
        velocity and position using Euler-Cromer.
        '''
        vp[i+1, :] = vp[i, :] + dt*a(rp[i, :], r1[i, :], r2[i, :], m1, m2)
        rp[i+1, :] = rp[i, :] + dt*vp[i+1, :]

        v1[i+1, :] = v1[i, :] + dt*a(r1[i, :], rp[i+1, :], r2[i, :], mp, m2)
        r1[i+1, :] = r1[i, :] + dt*v1[i+1, :]

        v2[i+1, :] = v2[i, :] + dt*a(r2[i, :], rp[i+1, :], r1[i+1, :], mp, m1)
        r2[i+1, :] = r2[i, :] + dt*v2[i+1, :]

    return rp, r1, r2, t  # returning arrays with time and position values.


sun1_mass = 1.0  # mass of first star in solar masses.
sun2_mass = 4.0  # mass of second star in solar masses.
mp = 3.213e-7  # mass of planet in solar masses.
mass = [mp, sun1_mass, sun2_mass]

# arrays with calculated position vectors:
rp = np.zeros((N, 2))
r1 = np.zeros((N, 2))
r2 = np.zeros((N, 2))

# arrays with calculated velocity vectors:
vp = np.zeros((N, 2))
v1 = np.zeros((N, 2))
v2 = np.zeros((N, 2))

# Initial values:
rp[0, :] = [-1.49, 0]
r1[0, :] = [0, 0]
r2[0, :] = [3, 0]

vp[0, :] = [0, -0.210945021]
v1[0, :] = [0, 6.32835063]
v2[0, :] = [0, -1.58208766]

# integrating orbit:
rp, r1, r2, t = integrate(T, dt, N, rp, r1, r2, vp, v1, v2, G, mass)

d1 = rp-r1
d2 = rp-r2

distance1 = np.sqrt(d1[:, 0]**2+d1[:, 1]**2)
distance2 = np.sqrt(d2[:, 0]**2+d2[:, 1]**2)

close1 = np.min(distance1)
close2 = np.min(distance2)

print("Closest approach to star 1: %g au" % close1)
print("Closest approach to star 2: %g au" % close2)

plt.plot(rp[:, 0], rp[:, 1], label="planet")
plt.plot(r1[:, 0], r1[:, 1], label="star1")
plt.plot(r2[:, 0], r2[:, 1], label="star2")


# system.dual_star_xml(t, rp, r1, r2)  # creating xml file for SSViewer

# labeling and displaying plot:
plt.title("Plot of orbits for %0.3f years" % T)
plt.xlabel("AU")
plt.ylabel("AU")
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()

# running example:
"""
$ python3 dual_star.py
Closest approach to star 1: 0.1529 au
Closest approach to star 2: 0.0176667 au
Iterations completed...dumping to xml...
"""
