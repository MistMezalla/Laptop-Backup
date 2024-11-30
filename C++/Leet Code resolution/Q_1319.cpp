#include <bits/stdc++.h>
using namespace std;

class Union_Find {
private:
    vector<int> parent,rank;

public:
    Union_Find(int n) {
        parent.resize(n);
        rank.resize(n,1);

        for(int i = 0;i<n;i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    /*
    -> union is a key word in c++
    */
    bool union_sets(int x,int y){
        int root_x = find(x);
        int root_y = find(y);

        if (root_x != root_y) {
            if (rank[root_x] > rank[root_y]) {
                parent[root_y] = root_x;
                rank[root_x] += rank[root_y];
            }
            else if (rank[root_x] < rank[root_y]) {
                parent[root_x] = root_y;
                rank[root_y] += rank[root_x];
            }
            else {
                rank[root_x] += rank[root_y];
                parent[root_y] = root_x;
            }
            return true;
        }
        return false;
    }
};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size() < n - 1)
            return -1;

        Union_Find uf(n);

        int num_edges = 0;
        for (auto edge: connections) {
            int u = edge[0];
            int v = edge[1];

            if (uf.union_sets(u,v)) {
                num_edges ++;
            }
        }
        int num_comp = 0;
        for (int i = 0;i < n;i++) {
            if (uf.find(i) == i) {
                num_comp ++;
            }
        }

        return num_comp - 1;
    }
};