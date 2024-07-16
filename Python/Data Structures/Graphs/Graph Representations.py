# For undirected graphs
'''
-> In python versions 3.7 + dictionaries maintain insertion order.
-> Sets are still unordered
'''
class Graph:
    def __init__(self,vertices):
        self.num_vertices = vertices
        self.adj_list = [[] for _ in range(vertices+1)]
        self.adj_matrix = [[0]*(vertices+1) for _ in range(vertices + 1)]
        self.adj_set = [set() for _ in range(vertices + 1)]
        # self.adj_dict = {v: [] for v in range(vertices+1)}
        '''
        -> The abv dict representation is of no use wrt sparse graphs
        '''
        self.adj_dict = {}

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.adj_set[u].add(v)
        self.adj_set[v].add(u)

        if u in self.adj_dict:
            self.adj_dict[u].append(v)
        else:
            self.adj_dict[u] = [v]

        if v in self.adj_dict:
            self.adj_dict[v].append(u)
        else:
            self.adj_dict[v] = [u]


    def add_edges(self,edge_list):
        for edges in edge_list:
            self.adj_list[edges[0]].append(edges[1])
            self.adj_list[edges[1]].append(edges[0])
            self.adj_matrix[edges[0]][edges[1]] = 1
            self.adj_matrix[edges[1]][edges[0]] = 1
            self.adj_set[edges[0]].add(edges[1])
            self.adj_set[edges[1]].add(edges[0])

            if edges[0] in self.adj_dict:
                self.adj_dict[edges[0]].append(edges[1])
            else:
                self.adj_dict[edges[0]] = [edges[1]]

            if edges[1] in self.adj_dict:
                self.adj_dict[edges[1]].append(edges[0])
            else:
                self.adj_dict[edges[1]] = [edges[0]]
    def del_edge(self,u,v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0
        self.adj_set[u].remove(v)
        self.adj_set[v].remove(u)

        self.adj_dict[u].remove(v)
        if self.adj_dict[u] is None:
            del self.adj_dict[u]
        self.adj_dict[v].remove(u)
        if self.adj_dict[v] is None:
            del self.adj_dict[v]


    def print_adj_list(self):
        print(self.adj_list[1:])

    def print_adj_matrix(self):
        print(self.adj_matrix)

    def print_adj_set(self):
        print(self.adj_set[1:])

    def print_adj_dict(self):
        print(self.adj_dict)


# graph data in (vertex1, vertex2) format
graph1_list = [(1,2),(1,3),(2,3),(2,5),(3,8),(3,4),(4,5),(4,7),(5,7),(6,7),(8,9),(8,10)]
graph1 = Graph(10)
graph1.add_edges(graph1_list)
graph1.print_adj_list()
graph1.print_adj_set()
graph1.print_adj_dict()
graph1.print_adj_matrix()
graph1.add_edge(4,8)
graph1.print_adj_list()
graph1.print_adj_set()
graph1.print_adj_dict()
graph1.print_adj_matrix()
graph1.del_edge(3,8)
graph1.print_adj_list()
graph1.print_adj_set()
graph1.print_adj_dict()
graph1.print_adj_matrix()