#include <bits/stdc++.h>

using namespace std;

class Graph {
public:
    unordered_map<int, vector<int>> adj_list;

    void add_edge(int u, int v) {
        adj_list[u].push_back(v);
    }

    void dfs1(int v, unordered_map<int, bool>& visited, stack<int>& s) {
        visited[v] = true;
        for (int neighbor : adj_list[v]) {
            if (!visited[neighbor]) {
                dfs1(neighbor, visited, s);
            }
        }
        s.push(v);
    }

    unordered_map<int, vector<int>> transpose_graph() {
        unordered_map<int, vector<int>> transposed;
        for (auto& [v, neighbors] : adj_list) {
            for (int neighbor : neighbors) {
                transposed[neighbor].push_back(v);
            }
        }
        return transposed;
    }

    void dfs2(int v, unordered_map<int, bool>& visited, unordered_map<int, vector<int>>& transposed, vector<int>& scc) {
        visited[v] = true;
        scc.push_back(v);
        for (int neighbor : transposed[v]) {
            if (!visited[neighbor]) {
                dfs2(neighbor, visited, transposed, scc);
            }
        }
    }

    vector<vector<int>> kosaraju_scc() {
        stack<int> s;
        unordered_map<int, bool> visited;
        for (auto& [v, _] : adj_list) {
            visited[v] = false;
        }

        for (auto& [v, _] : adj_list) {
            if (!visited[v]) {
                dfs1(v, visited, s);
            }
        }

        unordered_map<int, vector<int>> transposed_graph = transpose_graph();

        for (auto& [v, _] : adj_list) {
            visited[v] = false;
        }

        vector<vector<int>> scc_list;

        while (!s.empty()) {
            int v = s.top();
            s.pop();
            if (!visited[v]) {
                vector<int> scc;
                dfs2(v, visited, transposed_graph, scc);
                scc_list.push_back(scc);
            }
        }

        return scc_list;
    }
};

int main() {
    Graph g;
    g.add_edge(0, 1);
    g.add_edge(1, 2);
    g.add_edge(2, 0);
    g.add_edge(1, 3);
    g.add_edge(3, 4);

    vector<vector<int>> sccs = g.kosaraju_scc();
    for (const auto& scc : sccs) {
        for (int node : scc) {
            cout << node << " ";
        }
        cout << endl;
    }

    return 0;
}
