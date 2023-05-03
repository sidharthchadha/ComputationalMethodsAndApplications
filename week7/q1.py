import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def diffusion(step_size, start, end, time_step, diffusion_coefficient):
    # returns list containing the temperature distribution of the rod at each time step
    x_points = np.arange(start, end, step_size)
    time_points = np.arange(0, 1000, time_step)
    previous_u = []

    previous_u.append(np.exp(-x_points))

    previous_u[0][0] = 0
    previous_u[0][-1] = 0

    for i in range(1, len(time_points)):
        new_u = np.zeros(len(x_points))
        for j in range(1, len(x_points)-1):
            new_u_j = (diffusion_coefficient*(previous_u[-1][j-1] - 2*previous_u[-1][j] + previous_u[-1][j+1])/(step_size*step_size))
            new_u[j] = previous_u[-1][j] + time_step*new_u_j
        previous_u.append(new_u)

    return previous_u

u = diffusion(0.01, 0, 1, 15, diffusion_coefficient=  2.3*0.000001)    

# Update the data in the plot with the temperature distribution at each time step
def frame(i, u):
  im.set_array([u[i]])
  return [im]

frames=[]
for i in range(len(u)):
      frames.append(i)


fig, ax = plt.subplots()
im = ax.imshow([u[-1]], cmap = 'hot',aspect = 20)
ax.set_xlabel('unit rod')
ax.set_title('Heat Conduction')


animation = FuncAnimation(fig, frame, frames , interval = 1, fargs = (u, ))
plt.show()