# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root, arr):
        if root:
            arr.append(root.val)
            self.recur(root.left, arr)
            self.recur(root.right, arr)

        return arr

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        return self.recur(root, arr)
