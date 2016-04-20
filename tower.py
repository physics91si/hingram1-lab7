
# this code plots the position, velocity, and acceleration of a droptower over time 


# first step is to get info about droptower into this doc

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt 

a = np.loadtxt('droptower_vdata.txt', unpack = True)

# This section of code declares the position, velocity, and acceleration
init_position = 30 
pos = integrate.cumtrapz(a[1, :], dx = 1, initial = 0)
acceleration = np.diff(a[1, :])

plt.plot(a[0, :], pos, 'r:', a[0, :], a[1, :], 'g--', a[0,1:11], acceleration)

plt.xlabel("Time(s)")
plt.show()

