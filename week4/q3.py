import numpy as np
from math import sin,cos
import matplotlib.pyplot as plt

err_forw = []
err_cent = []

# F"(x) = 2cos(x^2) - 4x^2(sinx^2)
def df2(x):
  return (2*cos(x**2))- (4*(x**2)*sin(x**2))


h_range  = np.linspace(0.001,0.01,50)
theort_f   = []
theort_c   = []

for h in h_range:
  max_err_forw = 0
  max_err_cent = 0
  max_th_f = 0
  max_th_c = 0

  for x in np.linspace(0,1,1000):
     #updating the value of maximum error if getting  greater error in [0,1]    
    cur_f = abs(cos(x**2)*2*x - ((sin((x+h)**2) - sin(x**2))/(1*h)))
    max_err_forw = max(cur_f,max_err_forw)    
    cur_c = abs(cos(x**2)*2*x - ((sin((x+h)**2) - sin((x-h)**2))/(2*h)))
    max_err_cent = max(cur_c,max_err_cent)
    
    i=0
    while i < h:
      #updating the value of maximum theortical error 
      cur_theor_f   = df2(x+i)*h/2
      max_th_f = max(abs(cur_theor_f), max_th_f)

      cur_theor_c   = df2(x-i)*h/2.0
      max_th_c = max(abs(cur_theor_f-cur_theor_c)/2, max_th_c)

      i=i+(h/10)


  err_forw.append(max_err_forw)
  err_cent.append(max_err_cent)
  theort_f.append(max_th_f)
  theort_c.append(max_th_c)

plt.plot(h_range,theort_f,'black',label="Theoretical Error -> Forward Difference")
plt.plot(h_range,theort_c,'r',label="Theoretical Error -> Centered Difference")
plt.plot(h_range,err_forw,'g',label='Max Error -> Forward Difference')
plt.plot(h_range,err_cent,'b',label="Max Error -> Centered Difference")

plt.legend()
plt.xlabel('h')
plt.ylabel("Error due to approximation")
plt.show()
 