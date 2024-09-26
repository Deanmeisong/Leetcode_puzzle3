public class Solution {
    public int LongestWPI(int[] hours) {
        int ans = 0, s = 0;
        Dictionary<int, int> presums = new Dictionary<int, int>();

        for (int i = 0; i < hours.Length; ++i)
        {
            s += hours[i] > 8 ? 1 : -1;
            if (s > 0)
            {
                ans = i + 1;
            }
            else if (presums.ContainsKey(s - 1))
            {
                ans = Math.Max(ans, i - presums[s - 1]);
            }
            if (!presums.ContainsKey(s))
            {
                presums[s] = i;
            }
        }

        return ans;
    }
}