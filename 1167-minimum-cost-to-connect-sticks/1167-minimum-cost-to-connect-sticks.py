class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            z = heappop(sticks)+heappop(sticks)
            ans += z
            heappush(sticks, z)
        return ans;