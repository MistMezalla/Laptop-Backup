#include <bits/stdc++.h>
using namespace std;

class Graphs {
public:
    bool is_strongly_connected(unordered_map<int, vector<int>> &adj_list) {
        unordered_map<int, bool> visited;
        vector<int> node_list;

        for (auto &pair : adj_list) {
            visited[pair.first] = false;
            node_list.push_back(pair.first);
        }

        int curr_number = 0;
        int i = 0;
        while (i < node_list.size()) {
            if (visited[node_list[i]] == true) {
                i++;
                continue;
            }

            queue<int> q;
            q.push(node_list[i]);
            curr_number++;
            visited[node_list[i]] = true;

            while (static_cast<int>(q.size()) > 0) {
                auto node = q.front();
                q.pop();

                for (auto neighbour : adj_list[node]) {
                    if (!visited[neighbour]) {
                        visited[neighbour] = true;
                        q.push(neighbour);
                    }
                }
            }
        }
        return curr_number == 1;
    }

    int number_SC(unordered_map<int, vector<int>> &adj_list) {
        unordered_map<int, bool> visited;
        vector<int> node_list;

        for (auto &node : adj_list) {
            visited[node.first] = false;  // Corrected: Set visited to false
            node_list.push_back(node.first);
        }

        int curr_number = 0;
        int i = 0;

        while (i < node_list.size()) {
            if (visited[node_list[i]] == true) {
                i++;
                continue;
            }

            auto start = node_list[i];
            queue<int> q;
            q.push(start);
            visited[start] = true;
            curr_number++;

            while (static_cast<int>(q.size()) > 0) {
                auto node = q.front();
                q.pop();

                for (auto &neighbour : adj_list[node]) {
                    if (!visited[neighbour]) {
                        visited[neighbour] = true;
                        q.push(neighbour);
                    }
                }
            }
        }
        return curr_number;
    }
};

int main() {
    Graphs graph;

    // Test case 1: Strongly connected graph
    unordered_map<int, vector<int>> adj_list_strong;
    adj_list_strong[1] = {2};
    adj_list_strong[2] = {3};
    adj_list_strong[3] = {1}; // 1 -> 2 -> 3 -> 1 (cycle)
    adj_list_strong[2].push_back(4); // 2 -> 4
    adj_list_strong[4] = {2}; // 4 -> 2

    // Check if the graph is strongly connected
    cout << "Test case 1 (Strongly connected): "
         << (graph.is_strongly_connected(adj_list_strong) ? "Yes" : "No") << endl;

    // Test case 2: Non-strongly connected graph
    unordered_map<int, vector<int>> adj_list_weak;
    adj_list_weak[1] = {2};
    adj_list_weak[2] = {3};
    adj_list_weak[3] = {}; // No edge back to 1, so it's not strongly connected

    // Check if the graph is strongly connected
    cout << "Test case 2 (Non-strongly connected): "
         << (graph.is_strongly_connected(adj_list_weak) ? "Yes" : "No") << endl;

    // Test case 3: Counting Strongly Connected Components
    unordered_map<int, vector<int>> adj_list_count;
    adj_list_count[1] = {2};
    adj_list_count[2] = {1}; // Component 1
    adj_list_count[3] = {4};
    adj_list_count[4] = {3}; // Component 2
    adj_list_count[5] = {4};   // Component 3 (isolated node)

    // Count the number of strongly connected components
    int number_of_components = graph.number_SC(adj_list_count);
    cout << "Number of Strongly Connected Components: " << number_of_components << endl;

    return 0;
}
