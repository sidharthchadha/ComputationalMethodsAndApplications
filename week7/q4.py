import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin

def func(x):
    return 18*x*x - 5*cos(5*x) + 1

def secant(initial_values):
  
    x = [initial_values[0], initial_values[1]]
    y = [func(x[0]), func(x[1])]
    error_tolerance = 0.00001

    # Perform the secant method iteration until convergence
    while abs(y[-1] - 0) > error_tolerance:
        if y[-1] == y[-2]:
            denominator = 0.000001
        else:
            denominator = y[-1] - y[-2]
        next_x = x[-1] - (y[-1] * ((x[-1] - x[-2]) / denominator))
        next_y = func(next_x)
        x.append(next_x)
        y.append(next_y)

    return y


def newton_raphson(x):
  y = [func(x)]
  while abs(y[-1]-0) > 0.00001:
    x =x- (func(x)/(36*x + 5*5*sin(5*x)))
    y.append(func(x))

  return y

sec_y = secant([3, 3.5])
newt_y = newton_raphson(3)

l = max(len(sec_y), len(newt_y))

#  x and y values to be plotted
sec_x = np.array(range(1, len(sec_y)+1))
newt_x = np.array(range(1, len(newt_y)+1))
abs_zero_x = np.array(range(1, l+1))
abs_zero_y = np.array([0]*l)

plt.plot(sec_x, np.array(sec_y), label='Secant Method Convergence')
plt.plot(newt_x, np.array(newt_y), label='Newton Raphson Method Convergence')
plt.plot(abs_zero_x, abs_zero_y, label='Absolute Zero')
plt.title('Secant Method vs Newton Raphson Method')
plt.xlabel('Number of Iterations')
plt.ylabel('Function Value')
plt.legend()  
plt.show()



