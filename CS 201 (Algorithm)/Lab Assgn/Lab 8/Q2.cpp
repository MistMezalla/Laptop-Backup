#include <bits/stdc++.h>
using namespace std;

class Graph_undirected {
public:
    bool connected_adj_list(unordered_map<int,vector<int>> &adj_list) {
        unordered_map<int,bool> visited;
        for (auto &pair: adj_list) {
            visited[pair.first] = false;
        }

        auto start = adj_list.begin()->first;
        queue<int> q;
        q.push(start);
        visited[start] = true;

        while (!q.empty()){
            auto node = q.front();
            q.pop();

            for (auto &neighbour: adj_list[node]) {
                if (!visited[neighbour]) {
                    visited[neighbour] = true;
                    q.push(neighbour);
                }
            }
        }

        for(auto &elem: visited) {
            if (!elem.second) {
                return false;
            }
        }

        return true;
    }

    bool connected_adj_matrix(vector<vector<int>> &adj_matrix) {
        unordered_map<int,bool> visited;
        for(int i = 0;i < static_cast<int>(adj_matrix.size());i++) {
            visited[i] = false;
        }

        int start = 0;
        queue<int> q;
        q.push(start);
        visited[start] = true;

        while (!q.empty()) {
            auto node = q.front();
            q.pop();

            for(int j = 0; j < static_cast<int>(adj_matrix[node].size()); j++) {
                if (adj_matrix[node][j] == 1 && !visited[j]) {
                    visited[j] = true;
                    q.push(j);
                }
            }

        }

        for(auto &elem: visited) {
            if (!elem.second) {
                return false;
            }
        }

        return true;
    }
};

class Graph_directed {
public:
    bool cycle_detection_directed_graph(unordered_map<int,vector<int>> &adj_list) {

    }
};

int main() {
    Graph_undirected graph_undirected;

    // Test Case 1: Connected graph adjacency matrix
    vector<vector<int>> adj_matrix1 = {
        {0, 1, 0, 1},
        {1, 0, 1, 1},
        {0, 1, 0, 1},
        {1, 1, 1, 0}
    };

    bool is_connected_matrix1 = graph_undirected.connected_adj_matrix(adj_matrix1);

    if (is_connected_matrix1) {
        cout << "Test Case 1: The undirected graph (adjacency matrix) is connected." << endl;
    } else {
        cout << "Test Case 1: The undirected graph (adjacency matrix) is not connected." << endl;
    }

    // Test Case 2: Disconnected graph adjacency matrix
    vector<vector<int>> adj_matrix2 = {
        {0, 1, 0, 0},
        {1, 0, 0, 0},
        {0, 0, 0, 1},
        {0, 0, 1, 0}
    };

    bool is_connected_matrix2 = graph_undirected.connected_adj_matrix(adj_matrix2);

    if (is_connected_matrix2) {
        cout << "Test Case 2: The undirected graph (adjacency matrix) is connected." << endl;
    } else {
        cout << "Test Case 2: The undirected graph (adjacency matrix) is not connected." << endl;
    }

    return 0;
}
