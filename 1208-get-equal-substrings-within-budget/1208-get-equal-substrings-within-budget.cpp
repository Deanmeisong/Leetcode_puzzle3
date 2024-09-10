class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int i = 0, ans = 0, n = s.length();
        for(int j = 0; j < n; ++j) {
            maxCost -= abs(s[j]-t[j]);
            while(maxCost < 0 && i <= j && i < n) {
                maxCost += abs(s[i]-t[i]);
                ++i;
            }
            ans = max(ans, j-i+1);
        }
        return ans;
    }
};