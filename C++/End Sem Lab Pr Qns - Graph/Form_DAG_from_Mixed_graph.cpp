#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<pair<int,int>> DAG_from_gen_graph(vector<tuple<int,int,int>> edge_list) {
        unordered_map<int,vector<int>> adj_list;

        for (auto [u,v,sign]: edge_list) {
            if (sign == 0) { // undirected
                adj_list[u].push_back(v);
                adj_list[v].push_back(u);
            }
            else {
                adj_list[u].push_back(v);
            }
        }

        unordered_map<int,int> visited,arr;

        for (auto &elem: adj_list) {
            int node = elem.first;
            visited[node] = 0;
            arr[node] = -1;
        }

        int time = 0;
        vector<pair<int,int>> tree_edges,forward_edges,backward_edges,cross_edges;
        auto DFS = [&](int node) {
            visited[node] = 1;
            arr[node] = time;
            time ++;

            for (auto &neighbour: adj_list[node]) {
                if (visited[neighbour] == 0) {
                    tree_edges.emplace_back(node,neighbour);
                    DFS(neighbour);
                }
                else if (visited[neighbour] == 1) {
                    backward_edges.emplace_back(node,neighbour);
                }
                else if(arr[neighbour] > arr[node]) {
                    forward_edges.emplace_back(node,neighbour);
                }
                else {
                    cross_edges.emplace_back(node,neighbour);
                }

            }
            time++;
            visited[node] = 2;

        };

        for (auto &elem: adj_list) {
            int node = elem.first;

            if (visited[node] == 0){
                DFS(node);
            }
        }
    }
};

int main(){
    Solution sol;
    vector<tuple<int,int,int>> graph1_list = {
        {0,1,1},{1,2,0},{2,3,0},{2,4,0},{4,3,0},{4,0,0},{5,1,1},{5,4,1}
    };

    auto res = sol.DAG_from_gen_graph(graph1_list);

    for (auto [u,v]: res) {
        cout << u << " ---> " << v < endl;
    }
    return 0;
}