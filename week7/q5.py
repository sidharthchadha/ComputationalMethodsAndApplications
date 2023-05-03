import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv, norm
import numpy as np
from math import sin,cos,exp

def newton_raphson(x):
  y = []
  iteration=10
  x_values = np.array([x for x in range(1, iteration+1)])
  zero_array = np.array([0]*iteration)

  for i in range(iteration):
    x1, x2, x3 = x

    # The Jacobian Matrix 
    jacobian = [[3, x3*sin(x2*x3), x2*sin(x2*x3)], [8*x1, -625*2*x2, 2], [-x2*exp(-x1*x2), -x1*exp(-x1*x2), 20]]   
    jac_inv  = inv(np.array(jacobian)) #inverse

    Func     = np.array([3*x1-cos(x2*x3)-1.5, 4*x1*x1-625*x2*x2+2*x3-1, 20*x3+exp(-x1*x2)+9])

    x = x - np.dot(jac_inv, Func)
    y.append(norm(Func))

  print("Final x and y:", x, y[-1])

  # Plotting
  plt.plot(x_values, zero_array, label='Absolute Zero')
  plt.plot(x_values, np.array(y), label='Newton-Raphson Convergence')
  plt.title('Newton Raphson Method')
  plt.xlabel('Iterations')
  plt.ylabel('Value of function')
  plt.legend()  
  plt.show()


newton_raphson([2, 3, 1])


    