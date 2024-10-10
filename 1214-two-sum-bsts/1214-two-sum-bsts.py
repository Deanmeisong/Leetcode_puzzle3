# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, i):
        if root is None:
            return
        self.dfs(root.left, i)
        self.nums[i].append(root.val)
        self.dfs(root.right, i)
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """


        self.nums = [[], []]
        self.dfs(root1, 0)
        self.dfs(root2, 1)
        i, j = 0, len(self.nums[1]) - 1
        while i < len(self.nums[0]) and ~j:
            x = self.nums[0][i] + self.nums[1][j]
            if x == target:
                return True
            if x < target:
                i += 1
            else:
                j -= 1
        return False