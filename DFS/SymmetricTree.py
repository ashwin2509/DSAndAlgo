# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.recursion(root, root)
    
    
    def recursion(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        
        return (t1.val == t2.val and self.recursion(t1.left, t2.right) and self.recursion(t1.right, t2.left))
        