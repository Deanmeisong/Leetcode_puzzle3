class Solution {
public:
    int longestWPI(vector<int>& hours) {
        int ans = 0, s = 0;
        unordered_map<int,int> presums;
        for(int i = 0; i < hours.size(); ++i) {
            s += hours[i] > 8 ? 1 : -1;
            if(s > 0) ans = i+1;
            else if (presums.count(s - 1)) ans = max(ans, i - presums[s - 1]);
            if (!presums.count(s)) presums[s] = i;
        }
        return ans;
    }
};