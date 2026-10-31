# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            stack.append(node.val)
        traverse(root)
        return stack
        