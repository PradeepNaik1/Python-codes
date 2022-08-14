from collections import defaultdict


class vertex:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return self.__name


class Edge:
    def __init__(self, v1, v2):
        self.__source_vertex = v1
        self.__target_vertex = v2

    def get_source(self):
        return self.__source_vertex

    def get_target(self):
        return self.__target_vertex


class Graph:

    def __init__(self):
        self.__adjacency_list = defaultdict(list)

    # def add_adjacency(self, v1, v2):
    #     self.__adjacency_list[v1].append(v2)
    #     self.__adjacency_list[v2].append(v1)

    def print_graph(self):
        for key, val  in self.__adjacency_list.items():
            print(key, ":", val)
    
    def add_edges(self, edge_list):
        for edge in edge_list:
            v1 = edge.get_source()
            v2 = edge.get_target()
            self.__adjacency_list[v1].append(v2)
            self.__adjacency_list[v2].append(v1)


v0 = vertex('Delhi')
v1 = vertex('Banglore')
v2 = vertex('Kolkata')
v3 = vertex('Chennai')


e1 = Edge(v0, v1)
e2 = Edge(v0, v2)
e3 = Edge(v0, v3)
e4 = Edge(v1, v2)

edge = [e1, e2, e3, e4]

g = Graph()

g.add_edges(edge)
# g.add_adjacency(v0, v1)
# g.add_adjacency(v0, v2)
# g.add_adjacency(v0, v3)
# g.add_adjacency(v1, v2)

g.print_graph()
