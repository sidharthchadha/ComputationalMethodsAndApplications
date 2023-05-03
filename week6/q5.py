import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import integrate
import numpy as np

def dist(x1, x2, y1, y2):
      return max(1, np.abs(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1.5)))

def func(t, r):
  x = r[:6]
  p = r[6:]
  dx = p[:3]
  dy = p[3:]

  x1, x2, x3, y1, y2, y3 = x

  dpx1 = ((x2 - x1) / dist(x1, x2, y1, y2)) + ((x3 - x1) / dist(x1, x3, y1, y3))
  dpx2 = ((x1 - x2) / dist(x1, x2, y1, y2)) + ((x3 - x2) / dist(x2, x3, y2, y3))
  dpx3 = ((x1 - x3) / dist(x1, x3, y1, y3)) + ((x2 - x3) / dist(x2, x3, y2, y3))

  dpy1 = ((y2 - y1) / dist(x1, x2, y1, y2)) + ((y3 - y1) / dist(x1, x3, y1, y3))
  dpy2 = ((y1 - y2) / dist(x1, x2, y1, y2)) + ((y3 - y2) / dist(x2, x3, y2, y3))
  dpy3 = ((y1 - y3) / dist(x1, x3, y1, y3)) + ((y2 - y3) / dist(x2, x3, y2, y3))

  dp = np.array([dpx1, dpy1, dpx2, dpy2, dpx3, dpy3])
  return np.concatenate((dx, dy, dp))

#Plotting the lines
fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlim(-40,40)
ax.set_ylim(-40,40)
ax.set_facecolor(color='black')

# Frames of the Animation
def frame(i, graph):
  dx1, du1, dx2, du2, dx3, du3 = graph[:,i]

  pt1.set_offsets([dx1, du1])
  pt2.set_offsets([dx2, du2])
  pt3.set_offsets([dx3, du3])

  line1.set_xdata(graph[0,i-25:i])
  line1.set_ydata(graph[1,i-25:i])

  line2.set_xdata(graph[2,i-25:i])
  line2.set_ydata(graph[3,i-25:i])

  line3.set_xdata(graph[4,i-25:i])
  line3.set_ydata(graph[5,i-25:i])

  return pt1, pt2, pt3, line1, line2, line3


pt1  = ax.scatter([],[],c = 'g')
pt2  = ax.scatter([],[],c = 'r')
pt3  = ax.scatter([],[],c = 'b')

line1, = ax.plot([],[], 'g')
line2, = ax.plot([],[], 'r')
line3, = ax.plot([],[], 'b')


coff=    [8,0,-18,2,5,7]
ans = integrate.solve_ivp(func, (0, 1000),coff , t_eval = np.linspace(0, 1000, 1000), dense_output=True) 
X = ans.y
animation = FuncAnimation(fig, func=frame, frames= [i for i in range(len(X[0]))], interval=1, fargs =(X,))
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.show()