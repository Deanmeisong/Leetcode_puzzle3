class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        f = g = 0
        ans = -inf
        for x in nums:
            ff = max(f, 0) + x
            gg = max(g + x, max(f, 0) + x*x)
            f, g = ff, gg
            ans = max(f, g, ans)
        return ans