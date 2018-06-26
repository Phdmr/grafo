grafo = {0:[2,3],
         1:[4,8],
         2:[5],
         3:[7,8],
         4:[8],
         5:[6],
         6:[2],
         7:[9],
         8:[0],
         9:[7]}

def edge_list(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
            '''print(links)'''
    return links

def achar_aresta(gr):
    list_ares = []
    for key in gr:
        list_ares.append(key)
    return list_ares

def create(a, b):
    return (a, b)

def men_dist(graph, start, end):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
        print(edge)
        print(adjacencyList)
    while queue:
        print("Soloq :", queue)
        current = queue.pop()
        print('Estamos em: ', current)
        for neighbor in adjacencyList[current]:
            print('oi vizinho: ', neighbor)
            if neighbor not in visitedList and neighbor != end:
                queue.insert(0,neighbor)
                y = None
            elif neighbor == end:
                print('Ponto final encontrado')
                y = 1
                break
        if y is None:
            if current not in visitedList:
                visitedList.append(current)
            print("foram visitados: ", visitedList)
        else:
            visitedList.append(end)
            break
    return visitedList

edge = (edge_list(grafo))
arestas = (achar_aresta(grafo))
grafoo = (create(arestas, edge))

print(men_dist(grafoo, 1, 5))
