"implimeting an UNDIRECTED Graph"

from collections import defaultdict
 
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"], 
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
     
    
    for edge in edges:
        a, b = edge[0], edge[1]
         
        
        graph[a].append(b)
        graph[b].append(a)
    return graph
 
if __name__ == "__main__":
    graph = build_graph()
     
    print(graph)
    
    

'''implementing directed graph'''
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(3, 0, 4)
g.add_edge(2, 1, 1)
g.print_graph()
    
'''implimenting and searching in a graph'''
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []
def main():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    vertex = 'B'
    neighbors = graph.get_neighbors(vertex)
    print(f"The neighbors of vertex {vertex} are: {neighbors}")
if __name__ == "__main__":
    main()
    
'''implementing a WEIGHTED graph'''
class Graph:
     def __init__(self, size):
       self.adj_matrix = [[0] * size for _ in range(size)]
       self.size = size
       self.vertex_data = [''] * size
     def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = weight
          self.adj_matrix[v][u] = weight 
     def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
         self.vertex_data[vertex] = data
     def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
           print(' '.join(map(str, row)))
           print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
         print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3) 
g.add_edge(0, 3, 7) 
g.add_edge(1, 2, 2) 
g.print_graph()

'''creating an Acyclic graph'''
class Graph:
    def __init__(self, size):
     self.adj_matrix = [[0] * size for _ in range(size)]
     self.size = size
     self.vertex_data = [''] * size
    def add_edge(self, u, v):
     if 0 <= u < self.size and 0 <= v < self.size:
      self.adj_matrix[u][v] = 1
    def add_vertex_data(self, vertex, data):
     if 0 <= vertex < self.size:
      self.vertex_data[vertex] = data
    def print_graph(self):
     print("Adjacency Matrix:")
     for row in self.adj_matrix:
      print(' '.join(map(str, row)))
     print("\nVertex Data:")
     for vertex, data in enumerate(self.vertex_data):
      print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

'''creating a CYCLIC graph'''
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
         if 0 <= u < self.size and 0 <= v < self.size:
          self.adj_matrix[u][v] = 1
          self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
         if 0 <= vertex < self.size:
          self.vertex_data[vertex] = data
    def print_graph(self):
         print("Adjacency Matrix:")
         for row in self.adj_matrix:
            print(' '.join(map(str, row)))
         print("\nVertex Data:")
         for vertex, data in enumerate(self.vertex_data):
          print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.print_graph()

