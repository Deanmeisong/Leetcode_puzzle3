class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        int ans1 = 0, ans2 = 0;
        int n = nums.size();
        if(n < 3) return 0; 
        for(int j = 0; j < n; j += 2) {
            int d = 0;
            if(j) d = max(d, nums[j]-nums[j-1]+1);
            if(j < n-1) d = max(d, nums[j]-nums[j+1]+1);
            ans2 += d;
        }
        
        for(int j = 1; j < n; j += 2) {
            int d = 0;
            if(j) d = max(d, nums[j]-nums[j-1]+1);
            if(j < n-1) d = max(d, nums[j]-nums[j+1]+1);
            ans1 += d;
        }

        return min(ans1, ans2);
    }
};