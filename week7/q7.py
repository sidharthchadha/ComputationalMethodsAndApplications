import numpy as np
from array import *
import matplotlib.pyplot as plt
import random
import math
from math import cos,pi
import numpy as np
from array import *
import matplotlib.pyplot as plt


class Polynomial:
  def __init__(self,l):
    #attributes
    self.coeff = [] 
    self.integral_area=0
    for i in l:
      self.coeff.append(i)     
    
    self.ord = len(l)         

  def __str__(self):
    s = ""
    for x in self.coeff:
      s += str(x)+" "
    return s
  
  def check(self,v):
        if type(v) is Polynomial:
          pass
        else:
          raise Exception("Invalid")
        

  def __getitem__(self,i):
    
    itr = 1
    ans  = 0
    x=0
    while x < self.ord:
      ans  += self.coeff[x]*itr
      itr *= i
      x=x+1

    return ans      

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
  def show(self,a,b):
    
    if a>=b:
      raise Exception('Invalid Range.')
    x = np.arange(a,b,0.01)
    y = []
    
    for i in x:
      y.append(round(self[i],4))
    plt.plot(np.array(x),np.array(y))
      
  def derivative(self):
    d = []
    i=1
    while i < self.ord:
      d.append(i*self.coeff[i]) 
      i=i+1
    
    return Polynomial(d)

  def area(self, a, b):
 
    Integral_coeff = [0] 
    for i in range(self.ord):
      Integral_coeff.append(1.0*self.coeff[i]/(i+1))
    
    val_b=0
    itr=1
    x=0
    while x < len(Integral_coeff):
          val_b=val_b+Integral_coeff[x]*itr
          itr=itr*b
          x=x+1

    val_a=0
    itr=1
    x=0
    while x < len(Integral_coeff):
          val_a=val_a+Integral_coeff[x]*itr
          itr=itr*a
          x=x+1  

    self.integral_area=abs(val_b-val_a)          
    return ( "Area :" +str(abs(val_b-val_a)) )
    

  def best_fit(self,points, degree):
    matrix_a = []
    matrix_b = []

    for j in range(degree + 1):
        row = [sum(point[0] ** (j + k) for point in points) for k in range(degree + 1)]
        matrix_a.append(row)
        
        yk = sum(point[1] * (point[0] ** j) for point in points)
        matrix_b.append(yk)

    coefficients = np.linalg.solve(matrix_a, matrix_b)
    for _ in coefficients:
       print(_)
       
    polynomial = Polynomial(coefficients)
    polynomial.show(0, 10)

    return polynomial

  def printroots(self, f, a, b):
    polynomial = self
    derivative = polynomial.derivative()

    x_values = []
    for i in range(len(polynomial.coeff)):
        x_values.append(a + b * random.random())

    while True:
        new_x_values = []
        flag = 0

        for i in range(len(x_values)):
            if x_values[i] >= a and x_values[i] <= b and abs(f(x_values[i])-0) > 0.00001:  # error tolerance
                flag += 1
                break

        if flag == 0:
            break

        for i in x_values:
            sum = 0
            for j in x_values:
                if j != i:
                    sum += (1 / (i - j))

            if derivative[i] == 0:
                divisor = 0.001
            else:
                divisor = derivative[i]

            if 1 - (sum * (polynomial[i] / divisor)) == 0:
                denominator = 0.001
            else:
                denominator = 1 - (sum * (polynomial[i] / divisor))

            x_input = i - ((polynomial[i] / divisor) / denominator)
            if abs(x_input) > 50:
                x_input = 50 * x_input / abs(x_input)
            else:
                x_input = min(x_input, 50)
            new_x_values.append(x_input)

        x_values = sorted(new_x_values)

    answer = []

    for i in x_values:
        if i >= a - 0.001 and i <= b + 0.001:
            answer.append(i)

    print("The roots of the polynomial:", answer)


def roots(f, a, b):
  p = Polynomial([])
  x = np.arange(a, b, 0.1)
  pts = []

  for i in x:
    pts.append([i, f(i)])

  p = p.best_fit(pts, 10)
  p.printroots(f, a, b)


roots(cos, -3, 1)
#taking continous function to be cos
  

      