#include <bits/stdc++.h>
using namespace std;

class Graphs {
public:
    void dfs(int node, unordered_map<int, vector<int>>& adj_list, unordered_map<int, bool>& visited, stack<int>& finish_stack) {
        visited[node] = true;
        for (auto neighbour : adj_list[node]) {
            if (!visited[neighbour]) {
                dfs(neighbour, adj_list, visited, finish_stack);
            }
        }
        finish_stack.push(node);
    }

    void reverseDFS(int node, unordered_map<int, vector<int>>& reversed_adj_list, unordered_map<int, bool>& visited) {
        visited[node] = true;
        for (auto neighbour : reversed_adj_list[node]) {
            if (!visited[neighbour]) {
                reverseDFS(neighbour, reversed_adj_list, visited);
            }
        }
    }

    int number_SC(unordered_map<int, vector<int>>& adj_list) {
        unordered_map<int, bool> visited;
        stack<int> finish_stack;

        // Step 1: Fill nodes in stack according to their finishing times
        for (auto& node : adj_list) {
            if (!visited[node.first]) {
                dfs(node.first, adj_list, visited, finish_stack);
            }
        }

        unordered_map<int, vector<int>> reversed_adj_list;
        for (auto& node : adj_list) {
            for (auto& neighbour : node.second) {
                reversed_adj_list[neighbour].push_back(node.first);
            }
        }

        int scc_count = 0;
        visited.clear();
        while (!finish_stack.empty()) {
            int node = finish_stack.top();
            finish_stack.pop();
            if (!visited[node]) {
                reverseDFS(node, reversed_adj_list, visited);
                scc_count++;
            }
        }
        return scc_count;
    }
};

int main() {
    Graphs graph;

    // Test case 3: Counting Strongly Connected Components
    unordered_map<int, vector<int>> adj_list_count;
    adj_list_count[1] = {2};
    adj_list_count[2] = {1}; // Component 1
    adj_list_count[3] = {4};
    adj_list_count[4] = {3}; // Component 2
    adj_list_count[5] = {};   // Component 3 (isolated node)

    // Count the number of strongly connected components
    int number_of_components = graph.number_SC(adj_list_count);
    cout << "Number of Strongly Connected Components: " << number_of_components << endl;

    return 0;
}

