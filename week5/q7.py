import numpy as np
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



def calculate_coefficients(n):
    #Calculate Fourier coefficients for the given value of n.
    a, b = -np.pi, np.pi
    x = np.linspace(a, b, 10000)

    A = []
  
    for k in range(n + 1):
        ak = 0
        for i in range(len(x)):
            ak += (np.exp(x[i]) * np.cos(k * x[i]) + np.exp(x[i-1]) * np.cos(k * x[i-1]))

        ak *= ((b-a)/(2.0*10000)) * (1 / np.pi)
  
        A.append(ak)
    print("Coefficients ak:", A)
    B = []    
    for k in range(n + 1):
        bk = 0
        for i in range(len(x)):
            bk += (np.exp(x[i]) * np.sin(k * x[i]) + np.exp(x[i-1]) * np.sin(k * x[i-1]))

        bk *= ((b-a)/(2.0*10000)) * (1 / np.pi)

        B.append(bk)    
    
    print("Coefficients bk:", B)
    return A, B

def calculate_fourier(n):
    
    #Calculate Fourier transform for the given value of n.
    a, b = -np.pi, np.pi
    x = np.linspace(a, b, 10000)

    A, B = calculate_coefficients(n)

    f_actual = np.exp(x)
    f_fourier = np.zeros(len(x))

    for xi in range(len(x)):
        summation = 0
        for k in range(1, n+1):
            summation += (A[k] * np.cos(k * x[xi])) + (B[k] * np.sin(k * x[xi]))

        summation += A[0] / 2
        f_fourier[xi] = summation

    return x, f_actual, f_fourier

def plot_fourier(n):
  
    #Plot the Fourier transform for the given value of n.
    x, f_actual, f_fourier = calculate_fourier(n)

    plt.plot(x, f_fourier, label='Fourier Transform')
    plt.plot(x, f_actual, label='Actual function ')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('F(x) = e^x')
    plt.title('fourrier Approxn')
    plt.show()


plot_fourier(50)
