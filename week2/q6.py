import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import random
import math


class Lattice:
    def __init__(self, n):
        nodes=n**2
        self.G = nx.empty_graph(nodes)

        self.len = n
        self.edge = []
        self.pos = {}
        self.bottom_nodes2=[]
        
        i = 0
        while i < n:
            self.bottom_nodes2.append(n*i)
            i += 1
        
        i = 0
        while i < n**2:
            self.pos[i] = (i//n, i%n)
            i += 1
        self.percolated = False

        self.top_nodes = []
        i = 0
        while i < n:
          self.top_nodes.append(n*(i+1) - 1)
          i += 1

        self.bottom_nodes = []
        i = 0
        while i < n:
          self.bottom_nodes.append(n*i)
          i += 1


    def percolate(self , p):
        if p != 0:
            self.percolated = True
        pos = []

        i = 0
        while i < self.len * self.len:
             if (i+1) % self.len == 0:
                pass
             else:
                 pos.append((i, i + 1))
             i += 1
        i = 0
        while i < self.len * (self.len - 1):
           pos.append((i, i + self.len))
           i += 1



        i = 0
        while i < self.len * (self.len - 1):
             pos.append((i, i + self.len))
             i += 1


        for x,y in pos:
            
            if np.random.choice([True, False], size=1, p=[p, 1-p])[0] :
                self.edge.append((x,y))
                self.edge.append((y,x))
                self.G.add_edge(x , y , color = 'r'  , width = 1)

    def show(self):
        if self.percolated == False:
            nx.draw(self.G, self.pos, node_size=1 , node_color='b')
        else:
            nx.draw(self.G, self.pos, node_size=0 , node_color='b' , edge_color = nx.get_edge_attributes(self.G,'color').values() , width = list(nx.get_edge_attributes(self.G,'width').values()))
        plt.show()


    def existTopDownPath(self):
        flag=0
        for node1 in self.top_nodes:
            for node2 in self.bottom_nodes:
                if nx.has_path(self.G, node2, node1):
                    flag=1
                    return True
        if flag==0:        
            return False


    def showPaths(self):
    
        shortest_paths = {}
        for node1 in self.top_nodes:
            for node2 in self.bottom_nodes2:

                if nx.has_path(self.G, node1, node2):
                    if node1 not in shortest_paths.keys():
                        shortest_paths[node1] = nx.shortest_path(self.G , node1, node2)
                    else:
                        if len(nx.shortest_path(self.G , node1, node2)) < len(shortest_paths[node1]):
                            shortest_paths[node1] = nx.shortest_path(self.G , node1, node2)
                else:
                    self.bottom_nodes2.remove(node2)
    
        
        for node in self.top_nodes:
            if node in shortest_paths.keys():
                pass
            else:
                n = self.len
                Que = []
                Que.append(node)
                visited = []
                while True:
                    if len(Que)==0:
                      break
                    curr = Que.pop(0)
                    explored=[]
                    if curr not in visited:
                       visited.append(curr)
            
                    if (curr , curr + n) in self.edge:
                        explored.append(curr+n)
                    if (curr , curr - n) in self.edge:
                        explored.append(curr-n)
                    if (curr, curr+1) in self.edge:                       
                         explored.append(curr+1)  
                    if (curr , curr -1) in self.edge:
                        explored.append(curr-1)
            
                    if len(explored):
                        for x in explored:
                            if x not in visited and x < (n**2):
                                Que.append(x)

                    if len(Que)==0:
                        break       

                shortest_paths[node] = nx.shortest_path(self.G , node, visited[-1] )

        for i in shortest_paths:
            for j in range(len(shortest_paths[i])-1):
                self.edge.append((shortest_paths[i][j],shortest_paths[i][j+1]))
                self.edge.append((shortest_paths[i][j+1],shortest_paths[i][j]))
                self.G.add_edge(shortest_paths[i][j] , shortest_paths[i][j+1] , color = 'g'  , width = 2)
                
        nx.draw(self.G, self.pos, node_size=0 , node_color='b' , edge_color = nx.get_edge_attributes(self.G,'color').values() , width = list(nx.get_edge_attributes(self.G,'width').values()))
        plt.show()

        


def Verify(Num = 50):
    data=[]
    X_axis = np.linspace(0, 1, Num + 1)
    Y_axis = []
    i = 0
    while i <= Num:
        ts_ = 0
        fs_ = 0
        for _ in range(Num):
            L = Lattice(100)
            L.percolate(X_axis[i])
            if L.existTopDownPath():
                ts_ += 1
            else:            
                fs_ += 1
        
        Y_axis.append(ts_/(ts_ + fs_)) 
        i += 1
    data.append(X_axis)
    data.append(Y_axis)
    return  data 
    



x=Verify(50)


plt.plot(x[0] , x[1] , color = 'b')
plt.title("Critical cut-off in 2-D bond percolation")
plt.ylabel("Fraction of runs end-to-end perccolation occured")
plt.xlabel("p")
plt.show()




