from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.visited=set()
    def addEdge(self,u,v):
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
count=int(input("enter vertices count:"))
g=Graph()
while count>0:
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    g.addEdge(x,y)
    count-=1
sta=int(input("enter the starting vertex: "))
g.BFS(sta)