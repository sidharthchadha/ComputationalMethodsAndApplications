import numpy as np
from array import *
import matplotlib.pyplot as plt
from math import exp,sin,cos

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result



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


  def __getitem__(self,i):

    sum  = 0
    prod = 1

    # Returns f(i) where i is given parameter
    for x in range(self.ord):
      sum  += self.coeff[x]*prod
      prod *= i

    return sum
  
  def __mul__(self,m):
      
    if isinstance(m,int) or isinstance(m,float):
      for x in range(self.ord):
        self.coeff[x] *= m

      return self

    if type(m) is Polynomial:
     
      l   = self.ord+m.ord-1
      lis = [0]*l

      t1  = self.coeff
      t2  = m.coeff

      #Powers get added, therefore multiplied elements get new power of x
      for x in range(len(t1)):
        for y in range(len(t2)):
          lis[x+y] += t1[x]*t2[y]
    

      return Polynomial(lis)

  
  def __rmul__(self,m):
  
    if isinstance(m,int) or isinstance(m,float):
      for x in range(self.ord):
        self.coeff[x] *= m

      return self

    if type(m) is Polynomial:
     
      l   = self.ord+m.ord-1
      lis = [0]*l

      t1  = self.coeff
      t2  = m.coeff

      for x in range(len(t1)):
        for y in range(len(t2)):
          lis[x+y] += t1[x]*t2[y]
    

      return Polynomial(lis)



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

  def derivative(self):
    d = []
    
    # Constant becomes 0
    for i in range(1,self.ord):
      d.append(i*self.coeff[i]) 

    return Polynomial(d)

  def area(self, a, b):

    I = [0]
    for i in range(self.ord):
      I.append(1.0*self.coeff[i]/(i+1))

    p = Polynomial(I)
    return p[b]-p[a]



def Legendre(n):
  l = Polynomial([1])
  for i in range(n):
    l = l * Polynomial([-1, 0, 1])

  for i in range(n):
    l = l.derivative()  # nth derivative

  # Calculating (1/(2^n*n!))
  result = l * (1/((2**n)*(factorial(n))))
  return result


# Ln(x) = (1/(2^n*n!))*(dn/dx^n(x^2 - 1)^n)
def leastSquare(n):
  legendre = []
  for i in range(n+1):
    legendre.append(Legendre(i))

  Q = Polynomial([0])
  for j in range(n+1):
    c_ = legendre[j] * legendre[j]
    cj  = c_.area(-1,1)
    
    x_ = np.linspace(-1, 1, 10000)
    aj = 0
    # Calculating integral
    for i in range(len(x_)-1):
      aj += (legendre[j][x_[i]]*exp(x_[i])) + (legendre[j][x_[i+1]]*exp(x_[i+1])) 
    
    aj *= 1/(10000*cj)
    # Summation of all the Polynomials
    Q  += aj*legendre[j]

  plt.plot(x_, np.exp(x_),'r',label='Actual function')
  Q.show(-1,1)
  
  
leastSquare(7) 

