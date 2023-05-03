import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from array import *
from scipy.interpolate import *
import math
import random

def generate_true(x_true):
    y_fntrue, y_polytrue =  [], []
    for x in x_true:
        y_fntrue.append(math.tan(x)*math.sin(50*x)*math.exp(x))
        y_polytrue.append((3*(x**3))-(7*x**2)-(2*x)+5.5)
    return  y_fntrue, y_polytrue

# Function to define the frames of animation
def frame(i,t):

    t =t+ str(i+1)+" samples" 
    x_ax = np.linspace(0, 1, num=100)  # X-axis
    # slicing the x_observed and y_observed arrays up to the i+2-th element.
    ar_x=np.array(x_observed[:i+2])
    ar_y=np.array(y_observed[:i+2])
    sorted_indices = np.argsort(ar_x)  #sorting x wrt y
    y_sort = ar_y[sorted_indices]
    x_sort = np.sort(ar_x)     

    y1 = barycentric_interpolate(x_observed[:i+2], y_observed[:i+2], x_ax)  # Every Iteration we add one new point
    line1.set_xdata(x_ax)
    line1.set_ydata(y1)

    line2.set_xdata(x_ax)
    y2 = Akima1DInterpolator(x_sort,y_sort)
    line2.set_ydata(y2(x_ax))

    line3.set_xdata(x_ax)
    y3 = CubicSpline(x_sort, y_sort)
    line3.set_ydata(y3(x_ax))

    line4.set_xdata(x_true)
    y4 = y_true
    line4.set_ydata(y4)

    return line1, line2, line3, line4, #returns lines we plotted

#Generating Datasets
x_observed = []
y_function      = []
y_poly     = []

x_true = np.linspace(0,1,100)

for i in range(0,50):
    # 50 random points in range 0,1
    x = random.random()
    x_observed.append(x)

    # Functions Applied on x
    y_function.append(math.tan(x)*math.sin(50*x)*math.exp(x))
    y_poly.append((3*(x**3))-(7*x**2)-(2*x)+5.5)

# These are the true values
y_fntrue , y_polytrue =generate_true(x_true) 

# One animation for each function on x
y1=(y_fntrue,y_function,"tan(x).sin(50x).e^x")

    
y_true     = y1[0]
y_observed = y1[1]
#Plotting the lines
fig, ax = plt.subplots(figsize=(8,8))
    
line1, = ax.plot([],[],'r',label='Barycentric')
line2, = ax.plot([],[],'g',label='Akima')
line3, = ax.plot([],[],'yellow',label='Cubic')
line4, = ax.plot([],[],'blue',label='True')
ax.set_xlim(0.0,1.0)
ax.set_ylim(-10,10)
animation = FuncAnimation(fig, func=frame, frames= 50, interval=300, fargs=("Interpolations of "+y1[2]+" for ",))

plt.legend()
plt.xlabel("x")
plt.ylabel("y=f(x)")
plt.show()

y2=(y_polytrue,y_poly,"3x^3 - 7x^2 - 2x + 5.5")

y_true     = y2[0]
y_observed = y2[1]
#Plotting the lines
fig, ax = plt.subplots(figsize=(8,8))
    
line1, = ax.plot([],[],'r',label='Barycentric')
line2, = ax.plot([],[],'g',label='Akima')
line3, = ax.plot([],[],'yellow',label='Cubic')
line4, = ax.plot([],[],'blue',label='True')
ax.set_xlim(0.0,1.0)
ax.set_ylim(-10,10)
animation = FuncAnimation(fig, func=frame, frames= 50, interval=300, fargs=("Interpolations of "+y2[2]+" for ",))

plt.legend()
plt.xlabel("x")
plt.ylabel("y=f(x)")
plt.show()
