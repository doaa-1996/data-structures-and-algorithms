
class Graph:
    def __init__(self):
        self.graph = {}
        
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        
    def BFS(self, s):
        visited = [False] * len(self.graph)
        que = [s]
        visited[s] = True
        output=[]
        
        while len(que) > 0:
            s = que.pop(0)
            output.append(s)

            
            for node in self.graph[s]:
                if visited[node] == False:
                    que.append(node)
                    visited[node] = True
        return output
    
   
                    


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,0)
g.addEdge(5,2)
print(g.BFS(0))
