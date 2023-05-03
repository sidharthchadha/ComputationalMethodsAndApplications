import matplotlib.pyplot as plt
import math
from math import pi as PI


x = range(1 , 1000000)  #list for x axis 
Y1=[0]
for i in range (2,1000000):
    Y1.append(Y1[-1]+math.log10(i))   #log of factorials


def Log_Stirling(n):       
    return   (math.log10(n/math.e))*n + ( math.log10( 2* PI * n)  )*0.5

y=[]
for i in x:
    y.append(Log_Stirling(i))  #list of log of stirling apprxns


plt.plot(x, Y1 , label="Log of Factorial" , color = 'r')
plt.plot(x, y, label="Log of Stirling apprxn" , color = 'g' , linestyle='dashed')
plt.title("Stirling's apprxn" , loc='center')
plt.xlabel("n")
plt.ylabel("Log(n!)")
plt.show()
