#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map<int,vector<pair<int,int>>> adj_list;

        for (auto &edge: flights) {
            int u = edge[0];
            int v = edge[1];
            int wt = edge[2];

            adj_list[u].emplace_back(v,wt);
        }

        // Error: as pair not hashable
        //unordered_map<pair<int,int>,int> d;

        /*
        Custom Hash Function:
        unordered_map requires a hash function for the key type (here, a pair<int, int>). To facilitate this, we
        defined a custom hash function in the std namespace for pairs of integers. The hash function combines the
        hash values of the two integers to create a unique key hash.
         */

        // Unordered map to store the minimum cost to reach (node, stops)
        unordered_map<pair<int, int>, int, hash<pair<int, int>>> d;
        d[{src, 0}] = 0;

    }
};

// Hash function for pair<int, int> to use it in unordered_map
namespace std {
    template <>
    struct hash<pair<int, int>> {
        size_t operator()(const pair<int, int>& p) const {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };
}
