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

    # Diameter of a graph
    def diameter_of_graph(self):
        node_list = list(self.adj_list.keys())
        start = node_list[0]
        visited = {key: False for key in self.adj_list}

        def dfs(node):
            visited[node] = True
            deepest_node = node
            max_dist = 0

            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    curr_dist,deep_node = dfs(neighbour)

                    if curr_dist + 1 > max_dist:
                        max_dist = curr_dist + 1
                        deepest_node = deep_node

            return max_dist,deepest_node

        dist,imm_node = dfs(start)
        visited = {key: False for key in self.adj_list}
        max_dist,final_node = dfs(imm_node)

        return max_dist,imm_node,final_node

    # 2 edge connectivity
    def edge_connectivity(self):
        node_list = list(self.adj_list.keys())
        start = node_list[0]
        time = 0
        visited = {key: False for key in self.adj_list}
        parent = {key: None for key in self.adj_list}
        arr = {key: -1 for key in self.adj_list}
        dbe = {key: -1 for key in self.adj_list}
        is_2EC = True

        def EC(node):
            nonlocal time,is_2EC
            arr[node] = time
            dbe[node] = time
            time += 1
            visited[node] = True


            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    parent[neighbour] = node
                    EC(neighbour)

                    dbe[node] = min(dbe[node],dbe[neighbour])

                    if dbe[neighbour] > arr[node]: # bridge detection condition
                        is_2EC = False

                elif neighbour != parent[node]: # back edge condtion
                    dbe[node] = min(dbe[node], arr[neighbour])

            time += 1

        EC(start)

        if not all(visited.values()):
            return False
        return is_2EC

    # def edge_connectivity(self):
    #     node_list = list(self.adj_list.keys())
    #     start = node_list[0]
    #     time = 0
    #     visited = {key: False for key in self.adj_list}
    #     parent = {key: None for key in self.adj_list}
    #     arr = {key: -1 for key in self.adj_list}  # Discovery time of each node
    #     low = {key: -1 for key in self.adj_list}  # Low-link values of each node
    #     is_2_edge_connected = True  # To track if the graph is 2-edge-connected
    #
    #     def EC(node):
    #         nonlocal time, is_2_edge_connected
    #         visited[node] = True
    #         arr[node] = low[node] = time
    #         time += 1
    #
    #         for neighbour in self.adj_list[node]:
    #             if not visited[neighbour]:  # If neighbor is not visited
    #                 parent[neighbour] = node
    #                 EC(neighbour)
    #
    #                 # Update low-link value after visiting child
    #                 low[node] = min(low[node], low[neighbour])
    #
    #                 # Check if the edge is a bridge
    #                 if low[neighbour] > arr[node]:  # Condition for bridge
    #                     is_2_edge_connected = False
    #
    #             elif neighbour != parent[node]:  # Back edge to an ancestor
    #                 low[node] = min(low[node], arr[neighbour])
    #
    #     # Start DFS from the start node
    #     EC(start)
    #
    #     # Check if the graph is connected (all nodes should be visited)
    #     if not all(visited.values()):
    #         return False  # Not 2-edge-connected if the graph is disconnected
    #
    #     return is_2_edge_connected


graph1_list = [(1,2),(1,3),(2,3),(2,5),(3,8),(3,4),(4,5),(4,7),(5,7),(6,7),(8,9),(8,10),(6,11),(11,6)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
print(graph1.diameter_of_graph())
print(graph1.edge_connectivity())

graph2_list = [(1, 2), (1, 7), (2, 3), (2, 7), (3, 4), (3, 8), (4, 5), (4, 8), (5, 8), (7, 8)]
graph2 = Graph()
graph2.add_edges(graph2_list)
graph2.print_adj_list()
print(graph2.edge_connectivity())

class Directed_Graph():
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

    def kosaraju_scc(self,graph):
        # Step 1: DFS to get the finishing times of vertices
        def dfs1(v, visited, graph, stack):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs1(neighbor, visited, graph, stack)
            stack.append(v)

        # Step 2: Reverse the graph (transpose)
        def transpose_graph(graph):
            transposed = {i: [] for i in graph}
            for v in graph:
                for neighbor in graph[v]:
                    transposed[neighbor].append(v)
            return transposed

        # Step 3: DFS on the reversed graph to discover SCCs
        def dfs2(v, visited, transposed, scc):
            visited[v] = True
            scc.append(v)
            for neighbor in transposed[v]:
                if not visited[neighbor]:
                    dfs2(neighbor, visited, transposed, scc)

        # Main part of the Kosaraju's algorithm
        stack = []
        visited = {v: False for v in graph}

        # Perform DFS to fill vertices in stack by finish time
        for v in graph:
            if not visited[v]:
                dfs1(v, visited, graph, stack)

        # Step 4: Transpose the graph
        transposed_graph = transpose_graph(graph)

        # Step 5: Perform DFS on the reversed graph using the order in the stack
        visited = {v: False for v in graph}
        scc_list = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                scc = []
                dfs2(v, visited, transposed_graph, scc)
                scc_list.append(scc)

        return scc_list

