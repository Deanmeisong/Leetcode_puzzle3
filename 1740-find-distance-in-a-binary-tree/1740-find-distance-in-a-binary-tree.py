# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lca(root, p, q):
            if root == None or root.val in [p, q]: return root
            left, right = lca(root.left, p, q), lca(root.right, p, q)
            if left == None:
                return right
            if right == None:
                return left
            return root
        def dfs(root, v):
            if root == None: return -1
            if root.val == v: return 0
            left, right = dfs(root.left, v), dfs(root.right, v)
            if left == right == -1: return -1
            return max(left, right) + 1
        
        g = lca(root, p, q)
        return dfs(g,p) + dfs(g,q)
        