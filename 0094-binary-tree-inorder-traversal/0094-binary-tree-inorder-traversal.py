# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        def helper(root, result):
            if root != None:
                helper(root.left, result)  # Step 1: Visit left subtree
                result.append(root.val)     # Step 2: Visit the current node
                helper(root.right, result)  # Step 3: Visit right subtree
            
        result = []  # This will store the result of the traversal
        helper(root, result)  # Start the recursion from the root node
        return result  # Return the list of values collected from the traversal
