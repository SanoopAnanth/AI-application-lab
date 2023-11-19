# 6 implementation of BFST
# 7 Water jug program
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.visited=set()
    def addEdgeToGraph(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        queue=[]
        queue.append(s)
        self.visited.add(s)
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.add(i)
g=Graph()
count=int(input("enter the number of vertex you add to graph:"))
while count>0:
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    g.addEdgeToGraph(x,y)
    count-=1
sta=int(input("enter the startng vetrex: "))
g.BFS(sta)