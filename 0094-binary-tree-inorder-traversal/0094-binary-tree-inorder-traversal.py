# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
       stack = []
       def traverse(node):
            if node is None:
                return

            traverse(node.left)
            stack.append(node.val)
            traverse(node.right)

       traverse(root)
       return stack

            

        