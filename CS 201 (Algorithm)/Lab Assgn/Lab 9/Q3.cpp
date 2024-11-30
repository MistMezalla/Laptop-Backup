#include <bits/stdc++.h>
using namespace std;

class Graphs {
public:
    int diameter(unordered_map<int,vector<int>> &adj_list) {
        int start_node = adj_list.begin()->first;

        auto temp_res = dfs(start_node, adj_list, 0);

        auto res = dfs(temp_res.first, adj_list, 0);

        return res.second;
    }

private:
    pair<int, int> dfs(int node, unordered_map<int, vector<int>> &adj_list, int dist) {
        unordered_map<int, bool> visited;
        stack<pair<int, int>> stack;
        stack.push({node, dist});

        int farthest_node = node;
        int max_dist = dist;

        while (!stack.empty()) {
            auto [current_node, current_dist] = stack.top();
            stack.pop();
            visited[current_node] = true;

            if (current_dist > max_dist) {
                max_dist = current_dist;
                farthest_node = current_node;
            }

            for (auto &neighbour : adj_list[current_node]) {
                if (!visited[neighbour]) {
                    stack.push({neighbour, current_dist + 1});
                }
            }
        }

        return {farthest_node, max_dist};
    }
};

int main() {
    Graphs g;

    // Test Case 1
    unordered_map<int, vector<int>> adj_list1;
    adj_list1[1] = {2};
    adj_list1[2] = {1, 3, 4};
    adj_list1[3] = {2, 5};
    adj_list1[4] = {2, 6, 7};
    adj_list1[5] = {3};
    adj_list1[6] = {4};
    adj_list1[7] = {4};

    int diameter1 = g.diameter(adj_list1);
    cout << "Test Case 1 - Calculated Diameter: " << diameter1 << endl;
    if (diameter1 == 4) {
        cout << "Test Case 1 Passed!" << endl;
    } else {
        cout << "Test Case 1 Failed." << endl;
    }

    // Test Case 2: Linear chain graph
    unordered_map<int, vector<int>> adj_list2;
    adj_list2[1] = {2};
    adj_list2[2] = {1, 3};
    adj_list2[3] = {2, 4};
    adj_list2[4] = {3, 5};
    adj_list2[5] = {4};

    int diameter2 = g.diameter(adj_list2);
    cout << "Test Case 2 - Calculated Diameter: " << diameter2 << endl;
    if (diameter2 == 4) {
        cout << "Test Case 2 Passed!" << endl;
    } else {
        cout << "Test Case 2 Failed." << endl;
    }

    // Test Case 3: Tree with multiple longest paths
    unordered_map<int, vector<int>> adj_list3;
    adj_list3[1] = {2, 3};
    adj_list3[2] = {1, 4, 5};
    adj_list3[3] = {1, 6, 7};
    adj_list3[4] = {2};
    adj_list3[5] = {2};
    adj_list3[6] = {3};
    adj_list3[7] = {3};

    int diameter3 = g.diameter(adj_list3);
    cout << "Test Case 3 - Calculated Diameter: " << diameter3 << endl;
    if (diameter3 == 4) {
        cout << "Test Case 3 Passed!" << endl;
    } else {
        cout << "Test Case 3 Failed." << endl;
    }

    // Test Case 4: Star graph
    unordered_map<int, vector<int>> adj_list4;
    adj_list4[1] = {2, 3, 4, 5, 6};
    adj_list4[2] = {1};
    adj_list4[3] = {1};
    adj_list4[4] = {1};
    adj_list4[5] = {1};
    adj_list4[6] = {1};

    int diameter4 = g.diameter(adj_list4);
    cout << "Test Case 4 - Calculated Diameter: " << diameter4 << endl;
    if (diameter4 == 2) {
        cout << "Test Case 4 Passed!" << endl;
    } else {
        cout << "Test Case 4 Failed." << endl;
    }

    // Test Case 5: Unbalanced tree with one long chain
    unordered_map<int, vector<int>> adj_list5;
    adj_list5[1] = {2};
    adj_list5[2] = {1, 3};
    adj_list5[3] = {2, 4};
    adj_list5[4] = {3, 5};
    adj_list5[5] = {4};

    int diameter5 = g.diameter(adj_list5);
    cout << "Test Case 5 - Calculated Diameter: " << diameter5 << endl;
    if (diameter5 == 4) {
        cout << "Test Case 5 Passed!" << endl;
    } else {
        cout << "Test Case 5 Failed." << endl;
    }

    // Test Case 6: Single node
    unordered_map<int, vector<int>> adj_list6;
    adj_list6[1] = {};

    int diameter6 = g.diameter(adj_list6);
    cout << "Test Case 6 - Calculated Diameter: " << diameter6 << endl;
    if (diameter6 == 0) {
        cout << "Test Case 6 Passed!" << endl;
    } else {
        cout << "Test Case 6 Failed." << endl;
    }

    // Test Case 7: Sparse graph with disconnected components
    unordered_map<int, vector<int>> adj_list7;
    adj_list7[1] = {2};
    adj_list7[2] = {1};
    adj_list7[3] = {4};
    adj_list7[4] = {3};
    adj_list7[5] = {6};
    adj_list7[6] = {5};

    int diameter7 = g.diameter(adj_list7);
    cout << "Test Case 7 - Calculated Diameter (for one component): " << diameter7 << endl;
    if (diameter7 == 1) {
        cout << "Test Case 7 Passed!" << endl;
    } else {
        cout << "Test Case 7 Failed." << endl;
    }


    return 0;
}
