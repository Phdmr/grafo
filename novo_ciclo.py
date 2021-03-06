import numpy as np
class node:
    name:str
    value:int
    matriz:list

    def __init__(self,name,value,matriz):
        self.name = name
        self.value = value
        self.matriz = matriz
        if type(matriz)==str:
            self.matriz=matriz.split(' ')
    def __str__(self):
        return "(%s)"%(self.name)
    def __repr__(self):
        return "(%s)" % (self.name)
class grafos:

    nodes_list = []
    """"{"A": [0, 1, 0, 1, 1, 0, 0, 0],
     "B": [1, 0, 1, 0, 0, 1, 0, 0],
     "C": [0, 1, 0, 1, 0, 0, 0, 1],
     "D": [1, 0, 1, 0, 0, 0, 1, 0],
     "E": [1, 0, 0, 0, 0, 1, 1, 0],
     "F": [0, 1, 0, 0, 1, 0, 0, 1],
     "G": [0, 1, 0, 1, 1, 0, 0, 1],
     "H": [0, 0, 1, 0, 0, 1, 1, 0]} """
    adjMatrix = {}
    adjList = {}
    counter:int
    color = {"white": [], "gray": [], "black": []}
    pred = {}
    time = {}
    def file_treatment(self):
        with open("grafo.txt", "r") as file:
            for i, l in enumerate(file):
                pass
            input_test = ""
            node_names = []
            node_values = []
            file.seek(0)
            type = file.readline()
            for x in range(i):
                input_test = file.readline()
                print(input_test)
                intermediateSeperator = input_test.find("[")
                secondIntermediateSeperator = input_test.find("]")
                node_names.append(input_test[0])
                intermediateString = input_test[intermediateSeperator + 1:secondIntermediateSeperator]
                node_values.append(list(intermediateString))
            counter = 0
            for x in node_values:
                for y in x:
                    if y == ",":
                        counter += 1
            for x in range(counter):
                for y in node_values:
                    if "," in y:
                        y.remove(",")
            zipped = zip(node_names, node_values)
            nodes = []
            counter = 0
            for i in zipped:
                i = list(i)
                nodes.append(node(i[0], counter, i[1]))
                counter += 1
            self.nodes_list = nodes[:]
            self.create_repr(int(type))
            self.counter=counter
    def addNode(self,type):
        newNode = node(input("nome do vertice"),self.counter+1,input("adjacentes"))
        if type == 1:
            if newNode.name in self.adjList:
                print("Vertice ja existente")
                return 0
            else:
                for x in newNode.matriz:
                    if x not in self.adjList:
                        print("nao existe esse vertice",x)
                        return 0
                self.nodes_list.append(newNode)
                self.create_repr(type)
                self.updateAdjUndirected(newNode, type)
        elif type ==0:
            if newNode.name in self.adjMatrix:
                print("vertice ja existente")
                return 0
            else:
                for x in newNode.matriz:
                    if x not in self.adjMatrix:
                        print("Nao existe esse vertice",x)
                        return 0
                self.nodes_list.append(newNode)
                repr = ["0" for i in range(len(self.adjMatrix)+1)]
                self.adjMatrix.update({newNode.name:repr})
                self.updateAdjUndirected(newNode, type)

    def updateAdjUndirected(self,newNode,type):
        if type == 1:
            for x in newNode.matriz:
                for y in self.adjList:
                    if x == y:
                        updateValue = self.adjList[y]
                        updateValue.append(newNode.name)
                        self.adjList[y] = updateValue
            print(self.adjList)
        elif type ==0:
            for x in newNode.matriz:
                valueAdd = self.find_value(x)
                self.adjMatrix[newNode.name][valueAdd] = "1"
            print(self.adjMatrix)
            for y in self.adjMatrix:
               if y in newNode.matriz:
                   self.adjMatrix[y].append("1")
               else:
                   self.adjMatrix[y].append("0")


    def create_repr(self,type):
        repr_graph = {}
        if type ==0:
            for x in self.nodes_list:
                repr_graph.update({x.name:x.matriz})

            self.adjMatrix.update(repr_graph)
        elif type==1:
            for x in self.nodes_list:
                repr_graph.update({x.name: x.matriz})
            self.adjList.update(repr_graph)
            print(self.adjList)
    def find_value(self,edge1:str):
        value = 0
        for x in self.nodes_list:
            if x.name==edge1:
                value = x.value
                break
        return value
    def find_name(self,value:int):
        name:str
        for x in self.nodes_list:
            if x.value==value:
                name = x.name
                break
        return name
    def identify_edge(self,type_rep:int,edge:str,edge1:str):
        if type_rep == 0:
            value = self.find_value(edge1)
            if self.adjMatrix[edge][value] == "1":
                return True
            else:
                return False
        elif type_rep ==1:
            if edge1 in self.adjList[edge]:
                return True
            else:
                return False
    def find_adj(self,edge:str,type_rep:int,grafo):
        names = []
        if type_rep ==0:
            for x in range(len(grafo[edge])):
                if grafo[edge][x]== "1":
                    names.append(self.find_name(x))
            return names
        if type_rep==1:
            return self.adjList[edge]
    def remove_node(self,type,node):
        if type == 0:
            self.adjMatrix.pop(node,None)
            for y in self.adjMatrix:
                self.adjMatrix[y].pop(self.find_value(node))
        elif type ==1:
            self.adjList.pop(node,None)
            for y in self.adjList:
                if node in self.adjList[y]:
                    self.adjList[y].remove(node)



    def find_cicle(self,source,grafo,function_value):
        nova = []
        ender = []
        is_here = []
        global counter_timer
        counter_timer = 0
        global connected
        connected = []
        def visitDFS(node):
            tired = []
            global counter_timer
            global  connected
            counter_timer += 1
            connected.append(node)
            print("Visitando",node)
            color["white"].remove(node)
            color["gray"].append(node)
            time[node] =counter_timer
            print("Cores: ", color)
            adjs = self.find_adj(node,0,grafo)
            print("Vizinhos: ", adjs)
            for x in adjs:
                if x in color["white"]:
                    pred[x] = node
                    visitDFS(x)
                    print(x)
                else:
                    nova.append(x)
            color["gray"].remove(node)
            color["black"].append(node)
            counter_timer +=1
            time_final[node]+= counter_timer
            if not nova:
                test = None
            else:
                test = nova[0]
            for i in color["black"]:
                if i not in tired and i != test and test is not None:
                    if i not in ender:
                        tired.append(i)
                    print("Existem duvidas")
                print("Cansado disso: ", tired)
            if test in color["black"]:
                print("Entrei aqui")
                tired.append(nova.pop())
                ui = []
                while tired:
                    ui.append(tired.pop())
                    for c in ui:
                        if c not in is_here:
                            is_here.append(c)
            if is_here and test in color["black"]:
                is_here.append(test)
            elif len(nova)>1 and len(ender)>0:
                print("Saiu fora daqui")
                nova.append(node)
                nova.pop(0)
                print(nova)
            for i in range(len(is_here)):
                if is_here[0] not in ender:
                    ender.append(is_here[0])
                    is_here.pop(0)
                elif is_here[0] in ender:
                    print("Entrada final")
                    if ender.count(test)==1:
                        ender.append(test)
                        ender.append("")
                        is_here.pop(0)
                else:
                    is_here.pop(0)
            print("Finalizando",node)
            print("Cores finais: ", color)
            print("Ciclo final: ", ender)

        def iterate_paths(vertex):
            path =[]
            if pred[vertex][0] != None:
                path.append(pred[vertex][0])
                path = path+iterate_paths(pred[vertex][0])
                print(path)
                return path
            else:
                return path
        color ={"white":[],"gray":[],"black":[]}
        pred = {}
        time ={}
        time_final = {}
        print("Comecando busca em profundidade")
        for x in grafo:
            color["white"].append(x)
            pred.update({x:[None]})
            time.update({x:counter_timer})
            time_final.update({x:counter_timer})
        if (function_value == "3"):
            for x in grafo:
                if x in color["white"]:
                    visitDFS(x)
                print("Sem suporte")
                break
            print("Ainda sem suporte")

        return ender

    def FindConnectivity(self):
        transposed=self.adjMatrix.copy()
        matriz = []
        for x in transposed:
            matriz.append(transposed[x])
        transposedmatriz = np.transpose(matriz)
        transposedmatriz = transposedmatriz.tolist()
        print(list(transposedmatriz))
        for x,y in zip(transposed,transposedmatriz):
            transposed[x] = y[:]

        final1 = self.find_cicle("0",self.adjMatrix,"3")
        SCC = final1
        print("Ciclos encontrados :",SCC)




















if __name__ == '__main__':
    g = grafos()
    g.file_treatment()
    g.FindConnectivity()

