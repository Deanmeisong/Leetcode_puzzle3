public class Solution {
    public int EqualSubstring(string s, string t, int maxCost) {
        int i = 0, ans = 0, n = s.Length;
        for (int j = 0; j < n; ++j)
        {
            maxCost -= Math.Abs(s[j] - t[j]);
            while (maxCost < 0 && i <= j && i < n)
            {
                maxCost += Math.Abs(s[i] - t[i]);
                ++i;
            }

            ans = Math.Max(ans, j - i + 1);
        }

        return ans;
    }
}