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

    def BFSFun(self, u, visited):
        # Create a queue for BFS
        queue = []

        #  Mark the source node as visited and enqueue it
        queue.append(u)
        visited[u] = True

        # Get all adjacent vertices of the dequeued vertex s. If a adjacent
        # has not been visited, then mark it visited and enqueue it
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print(end='\n')

    # function to add an edge to graph
    def BFS(self, u):

        # Get the number of graph vertices
        V = len(self.graph)

        # Mark all the vertices as not visited
        visited = [False]*V

        # Callingthe BFS function
        self.BFSFun(u, visited)

        # Find DFS from the 0th vertex an traverse through the complete graph,
        # comment the above line and uncomment the below lines
        # for i in range(V):
        #     if visited[i] == False:
        #         self.BFSFun(i, visited)


# Create a graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 0)")

g.BFS(2)
