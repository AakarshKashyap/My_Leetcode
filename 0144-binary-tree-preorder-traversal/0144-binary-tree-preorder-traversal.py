# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        stack = []
        def transverse(node):
            if node is None:
                return 
            stack.append(node.val)
            transverse(node.left)
            transverse(node.right)
        transverse(root)
        return stack
