from collections import defaultdict
 
# function for adding edge to graph
def addEdge(graph,u,v):
    graph[u].append(v)

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self,v,visited):         
        visited[v]= True
        print (v, end = " ")        
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited) 
 
    def DFS(self,v):        
        visited = [False]*(len(self.graph))
        self.DFSUtil(v,visited) 
    
    def BFS(self, s): 
        visited = [False] * (len(self.graph))
        queue = [] 
        queue.append(s)
        visited[s] = True 
        while queue: 
            s = queue.pop(0)
            print (s, end = " ")            
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

#implementar:
#adjacentes(G, x, y) se ha aresta de x a y
#neighbors(G, x) todos os adjacentes de x
#remove_vertex(G,x)
#add_vertex(G,x)
#remove_edge(G, x, y)
#get_vertex_value(G,x)
#set_vertex_value(G,x)
#for edge too
#add vertex e edge from matrix and list

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is DFS from (starting from vertex 2)")
g.DFS(0)
g.BFS(2)

 
