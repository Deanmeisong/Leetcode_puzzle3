"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(root: 'Node'):
            if root is None:
                return 0
            nonlocal ans
            m1 = m2 = 0
            for node in root.children:
                t = dfs(node)
                if t > m1:
                    m1,m2 = t,m1
                elif t > m2:
                    m2 = t
            ans = max(ans, m1+m2)
            return m1+1
        
        ans = 0
        dfs(root)
        return ans
            