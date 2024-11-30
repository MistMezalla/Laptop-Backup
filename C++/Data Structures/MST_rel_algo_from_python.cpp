#include <bits/stdc++.h>
using namespace std;

class Union_Find {
private:
    unordered_map<char, char> parent;
    unordered_map<char, int> rank;

public:
    Union_Find(unordered_map<char, vector<pair<char, int>>>& adj_list) {
        for (auto& elem : adj_list) {
            char node = elem.first;
            parent[node] = node;
            rank[node] = 1;
        }
    }

    char find(char x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool union_sets(char x, char y) {
        char root_x = find(x);
        char root_y = find(y);

        if (root_x != root_y) {
            if (rank[root_x] > rank[root_y]) {
                parent[root_y] = root_x;
                rank[root_x] += rank[root_y];
            } else if (rank[root_x] < rank[root_y]) {
                parent[root_x] = root_y;
                rank[root_y] += rank[root_x];
            } else {
                parent[root_y] = root_x;
                rank[root_x] += rank[root_y];
            }
            return true;
        }
        return false;
    }
};

class Graph {
private:
    unordered_map<char, vector<pair<char, int>>> adj_list;

public:
    void add_edge(char u, char v, int wt) {
        adj_list[u].emplace_back(v, wt);
        adj_list[v].emplace_back(u, wt);
    }

    void add_edges(vector<tuple<char, char, int>>& edge_list) {
        for (const auto& [u, v, wt] : edge_list) {
            add_edge(u, v, wt);
        }
    }

    void print_adj_list() {
        for (auto& [u, neighbors] : adj_list) {
            cout << u << " -> ";
            for (auto& [v, wt] : neighbors) {
                cout << "(" << v << ", " << wt << ") ";
            }
            cout << endl;
        }
    }

    vector<tuple<char, char, int>> mst_kruskal(vector<tuple<char, char, int>>& edge_list) {
        sort(edge_list.begin(), edge_list.end(), [](tuple<char, char, int>& a, tuple<char, char, int>& b) {
            return get<2>(a) < get<2>(b);
        });

        vector<tuple<char, char, int>> mst;
        Union_Find uf(adj_list);

        for (auto [u, v, wt] : edge_list) {
            if (uf.union_sets(u, v)) {
                mst.emplace_back(u, v, wt);
            }

            if (mst.size() == adj_list.size() - 1)
                break;
        }
        return mst;
    }

    unordered_map<char, char> mst_prims(char start) {
        unordered_map<char, int> d;
        unordered_map<char, char> parent;

        for (auto& elem : adj_list) {
            char node = elem.first;
            d[node] = INT_MAX;
            parent[node] = '\0';
        }

        d[start] = 0;
        priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> min_heap;
        min_heap.emplace(0, start);

        while (!min_heap.empty()) {
            int curr_weight;
            char node;

            tie(curr_weight, node) = min_heap.top();
            min_heap.pop();

            for (auto [neighbour, weight] : adj_list[node]) {
                if (d[neighbour] > weight) {
                    parent[neighbour] = node;
                    d[neighbour] = weight;
                    min_heap.emplace(weight, neighbour);
                }
            }
        }
        return parent;
    }

    pair<int, vector<tuple<char, char, int>>> sec_mst_kruskal_optimised(vector<tuple<char, char, int>>& edge_list) {
        vector<tuple<char, char, int>> og_mst_edge_list = mst_kruskal(edge_list);
        int og_mst_weight = 0;
        for (auto [u, v, w] : og_mst_edge_list) {
            og_mst_weight += w;
        }

        int sec_mst_weight = INT_MAX;
        vector<tuple<char, char, int>> second_mst_edge_list;

        for (auto rem_edge : og_mst_edge_list) {
            int temp_weight = 0;
            vector<tuple<char, char, int>> temp_list;
            Union_Find uf(adj_list);

            for (auto [u, v, w] : edge_list) {
                if (make_tuple(u, v, w) == rem_edge || make_tuple(v, u, w) == rem_edge) {
                    continue;
                }

                if (uf.union_sets(u, v)) {
                    temp_list.emplace_back(u, v, w);
                    temp_weight += w;

                    if (temp_list.size() == og_mst_edge_list.size()) {
                        break;
                    }
                }
            }
            if ((temp_list.size() == og_mst_edge_list.size()) && (temp_weight > og_mst_weight && temp_weight < sec_mst_weight)) {
                sec_mst_weight = temp_weight;
                second_mst_edge_list = temp_list;
            }
        }

        return {sec_mst_weight, second_mst_edge_list};
    }
};

int main() {
    vector<tuple<char, char, int>> graph1_list = {
        {'A', 'B', 2}, {'B', 'F', 8}, {'F', 'E', 1}, {'B', 'D', 1},
        {'A', 'D', 7}, {'A', 'C', 10}, {'B', 'C', 3}, {'F', 'C', 4},
        {'D', 'C', 5}, {'C', 'G', 11}, {'D', 'E', 13}, {'C', 'H', 9},
        {'E', 'H', 2}
    };

    Graph graph1;
    graph1.add_edges(graph1_list);

    cout << "Adjacency List:" << endl;
    graph1.print_adj_list();

    cout << "\nMST using Kruskal's Algorithm:" << endl;
    auto mst = graph1.mst_kruskal(graph1_list);
    for (auto [u, v, w] : mst) {
        cout << "(" << u << ", " << v << ", " << w << ") ";
    }
    cout << endl;

    cout << "\nSecond MST Weight and Edges:" << endl;
    auto [sec_weight, sec_mst] = graph1.sec_mst_kruskal_optimised(graph1_list);
    cout << "Weight: " << sec_weight << endl;
    for (auto [u, v, w] : sec_mst) {
        cout << "(" << u << ", " << v << ", " << w << ") ";
    }
    cout << endl;

    return 0;
}
