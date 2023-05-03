import numpy as np
from math import exp,cos, sin
from array import *
import matplotlib.pyplot as plt
import math


class Polynomial:
   
  def __init__(self,l):
    self.coeff = []
    if type(l) is not list:
      raise Exception('l should be a List.')

    for x in l:
      if (not isinstance(x,int)) and (not isinstance(x,float)):
        raise Exception('invalid input')
    
    for i in l:
      self.coeff.append(i);
               # Coefficients with coeff[i] being coeffecient of x^i
    self.ord = len(l)         # Order of polynomail
  def check(self,v):
        if type(v) is Polynomial:
          pass
        else:
          raise Exception("Invalid")  

  def __str__(self):
    s = ""
    for x in self.coeff:
      s += str(x)+" "
    return s

  def __add__(self,v):
    self.check(v)

    lis = []
    l   = min(self.ord,v.ord)
    for x in range(l):
      lis.append(self.coeff[x]+v.coeff[x])

    # Polynomials of different orders can be added
    if v.ord > self.ord:
      for x in range(self.ord,v.ord):
        lis.append((v.coeff[x]))

    if v.ord < self.ord:
      for x in range(v.ord,self.ord):
        lis.append(self.coeff[x])
      
    return Polynomial(lis)

  def __sub__(self,v):
    self.check(v)
    lis = []
    l   = min(self.ord,v.ord)
    for x in range(l):
      lis.append(self.coeff[x]-v.coeff[x])

    if v.ord < self.ord:
      for x in range(v.ord,self.ord):
        lis.append(self.coeff[x])


    if v.ord > self.ord:
        for x in range(self.ord,v.ord):
            lis.append((-1*v.coeff[x]))    
      
    return Polynomial(lis)

  def __mul__(self,m):
        
    if type(m) is float:
      for x in range(self.ord):
          self.coeff[x] *= m
      return self    
    
    if type(m)  is Polynomial:
      l   = self.ord+m.ord-1
      lis = [0]*l

      coff1  = self.coeff
      coff2  = m.coeff

      #  multiplied elements get new power of x
      for x in range(len(coff1)):
        for y in range(len(coff2)):
          lis[x+y] += coff1[x]*coff2[y]

      return Polynomial(lis)
  
    if type(m) is int:
      for x in range(self.ord):
          self.coeff[x] *= m
      return self

  def __rmul__(self,m):

    if type(m) is float:
      for x in range(self.ord):
            self.coeff[x] *= m
      return self    
  
    if type(m) is Polynomial:
      l   = self.ord
      l=l+m.ord-1
      lis = [0]*l

      coff1  = self.coeff
      coff2  = m.coeff

      for x in range(len(coff1)):
        for y in range(len(coff2)):
          lis[x+y] =lis[x+y] + coff1[x]*coff2[y]
  
      return Polynomial(lis)
    
    if type(m) is float:
        for x in range(self.ord):
            self.coeff[x] *= m
        return self

  def __getitem__(self,i):
        
    itr = 1
    ans  = 0
    x=0
    while x < self.ord:
      ans  += self.coeff[x]*itr
      itr *= i
      x=x+1

    return ans

  def show(self,a,b):
    x = np.arange(a,b,0.01)  #equal spacing
    y = []
    
    for i in x:
      y.append(self[i])

    # Plotting
    plt.title("Best Fit Polynomial")
    plt.plot(np.array(x),np.array(y),'b', label='Best Fit Curve')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.legend()
    plt.show()


degree=10
A  = []

for j in range(degree+1):
  row = [] # contain the equation of some degree provided
  l = np.linspace(0, math.pi, 10000)
  for k in range(degree+1):
    sum = 0
    for i in range(len(l)-1):
      sum += l[i]**(j+k) + l[i+1]**(j+k)

    sum =sum* math.pi
    sum=sum/20000
    row.append(sum)
  A.append(row)

B  = []
x_values = []
y_values = []
for j in range(degree+1):
  sum = 0
  for i in range(len(l)-1):
    x_values.append(l[i])
    y_values.append((np.sin(l[i])+np.cos(l[i])))
    sum += (l[i]**j)*(np.sin(l[i])+np.cos(l[i])) + (l[i+1]**j)*(np.sin(l[i+1])+np.cos(l[i+1]))
    
  sum *= (math.pi/(2*len(l)))
  B.append(sum)

plt.plot(l, np.sin(l)+np.cos(l),'r' ,label = 'Actual function')
Polynomial(list(np.linalg.solve(A, B))).show(0, math.pi)
plt.show()
  


