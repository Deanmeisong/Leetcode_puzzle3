class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int n = arr.size();
        int sum = 0;
        auto dp = vector<vector<int>>(n, vector<int>(n, INT_MAX));
        auto larger = vector<vector<int>>(n, vector<int>(n, INT_MIN));
        
        for(int i = 0; i < n; ++i) {
            dp[i][i] = arr[i];
            larger[i][i] = dp[i][i];
            sum += arr[i];
        }
        
        for(int len = 2; len <= n; ++len) {
            for(int i = 0; i <= n-len; ++i) {
                int j = i+len-1;
                for(int k = i; k < j; ++k) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + larger[i][k]*larger[k+1][j]);
                    larger[i][j] = max(larger[i][k], larger[k+1][j]);
                }
            }
        }
        
        return dp[0][n-1] - sum;
    }
};