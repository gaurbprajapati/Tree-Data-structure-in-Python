# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = -float('inf')

    def solution(self, root):
        if not root:
            return 0

        lh = max(0, self.solution(root.left))
        rh = max(0, self.solution(root.right))
        self.ans = max(self.ans, lh+rh+root.val)
        return root.val+max(lh, rh)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solution(root)
        return self.ans
