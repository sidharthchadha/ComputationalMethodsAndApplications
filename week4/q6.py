import numpy as np
from array import *
import matplotlib.pyplot as plt

class Polynomial:
  def __init__(self,l):
    #attributes
    self.coeff = [] 
    self.integral_area=0
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
  
    return ( "Area :" +str(self.integral_area) )


p = Polynomial([1, 2, 3])
pd = p.derivative()
print(pd)

p = Polynomial([1, 2, 3])
print(p.area(1,2))