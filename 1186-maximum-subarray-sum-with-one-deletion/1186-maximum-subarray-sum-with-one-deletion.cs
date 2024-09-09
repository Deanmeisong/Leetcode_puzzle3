public class Solution {
    public int MaximumSum(int[] arr) {
        int n = arr.Length;
        int[] ends = new int[n];
        int[] starts = new int[n];
        
        // Calculating maximum subarray sum ending at each index
        for (int i = 0, s = 0; i < n; ++i)
        {
            s = Math.Max(s, 0) + arr[i];
            ends[i] = s;
        }

        // Calculating maximum subarray sum starting at each index
        for (int i = n - 1, s = 0; i >= 0; --i)
        {
            s = Math.Max(s, 0) + arr[i];
            starts[i] = s;
        }

        // Find the maximum subarray sum in the array
        int ans = int.MinValue;
        for (int i = 0; i < n; i++)
        {
            ans = Math.Max(ans, ends[i]);
        }

        // Find the maximum sum with one element removed
        for (int i = 1; i < n - 1; ++i)
        {
            ans = Math.Max(ans, ends[i - 1] + starts[i + 1]);
        }

        return ans;
    }
}