class Vertex:
    def __init__(self, name):
        self.__name = name
        self.__visited = False
        self.__adjacent_vertex = []

    def get_name(self):
        return self.__name

    def set_visited(self, val):
        self.__visited = val

    def get_visited(self):
        return self.__visited

    def add_adjacent_vertex(self, vertex):
        self.__adjacent_vertex.append(vertex)

    def get_adjacent_vertex(self):
        return self.__adjacent_vertex


class BreathFirstSearch:

    def traverse_graph(self, vertex):
        queue = []
        queue.append(vertex)
        vertex.set_visited(True)
        while queue:
            v = queue.pop(0)
            print(v.get_name(), end=" ")
            for av in v.get_adjacent_vertex():
                if not av.get_visited():
                    av.set_visited(True)
                    queue.append(av)


a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
g = Vertex("G")
h = Vertex("H")

a.add_adjacent_vertex(b)
a.add_adjacent_vertex(f)
a.add_adjacent_vertex(g)
b.add_adjacent_vertex(c)
b.add_adjacent_vertex(d)
d.add_adjacent_vertex(e)
g.add_adjacent_vertex(h)

bfs = BreathFirstSearch()
bfs.traverse_graph(a)




