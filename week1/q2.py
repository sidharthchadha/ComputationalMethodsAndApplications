import matplotlib.pyplot as plt
import random
import numpy as np

class Dice:
    
    def __init__(self, numSides = 6):

        self.numSides  = numSides
        if numSides < 4:
                raise Exception("<class 'Exception'> \nCannot construct the dice") 
        if not isinstance(numSides , int):
                raise Exception("<class 'Exception'> \nCannot construct the dice")  
        
        self.Prob_Dist = [1.0/float(self.numSides)] * numSides        #default Distribution 
   
    def roll(self , num_throws):
        freq = []
        self.NumOfThrows = num_throws

        for i in range(self.numSides):
            freq.append(0)
            self.Prob_Dist[i] = 10 * self.Prob_Dist[i]
            
        for i in range(num_throws):
            temp = random.choices(range(0 ,  self.numSides , 1) , weights=self.Prob_Dist , k=1)
            freq[temp[0]] = freq[temp[0]]+1

        return freq    
        

    def setProb(self , new_Prob_Dist ):
    
        if sum(new_Prob_Dist) != 1 :
            raise Exception("<class 'Exception'>\nInvalid probability distribution")        
        if len(new_Prob_Dist) != self.numSides:
            raise Exception("<class 'Exception'>\nInvalid probability distribution")        

        self.Prob_Dist = list(new_Prob_Dist)  

    def _str_(self ):
            return f'Dice with {self.numSides} faces and probability dist. {tuple(self.Prob_Dist)}'.replace('(' , '{').replace(')' , '}')
    
    def get_num_throws(self):
        return self.NumOfThrows

d = Dice(4)
d.setProb((0.1, 0.2, 0.3, 0.4))
simulated_result = d.roll(100000)
print(d)

#plotting   
x_axis = []
expected = []    
 
for i in range(d.numSides):
    expected.append( d.get_num_throws() * d.Prob_Dist[i] /10)
    x_axis.append(i+1)
    

X_axis = np.arange(len(x_axis))

plt.bar(X_axis - 0.1, simulated_result ,color = 'g' , width = 0.2, label = 'actual'  )
plt.bar(X_axis + 0.1, expected, color = 'r' , width= 0.2, label = 'expected')

plt.xticks(X_axis, x_axis)
plt.xlabel("sides")
plt.ylabel("Occur")
plt.title(f'Outcome')
plt.show()