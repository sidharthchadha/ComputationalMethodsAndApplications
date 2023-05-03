import numpy as np
from array import *
import matplotlib.pyplot as plt


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

  def __str__(self):
    s = ""
    for x in self.coeff:
      s += str(x)+" "
    return s
  
  def __getitem__(self,i):
        
    itr = 1
    ans  = 0
    x=0
    while x < self.ord:
      ans  += self.coeff[x]*itr
      itr *= i
      x=x+1

    return ans
  

  def check(self,v):
        if type(v) is Polynomial:
          pass
        else:
          raise Exception("Invalid")

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




# Chebyshev polynomials
def Chebyshev(n):
  #  T0
  if n==0:
    return Polynomial([1])

  #  T1
  if n==1:
    return Polynomial([0,1])

  # Initializing variables for T_{n-1} and T_{n-2}
  Tn_1 = Polynomial([0,1])
  Tn_2 = Polynomial([1])
  
  # calculating T_n using T_{n-1} and T_{n-2}
  for i in range(2, n+1):
    Tn = (2 * Polynomial([0,1]) * Tn_1) - Tn_2
    Tn_2 = Tn_1
    Tn_1 = Tn
  
  return Tn

def chebyshev_product(i, j, x):
    # i and j denote any two Chebyshev polynomials
    p = i * j
    return p[x] * (1 / (1 - x ** 2) ** 0.5)


# Calculate the first five Chebyshev polynomials
t = [Chebyshev(i) for i in range(5)]
 # Orthogonality test
for i in range(5):
  for j in range(i, 5):
   # Divide range into 10,000 points
    x = np.linspace(1, -1, 10000)

    # Calculate approximate integral
    Im=0
    for k in range(2, len(x)-1):
        Im = Im+chebyshev_product(t[i], t[j], x[k]) + chebyshev_product(t[i], t[j], x[k-1])
      
    Im *= 2 / (2.0 * 10000)  # Area under trapezoids
    print(f"Polynomial numbers: ({i}, {j}): {round(Im, 2)}")

