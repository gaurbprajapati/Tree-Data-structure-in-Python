class Solution:
    def recur(self, root, res):
        if root:
            self.recur(root.left, res)
            res.append(root.val)
            self.recur(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recur(root, res)
        return res
