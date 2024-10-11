#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int num_intersections(vector<pair<int,int>> &P, vector<pair<int,int>> &Q) {
            sort(P.begin(),P.end());
            return intersections(P,Q,0,static_cast<int>(P.size()));
        }

        int intersections(vector<pair<int,int>> &P,vector<pair<int,int>> &Q,int left,int right) {
            if (right - left <= 1)
                return 0;

            int mid = (left + right)/2;

            int left_intersections = intersections(P,Q,left,mid);
            int right_intersections = intersections(P,Q,mid,right);

            return left_intersections + right_intersections + cross_intersections(P,Q,left,mid,right);
        }

        int cross_intersections(vector<pair<int,int>> &P, vector<pair<int,int>> &Q,int left,int mid,int right) {
            vector<pair<int,int>> temp;
            int i = left, j = mid;
            int cnt = 0;

            while (i< mid && j < right) {
                if (Q[i] <= Q[j]) {
                    temp.push_back(Q[i]);
                    i++;
                }
                else {
                    cnt += mid - i;
                    temp.push_back(Q[j]);
                    j++;
                }
            }

            while (i < mid) {
                temp.push_back(Q[i]);
                i++;
            }

            while (j<right) {
                temp.push_back(Q[j]);
                j++;
            }


            for (i = 0;i<temp.size();i++) {
                Q[left + i] = temp[i];
            }
            return cnt;
        }
};

int main()
{
    Solution sol;
    vector<pair<int,int>> P = {{2,0},{1,0},{4,0},{3,0}};
    vector<pair<int,int>> Q = {{1,1},{4,1},{3,1},{2,1}};
    cout << sol.num_intersections(P,Q);
    return 0;
};