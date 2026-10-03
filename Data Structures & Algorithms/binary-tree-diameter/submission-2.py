# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def path(root):
            if root is None:
                return [0,0]
            
            leftHeight = path(root.left)
            rightHeight = path(root.right)

            node_height = max(leftHeight[0],rightHeight[0]) + 1
            path_length = max(leftHeight[0]+rightHeight[0],leftHeight[1], rightHeight[1])

            return [node_height,path_length]

        a = path(root)
        return a[1]        