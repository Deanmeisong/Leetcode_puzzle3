public class Solution {
    public int MinSwaps(int[] data) {
        int sum = 0;
        foreach (int d in data)
            sum += d;
        
        int sumLocal = 0;
        for (int i = 0; i < sum; i++)
            sumLocal += data[i];
        
        int ans = sum - sumLocal;
        for (int i = sum; i < data.Length; i++) {
            sumLocal -= data[i - sum];
            sumLocal += data[i];
            ans = Math.Min(ans, sum - sumLocal);
        }
        
        return ans;
    }
}