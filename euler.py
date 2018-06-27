from collections import defaultdict


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.IN = [0] * vertices

    def addEdge(self, v, u):

        self.graph[v].append(u)
        self.IN[u] += 1

    def DFSUtil(self, v, visited):
        visited[v] = True
        for node in self.graph[v]:
            if visited[node] == False:
                self.DFSUtil(node, visited)

    def getTranspose(self):
        gr = Graph(self.V)

        for node in range(self.V):
            for child in self.graph[node]:
                gr.addEdge(child, node)

        return gr

    def isSC(self):
        visited = [False] * self.V

        v = 0
        for v in range(self.V):
            if len(self.graph[v]) > 0:
                break

        self.DFSUtil(v, visited)

        # If DFS traversal doesn't visit all
        # vertices, then return false.
        for i in range(self.V):
            if visited[i] == False:
                return False

        gr = self.getTranspose()

        visited = [False] * self.V
        gr.DFSUtil(v, visited)

        for i in range(self.V):
            if visited[i] == False:
                return False

        return True

    def isEulerianCycle(self):

        # Check if all non-zero degree vertices
        # are connected
        if self.isSC() == False:
            return False

        # Check if in degree and out degree of
        # every vertex is same
        for v in range(self.V):
            if len(self.graph[v]) != self.IN[v]:
                return False

        return True


def edge_list(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
            '''print(links)'''
    return links


G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8],
         8: [0, 1, 6, 7]}
edge = edge_list(G)
for i in range(len(edge)):
    print(edge[i])
print(len(G))
g = Graph(len(G))
for i in range(len(edge)):
    a = edge[i]
    b = a[0]
    c = a[1]
    g.addEdge(b,c)
if g.isEulerianCycle():
    print("Given directed graph is eulerian")
else:
    print("Given directed graph is NOT eulerian")
