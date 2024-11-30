from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}
        self.tree_edges = []
        self.back_edges = []

    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

        if v in self.adj_list:
            self.adj_list[v].append(u)
        else:
            self.adj_list[v] = [u]

    def add_edges(self, edge_list):
        for u, v in edge_list:
            self.add_edge(u, v)

    def del_edge(self, u, v):
        self.adj_list[u].remove(v)
        if not self.adj_list[u]:
            del self.adj_list[u]
        self.adj_list[v].remove(u)
        if not self.adj_list[v]:
            del self.adj_list[v]

    def print_adj_list(self):
        print(self.adj_list)

    '''
    -> In python mutable obj like 'list and dict' are passed as ref whereas immutable obj like 'int,float,set,etc'
    are passed by value
    '''

    def dfs(self, start):
        stack = deque()
        visited = {key: False for key in self.adj_list}
        arr = {key: -1 for key in self.adj_list}
        dep = {key: -1 for key in self.adj_list}
        parent = {key: None for key in self.adj_list}
        time = 0

        stack.append((start, 'In'))
        while stack:
            node, state = stack.pop()

            if state == 'In':
                if not visited[node]:
                    visited[node] = True
                    time += 1
                    arr[node] = time
                    print(node, end=" ")
                    stack.append((node, "Out"))
                    if parent[node]:
                        self.tree_edges.append((parent[node],node))
                    for neighbour in self.adj_list[node]:
                        if not visited[neighbour]:
                            stack.append((neighbour, "In"))
                            parent[neighbour] = node
                        elif neighbour != parent[node]:
                            if arr[neighbour] < arr[node]:
                                self.back_edges.append((node, neighbour))
            elif state == "Out":
                time += 1
                dep[node] = time

        print()
        print(f"arr={arr}")
        print(f"dep={dep}")
        print(f"Tree edges: {self.tree_edges}")
        print(f"Back edges: {self.back_edges}")

    # def dfs_recursive(self, start):
    #     visited = {key: False for key in self.adj_list}
    #     arr = {key: -1 for key in self.adj_list}
    #     dep = {key: -1 for key in self.adj_list}
    #     time = [0]
    #     self.dfs_helper(start, visited, arr, dep, time)
    #     print()
    #     print(f"arr : {arr}")
    #     print(f"dep : {dep}")
    #
    # def dfs_helper(self, node, visited, arr, dep, time):
    #     if visited[node]:
    #         return
    #
    #     print(node, end=" ")
    #     visited[node] = True
    #     time[0] += 1
    #     arr[node] = time[0]
    #     for neighbour in self.adj_list[node]:
    #         if not visited[neighbour]:
    #             self.dfs_helper(neighbour, visited, arr, dep, time)
    #     time[0] += 1
    #     dep[node] = time[0]
    '''
    -> Instead of passing too many para to the helper() we can initialise these variables(like visited,arr,dep) 
    as 'instance(obj) variables' of the 'Graph class' under the dfs_recursive method 
    '''
    def dfs_recursive(self, start):
        self.visited = {key: False for key in self.adj_list}
        self.arr = {key: -1 for key in self.adj_list}
        self.dep = {key: -1 for key in self.adj_list}
        self.time = 0
        self.tree_edges = []
        self.back_edges = []
        self.parent = {key: None for key in self.adj_list}
        self.dfs_helper(start)
        print()
        print(f"arr : {self.arr}")
        print(f"dep : {self.dep}")
        print(f"Tree edges: {self.tree_edges}")
        print(f"Back edges: {self.back_edges}")

    def dfs_helper(self, node):
        if self.visited[node]:
            return

        print(node, end=" ")
        self.visited[node] = True
        self.time += 1
        self.arr[node] = self.time
        for neighbour in self.adj_list[node]:
            if not self.visited[neighbour]:
                self.tree_edges.append((node, neighbour))
                self.parent[neighbour] = node
                self.dfs_helper(neighbour)
            elif neighbour != self.parent[node] and self.arr[neighbour] < self.arr[node]:
                self.back_edges.append((node, neighbour))
        self.time += 1
        self.dep[node] = self.time


graph1_list = [(1, 2), (1, 3), (2, 3), (2, 5), (3, 8), (3, 4), (4, 5), (4, 7), (5, 7), (6, 7), (8, 9), (8, 10)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
graph1.dfs(1)
print()
graph1.dfs_recursive(1)
print()

class Dir_Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,u,v):
        if u in self.adj_list:
            self.adj_list[u].append(v)

        else:
            self.adj_list[u] = [v]

    def add_edges(self,edge_list):
        for u,v in edge_list:
            self.add_edge(u,v)

    def print_adj_list(self):
        print(self.adj_list)

    def dfs(self):
        visited = {key: 0 for key in self.adj_list} # 0 = not visited, 1 = in progress, 2 = finished
        time = 0
        arr = {key: 0 for key in self.adj_list}
        dep = {key: 0 for key in self.adj_list}
        node_list = list(self.adj_list.keys())

        back_edges = []
        tree_edges = []
        forward_edges = []
        cross_edges = []

        def rec_helper(node):
            visited[node] = 1
            nonlocal time
            arr[node] = time
            time += 1

            for neighbour in self.adj_list[node]:
                if visited[neighbour] == 0:
                    tree_edges.append((node,neighbour))
                    rec_helper(neighbour)
                elif visited[neighbour] == 1:
                    back_edges.append((node,neighbour))
                elif arr[neighbour] > arr[node]:
                    forward_edges.append((node,neighbour))
                else:
                    cross_edges.append((node,neighbour))

            visited[node] = 2
            dep[node] = time
            time += 1

        for node in node_list:
            if visited[node] != 2:
                rec_helper(node)

        print(tree_edges)
        print(back_edges)
        print(forward_edges)
        print(cross_edges)

# Define a directed graph
edge_list1 = [
    (0, 1),
    (1, 2),
    (2, 0),  # Back edge (cycle)
    (1, 3),
    (3, 4),
    (4, 1),  # Back edge (cycle)
    (3, 5),
    (5, 6),  # Tree edge
    (6, 3)   # Back edge (cycle)
]

# Create the graph and add edges
graph1 = Dir_Graph()
graph1.add_edges(edge_list1)

# Perform DFS and classify edges
graph1.print_adj_list()
graph1.dfs()

print()
edge_list2 = [
    (0, 1),
    (1, 2),
    (2, 0),  # Back edge (cycle)
    (1, 3),
    (3, 4),
    (4, 1),  # Back edge (cycle)
    (5, 6),  # Tree edge
    (6, 3),
    (0,4) # Back edge (cycle)
]
graph2 = Dir_Graph()
graph2.add_edges(edge_list2)

graph2.print_adj_list()
graph2.dfs()



