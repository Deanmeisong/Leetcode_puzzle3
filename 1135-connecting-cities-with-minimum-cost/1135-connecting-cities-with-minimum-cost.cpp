class Solution {
public:
    int minimumCost(int n, vector<vector<int>>& connections) {
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        sort(connections.begin(), connections.end(), [](auto& a, auto& b) {return a[2]<b[2];});

        function<int(int)> find = [&](int x) {
            if(x != p[x]) p[x] = find(p[x]);
            return p[x];
        };
        int ans = 0;
        for(const auto& con : connections) {
            int x = con[0]-1, y = con[1]-1, cost = con[2];
            if(find(x) == find(y)) continue;
            p[find(x)] = find(y);
            ans += cost;
            if(--n == 1) return ans;
        }
        return -1;
        
    }
};