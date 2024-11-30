from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,u,v):
        if v is None:
            self.adj_list[u] = [v]

        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

        if v in self.adj_list:
            self.adj_list[v].append(u)
        else:
            self.adj_list[v] = [u]

    def add_edges(self,edge_list):
        for u,v in edge_list:
            self.add_edge(u,v)

    def print_adj_list(self):
        print(self.adj_list)

    def bfs(self,start):
        queue = deque()

        parent = {key: None for key in self.adj_list}
        level = {key: -1 for key in self.adj_list}
        visited = {key: False for key in self.adj_list}

        queue.append(start)
        level[start] = 0
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(f"node: {node}, parent: {parent[node]}, level: {level[node]}")

            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    parent[neighbour] = node
                    level[neighbour] = level[node] + 1
                    queue.append(neighbour)
        print()

    def dfs_iterative(self,start):
        stack = deque()

        time = 0
        parent = {key: None for key in self.adj_list}
        visited = {key: False for key in self.adj_list}
        arr = {key: -1 for key in self.adj_list}
        dep = {key: -1 for key in self.adj_list}

        stack.append((start,"In"))
        while stack:
            node,state = stack.pop()

            if state == "In":
                if not visited[node]:
                    visited[node] = True
                    arr[node] = time
                    time += 1
                    print(f"node: {node}, parent: {parent[node]}")
                    stack.append((node,"Out"))

                    for neighbour in self.adj_list[node]:
                        if not visited[neighbour]:
                            stack.append((neighbour,"In"))
                            parent[neighbour] = node

            else:
                time += 1
                dep[node] = time

        print(arr)
        print(dep)

    def dfs_rec(self,start):
        parent = {key: None for key in self.adj_list}
        visited = {key: False for key in self.adj_list}
        arr = {key: -1 for key in self.adj_list}
        dep = {key: -1 for key in self.adj_list}
        time = 0
        tree_edges = []
        back_edges = []

        def rec_helper(node):
            if visited[node]:
                return

            nonlocal time
            print(node,end = " ")
            visited[node] = True
            arr[node] = time
            time += 1
            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    parent[neighbour] = node
                    tree_edges.append((node,neighbour))
                    rec_helper(neighbour)
                elif neighbour != parent[node] and arr[neighbour] <  arr[node]:
                    back_edges.append((node,neighbour))

            time += 1
            dep[node] = time

        rec_helper(start)
        print()
        print(arr)
        print(dep)
        print(parent)
        print(tree_edges)
        print(back_edges)


graph1_list = [(1,2),(1,3),(2,3),(2,5),(3,8),(3,4),(4,5),(4,7),(5,7),(6,7),(8,9),(8,10)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
graph1.bfs(1)
print()
graph1.dfs_iterative(1)
print()
graph1.dfs_rec(1)
print()

