import numpy as np
from math import sin,cos
import matplotlib.pyplot as plt

h = 0.01     
interval = np.linspace(0,1,5000)
actual_derivative  = []
forward_diff = []

# Calculating derivative 
for x in interval:    
  actual_derivative.append(2*x*cos(x**2))  # f'(x) = 2*x*cos(x^2)

#calculating the finite forward difference derivative 
for x in interval:              
  forward_diff.append(((sin((x+h)**2) - sin(x**2))/(1.0*h)))

plt.xlabel('x')
plt.ylabel("f'(x)")
plt.plot(interval,actual_derivative,'r',label='Actual Derivative')
plt.plot(interval,forward_diff,'g',label="Finite Forward Difference")
plt.legend()

plt.show()