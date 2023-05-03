import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math
import json
from collections import defaultdict

class UndirectedGraph:
    def __init__(self , N=None):
        self.adj_list = {}
        self.freeG=1
        self.NumEdges = 0
        self.maxnodes = sys.maxsize
        if N is None:
            self.maxnodes = sys.maxsize
            self.NumNodes = 0
            self.freeG = 1
        else:
            self.maxnodes = N
            self.NumNodes = N
            self.freeG = -1
            i = 0
            while i < N:
                self.adj_list[i+1] = []
                i += 1
            
        
        
    def addNode(self , Node_ ):
        if type(Node_)== int :
            if Node_ <= self.maxnodes and Node_ > 0:
                if Node_ not in self.adj_list.keys():
                    self.adj_list[Node_] = []
                    self.NumNodes += 1
                    print(f"added node {Node_}")
                
                return
            else:
                raise Exception("index out of bound(> no of nodes)")  
        else :              
            raise Exception("Node if not of type integer") 
    
    def addEdge(self , x , y):
        if self.freeG == -1:
            if x  in self.adj_list.keys() and y in self.adj_list.keys():
                self.NumEdges += 1 
                self.adj_list[y].append(x)  
                self.adj_list[x].append(y)             
            else:
                raise Exception("index out of bound (> no of nodes)") 
    
        else:
            self.NumEdges += 1

            self.adj_list = defaultdict(list)
            self.adj_list[x].append(y)
            self.adj_list[y].append(x)

    
    def __add__(self , n):
        if type(n) == tuple:
            self.addNode(n[0])
            self.addNode(n[1])
            self.addEdge(n[0] , n[1]) 
            return self 
        
        if type(n) == int:
            self.addNode(n)  
            return self        

        if type(n) == tuple:
            self.addNode(n[0])
            self.addNode(n[1])
            self.addEdge(n[0] , n[1]) 
            return self 
         
        return self
    
    def __str__(self):
        data = {f"Node {i}": self.adj_list[i] for i in self.adj_list}
        return f"Graph with {self.NumNodes} nodes and {self.NumEdges} edges. Neighbours of the nodes are below:\n{json.dumps(data, indent=2)}"
    

    def plotDegDist(self):
    
        FofNodes = [0] * (self.NumNodes )
        
        
        for i in self.adj_list:
            x=len(self.adj_list[i])
            FofNodes[x] += 1

        Total_sum=0
        for i in FofNodes:    
            Total_sum = Total_sum + i

        for i in range(len(FofNodes)):
            FofNodes[i] = FofNodes[i]/Total_sum

        j = 1
        AvgNodeDegree = 0
        for i in FofNodes:
            AvgNodeDegree += i *j  
            j+=1

        AvgNodeDegree =AvgNodeDegree-1
        print(AvgNodeDegree)
        
        plt.plot(FofNodes , 'bo' , label = "Actual degree distt")
        plt.axvline(AvgNodeDegree , color = 'r' , label = "Avg node degree")
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")
        plt.grid()
        plt.show()


class ERRandomGraph(UndirectedGraph):
    def sample(self , p):
        for i in self.adj_list:
            for j in self.adj_list:
                if i < j:
                    if np.random.choice([True, False], p=[p, 1-p]):
                        self.addEdge(i,j)


g = ERRandomGraph(1000)
g.sample(0.4)
g.plotDegDist()
