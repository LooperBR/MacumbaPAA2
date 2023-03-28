# define a classe vertice
class Vertice:
    def __init__(self,name,x=0,y=0):
        self.name = name
        # distancia da origem
        self.dist=-1
        # vizinhos do vertice
        self.neighbors = []
        # predecessor do vertice
        self.pred = -1
        # posição x e y do vertice
        self.x = x
        self.y = y

    #função que adiciona um vizinho com o peso do caminho entre ele e o vertice atual
    def addNeighbor(self,neighbor,peso):
        self.neighbors.append([neighbor,peso])

#classe grafo
class Graph:
    def __init__(self):
        #dicionario de vertices
        self.vertices = {}
        #lista de arestas
        self.arestas = []

    #funcao que adiciona o vertice
    def addVertice(self,vertice,x=0,y=0):
        self.vertices[vertice] = Vertice(vertice,x,y)

    #funcao que adiciona as arestas
    def addEdge(self,v1,v2,peso=0):
        aresta = [v1,v2,peso]
        self.arestas.append(aresta)
        #adiciona v2 como vizinho de v1
        self.vertices[v1].addNeighbor(v2,peso)
        #adiciona v2 como vizinho de v1
        self.vertices[v2].addNeighbor(v1,peso)

    #funcao do dijktra
    def dijkstra(self,raiz,termino):
        
        #lista de vertices nao vizitados
        lista = []

        #reseta os valores de todos os vertices
        for i in self.vertices:
            self.vertices[i].dist = -1
            self.vertices[i].pred = -1
            lista.append(i)
        
        #seta a distancia da raiz como 0
        self.vertices[raiz].dist = 0

        #seta a raiz como vertice atual
        vertice_atual = raiz

        #enquanto não chegar no final
        while(vertice_atual!=termino):
            #checa os vertices vizinhos do vertice atual
            for i in self.vertices[vertice_atual].neighbors:
                #se a distancia do vertice atual até o vizinho for menor do que a distancia atual do vizinho atualiza a distancia do vizinho
                if(self.vertices[i[0]].dist==-1 or self.vertices[i[0]].dist > self.vertices[vertice_atual].dist+i[1]):
                    
                    self.vertices[i[0]].dist = self.vertices[vertice_atual].dist+i[1]
                    self.vertices[i[0]].pred = vertice_atual
            
            #marca o vertice atual como vizitado
            lista.remove(vertice_atual)
            vertice_atual = lista[0]
            #define o vertice atual como o vertice não vizitado de menor distancia
            for i in lista:
                if((self.vertices[vertice_atual].dist>self.vertices[i].dist and self.vertices[i].dist!=-1) or(self.vertices[vertice_atual].dist==-1)):
                    vertice_atual=i
        #printa todos os vertices
        self.printAll()

        caminho = []

        #adiciona o ultimo vertice no caminho e volta 
        while(vertice_atual!=raiz):
            caminho.append(vertice_atual)
            vertice_atual = self.vertices[vertice_atual].pred
        caminho.append(vertice_atual)

        #inverte o caminho pra ficar na ordem certa
        caminho.reverse()

        print(caminho)


    def printAll(self):
        for i in self.vertices:
            print(self.vertices[i].name,self.vertices[i].dist,self.vertices[i].pred)




grafo = Graph()

grafo.addVertice("s",0,10)
grafo.addVertice("a",10,0)
grafo.addVertice("b",20,0)
grafo.addVertice("c",15,10)
grafo.addVertice("d",20,20)
grafo.addVertice("t",15,25)
grafo.addEdge("s","a",18)
grafo.addEdge("s","c",15)
grafo.addEdge("a","b",9)
grafo.addEdge("a","c",6)
grafo.addEdge("b","c",14)
grafo.addEdge("b","d",10)
grafo.addEdge("b","t",28)
grafo.addEdge("c","d",7)
grafo.addEdge("d","t",36)


grafo.dijkstra("s","t")