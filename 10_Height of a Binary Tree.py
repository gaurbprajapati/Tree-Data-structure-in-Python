

'''
# Intuition + Approach: Using LEVEL ORDER TRAVERSAL

'''


# -----------------------------------


'''
Intuition: Recursively ( Post Order Traversal )

'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        val1 = self.maxDepth(root.left)
        val2 = self.maxDepth(root.right)

        return max(val1, val2)+1
