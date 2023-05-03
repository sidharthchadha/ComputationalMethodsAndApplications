import matplotlib.pyplot as plt
import numpy as np
from math import exp

range_=[]  # range of no of intervals to check(M) 
i=1
while i<5000:
      range_.append(i)
      i=i+1


def f(x):
  return 2*x*exp(x**2)


l = 1
h= 3
trapezoid  = []                         # Approximated Interval
abs_integral = []                         # Absolute Interval

for M in range_:
  # Calculate the approximate integral using trapezoid
  h = (h - l) / M
  x = [l + i * h for i in range(M+1)]
  Im = 0
  for k in range(1, M):
        Im += f(x[k])
  Im = h * (0.5 * f(x[0]) + Im + 0.5 * f(x[M]))

  trapezoid.append(Im)
  abs_integral.append(exp(h**2)-exp(l**2))


plt.plot(range_, trapezoid, label="Approximate Integral (Trapezoidal Formula)")
plt.plot(range_, abs_integral, label="Absolute Integral")
plt.legend()
plt.title('Integral of 2x e^(x^2)')
plt.xlabel('M')
plt.ylabel('Integral in the range [1,3]')
plt.show()

