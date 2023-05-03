import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import integrate
import numpy as np

def f(t, r, mu):
  x, u = r
  dx = u                  # x'(t) = u
  du = mu*(1-x**2)*u 
  return dx, du-x

# Frames of the animation
def frame(i, graph):
  dx1 = graph[0][0][i]
  du1 = graph[0][1][i]
  dx2 = graph[1][0][i]
  du2 = graph[1][1][i]
  dx3  = graph[2][0][i]
  du3 = graph[2][1][i]
  dx4  = graph[3][0][i]
  du4 = graph[3][1][i]

  pt1.set_offsets([dx1, du1])
  line1.set_xdata(graph[0][0])
  line1.set_ydata(graph[0][1])

  pt2.set_offsets([dx2, du2])
  line2.set_xdata(graph[1][0])
  line2.set_ydata(graph[1][1])

  pt3.set_offsets([dx3, du3])
  line3.set_xdata(graph[2][0])
  line3.set_ydata(graph[2][1])

  pt4.set_offsets([dx4, du4])
  line4.set_xdata(graph[3][0])
  line4.set_ydata(graph[3][1])

  return pt1, pt2, pt3, pt4, line1, line2, line3, line4

fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_facecolor(color='black')

pt1  = ax.scatter([],[],c = 'r')
pt2  = ax.scatter([],[],c = 'r')
pt3  = ax.scatter([],[],c = 'r')
pt4  = ax.scatter([],[],c = 'r')

line1, = ax.plot([],[], 'g')
line2, = ax.plot([],[], 'g')
line3, = ax.plot([],[], 'g')
line4, = ax.plot([],[], 'g')

graph = []
for i in range(4):
    if i%2:
      x = -i
    else:
      x = i

    sol = integrate.solve_ivp(f, [0, 40], [x, x-0.5], max_step=0.01, args=(5,), t_eval=np.linspace(0, 40, 500))
    t = sol.t
    dx, du = sol.y
    roots = []

    for i in range(1, len(t)):
        if (du[i]*du[i-1] < 0):
            roots.append((t[i]+t[i-1])/2)

    period = roots[-1] - roots[-3]
    graph.append((dx, du))

animation = FuncAnimation(fig, func=frame, frames= [i for i in range(len(t))], interval=1, fargs =(graph,))
plt.xlabel('x(t)')
plt.ylabel('dx/dt')
plt.title('mu = 5 and Time Period '+str(round(period,4)))
plt.show()

