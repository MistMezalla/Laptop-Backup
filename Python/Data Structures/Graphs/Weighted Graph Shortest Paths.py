import heapq
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

    def Dijkstra(self,start):
        d = {node: float('inf') for node in self.adj_list}
        d[start] = 0

        #min_heap = [(d[node],node) for node in self.adj_list]
        #heapq.heapify(min_heap)
        #node_ind = {node: i for i,(_,node) in enumerate(min_heap)}
        min_heap = [(0,start)]
        parent = {node: None for node in self.adj_list}

        while min_heap:
            curr_dist,curr_node = heapq.heappop(min_heap)
            #node_ind.pop(curr_node)

            if curr_dist > d[curr_node]:
                continue

            for neighbour,weight in self.adj_list[curr_node]:
                dist = curr_dist + weight

                if dist < d[neighbour]:
                    parent[neighbour] = curr_node
                    d[neighbour] = dist
                    heapq.heappush(min_heap,(dist,neighbour))
                    # if neighbour in node_ind:
                    #     ind = node_ind[neighbour]
                    #     min_heap[ind] = (dist,neighbour)
                    #
                    #     while ind > 0 and min_heap[(ind-1)//2][0] > min_heap[ind][0]:
                    #         parent_ind = (ind-1)//2
                    #
                    #         min_heap[ind],min_heap[parent_ind] = min_heap[parent_ind],min_heap[ind]
                    #         node_ind[min_heap[ind][1]] = ind
                    #         node_ind[min_heap[parent_ind][1]] = parent_ind
                    #
                    #         ind = parent_ind

        return d,parent

    def bellman_ford(self,start):
        d = {node: float('inf') for node in self.adj_list}
        d[start] = 0
        node_list = list(self.adj_list.keys())
        parent = {node: None for node in self.adj_list}

        for i in range(len(node_list) - 1):
            for u in self.adj_list:
                for v,weight in self.adj_list[u]:
                    if d[v] > d[u] + weight:
                        d[v] = d[u] + weight
                        parent[v] = u


        for u in self.adj_list:
            for v,weight in self.adj_list[u]:
                if d[v] > d[u] + weight:
                    raise ValueError("There exists negative weight cycle")

        return d,parent


graph1_list = [('A','B',2),("B","F",8),("F","E",1),("B","D",1),("A","D",7),("A","C",10),("B","C",3),("F","C",4),
              ("D","C",5),("C","G",11),("D","E",13),("C","H",9),("E","H",2)]
graph1 = Graph()
graph1.add_edges(graph1_list)
graph1.print_adj_list()
print()
distances,parent = graph1.Dijkstra("A")
print(distances)
print(parent)
print()
distances,parent = graph1.bellman_ford("A")
print(distances)
print(parent)


