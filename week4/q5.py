from math import exp
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.integrate import *

#for the selection of variable upper bound on calculating area in interval  [0.u]
interval = np.linspace(0.001,3,100) 

actual     = []
trapezoid  = []
cumulative = []

for upper_bound in interval:
    evenly_strips = np.linspace(0, upper_bound, 1000)
    values = []
    for i in evenly_strips:
        values.append(2*i*exp(i**2))  #2xe^(x^2)
    
    trapezoid.append(scipy.integrate.trapezoid(values,evenly_strips))
    cumulative.append(scipy.integrate.cumulative_trapezoid(values,evenly_strips)[-1]) 
    actual.append(exp(upper_bound**2)- 1)    # e^(x^2)


plt.plot(interval,actual,'r',label='Absolute Integral')
plt.plot(interval,trapezoid,'g',label="Trapezoid")
plt.plot(interval,cumulative,'b',label="Cumulative")
plt.legend()
plt.xlabel('u')
plt.ylabel('Integral of 2xe^(x^2)')
plt.show()