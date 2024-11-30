import heapq

class Union_Find:
    def __init__(self, adj_list):
        self.parent = {key: key for key in adj_list}
        self.rank = {key: 1 for key in adj_list}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def add_edges(self, edge_list):
        for u, v, weight in edge_list:
            self.add_edge(u, v, weight)

    def mst_kruskal(self, edge_list):
        edge_list.sort(key=lambda x: x[2])  # Sort edges by weight
        uf = Union_Find(self.adj_list)
        mst = []
        for u, v, weight in edge_list:
            if uf.union(u, v):
                mst.append((u, v, weight))
                if len(mst) == len(self.adj_list) - 1:  # MST is complete
                    break
        return mst

    def second_mst(self, edge_list):
        # Find the original MST
        og_mst_edges = self.mst_kruskal(edge_list)
        og_mst_weight = sum(weight for _, _, weight in og_mst_edges)

        # Create an optimized approach for second MST
        sec_mst_weight = float("inf")

        # Iterate through each edge in the original MST
        for removed_edge in og_mst_edges:
            uf = Union_Find(self.adj_list)
            mst_weight = 0
            mst_edges = []

            for u, v, weight in edge_list:
                if (u, v, weight) == removed_edge or (v, u, weight) == removed_edge:
                    continue  # Skip the removed edge
                if uf.union(u, v):
                    mst_edges.append((u, v, weight))
                    mst_weight += weight
                    if len(mst_edges) == len(self.adj_list) - 1:  # MST complete
                        break

            # Check if the MST formed after removing `removed_edge` is valid
            if len(mst_edges) == len(self.adj_list) - 1 and mst_weight > og_mst_weight:
                sec_mst_weight = min(sec_mst_weight, mst_weight)

        return sec_mst_weight if sec_mst_weight != float("inf") else "2nd MST doesn't exist"





# Example Usage
graph1_list = [
    ('A', 'B', 2), ('B', 'F', 8), ('F', 'E', 1), ('B', 'D', 1), ('A', 'D', 7),
    ('A', 'C', 10), ('B', 'C', 3), ('F', 'C', 4), ('D', 'C', 5), ('C', 'G', 11),
    ('D', 'E', 13), ('C', 'H', 9), ('E', 'H', 2)
]

graph1 = Graph()
graph1.add_edges(graph1_list)

# Find the original MST and the second MST
print("Original MST:", graph1.mst_kruskal(graph1_list))
print("Second MST Weight:", graph1.second_mst(graph1_list))
