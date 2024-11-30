#include <bits/stdc++.h>
using namespace std;

// Dijkstra based implementation
class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        unordered_map<int,vector<int>> adj_list;

        for (int i=1;i<=n;i++) {
            adj_list[i] = {};
        }

        for (auto &edge: edges) {
            int u = edge[0],v = edge[1];
            adj_list[u].push_back(v);
            adj_list[v].push_back(u);
        }

        unordered_map<int,int> d1;
        unordered_map<int,int> d2;
        unordered_map<int,int>freq;

        for (int i = 1;i<=n;i++) {
            d1[i] = INT_MAX;
            d2[i] = INT_MAX;
            freq[i] = 0;
        }

        d1[1] = 0;
        // priority_queue<pair<int,int>> min_heap;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> min_heap;
        /*
        -> By default: A priority_queue in C++ uses a less<> comparator, which creates a max-heap.
        -> greater<>: Changes the behavior to a min-heap by making smaller elements have higher priority.
         */
        min_heap.emplace(0,1); // dist,node

        while (! min_heap.empty()) {
            // int curr_time,node;
            auto [curr_time,node] = min_heap.top();
            min_heap.pop();
            freq[node] ++;

            if (freq[node] == 2 && node == n)
                return curr_time;

            if ((curr_time/change) & 1) {
                curr_time = change * (curr_time/change + 1) + time;
            }
            else {
                curr_time += time;
            }

            for (auto &neighbour: adj_list[node]) {
                if (freq[neighbour] == 2)
                    continue;

                if (curr_time < d1[neighbour]) {
                    d2[neighbour] = d1[neighbour];
                    d1[neighbour] = curr_time;
                    min_heap.emplace(curr_time,neighbour);
                }
                else if (curr_time < d2[neighbour] && curr_time != d1[neighbour]) {
                    d2[neighbour] = curr_time;
                    min_heap.emplace(curr_time,neighbour);
                }
            }
        }
        return 0;
    }
};

// BFS based implementation
class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        unordered_map<int,vector<int>> adj_list;

        for (int i=1;i<=n;i++) {
            adj_list[i] = {};
        }

        for (auto &edge: edges) {
            int u = edge[0],v = edge[1];
            adj_list[u].push_back(v);
            adj_list[v].push_back(u);
        }

        unordered_map<int,int> d1;
        unordered_map<int,int> d2;

        for (int i = 1;i<=n;i++) {
            d1[i] = -1;
            d2[i] = -1;
        }

        d1[1] = 0;
        queue<pair<int,int>> q; // node,freq
        q.emplace(1,1);
        while (! q.empty()) {
            auto [node,freq] = q.front();
            q.pop();

            int curr_time = freq == 1 ? d1[node] : d2[node];

            if ((curr_time/change) & 1) {
                curr_time = change * (curr_time/change + 1) + time;
            }
            else {
                curr_time += time;
            }

            for (auto &neighbour: adj_list[node]) {
                if (d1[neighbour] == -1) {
                    d1[neighbour] = curr_time;
                    q.emplace(neighbour,1);
                }
                else if (d2[neighbour] == -1 && curr_time != d1[neighbour]) {
                    if (neighbour == n) {
                        return curr_time;
                    }
                    d2[neighbour] = curr_time;
                    q.emplace(neighbour,2);
                }
            }
        }
        return 0;
    }
};