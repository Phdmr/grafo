grafo = {0: [2, 3],
         1: [4, 8],
         2: [5],
         3: [7, 8],
         4: [8],
         5: [6],
         6: [2],
         7: [9],
         8: [0],
         9: [7]}

def edge_list(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u, v))
    return links


def achar_aresta(gr):
    list_ares = []
    for key in gr:
        list_ares.append(key)
    return list_ares


def create(a, b):
    return (a, b)


def achar_ciclo(graph, start):
    vertexList, edgeList = graph
    print(graph)
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for v in vertexList]
    print(adjacencyList)

    for edge in edgeList:
        print("edge: ", edge)
        adjacencyList[edge[0]].append(edge[1])
        print(adjacencyList)

    while stack:
        print('Pilha ', stack)
        current = stack.pop()
        print("estamos em: ", current)
        for neighbor in adjacencyList[current]:
            print("oi vizinho: ", neighbor)
            if not neighbor in visitedVertex:
                stack.append(neighbor)
                y = None
                print(y)
            else:
                y = neighbor
                print("ja estive aqui: ", y)
        if y is None:
            visitedVertex.append(current)
            print("foram visitados: ", visitedVertex)
        else:
            print("Cilco achado")
            visitedVertex.append(current)
            visitedVertex.append(y)
            g = []
            for i in reversed(visitedVertex):
                if i not in g:
                    g.append(i)
                else:
                    g.append(i)
                    break
            g = g[::-1]
            return g


edge = (edge_list(grafo))
arestas = (achar_aresta(grafo))
grafoo = (create(arestas, edge))

print(achar_ciclo(grafoo, 1))
