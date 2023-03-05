# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, root):
        if not root:
            return None
        stack = []
        stack.append(root)
        while(stack):
            node = stack.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    def recur(self, root):
        if not root:
            return

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.iterative(root)
