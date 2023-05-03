import numpy as np
import copy
import math


class RowVectorFloat:
    def __init__(self,list):
        self.vector=[]
       #attributes for our vector
        for i in list:
            self.vector.append(i)


    def __setitem__(self,i,x):
    
        if i >= len(self.vector):
          raise Exception("invalid index")

        self.vector[i] = x        


    def __str__(self):

        #for printing the rowfloatvector object (predefined function)
        x=""
        for i in self.vector:
            if type(i) is float:
                x=x+"{:.2f}".format(i)

            else:
                x=x+str(i)  
            x=x+" "
        return x  

    def __len__(self):
        #returns the length of rowfloat so tat we can directly print length
        return len(self.vector)  


    def __getitem__(self, index):
        #checking for the index from both 0 based indexing and for the negative indexing also that is from back
        if index<0:
            x=-1*index
            if x> len(self.vector):
                return "index out of bound"
            
            return self.vector[index]

        if len(self.vector)<= index :
            return "index out of bound"

        return self.vector[index] 
    
 
    def __rmul__(self, scalar):
        #multiplicand is on right predefined method
        new_vector = np.array(self.vector) * scalar
        return RowVectorFloat(new_vector.tolist())

    def __mul__ (self,scalar):
        #predefined method to multiply
        new_vector = np.array(self.vector) * scalar
        return RowVectorFloat(new_vector.tolist())


    def __add__(self, rv):
        #predefined method
        if type(rv) != RowVectorFloat:
            raise Exception("Invalid ")
        if len(self) != len(rv):
             raise Exception("Invalid ")

        ans = np.array(self.vector) + np.array(rv.vector)
        return RowVectorFloat(ans.tolist())
    

class SquareMatrixFloat:
    def __init__(self,n):
        #attributes of class
        self.n=n
        self.matrix=[]
        i=0
        while i<n:
            i=i+1
            self.matrix.append(RowVectorFloat([0]*n))



    def __str__(self):
        #defining this method to print matrix by printing rowvectors individually
        s=""
        for i in self.matrix:
            s=s+str(i)+"\n"

        return s 

  
    def sampleSymmetric(self):
    #function to sample a random symmetric matrix
        for i in range(self.n):
            self.matrix[i][i] = np.random.uniform(0,self.n) #  random number in 0 to n
            for j in range(i+1, self.n):
                self.matrix[i][j] = np.random.uniform(0,1) # random number in 0 to 1
                self.matrix[j][i] = self.matrix[i][j]
                self.matrix[i][j]=round(self.matrix[i][j],2)


    def toRowEchelonForm(self):
        col    = 0
        row    = 0
        for  row in range(self.n):
        #Swapping row 
           if self.matrix[row][col] == 0:
              itr = row[:] + [1]
              flag = False
              for itr in range(self.n):
                  if self.matrix[itr][col] != 0:
                      self.matrix[row], self.matrix[j] = self.matrix[j], self.matrix[row] 
                      flag =True
                      break
                  itr += 1
              if flag is not True:
                  col += 1
                  row += 1
                  continue
      
           # Making cth element of given row 1
           div = self.matrix[row][col]
           for j in range(len(self.matrix[row])):
                self.matrix[row][j] /= div
   
         #S Making all columns below zero
           j = row + 1
           while j < self.n:
                  self.matrix[j] += -1*copy.deepcopy(self.matrix[j][col])*copy.deepcopy(self.matrix[row])
                  j += 1
               
           col += 1
           row += 1

        self.round(2)

    #custom function to round off elements in matrix to some places
    def round(self,x):
        for i in range(self.n):
           for j in range(self.n):
              self.matrix[i][j] = round(self.matrix[i][j],x)


    def isDRDominant(self):
        # diagonal element in each row should be > the sum of other elements in that row.
        n = self.n
        flag=0
        for i in range(n):
            row_sum = sum(abs(self.matrix[i][j]) for j in range(n) if j != i)
            if abs(self.matrix[i][i]) <= row_sum:
                flag=1
        if flag:
            return "False"        
        return "True"
    
    def jSolve(self,b,k):
    
        if self.isDRDominant():
            # If the matrix is diagonally dominant
            x = []
            for it in range(self.n):
                x.append(1)
            e = []
            for _ in range(k):
                # In each iteration, a new xi vector is calculated by applying the Jacobi method formula for each element. 
                xi=[]
                for it2 in range(self.n):
                    xi.append(1)
                for i in range(self.n):
                    sum = 0
                    for j in range(self.n):
                         if i!=j:
                             sum += self.matrix[i][j] * x[j]
        
                    xi[i] = (1/self.matrix[i][i])*(b[i]-sum)

                x = copy.deepcopy(xi)
                r = []
                for i in range(self.n):
                    sum = 0
                    for j in range(self.n):
                        sum += self.matrix[i][j] * x[j]
                    r.append(sum-b[i])

           # Error is norm of the value ||Ax -b||
                e.append(self.euclidean(r))

            return e,x
        else:
            raise Exception("not solving because convergence is not guaranteed")

    def gsSolve(self,b,k):
        if self.isDRDominant():
            # If the matrix is diagonally dominant
            e    = []
            x = []
            for it in range(self.n):
                x.append(1)
            for t in range(k):
                # iteratively updated k times until convergence
                xi = []
                for it2 in range (self.n):
                    xi.append(0)
                for i in range(self.n):
                    sum=0
                    for j in range(i):
                        sum += self.matrix[i][j] * xi[j]
                    for j in range(i+1,self.n):
                        sum += self.matrix[i][j] * x[j]
                    xi[i] = (1/self.matrix[i][i])*(b[i]-sum)
        
                x     = copy.deepcopy(xi)      
                r     = []
                for i in range(self.n):
                    sum = 0
                    for j in range(self.n):
                        sum += self.matrix[i][j] * x[j] 
                    r.append(sum-b[i])
                # error
                e.append(self.euclidean(r))

            return e,x
        else:
            raise Exception("not solving because convergence not guaranteed")

    def euclidean(self,r): #helper function
       
        sum_of_squares = sum([x**2 for x in r])
        # Take the square root of the sum of squares to get the Euclidean norm
        norm = sum_of_squares**0.5
        return norm



def visualize():

  s = SquareMatrixFloat(5)
  s.sampleSymmetric()

  # sampling until the matriz is Row Dominant
  while (not s.isDRDominant()):
    s.sampleSymmetric()

  err1 = s.jSolve([1, 2, 3, 4, 5], 100)[0]
  print(err1)
  err2 = s.gsSolve([1, 2, 3, 4, 5], 100)[0]
  Yj=np.array(err1)
  Xj=np.array(range(100))
  plt.plot(Xj,Yj,'g',label='Jacobi ')
  Xg=np.array(range(100))
  Yg=np.array(err2)
  plt.plot(Xg,Yg,'r',label='Gauss - Siedel ')
  plt.xlabel('Iterations')
  plt.ylabel('Error / Iteration')
  plt.legend()
  plt.show()

import matplotlib.pyplot as plt
visualize()