# ✅ Approach 1: Extra Space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        nodes = []
        
        def preorder(node):
            if not node: return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

# ✅ Approach 2: In-Place Optimized
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        while current:
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                temp.right = current.right
                current.right = current.left
                current.left = None
            current = current.right