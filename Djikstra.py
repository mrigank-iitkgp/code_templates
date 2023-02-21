import heapq

class Edge :
    def __init__(self , vertex , weight) :
        self.vertex = vertex
        self.weight  = weight
    
    def __lt__(self , obj) :
        return self.weight <= obj.weight
    
    def __gt__(self , obj) :
        return self.weight > obj.weight
    

class Graph :
    def __init__(self , nVertex) :
        self.graph = [[] for _ in range(0 , nVertex)]
        self.nVertex = nVertex
    
    def add_edge(self , u , v , weight) :
        edge1 = Edge(v , weight)
        edge2 = Edge(u , weight)
        self.graph[u].append(edge1)
        self.graph[v].append(edge2)
    
    def print_graph(self) :
        for idx , child in enumerate(self.graph) :
            for edge in child :
                print(f" Source : {idx} , Dest : {edge.vertex} , Weight : {edge.weight}")
    
    def shortest_path(self , src) :
        pq = []
        heapq.heappush(pq , Edge(src , 0))
        dist = [float('inf') for _ in range(0 , self.nVertex)]
        dist[src] = 0

        while pq :
            startEdge = heapq.heappop(pq)
            u = startEdge.vertex
            wt = startEdge.weight
            # print(u , wt)
            for edge in self.graph[u] :
                if dist[edge.vertex] > dist[u] + edge.weight :
                    dist[edge.vertex] = dist[u] + edge.weight
                    heapq.heappush(pq , Edge(edge.vertex , dist[edge.vertex]))
        
        for i in range(0 , self.nVertex) :
            print(f"Shortest Distance from {src} to {i} is {dist[i]}")

if __name__ == "__main__" :
    start = [0 , 0 , 1 , 1 , 2 , 2 , 2 , 3 , 3 , 4 , 5 , 6 , 6 , 7]
    to = [1 , 7 , 2 , 7 , 3 , 8 , 5 , 4 , 5 , 5 , 6 , 7 , 8 , 8]
    weight = [4 , 8 , 8 , 11 , 7 , 2 , 4 , 9 , 14 , 10 , 2 , 1 , 6 , 7]

    graph = Graph(9)

    for i in range(0 , len(start)) :
        graph.add_edge(start[i] , to[i] , weight[i])
    graph.print_graph()
    graph.shortest_path(0)

