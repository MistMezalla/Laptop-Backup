# undirected list(list) implementation
from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,u,v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

        if v in self.adj_list:
            self.adj_list[v].append(u)
        else:
            self.adj_list[v] = [u]


    def add_edges(self,edge_list):
        for edges in edge_list:
            if edges[0] in self.adj_list:
                self.adj_list[edges[0]].append(edges[1])
            else:
                self.adj_list[edges[0]] = [edges[1]]

            if edges[1] in self.adj_list:
                self.adj_list[edges[1]].append(edges[0])
            else:
                self.adj_list[edges[1]] = [edges[0]]

    def del_edge(self,u,v):
        self.adj_list[u].remove(v)
        if self.adj_list[u] is None:
            del self.adj_list[u]
        self.adj_list[v].remove(u)
        if self.adj_list[v] is None:
            del self.adj_list[v]


    def print_adj_list(self):
        print(self.adj_list)

    def bfs(self,start):
        visited = {key: False for key in self.adj_list}
        parent = {key: None for key in self.adj_list}
        level = {key: -1 for key in self.adj_list}
        queue = deque()
        queue.append(start)
        visited[start] = True
        level[start] = 0

        while queue:
            node = queue.popleft()
            print(f"node : {node} parent : {parent[node]} level : {level[node]}")

            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    parent[neighbour] = node
                    level[neighbour] = level[node] + 1
                    queue.append(neighbour)
        print()



graph1_list = [(1,2),(1,3),(2,3),(2,5),(3,8),(3,4),(4,5),(4,7),(5,7),(6,7),(8,9),(8,10)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
graph1.bfs(1)
print()
