#include <bits/stdc++.h>
using namespace std;

class Graph_undirected {
public:
    unordered_map<int,vector<int>> adj_list_from_adj_matrix(vector<vector<int>> &adj_matrix) {
        unordered_map<int,vector<int>> adj_list;

        for(int i = 0; i < static_cast<int>(adj_matrix.size()); i++) {
            for(int j = 0; j < static_cast<int>(adj_matrix[i].size()); j++) {
                if (adj_matrix[i][j] == 1) {
                    if (adj_list.find(i) != adj_list.end()) {
                        adj_list[i].push_back(j);
                    } else {
                        adj_list[i] = {j};
                    }
                }
            }
        }

        return adj_list;
    }

    void print_adj_list(unordered_map<int, vector<int>> &adj_list) {
        for (const auto &pair : adj_list) {
            cout << "Vertex " << pair.first << ": ";
            for (int neighbor : pair.second) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }

    vector<vector<int>> adj_matrix_from_adj_list(unordered_map<int,vector<int>> &adj_list) {
        int n = 0;
        for (const auto &elem: adj_list) {
            n = max(n, elem.first);
        }

        vector<vector<int>> adj_matrix(n + 1, vector<int>(n + 1, 0));

        for (const auto &u: adj_list) {
            for (int neighbor : u.second) {
                adj_matrix[u.first][neighbor] = 1;
            }
        }

        return adj_matrix;
    }

    void print_adj_matrix(vector<vector<int>> &adj_matrix) {
        for (int i = 0; i < static_cast<int>(adj_matrix.size()); i++) {
            for (int j = 0; j < static_cast<int>(adj_matrix[i].size()); j++) {
                cout << adj_matrix[i][j] << "\t";
            }
            cout << "\n";
        }
    }
};

class Graph_directed {
public:
    unordered_map<int,vector<int>> adj_list_from_adj_matrix(vector<vector<int>> &adj_matrix) {
        unordered_map<int,vector<int>> adj_list;

        for(int i = 0; i < static_cast<int>(adj_matrix.size()) ; i++) {
            for (int j = 0; j < static_cast<int> (adj_matrix[i].size()); j++) {
                if (adj_list.find(i) != adj_list.end()) {
                    adj_list[i].push_back(j);
                }
                else {
                    adj_list[i] = {j};
                }
            }
        }

        return adj_list;
    }

    void print_adj_list(unordered_map<int,vector<int>> &adj_list) {
        for(auto &pair: adj_list) {
            cout << pair.first << " : ";
            for (auto elem: pair.second) {
                cout << elem << ", ";
            }
            cout << endl;
        }
    }

    vector<vector<int>> adj_matrix_from_adj_list(unordered_map<int,vector<int>> &adj_list) {
        int n;
        for (auto &pair: adj_list) {
            n = max(n,pair.first);
        }

        vector<vector<int>> adj_matrix(n+1,vector<int>(n+1,0));
    }
};

int main() {
    vector<vector<int>> adj_matrix = {
        {0, 1, 0, 1},
        {1, 0, 1, 0},
        {0, 1, 0, 0},
        {1, 0, 0, 0}
    };

    Graph_undirected graph;
    unordered_map<int, vector<int>> adj_list = graph.adj_list_from_adj_matrix(adj_matrix);
    graph.print_adj_list(adj_list);

    vector<vector<int>> adj_matrix_converted = graph.adj_matrix_from_adj_list(adj_list);
    graph.print_adj_matrix(adj_matrix_converted);

    return 0;
}
