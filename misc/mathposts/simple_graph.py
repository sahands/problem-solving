class simple_graph(object):
    """Implements a weighted simple graph."""
    def __init__(self):
        self.vertices = dict()
        self.edges = dict()

    def add_vertex(self, label):
        self.vertices[label] = []

    def add_vertices(self, labels):
        for l in labels:
            self.add_vertex(l)

    def add_edge(self, source, target, weight=None):
        e = frozenset([source, target])
        if len(e) == 1:
            raise ValueError("No loops allowed!")

        for x in e:
            if x not in self.vertices:
                self.vertices[x] = [e]
            else:
                self.vertices[x].append(e)

        self.edges[e] = weight

    def get_vertices(self):
        return self.vertices.keys()

    def get_edges(self):
        return self.edges.keys()

    def get_edge_weight_tuples(self):
        return self.edges.items()

    def get_adjacency_list(self, vertex):
        return self.vertices[vertex]

    def __str__(self):
        return self.edges.items().__str__()

    def mst_kruskal(self):
        mst = []
        weight_sum = 0
        forest = dict()
        for x in self.vertices:
            forest[x] = {x}
        sorted_edges = sorted(self.get_edge_weight_tuples(),
                              key=lambda e: e[1])
        for e in sorted_edges:
            u = list(e[0])[0]
            v = list(e[0])[1]
            if forest[u] is not forest[v]:
                mst.append(e)
                weight_sum += e[1]
                s = forest[u] | forest[v]
                for x in s:
                    forest[x] = s
        return mst, weight_sum


if __name__ == '__main__':
    g = simple_graph()
    g.add_edge('a', 'b', 4)
    g.add_edge('b', 'c', 8)
    g.add_edge('c', 'd', 9)
    g.add_edge('d', 'e', 9)
    g.add_edge('e', 'f', 10)
    g.add_edge('d', 'f', 14)
    g.add_edge('f', 'g', 2)
    g.add_edge('g', 'h', 1)
    g.add_edge('h', 'a', 8)
    g.add_edge('b', 'h', 11)
    g.add_edge('h', 'i', 7)
    g.add_edge('i', 'c', 2)
    g.add_edge('i', 'g', 6)
    g.add_edge('c', 'f', 4)

    t, w = g.mst_kruskal()
    print w
    for e, w in t:
        print list(e)

