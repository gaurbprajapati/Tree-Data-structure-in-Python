# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        return self.solve(root, arr)

    def solve(self, root, arr):
        q = []
        q.append(root)
        ans = []
        flag = 0
        while(q):
            qlen = len(q)
            sublist = []
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    sublist.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if flag == 0:
                ans.append(sublist)
                flag = 1
            else:
                ans.append(sublist[::-1])
                flag = 0

        return ans[:-1]
