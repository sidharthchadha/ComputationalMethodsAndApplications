import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def compute_trajectory(g, L, theta0, a=0, b=10, ds=[0.01]):
        x, y, t = [], [], []
        h=0.01
        t_vals = np.arange(a, b, h)  
        theta_vals, alpha_vals = compute_angles_and_velocities(g, L, theta0, h, t_vals)
        x_vals, y_vals = compute_coordinates(L, theta_vals)
        x.extend(x_vals)
        y.extend(y_vals)
        t.extend(t_vals)
        return x, y, t

def compute_angles_and_velocities(g, L, theta0, h, t_vals):
    theta_vals, alpha_vals = [theta0], [0]
    for i in t_vals[1:]:
        tn = theta_vals[-1] + h * alpha_vals[-1]  
        an = alpha_vals[-1] + (h * (g / L) * math.sin(theta_vals[-1]))  
        theta_vals.append(tn)
        alpha_vals.append(an)
    return theta_vals, alpha_vals

def compute_coordinates(L, theta_vals):
    x_vals = [L * math.sin(theta) for theta in theta_vals]
    y_vals = [L - (L * math.cos(theta)) for theta in theta_vals]
    return x_vals, y_vals

fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlim(-2.5,2.5)
ax.set_ylim(-1, 3)

def frame(i,x,y,L):
    line1.set_offsets([x[i], y[i]])
    line2.set_xdata([0,x[i]])
    line2.set_ydata([L,y[i]])
    line3.set_xdata([-1,1])
    line3.set_ydata([L,L])

    return line1, line2, line3

line1 = ax.scatter([],[],c = 'black', marker = 'o', s = 100)
line2, = ax.plot([],[],'g')
line3, = ax.plot([],[],'black')
x, y, t = compute_trajectory(-9.81, 2, math.pi/8)
animation = FuncAnimation(fig, func=frame, frames= [i for i in range(len(t))], interval=1, fargs=(x,y,2,))
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.show()