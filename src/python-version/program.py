# 1.B.7 part 1, Anders P. Åsbø
import matplotlib.pyplot as plt
import numpy as np
from numba import jit
from AST2000SolarSystemViewer import AST2000SolarSystemViewer

seed = 31948  # generated using myseed.py from course website.
system = AST2000SolarSystemViewer(seed)

# Constants
G = 4*np.pi**2  # Gravitational constant in astronomical units.

# Simulation time set to orbital period of second outermost planet.
# T in years found solving Kepler's 3. law:
T = np.sqrt(system.a[2]**3/(system.star_mass+system.mass[2]))
# system.a[2] is the semimajor axis in au.
# system.star_mass is the mass of the parent star in solar masses.
# system.mass[2] is the mass of the planet in solar masses.

N = int(2e4)  # Number of time steps
dt = T/N  # time step in years


@jit(nopython=True)
def a(r):
    '''
    Function calculating gravitational acceleration in AU/year^2
    from Newton's law of universal gravity.
    '''
    d = np.sqrt(r[0]**2+r[1]**2)
    r_unit = r/d
    return -r_unit*G*sun_mass/d**2


@jit(nopython=True)
def integrate(T, dt, N, x0, y0, vx0, vy0, G, sun_mass):
    '''
    Function creating arrays for time, position and velocity,
    and solving orbital motion numerically using Euler-Cromer.
    '''
    t = np.linspace(0, T, N)  # array of time values.
    r = np.zeros((N, 2))  # array with calculated position vectors.
    v = np.zeros((N, 2))  # array with calculated velocity vectors.

    r[0, :] = [x0, y0]  # setting initial position vector [AU].
    v[0, :] = [vx0, vy0]  # setting initial velocity vector [AU/year].

    for i in range(N-1):
        '''
        Looping over time steps, and integrating
        velocity and position using Euler-Cromer.
        '''
        v[i+1, :] = v[i, :] + dt*a(r[i, :])
        r[i+1, :] = r[i, :] + dt*v[i+1, :]

    return t, r, v  # returning arrays with time, position and velocity values.


def find_analytical_orbit(N, k):
    '''
    Function calculating orbit of given planet using
    Kepler's first law formulated for the orbit of one object
    with respect to another.

    system.e[k] is the eccentricity of the relevant orbit.
    '''
    # creating array of positions:
    angles = np.linspace(0, 2.*np.pi, N)
    # calculating positions in polar coordinates:
    r_pos = system.a[k]*(1-system.e[k]**2)/(1+system.e[k]*np.cos(angles))

    # converting to kartesian coordinates:
    x_analytic = r_pos*np.cos(angles)
    y_analytic = r_pos*np.sin(angles)

    return x_analytic, y_analytic  # returning analytical solution


# creating array for exporting orbit data to AST2000SolarSystemViewer:
planet_pos = np.zeros(shape=(2, system.number_of_planets, N))

sun_mass = system.star_mass  # Mass of the parent star.

with open("system.txt", "w") as outfile:
    outfile.write(str(("star", system.star_mass)))
    for k in range(system.number_of_planets):  # looping over planets.

        # Initial values:
        x0 = system.x0[k]  # x-position at t = 0
        y0 = system.y0[k]  # y-position at t = 0
        vx0 = system.vx0[k]  # x-velocity at t = 0
        vy0 = system.vy0[k]  # y-velocity at t = 0

        # finding analytical solution:
        x_analytic, y_analytic = find_analytical_orbit(N, k)
        # integrating orbit:
        t, r, v = integrate(T, dt, N, x0, y0, vx0, vy0, G, sun_mass)
        planet_pos[0, k, :] = r[:, 0]
        planet_pos[1, k, :] = r[:, 1]

        # writing system info to file eccentricity for each planet.
        outfile.write(str((k, system.mass[k], system.a[k], (x0, y0),
                           (vx0, vy0), system.e[k])))
        outfile.write("")
        # plotting the analytic and numerical orbits:
        plt.plot(x_analytic, y_analytic, color="black", linewidth=3.0)
        plt.plot(r[:, 0], r[:, 1], label="%i" % k)


# system.orbit_xml(planet_pos, t)  # creating xml file for SSViewer

# Plotting star, labeling and displaying plot:
plt.plot(0, 0, 'bo', label='Star')
plt.title("Plot of orbits for %0.3f years" % T)
plt.xlabel("AU")
plt.ylabel("AU")
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()

# running example:
"""
$ python3 program.py
Writing xml with 20000 frames. (Skipping 0 for each).
Rotation factor is 0.13673548670387356 (IRL planets rotate 7 times faster).
"""
