from collections import deque


class NaoEncontrado(Exception): pass


def search(graph, start, goal):
    visited = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print("Visitando: ",node)
        if node == goal:
            print("Estamos no vizinho: ",node)
            path = []
            while node is not None:
                path.append(node)
                print("Visitados: ",path)
                node = visited[node]
                print("Estus: ",node)
                print("Falta: ", visited)
            return path[::-1]
        for neighbour in graph[node]:
            if neighbour not in visited:
                print("Visitando Vizinho: ", neighbour)
                visited[neighbour] = node
                print(visited[neighbour]," esta mais proximo de ",neighbour)
                queue.append(neighbour)
                print("ESTAMOS AQUI: ",visited)
                print("Precisamos de: ",node)
    raise NaoEncontrado('Sem caminho de {} para {}'.format(start, goal))



grafo = {0:[2,3],
         1:[4,8],
         2:[5],
         3:[7,8],
         4:[8],
         5:[6],
         6:[2],
         7:[9],
         8:[0],
         9:[7]
         }
print(search(grafo, 1, 6))

