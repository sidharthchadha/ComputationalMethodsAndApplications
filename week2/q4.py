import sys
import matplotlib.pyplot as plt
import random
import math

class UndirectedGraph:
    
    def __init__(self , NoOfVertices = None):
        self.adj_list = {}
        if NoOfVertices is not None:
            self.maxnodes = NoOfVertices
            self.NumNodes = NoOfVertices
            self.freeGraph = False
            for i in range(NoOfVertices):
                self.adj_list[i+1] = []
        else:
            self.maxnodes = sys.maxsize
            self.NumNodes = 0
            self.freeGraph = True
        self.NumEdges = 0
        




    def addNode(self , NodeToAdd ):
        if NodeToAdd <= self.maxnodes and isinstance(NodeToAdd , int) and NodeToAdd > 0:
            if NodeToAdd not in self.adj_list.keys():
                self.adj_list[NodeToAdd] = []
                # print(f"added node {NodeToAdd}")
                self.NumNodes += 1
            return
        else:
            raise Exception("Node index cannot exceed number of nodes")            

    def addEdge(self , x , y):
        if self.freeGraph:
            self.NumEdges += 1
            if x in self.adj_list.keys():
                self.adj_list[x].append(y)
            else:
                self.adj_list[x] = [y]

            if y in self.adj_list.keys():
                self.adj_list[y].append(x)
            else:
                self.adj_list[y] = [x]
        else:
            if x  in self.adj_list.keys() and y in self.adj_list.keys():
                self.adj_list[x].append(y)
                self.adj_list[y].append(x)  
                self.NumEdges += 1              
            else:
                raise Exception("Node index cannot exceed number of nodes")             

    def plotDegDist(self):

        FractionOfNodes = [0] * (self.NumNodes )
        X_axis = [i for i in range(self.NumNodes)]
        
        for i in self.adj_list:
            FractionOfNodes[len(self.adj_list[i])] += 1
        Total_sum = sum(FractionOfNodes)
        for i in range(len(FractionOfNodes)):
            FractionOfNodes[i] = FractionOfNodes[i]/Total_sum
        k = 1
        AvgNodeDegree = 0
        for i in FractionOfNodes:
            AvgNodeDegree += i * k 
            k+=1

        AvgNodeDegree -= 1
        print(AvgNodeDegree)
        #plotting
        # plt.plot(FractionOfNodes , 'bo' , label = "Actual degree distribution"  )
        plt.scatter(X_axis , FractionOfNodes , s = 5 , color = 'b' , label = "Actual degree distribution")
        plt.axvline(AvgNodeDegree , color = 'r' , label = "Avg node degree")
        plt.grid()
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")
        plt.title("Node Degree Distribution")
        plt.legend()
        plt.show()

    def bfs(self , start_node):
        n = self.NumNodes
        Q = [start_node]
        visited = []
        while Q:
            curr = Q.pop(0)
            
            if curr not in visited:
                visited.append(curr)
                for i in self.adj_list[curr]:
                    Q.append(i)
                # if curr + 1 not in visited and (curr, curr+1) in self.edge:                       
                #         Q.append(curr+1)
                # if curr - 1 not in visited and (curr , curr -1) in self.edge:
                        
                #         Q.append(curr-1)
                # if curr + n not in visited and curr + n < n * n and (curr , curr + n) in self.edge:
                        
                #         Q.append(curr+n)
                # if curr - n not in visited and curr -n > -1 and (curr , curr - n) in self.edge:
                        
                #         Q.append(curr-n)
        return visited

    def isConnected(self):
        temp = self.bfs(random.choice(list(self.adj_list.keys())))


        temp.sort()
        temp2 = [i for i in self.adj_list]
        temp2.sort()

        if temp == temp2:
            return True
        else:
            return False


    
    def __str__(self):
        text = f"Graph with {self.NumNodes} nodes and {self.NumEdges} edges. Neighbours of the nodes are belows:\n"
        for i in self.adj_list:
            text += f"Node {i}: " + str(self.adj_list[i]) + '\n'
        return text.replace('[' , '{').replace(']' , '}')
    
    def __add__(self , n):
        if isinstance(n , int):
            self.addNode(n)          

        elif isinstance(n , tuple):
            self.addNode(n[0])
            self.addNode(n[1])
            self.addEdge(n[0] , n[1]) 
        return self  
    
    def OneTwoComponentSizes(self):
        components = []
        present = []
        sizes = []
        for i in self.adj_list:
            if i not in present:
                temp = self.bfs(i)
                for Neighbours in temp:
                    present.append(Neighbours)
                components.append(tuple(temp))
        for i in components:
          sizes.append(len(i))
        sizes.sort()
        if len(sizes) != 1:
          return [sizes[-1] , sizes[-2]]
        else:
          return [sizes[-1] , 0]






class ERRandomGraph(UndirectedGraph):
    def sample(self , p):
        for x in self.adj_list:
            for y in self.adj_list:
                if y > x:
                    temp = random.choices([True , False] , weights = [p*100 , (1-p)*100])
                    if temp[0]:
                        self.addEdge(x,y)



def FunToVerifyStatement(NumOFTrials):
    Largest = []
    second_largest = []
    X_axis = [float(i)/(float(10000)) for i in range(100+1)]
    for i in X_axis:
        Ts = 0
        Fs = 0
        for _ in range(NumOFTrials):
          g = ERRandomGraph(1000)
          g.sample(i)
          temp = g.OneTwoComponentSizes()
          Ts += temp[0]
          Fs += temp[1]
        print(int(i* 10000) , '/', "100")
        Largest.append(Ts/g.NumNodes * NumOFTrials )
        second_largest.append(Fs / g.NumNodes * NumOFTrials) 

    # Threshold = ( math.log10(100) / math.log10(math.e)) * 0.01
    plt.plot(X_axis , Largest , color = 'g' , label ="Largest connected component" )
    plt.plot(X_axis , second_largest , color = 'b' , label = "2nd largest connected component")
    plt.axvline(1/g.NumNodes , label = " Largest CC size threshold" , color = 'r')
    plt.axvline(math.log(g.NumNodes)/g.NumNodes , label = "Connectedness threshold" , color = 'y')
    # plt.axvline(Threshold , color = 'r' , label = "Theoretical threshold")
    plt.title(f"Fraction of nodes in the largest and second-largest connected components (CC) of  G({g.NumNodes}, p) as function of p")
    plt.ylabel(f"Fraction of runs G({g.NumNodes},p) is connected")
    plt.xlabel("p")
    plt.legend()
    plt.show()


# g = UndirectedGraph(5)
# g = g + (1, 2)
# g = g + (2, 3)
# g = g + (3, 4)
# g = g + (3, 5)
# print(g)
# a = g.bfs(1)

# print(g.isConnected())


# g = UndirectedGraph(6)
# g = g + (1, 2)
# g = g + (3, 4)
# g = g + (6, 4)
# print(g.OneTwoComponentSizes())

FunToVerifyStatement(10)
