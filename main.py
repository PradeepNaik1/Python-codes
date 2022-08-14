class Graph:
    def __init__(self, vertices):
        self.__vertices = vertices
        self.__adjacency_graph = [[0]*vertices for _ in range(vertices)]

    def add_edge(self, v1, v2):
        self.__adjacency_graph[v1][v2] = 1
        self.__adjacency_graph[v2][v1] = 1


    def print_graph(self):
        for row in self.__adjacency_graph:
            for val in row:
                print(val, end=" ")
            print()
    # For adding edge to directed graph the use this below commented method instead of add_edge()
    # def add_edge(self, v1, v2):
    #     self.__adjacency_graph[v1][v2] = 1


g = Graph(4)

g.add_edge(1,1)
g.add_edge(1,0)

g.print_graph()
