from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import astropy.units.imperial as imp
from astropy.visualization import quantity_support
from datafile import DataFile


def ellipse(major, minor, n):
    """Return ellipse edge"""
    a = major/2
    b = minor/2
    t = np.linspace(0, 2*np.pi, n)
    return a*np.cos(t), b*np.sin(t)


data = DataFile('touchdown_data.h5')
xunits = imp.ft
yunits = imp.ft
npoints = 1000

fig, ax = plt.subplots()
with quantity_support():
    ax.plot(data['miss_x'], data['miss_y'], '.', 
            xunits=xunits, yunits=yunits, label='simulation data')

    x, y = ellipse(8*imp.mile, 6*imp.mile, npoints)
    ax.plot(x, y, label='accuracy requirement')

    x, y = ellipse(20*imp.mile, 7*imp.mile, npoints)
    ax.plot(x, y, label='keepout zone')

    ax.set_xlabel('X Miss Distance ({})'.format(ax.xaxis.units))
    ax.set_ylabel('Y Miss Distance ({})'.format(ax.yaxis.units))
    ax.grid(True)
    ax.axis('equal')
    ax.legend()

    plt.show()
