class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        ans = n
        for i in range(m):
            j = self.bisect_left(range(n), 1, key=lambda k: binaryMatrix.get(i, k))
            ans = min(ans, j)
        return -1 if ans >= n else ans

    def bisect_left(self, arr, target, key):
        """
        Custom implementation of bisect_left since Python 2 lacks the key argument in bisect.
        """
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if key(arr[mid]) < target:
                low = mid + 1
            else:
                high = mid
        return low
