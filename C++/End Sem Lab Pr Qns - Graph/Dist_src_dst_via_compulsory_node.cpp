# include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int distSrctoDestvisIntermediateNode(vector<tuple<int,int,int>> edge_list,int src,int dst,int mandatory) {
        unordered_map<int,vector<pair<int,int>>> adj_list;

        for (auto [u,v,w]: edge_list) {
            adj_list[u].emplace_back(v,w);
            adj_list[v].emplace_back(u, w);
        }

        // function<int> Dijkstra (int source,int dest){
        auto Dijkstra = [&](int source, int dest) -> int { // Fix: Use a lambda and specify return type explicitly.
            unordered_map<int,int> d;
            for (auto &elem: adj_list) {
                d[elem.first] = INT_MAX;
            }

            d[source] = 0;
            priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> min_heap;
            min_heap.emplace(0,source); // dist,node

            while (! min_heap.empty()) {
                int node,curr_dist;
                tie(curr_dist,node) = min_heap.top();
                min_heap.pop();

                if (node == dest)
                    return curr_dist;

                if (curr_dist > d[node])
                    continue;

                for (auto [neighbour,weight]: adj_list[node]) {
                    int temp_dist = curr_dist + weight;

                    if (temp_dist < d[neighbour]) {
                        d[neighbour] = temp_dist;
                        min_heap.emplace(temp_dist,neighbour);
                    }
                }

            }
            return -1;
        };

        // Calculate the two parts of the path
        int part1 = Dijkstra(src, mandatory);
        int part2 = Dijkstra(mandatory, dst);

        if (part1 == -1 || part2 == -1)
            return -1; // If any part of the path is unreachable, return -1.

        cout << part1 << " " << part2 << endl;
        return part1 + part2; // Return the total distance.
        // return Dijkstra(src,mandatory) + Dijkstra(mandatory,dst);
    }
};

int main() {
    Solution sol;
    vector<tuple<int, int, int>> edges = {
        {0, 1, 4}, {0, 2, 2}, {1, 2, 5}, {1, 3, 10}, {2, 3, 3}, {3, 4, 1}
    };

    int n = 5;
    int src = 0;
    int dst = 4;
    int mandatory = 2;

    int result = sol.distSrctoDestvisIntermediateNode(edges, src, dst, mandatory);

    cout << "Shortest path weight via mandatory node: " << result << endl;

    return 0;
}