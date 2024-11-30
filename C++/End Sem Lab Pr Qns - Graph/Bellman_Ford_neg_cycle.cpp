#include <bits/stdc++.h>

using namespace std;

class Graph {
public:
    unordered_map<int, vector<pair<int, int>>> adj_list;

    void add_edge(int u, int v, int weight) {
        adj_list[u].emplace_back(v, weight);
    }

    tuple<unordered_map<int, int>, unordered_map<int, int>, bool> bellman_ford(int start) {
        unordered_map<int, int> d;
        unordered_map<int, int> parent;
        set<int> negative_cycle_nodes;
        set<int> reachable_from_neg_cycle;

        for (auto& node : adj_list) {
            d[node.first] = numeric_limits<int>::max();
            parent[node.first] = -1;
        }
        d[start] = 0;

        int num_nodes = adj_list.size();
        for (int i = 0; i < num_nodes - 1; i++) {
            for (auto& [u, neighbors] : adj_list) {
                for (auto& [v, weight] : neighbors) {
                    if (d[u] != numeric_limits<int>::max() && d[v] > d[u] + weight) {
                        d[v] = d[u] + weight;
                        parent[v] = u;
                    }
                }
            }
        }

        for (auto& [u, neighbors] : adj_list) {
            for (auto& [v, weight] : neighbors) {
                if (d[u] != numeric_limits<int>::max() && d[v] > d[u] + weight) {
                    negative_cycle_nodes.insert(v);
                }
            }
        }

        if (!negative_cycle_nodes.empty()) {
            auto dfs = [&](int v, auto& dfs_ref) -> void {
                if (reachable_from_neg_cycle.find(v) == reachable_from_neg_cycle.end()) {
                    reachable_from_neg_cycle.insert(v);
                    for (auto& [neighbor, _] : adj_list[v]) {
                        dfs_ref(neighbor, dfs_ref);
                    }
                }
            };

            for (int node : negative_cycle_nodes) {
                dfs(node, dfs);
            }

            if (reachable_from_neg_cycle.find(start) != reachable_from_neg_cycle.end()) {
                return {d, parent, true};
            } else {
                return {d, parent, false};
            }
        }

        return {d, parent, false};
    }
};

int main() {
    Graph g;
    g.add_edge(0, 1, 4);
    g.add_edge(1, 2, -10);
    g.add_edge(2, 3, 3);
    g.add_edge(3, 1, 1);

    auto [distances, parents, has_negative_cycle] = g.bellman_ford(0);

    cout << "Distances from source:" << endl;
    for (auto& [node, dist] : distances) {
        cout << "Node " << node << ": " << (dist == numeric_limits<int>::max() ? "INF" : to_string(dist)) << endl;
    }

    cout << "Has negative cycle reachable from source: " << (has_negative_cycle ? "Yes" : "No") << endl;

    return 0;
}
