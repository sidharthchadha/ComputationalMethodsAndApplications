import numpy as np
import math
from math import sin,cos
import matplotlib.pyplot as plt

h     = 0.01 
interval = np.linspace(0,1,5000)

err1 = []
err2 = []
err3 = []

for x in interval:   
  err1.append(abs(cos(x**2)*2*x - ((sin((x+h)**2) - sin(x**2))/(h)))) #  2*x*cos(x^2) -> (forward difference)
  err2.append(abs(cos(x**2)*2*x - ((sin((x-h)**2) - sin(x**2))/(-1*h))) ) # 2*x*cos(x^2) -> (backward difference)
  err3.append(abs(cos(x**2)*2*x - ((sin((x+h)**2) - sin((x-h)**2))/(2*h))) ) # 2*x*cos(x^2) -> (centred difference)


plt.xlabel('x')
plt.ylabel("Error")
plt.plot(interval,err1,'b',label='Error of forward difference')
plt.plot(interval,err2,'g',label="Error of backward difference")
plt.plot(interval,err3,'r',label="Error of centered difference")
plt.legend()
plt.show()