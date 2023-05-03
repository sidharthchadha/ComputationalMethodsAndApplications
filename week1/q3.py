import matplotlib.pyplot as plt
import random
 
def estimatePi(n):
    fraction = []
    x = []
    for i in range(n):
        x.append(i)   #x-axis list

    Pointc = 0
    Pointsq = 0    

    for i in range(n):    
        x_ = random.uniform(-1 , 1 )
        y_ = random.uniform(-1 , 1)
        Pointsq = Pointsq + 1 #every point is in square so increasing count
        if check(x_,y_) :    #checking if poiint lies in circle
            Pointc = Pointc + 1  # increasing count of points in circle 
        fraction.append(4 * float(Pointc)/float(Pointsq))

    plt.plot(x , fraction , color = 'g' , label = "Monte Carlo method") 
    plt.axhline(y = 3.14, color = 'r', linestyle = '-', label="value of pi (3.14)") #horizonal line representing mathematical value expected
    plt.title("Estimating pi")
    plt.xlabel("No. of points generated")
    plt.ylabel("4 x fraction of points withing the circle")
    plt.ylim(2.7,3.5)
    plt.legend()
    plt.show()
    return fraction

def check(x,y):
    if x*x +y*y <=1:
        return 1
    else :
        return 0    

x=int(input("enter the argment"))
estimatePi(x)
        
    