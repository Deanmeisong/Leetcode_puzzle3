class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        bool s[8][8]{};
        for(const auto& q : queens)
            s[q[0]][q[1]] = 1;
        vector<vector<int>> ans;
        for(int a = -1; a <= 1; ++a)
            for(int b = -1; b <= 1; ++b) {
                if(a || b) {
                    int x = king[0]+a; int y = king[1]+b;
                    while(x >= 0 and x < 8 and y >= 0 and y < 8) {
                        if(s[x][y]) {
                            ans.push_back({x,y});
                            break;
                        }
                        x += a; y += b;
                    }
                }
            }
        return ans;
    }
};