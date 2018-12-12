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

    # function to add an edge to graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))

        # Create a queue for BFS
        queue = []

        #  Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

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


# Create a graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 0)")

g.BFS(0)
