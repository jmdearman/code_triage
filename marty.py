import numpy as np
import h5py
import matplotlib.pyplot as plt

MILES_TO_FEET = 5280
METERS_TO_FEET = 1/.3049

# Simulation Data
nominal = h5py.File('touchdown_data.h5')
assert nominal['miss_x'].attrs['unit'] == 'm'  # ensure data is in meters
x = nominal['miss_x'][:] * METERS_TO_FEET
assert nominal['miss_y'].attrs['unit'] == 'm'
y = nominal['miss_y'][:] * METERS_TO_FEET
plt.plot(x, y, '.', label='simulation data')

# Accuracy Ellipse
a = 8/2*MILES_TO_FEET
b = 6/2*MILES_TO_FEET
x = np.zeros(1000)
y = np.zeros(1000)
for ii in range(0, 1000):
    t = ii/(2*np.pi)
    x[ii] = a*np.cos(t)
    y[ii] = b*np.sin(t)
plt.plot(x, y, label='accuracy requirement')

# Keepout Zone Ellipse
a = 20/2*MILES_TO_FEET
b = 7/2*MILES_TO_FEET
x = np.zeros(1000)
y = np.zeros(1000)
for ii in range(0, 1000):
    t = ii/(2*np.pi)
    x[ii] = a*np.cos(t)
    y[ii] = b*np.sin(t)
plt.plot(x, y, label='keepout zone')

plt.axhline(18480, linestyle='--', label='keepout zone should stop here!')
plt.axhline(-18480, linestyle='--', label='keepout zone should stop here!')

plt.xlabel('X Miss Distance (ft)')
plt.ylabel('Y Miss Distance (ft)')
plt.grid(True)
plt.axis('equal')
plt.legend()

plt.show()
