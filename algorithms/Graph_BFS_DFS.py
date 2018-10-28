import sys


class Vertex(object):

    def __init__(self, n):

        self.name = n
        self.neighbours = []
        self.dist = sys.maxsize
        self.color = "White"
        self.parent = None

    def neighbour(self, v):

        if v not in self.neighbours:
            self.neighbours.append(v)


class Graph(object):

    vertices = {}

    def add_vertex(self, v):

        new_vertex = Vertex(v)

        if v not in self.vertices:
            self.vertices[v] = new_vertex

    def add_edge(self, u, v):

        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.neighbour(self.vertices[v])
                if key == v:
                    value.neighbour(self.vertices[u])

            return True

        return False

    def print_graph(self):

        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours) + "  " + str(self.vertices[key].dist))

    def bfs(self, s, d):

        source_vertex = self.vertices[s]

        for v in source_vertex.neighbours:
            v.color = "White"
            v.dist = sys.maxsize
            v.parent = None

        source_vertex.color = "Gray"
        source_vertex.dist = 0
        source_vertex.parent = None
        queue = [source_vertex]

        while len(queue) > 0:

            u = queue.pop(0)

            for v in u.neighbours:
                if v.color == "White":
                    v.color = "Gray"
                    v.dist = u.dist + 1
                    v.parent = u
                    queue.append(v)

            u.color = "Black"

        s_path = []
        path = self.vertices[d]

        while path:
            s_path.append(path.name)
            path = path.parent

        return s_path

    def dfs(self):

        for v in self.vertices:
            v.color = "White"
            self.dfs_visit(v)

    def dfs_visit(self, u):

        u.color = "Gray"

        for v in u.neighbours:
            if v.color == "White":
                v.parent = u
                self.dfs_visit(v)

        u.color = "Black"


g = Graph()
for i in range(ord('A'), ord('K')):
    g.add_vertex(chr(i))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'GH', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

print(g.bfs('A', 'H'))
