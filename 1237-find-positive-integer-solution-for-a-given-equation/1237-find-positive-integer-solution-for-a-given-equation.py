"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        ans = []
        for x in range(1, z + 1):
            # Use a simple binary search implementation without bisect.
            left, right = 1, z
            while left <= right:
                y = (left + right) // 2
                value = customfunction.f(x, y)
                if value == z:
                    ans.append([x, y])
                    break
                elif value < z:
                    left = y + 1
                else:
                    right = y - 1
        return ans
        