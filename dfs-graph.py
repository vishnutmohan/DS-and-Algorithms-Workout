# Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.

from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary of list as values to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSFun(self, u, visited):

        # Seting the vertex as visited and print
        visited[u] = True
        print(u,)

        # Using recusrsion to go through the graph and call the function if not visited vertex comes
        for i in self.graph[u]:
            if visited[i] == False:
                self.DFSFun(i, visited)

    # DFS function. If not starting from a specific node remove the 2nd parameter
    def DFS(self, u):
        V = len(self.graph)
        visited = [False]*V

        # Find DFS from a given vertex
        self.DFSFun(u, visited)

        # Find DFS from the 0th vertex an traverse through the complete graph, coomment the above line and uncomment the below lines
        # for i in range(V):
        #     if visited[i] == False:
        #         self.DFSFun(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS")
g.DFS(2)
