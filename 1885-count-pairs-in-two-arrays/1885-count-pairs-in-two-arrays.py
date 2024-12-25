class Solution(object):
    def countPairs(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        # 1) Build the difference array d
        d = [nums1[i] - nums2[i] for i in range(n)]

        # 2) Sort d
        d.sort()

        # 3) Two-pointer approach
        left, right = 0, n - 1
        count = 0
        while left < right:
            if d[left] + d[right] > 0:
                count += (right - left)
                right -= 1
            else:
                left += 1

        return count