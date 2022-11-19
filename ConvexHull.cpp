// Convex Hull : Smallest convex polygon containing a set of points on a grid.
// The below code solves the problem in O(nlog(n)) time complexity where n is the number of points.
// Algorithm name : Monotone Chain

class Solution {
public:
    int crossProduct(vector < int >& O , vector < int >& P , vector < int >& Q) {
        return (P[0] - O[0]) * (Q[1] - O[1]) - (P[1] - O[1]) * (Q[0] - O[0]);
    }
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) 
    {
        vector < vector < int > > hull;
        sort(trees.begin() , trees.end() , 
        [&](const vector < int >& a , const vector < int >& b) {
            if(a[0] == b[0])
                return (a[1] < b[1]);
            return a[0] < b[0];
        });
        trees.erase(unique(trees.begin() , trees.end()) , trees.end());
        int n = trees.size();
        for(int i = 0 ; i < n ; i++) {
          // cross product can be less than equal to zero if we do not want to include collinear points
            while(hull.size() > 1 && crossProduct(hull[hull.size() - 2] , hull.back() , trees[i]) < 0) {
                hull.pop_back();
            }
            hull.push_back(trees[i]);
        }
        int lowerHullSize = hull.size();
        for(int i = n - 2 ; i >= 0 ; i--) {
          // // cross product can be less than equal to zero if we do not want to include collinear points
            while(hull.size() > lowerHullSize && crossProduct(hull[hull.size() - 2] , hull.back() , trees[i]) < 0) {
                hull.pop_back();
            }
            hull.push_back(trees[i]);
        }
        sort(hull.begin() , hull.end());
        hull.erase(unique(hull.begin() , hull.end()) , hull.end());
        return hull;
    }
};
