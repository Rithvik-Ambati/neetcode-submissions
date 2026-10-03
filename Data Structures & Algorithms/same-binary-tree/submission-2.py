# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check_same_val(p,q): 
            if p is None and q is None:
                return True

            if p is None and q is not None:
                return False

            if p is not None and q is None:
                return False

            if p is not None and q is not None:
                if p.val != q.val:
                    return False

            return check_same_val(p.left, q.left) and check_same_val(p.right, q.right)
        

        return check_same_val(p,q)