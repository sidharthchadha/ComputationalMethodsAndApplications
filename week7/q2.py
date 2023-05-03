import numpy as np
import math
from math import exp, sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def func(xc, yc, i, j):
  return exp(-1*sqrt(((i-xc)**2) + ((j-yc)**2)))

def frame(i, u):
  im.set_array(u[i])
  return [im]

def diffusivity(step_size, start, end, time_step, x_center, y_center, viscosity):
    
  x_values = np.arange(start, end, step_size)
  y_values = np.arange(start, end, step_size)
  time_values = np.arange(0, 5, time_step)
  
  u = []
  u.append([[0]*len(x_values)]*len(y_values))

  # Iterate through each time value
  for _ in range(1, len(time_values)):
    new_u = [[0]*len(x_values)]
   
    for x_index in range(1, len(x_values)-1):
      new_row = [0]
     
      for y_index in range(1, len(y_values)-1):
        # Calculate new_uij
        diffusivity_value = viscosity*(u[-1][x_index+1][y_index] - 4*u[-1][x_index][y_index] + u[-1][x_index-1][y_index] + u[-1][x_index][y_index+1] + u[-1][x_index][y_index-1])/(step_size*step_size)
        function_value = func(x_center, y_center, x_values[x_index], y_values[y_index])
        new_uij = diffusivity_value + function_value
        new_row.append(u[-1][x_index][y_index] + time_step*new_uij)
      
      new_row.append(0)
      new_u.append(new_row)
    
    new_u.append([0]*len(x_values))
    u.append(new_u)

  return u


u = diffusivity(0.01, 0, 1, 0.05, 0.5,  0.5,  2.3*0.000001)

fig, ax = plt.subplots()
im = ax.imshow(u[-1], cmap = 'hot')

ax.set_title('Heat Conduction for Square Sheet')
ax.set_xlabel('X')
ax.set_ylabel('Y')

frames=[]
for i in range(len(u)):
      frames.append(i)



animation = FuncAnimation(fig, frame, frames, interval = 1, fargs = (u, ))
plt.show()