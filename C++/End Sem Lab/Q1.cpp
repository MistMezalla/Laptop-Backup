#include <bits/stdc++.h>
using namespace std;

class Solution {
public :
    int graph_dist(int n,vector<pair<int,int>> &edge_list,vector<int> subset1,vector<int> subset2) {
        unordered_map<int,vector<int>> adj_list,adj_list_modified;

        for (auto [u,v]: edge_list) {
            adj_list[u].push_back(v);
            adj_list[v].push_back(u);
        }

        cout << "The adjacency list of the given graph is: " << endl;
        for (auto &elem: adj_list) {
            int node = elem.first;
            cout << node << " : ";
            for (auto neighbour: adj_list[node]) {
                cout << neighbour << " ";
            }
            cout << endl;
        }

        unordered_set<int> Sub1(subset1.begin(),subset1.end());
        unordered_set<int> Sub2(subset2.begin(),subset2.end());

        // In the modified adj_list S1 = -1 and S2 = -2;
        unordered_set<int> temp1;
        for (int node: subset1) {
            for (auto neighbour: adj_list[node]) {
                if (Sub2.find(neighbour) != Sub2.end()) {
                    temp1.insert(-2);
                }
                else if (Sub1.find(neighbour) == Sub1.end())
                    temp1.insert(neighbour);

            }
        }
        vector<int> set_neighbours1(temp1.begin(),temp1.end());
        adj_list_modified[-1] = set_neighbours1;

        unordered_set<int> temp2;
        for (int node: subset2) {
            for (auto neighbour: adj_list[node]) {
                if (Sub1.find(neighbour) != Sub1.end()) {
                    temp2.insert(-1);
                }
                else if (Sub2.find(neighbour) == Sub2.end())
                    temp2.insert(neighbour);
            }
        }
        vector<int> set_neighbours2(temp2.begin(),temp2.end());
        adj_list_modified[-2] = set_neighbours2;

        for (int node = 0;node < n;node++) {
            if (Sub1.find(node) == Sub1.end() && Sub2.find(node) == Sub2.end()) {
                for (auto neighbour: adj_list[node]) {
                    if (Sub1.find(neighbour) != Sub1.end()) {
                        adj_list_modified[node].push_back(-1);
                    }
                    else if (Sub2.find(neighbour) != Sub2.end()) {
                        adj_list_modified[node].push_back(-2);
                    }
                    else
                        adj_list_modified[node].push_back(neighbour);
                }
            }
        }

        // cout << "The modified adjacency list of the given graph is: " << endl;
        // for (auto &elem: adj_list_modified) {
        //     int node = elem.first;
        //     cout << node << " : ";
        //     for (auto neighbour: adj_list_modified[node]) {
        //         cout << neighbour << " ";
        //     }
        //     cout << endl;
        // }

        unordered_map<int,bool> visited;
        unordered_map<int,int> level;
        for (auto elem: adj_list_modified) {
            int node = elem.first;
            visited[node] = false;
            level[node] = -1;
        }

        queue<int> q;
        q.push(-1);

        level[-1] = 0;

        while (!q.empty()) {
           int node = q.front();
            q.pop();
            visited[node] = true;

            for(auto &neighbour : adj_list_modified[node]) {
                if (! visited[neighbour]) {
                    level[neighbour] = level[node] + 1;
                    if (neighbour == -2) {
                        return level[neighbour];
                    }
                    q.push(neighbour);
                }
            }
        }
        return INT_MAX;
    }
};

int main() {
    Solution sol;

    // int n = 5;
    // vector<pair<int,int>> edge_list = {{0,1},{1,2},{2,3},{3,4}};
    // vector<int> subset1 = {0,1};
    // vector<int> subset2 = {3,4};
    // auto res = sol.graph_dist(n,edge_list,subset1,subset2);
    // cout << res;

    // int n = 6;
    // vector<pair<int,int>> edge_list = {{0,1},{2,3},{4,5}};
    // vector<int> subset1 = {0,1};
    // vector<int> subset2 = {5,4};
    // auto res = sol.graph_dist(n,edge_list,subset1,subset2);
    // cout << res;

    // int n = 4;
    // vector<pair<int,int>> edge_list = {{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
    // vector<int> subset1 = {0,1};
    // vector<int> subset2 = {2,3};
    // auto res = sol.graph_dist(n,edge_list,subset1,subset2);
    // cout << res;

    // int n = 12;
    // vector<pair<int,int>> edge_list = {{1,2},{1,5},{2,8},{2,6},{3,11},{3,5},
    //     {3,7},{3,10},{4,8},{5,9},{6,9},{6,11},{7,9},{7,10},{8,10}};
    // vector<int> subset1 = {0,1,2};
    // vector<int> subset2 = {10,11};
    // auto res = sol.graph_dist(n,edge_list,subset1,subset2);
    // cout << res;

    int t;
    cout << "Enter the number of test cases" << endl;
    cin >> t;
    cout << endl;

    while (t--) {
        int n;
        cout << "Enter the number of nodes" << endl;
        cin >> n ;
        cout << endl;

        vector<pair<int,int>> edge_list;
        cout << "Enter the edges of  the graph" << endl;
        while (true) {
            int choice;
            cout << "Enter the choice\n1 to input edge\n0 to stop" << endl;
            cin >> choice;

            if (choice == 0) {
                break;
            }

            int u,v;
            cout << "Enter the nodes of the edge" << endl;
            cin >> u;
            cin >> v;
            edge_list.emplace_back(u,v);
        }
        cout << endl;

        int n1,n2;
        vector<int> subset1,subset2;

        cout << "Enter the size of first subset" << endl;
        cin >> n1;
        cout << endl;
        cout << "Enter the nodes of subset1" << endl;
        for (int i = 0;i < n1;i++) {
            int val;
            cin >> val;
            subset1.push_back(val);
        }

        cout << "Enter the size of second subset" << endl;
        cin >> n2;
        cout << endl;
        cout << "Enter the nodes of subset2" << endl;
        for (int i = 0;i < n2;i++) {
            int val;
            cin >> val;
            subset2.push_back(val);
        }

        auto res = sol.graph_dist(n,edge_list,subset1,subset2);
        cout << "Ans" << endl;
        cout << res << endl;
    }

}