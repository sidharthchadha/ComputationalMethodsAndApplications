import numpy as np
from array import *
import matplotlib.pyplot as plt

class Polynomial:
  def __init__(self,l):
    #attributes
    self.coeff = [] 
    for i in l:
      if type(i) is float or type(i) is int:
          self.coeff.append(i)     
      else:
            raise Exception("invlaid input")
            
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
    # Returns f(x) ,given x
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


  def fitViaMatrixMethod(self,l):
    ord = len(l)
    x_  = []
    A   = []
    b   = []

    # l is a list of x,y points
    for p in l:
      x_.append(p[0])
      b.append(p[1])
      row = []
      i   = 1
      for _ in range(ord):
        row.append(i)
        i *= p[0]
      A.append(row)

    # np function to solve
    x = (np.linalg.solve(np.array(A),np.array(b))).tolist()
    self.coeff = x
    self.ord  = ord

    # Plotting
    plt.scatter(x_,b,color='r')
    # spacing of 0.1
    x = np.arange(min(x_),max(x_)+0.1,0.1)
    y = []
    
    for i in x:
      y.append(self[i])
    # Plotting
    plt.plot(np.array(x),np.array(y),'b')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title(str(self.coeff)+"matrix method")
    plt.show()

  def fitViaLagrangePoly(self,l):
    x_  = []
    y_ = [] 
    for p in range(len(l)):
      x_.append(l[p][0])
      y_.append(l[p][1])
      it = Polynomial([1])
      x = l[p][0]
      y = l[p][1]
      it = it * y
    
      for q in range(len(l)):
        if p==q: 
          pass   
        else:  
          # Numerator -> (x - q[0]) form
          # Denominator ->  sum of product of respective x with coff.
           it = it * Polynomial([-1*l[q][0],1])
           it *= 1/(x-l[q][0])

      self += it
    self.ord = len(self.coeff)

    plt.scatter(x_,y_,color='r')
    # Taking x in given range at a spacing of 0.1
    x = np.arange(min(x_),max(x_)+0.1,0.1)
    y = []
    for i in x:
      y.append(self[i])

    # Plotting
    plt.plot(np.array(x),np.array(y),'b')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title(str(self.coeff)+"lagrange")
    plt.show()



p = Polynomial([1,2,4,5])
print(p)
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([3, 2, 1])
p3 = p1 - p2
print(p3)

p1 = Polynomial([1, 2, 3])
p2 = (-0.5)*p1
print(p2)
print(p2[2])

p1 = Polynomial([-1, 1])
p2 = Polynomial([1, 1, 1])
p3 = p1 * p2
print(p3)

p.fitViaMatrixMethod([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])
p = Polynomial([])
p.fitViaLagrangePoly([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])
