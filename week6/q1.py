import copy
import numpy as np
from array import *
import matplotlib.pyplot as plt

class Polynomial:
   
  def __init__(self,l):

    if not isinstance(l,list):
      raise Exception('<class \'Exception\'>\nInput should be a List.')

    for x in l:
      if (not isinstance(x,int)) and (not isinstance(x,float)):
        raise Exception('<class \'Exception\'>\nInput should be a Integer/Float List.')

    self.coeff = l            # Coefficients with coeff[i] being coeffecient of x^i
    self.ord = len(l)         # Order of polynomail

  def __str__(self):

    s = "Coefficients of the polynomial are:\n"
    for x in self.coeff:
      s += str(x)+" "

    return s

  def __add__(self,v):


    if not isinstance(v,Polynomial):
      raise Exception('<class \'Exception\'>\nCan add only Polynomials.')

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

    print(self.ord,v.ord)

    if not isinstance(v,Polynomial):
      raise Exception('<class \'Exception\'>\nCan add only Polynomials.')

    lis = []
    l   = min(self.ord,v.ord)
    for x in range(l):
      lis.append(self.coeff[x]-v.coeff[x])

    if v.ord > self.ord:
      for x in range(self.ord,v.ord):
        lis.append((-1*v.coeff[x]))

    if v.ord < self.ord:
      for x in range(v.ord,self.ord):
        lis.append(self.coeff[x])
      
    return Polynomial(lis)

  def __mul__(self,m):
  
    if isinstance(m,int) or isinstance(m,float):
      for x in range(self.ord):
        self.coeff[x] *= m

      return self

    if isinstance(m,Polynomial):
     
      l   = self.ord+m.ord-1
      lis = [0]*l

      t1  = copy.deepcopy(self.coeff)
      t2  = copy.deepcopy(m.coeff)

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

    if isinstance(m,Polynomial):
     
      l   = self.ord+m.ord-1
      lis = [0]*l

      t1  = copy.deepcopy(self.coeff)
      t2  = copy.deepcopy(m.coeff)

      for x in range(len(t1)):
        for y in range(len(t2)):
          lis[x+y] += t1[x]*t2[y]
    

      return Polynomial(lis)

  def __getitem__(self,i):

    sum  = 0
    prod = 1

    # Returns f(i) where i is given parameter
    for x in range(self.ord):
      sum  += self.coeff[x]*prod
      prod *= i

    return sum

  def show(self,a,b,t=""):

    if a>=b:
      raise Exception('<class \'Exception\'>\nInvalid Range.')

    # Taking x in given range at a spacing of 0.125
    x = np.arange(a,b,0.01)
    y = []
    
    for i in x:
      y.append(round(self[i],4))

    if t=="":
      title =  "Plot of the Polynomial"
      
    else:
      title = t
    
    # Plotting
    plt.plot(np.array(x),np.array(y), label=t)
    

  def fitViaMatrixMethod(self,l):
    ord = len(l)
    xl  = []
    A   = []
    b   = []

    # l is a list of x,y points
    for p in l:

      xl.append(p[0])

      # b is output point
      b.append(p[1])
      row = []
      i   = 1
      for _ in range(ord):
        row.append(i)
        # Substituting given x
        i *= p[0]
      A.append(row)
   

    # Using np function to solve the matrix
    x = (np.linalg.solve(np.array(A),np.array(b))).tolist()
    self.coeff = x
    self.ord   = ord

    # Plotting
    plt.scatter(xl,b,color='r')
    self.show(0,10,'Polynomial Interpolation using matrix method')


  def fitViaLagrangePoly(self,l):

    xl  = []
    yl  = [] 
    for p in range(len(l)):

      xl.append(l[p][0])
      yl.append(l[p][1])
      x = l[p][0]
      y = l[p][1]

      temp = Polynomial([1])
      temp = temp * y

      # Using Lagrange Formula
      for q in range(len(l)):
        if p!=q:
          # Numerator must have polynomials with (x - q[0]) form
          temp = temp * Polynomial([-1*l[q][0],1])
          # Denominator must be sum of product of respective x with other coefficients 
          temp *= 1/(x-l[q][0])

      self += temp
    
    self.ord = len(self.coeff)

    plt.scatter(xl,yl,color='r')
    self.show(min(xl),max(xl)+0.1,'Polynomial Interpolation using Lagrange method')

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
    return "Area in the interval ["+str(a)+", "+str(b)+"] is: "+str(p[b]-p[a])
  

def best_fit(points, degree):
    matrix_a = []
    matrix_b = []

    for j in range(degree + 1):
        row = [sum(point[0] ** (j + k) for point in points) for k in range(degree + 1)]
        matrix_a.append(row)
        
        yk = sum(point[1] * (point[0] ** j) for point in points)
        matrix_b.append(yk)

    coefficients = np.linalg.solve(matrix_a, matrix_b)
    polynomial = Polynomial(list(coefficients))
    polynomial.show(0, 10)

    return polynomial

# Forward Euler 
a,b = 0, 10                     
steps = [0.1, 0.5, 1, 2, 3]        # Discretization steps
  
for h in steps:
    x = np.arange(a, b, h)
    y = [5]
    pts = [(a,5)]                 
    
    for i in x[1:]:
      yn = y[-1] - (2*h*y[-1])    
      y.append(yn)  
      pts.append((i,yn))
    p = best_fit(pts,20)        

xa = np.linspace(a,b,1000)
plt.plot(xa, 5*np.exp(-2*xa), label='Actual Function')
plt.ylim(-50, 50)
plt.xlim(0, 10)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.title('Forward Euler Method')
plt.show()