from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edges(self,edges):
        for u,v in edges:
            if v is None:
                self.adj_list[u] = []
                continue

            if u in self.adj_list:
                self.adj_list[u].append(v)
            else:
                self.adj_list[u] = [v]

            if v in self.adj_list:
                self.adj_list[v].append(u)
            else:
                self.adj_list[v] = [u]

    def print_adj_list(self):
        print(self.adj_list)

    # To find the connected in a graph
    def bfs_connected_component(self):
        queue = deque()

        visited = {key: False for key in self.adj_list}
        # parent = {key: None for key in self.adj_list}
        # level = {key: -1 for key in self.adj_list}
        connected_comp_number = {key: 0 for key in self.adj_list}
        node_list = list(connected_comp_number.keys())

        curr_number = 0
        i = 0
        while i < len(node_list):
            if connected_comp_number[node_list[i]] != 0:
                i += 1
            else:
                start = node_list[i]
                queue.append(start)
                visited[start] = True
                curr_number += 1
                connected_comp_number[start] = curr_number
                while queue:
                    node = queue.popleft()

                    for neighbour in self.adj_list[node]:
                        if not visited[neighbour]:
                            visited[neighbour] = True
                            queue.append(neighbour)
                            connected_comp_number[neighbour] = curr_number


        return curr_number

    # Is the graph bipartite?
    def is_graph_bipartite(self):
        queue = deque()
        node_list = list(self.adj_list.keys())
        start = node_list[0]

        visited = {key: False for key in self.adj_list}
        level = {key : -1 for key in self.adj_list}

        lvl = 0

        for start in node_list:
            visited[start] = True
            queue.append(start)
            while queue:
                n = len(queue)

                for node in queue:
                    level[node] = lvl

                lvl += 1
                for i in range(n):
                    node = queue.popleft()

                    for neighbour in self.adj_list[node]:
                        if level[node] == level[neighbour]:
                            return False
                        if not visited[neighbour]:
                            visited[neighbour] = True
                            queue.append(neighbour)

        return True



graph1_list = [(10,50),(83,None),(40,10),(12,43),(67,12),(12,75),(67,75),(21,7),(33,27),(52,15),(27,52),(1,15)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
print(graph1.bfs_connected_component())

graph2_list = [(10,1),(10,2),(20,1),(20,3),(30,1),(30,2),(30,3),(40,3),(4,None),(4,1),(4,20)]
graph2 = Graph()
graph2.add_edges(graph2_list)
graph2.print_adj_list()
print(graph2.is_graph_bipartite())
