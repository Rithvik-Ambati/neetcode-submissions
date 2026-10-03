# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subroot):
            if root is None and subroot is None:
                return True

            if root is None or subroot is None:
                return False

            if root.val != subroot.val:
                return False

            return (sameTree(root.left, subroot.left) and
                    sameTree(root.right, subroot.right))

        def search(root):
            if root is None:
                return False

            if sameTree(root, subRoot):
                return True

            return (search(root.left) or
                    search(root.right))

        return search(root)