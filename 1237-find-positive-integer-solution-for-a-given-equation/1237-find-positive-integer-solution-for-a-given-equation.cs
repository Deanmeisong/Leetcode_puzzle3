/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * public class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */

public class Solution {
    public IList<IList<int>> FindSolution(CustomFunction customfunction, int z) {
        List<IList<int>> ans = new List<IList<int>>();
        
        for (int x = 1; x <= 1000; x++)
        {
            int l = 1, r = 1000;
            while (l < r)
            {
                int m = (r - l) / 2 + l;
                if (customfunction.f(x, m) >= z)
                {
                    r = m;
                }
                else
                {
                    l = m + 1;
                }
            }
            if (customfunction.f(x, l) == z)
            {
                ans.Add(new List<int> { x, l });
            }
        }

        return ans;
    }
}