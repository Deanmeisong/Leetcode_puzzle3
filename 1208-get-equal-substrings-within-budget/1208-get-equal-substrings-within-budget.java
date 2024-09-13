class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int i = 0, ans = 0, n = s.length();
        for (int j = 0; j < n; ++j) {
            maxCost -= Math.abs(s.charAt(j) - t.charAt(j)); // Calculate the cost for current character
            while (maxCost < 0 && i <= j && i < n) { // If the cost exceeds maxCost, move the start index
                maxCost += Math.abs(s.charAt(i) - t.charAt(i));
                ++i;
            }
            ans = Math.max(ans, j - i + 1); // Calculate the maximum length of substring within the maxCost
        }
        return ans;
    }
}