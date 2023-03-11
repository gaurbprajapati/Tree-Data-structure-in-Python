# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        val1 = self.maxDepth(root.left)
        val2 = self.maxDepth(root.right)

        return max(val1, val2)+1
# Naive Approach

    def solution1(self, root):
        if root == None:
            return 0

        lh = self.solution1(root.left)
        rh = self.solution1(root.right)
        op3 = self.maxDepth(root.left)+self.maxDepth(root.right)

        return max(op3, max(lh, rh))

# Optimize O(n)

    def solution2(self, root):
        if root == None:
            return 0
        lh = self.solution2(root.left)
        rh = self.solution2(root.right)

        self.maxi = max(self.maxi, lh+rh)

        return max(lh, rh)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # return self.solution1(root)

        self.solution2(root)
        return self.maxi
