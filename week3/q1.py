import json
import numpy as np

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


r = RowVectorFloat([1,2,3])
print(len(r))
print(r)
print(r[2])
print(r[-1])
r=r*2
print(r)
r=r+r
print(r)
r2=RowVectorFloat((2,4,5))
r=-1*r+3*r2
print(r)
        