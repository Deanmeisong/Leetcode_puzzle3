class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        queue<pair<int,int>> q;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                if(grid[i][j]) q.push({i,j});
        
        int ans = -1;
        if(q.size() == n*n || q.empty()) return ans;
        int dirs[5] = {-1, 0, 1, 0, -1};
        
        while(!q.empty()) {
            int len = q.size();
            while(len--) {
                auto [i, j] = q.front(); q.pop();
                for(int d = 0; d < 4; ++d) {
                    int x = dirs[d] + i;
                    int y = dirs[d+1] + j;
                    if(x >= 0 && x < n && y >= 0 && y < n && !grid[x][y]) {
                        grid[x][y] = 1;
                        q.push({x, y});
                    }
                }
            }
            ++ans;
        }
        return ans;
    }
};