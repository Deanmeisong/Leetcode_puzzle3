"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        cur = leaf       
        parent = cur.parent
        while cur != root:
            grand_parent = parent.parent
            if cur.left:
                cur.right = cur.left
            
            cur.left = parent
            parent.parent = cur
            
            if parent.left == cur:
                parent.left = None
            if parent.right == cur:
                parent.right = None
            
            cur = parent
            parent = grand_parent
        leaf.parent = None
        return leaf
                
        