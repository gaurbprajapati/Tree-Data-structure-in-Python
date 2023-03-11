# Definition for a binary tree node.
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
# Naive Approach

# the time complexity is O(N*2)
    def solution1(self, root):
        if root == None:
            return True

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        if (abs(lh-rh) > 1 or self.solution1(root.left) != True or self.solution1(root.right) != True):
            return False
        return True

# Optimize T.C. O(N)

    def solution2(self, root):

        if root == None:
            return 0

        lh = self.solution2(root.left)
        # if lh ==-1 :
        #     return -1

        rh = self.solution2(root.right)
        if rh == -1 or lh == -1:
            return -1

        if (abs(lh-rh) > 1):
            return -1

        return max(lh, rh)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # return self.solution1(root)

        return self.solution2(root) != -1
