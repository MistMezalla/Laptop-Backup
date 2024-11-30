import heapq
class Union_Find:
    def __init__(self,adj_list):
        self.parent = {key: key for key in adj_list}
        self.rank = {key: 1 for key in adj_list}

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression

        return self.parent[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
            else:
                self.parent[root_y] = root_x  # WLOG assigning y to x
                self.rank[root_x] += self.rank[root_y]

            return True

        return False

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,u,v,weight):
        if u in self.adj_list:
            self.adj_list[u].append((v,weight))

        else:
            self.adj_list[u] = [(v,weight)]

        if v in self.adj_list:
            self.adj_list[v].append((u, weight))

        else:
            self.adj_list[v] = [(u, weight)]

    def add_edges(self,edge_list):
        for u,v,weight in edge_list:
            self.add_edge(u,v,weight)

    def print_adj_list(self):
        print(self.adj_list)

    def mst_kruskal(self,edge_list):
        edge_list.sort(key = lambda x: x[2])
        mst = []
        uf = Union_Find(self.adj_list)

        for u,v,weight in edge_list:
            if uf.union(u,v):
                mst.append((u,v,weight))

                if len(mst) == len(self.adj_list) - 1: # way to quickly terminate the loop. Without this cond as well the
                    break                        # ans will remain the same

        return mst

    def mst_prims(self,start):
        mst = []
        d = {key: float('inf') for key in self.adj_list}
        d[start] = 0
        min_heap = [(0,start)]
        parent = {key: None for key in self.adj_list}

        while min_heap:
            curr_weight,node = heapq.heappop(min_heap)

            if curr_weight > d[node]:
                continue

            for neighbour,w in self.adj_list[node]:
                weight = w + curr_weight

                if weight < d[neighbour]:
                    d[neighbour] = weight
                    heapq.heappush(min_heap,(weight,neighbour))
                    parent[neighbour] = node
                    #mst.append((node,neighbour,weight))

        return parent

    def second_mst(self,edge_list):
        og_mst_edge_list = self.mst_kruskal(edge_list)
        og_mst_weight = sum(weight for _,_,weight in og_mst_edge_list)

        sec_mst_weight = float("inf")
        sec_mst_edge_list = []
        for edge in og_mst_edge_list:
            temp_edge_list = [edges for edges in edge_list if edges != edge]

            new_mst_edge_list = self.mst_kruskal(temp_edge_list)

            if len(new_mst_edge_list) == len(og_mst_edge_list):
                new_mst_weight = sum(weight for _, _, weight in new_mst_edge_list)
                if og_mst_weight < new_mst_weight < sec_mst_weight:
                    sec_mst_weight = new_mst_weight
                    sec_mst_edge_list = new_mst_edge_list




        return sec_mst_weight,sec_mst_edge_list if sec_mst_weight != float("inf") else "2nd MST doesn't exist"

    def second_mst_optimised(self,edge_list):
        og_mst_edge_list = self.mst_kruskal(edge_list)
        og_mst_weight = sum(weight for _,_,weight in og_mst_edge_list)

        second_mst_weight = float("inf")
        second_mst_edge_list = []
        for rem_edge in og_mst_edge_list:
            uf = Union_Find(self.adj_list)
            temp_edge_list = []
            temp_weight = 0

            for u,v,wt in edge_list:
                if (u,v,wt) == rem_edge or (v,u,wt) == rem_edge:
                    continue
                if uf.union(u,v):
                    temp_weight += wt
                    temp_edge_list.append((u,v,wt))

                    if len(temp_edge_list) == len(og_mst_edge_list):
                        break

            if len(temp_edge_list) == len(og_mst_edge_list) and og_mst_weight < temp_weight < second_mst_weight:
                second_mst_edge_list = temp_edge_list
                second_mst_weight = temp_weight

        return second_mst_weight,second_mst_edge_list if second_mst_weight != float('inf') else "2nd MST doesn't exist"





graph1_list = [('A','B',2),("B","F",8),("F","E",1),("B","D",1),("A","D",7),("A","C",10),("B","C",3),("F","C",4),
              ("D","C",5),("C","G",11),("D","E",13),("C","H",9),("E","H",2)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
print()
print(graph1.mst_kruskal(graph1_list))
print(graph1.mst_prims("A"))
print(graph1.second_mst(graph1_list))
print(graph1.second_mst_optimised(graph1_list))

